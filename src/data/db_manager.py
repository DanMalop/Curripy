import sqlite3
from .sections import Curriculum, Job, Study, Comp_study


class DB_manager:
    def __init__(self, db_file: str = "curriculum_data.db") -> None:
        self.db_file = db_file
        self.conn = None  # Database connection
        self.cursor = None  # Database commands excecuter
        self._connect()  # Call connection to database
        self._create_tables()  # Prepare the database

    def _connect(self):
        # ------ Database connection ------
        try:
            self.conn = sqlite3.connect(self.db_file)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print(f"Connection error with database: {e}")

    def _create_tables(self):
        # Create needed tables if doesn't exist
        if not self.cursor:
            return

        # Curriculum Table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXIST curriculum (
                id INTEGER PRIMARY KEY,
                name TEXT,
                lastname TEXT,
                phone INTEGER,
                emain TEXT,
                linkedin TEXT,
            )
            """)

        # job table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXIST job (
            id INTEGER PRIMARY KEY,
            curriculum_id INTEGER,
            position TEXT,
            company TEXT,
            start_date TEXT,
            end_date TEXT,
            FOREIGN KEY (curriculum_id) REFERENCES curriculum (id)
            )
            """)

        # function table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXIST function (
            id INTEGER PRIMARY KEY,
            job_id INTEGER,
            description TEXT,
            FOREIGN KEY (job_id) REFERENCES job (id)
            )
            """)

        # function table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXIST achievements (
            id INTEGER PRIMARY KEY,
            job_id INTEGER,
            description TEXT,
            FOREIGN KEY (job_id) REFERENCES job (id)
            )
            """)
