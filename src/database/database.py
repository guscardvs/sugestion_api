from datetime import datetime
from pathlib import Path

from core.settings import DATABASE, MIGRATIONS
from pony import orm

from database.decorators import db_session


class Client:

    db = orm.Database()
    binded = False
    mapped = False

    def start(self):
        if not self.binded:
            self.db.bind(**DATABASE)
            self.binded = True

    @db_session
    def _verify_migration_table(self, connection):
        try:
            connection.execute(
                'SELECT id, `filename`, created_at FROM migrations WHERE 1 = 0'
            )
            return True
        except Exception:
            return False

    @db_session
    def _get_migrated_files(self, connection):
        with connection.cursor() as cursor:
            cursor.execute('SELECT `filename` FROM migrations')
            records = cursor.fetchall()
            return [filename for filename, in records]

    def _get_tables(self, migrated_files: list[str]):
        for file in MIGRATIONS.glob("*.sql"):
            if str(file) not in migrated_files and "0000" not in str(file):
                yield file

    @db_session
    def _create_table(self, connection, file: Path):
        with connection.cursor() as cursor:
            cursor.execute(file.read_text())
            cursor.execute(
                'INSERT INTO migrations(`filename`, created_at) VALUES(%s, %s)',
                (str(file), datetime.utcnow()),
            )

    @db_session
    def migrate(self):
        connection = self.db.get_connection()
        migration_table_created = self._verify_migration_table(connection)
        with connection.cursor() as cursor:
            if not migration_table_created:
                cursor.execute((MIGRATIONS / "0000__create_migrations.sql").read_text())
        migrated_files = self._get_migrated_files(connection)
        for file in self._get_tables(migrated_files):
            self._create_table(connection, file)
        connection.commit()

    def generate_mapping(self):
        if not self.mapped:
            from database.entities import entry
            self.db.generate_mapping(check_tables=True)
            self.mapped = True

client = Client()
Entity = client.db.Entity
