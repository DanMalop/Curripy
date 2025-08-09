import sqlite3
from .sections import Curriculum, Job, Study, Course


class DB_manager:
    def __init__(self, db_file: str = "curriculum_data.db") -> None:
        self.db_file = db_file
        self.conn = None
        self.cursor = None
        self._connect()
        self._create_tables()

    def _connect(self):
        pass

    def _create_tables(self):
        pass
