# ==========================================
# IMPORTS
# ==========================================

import sqlite3
from pathlib import Path


# ==========================================
# PATHS
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_PATH = BASE_DIR / "database" / "biotrack.db"

SCHEMA_PATH = BASE_DIR / "database" / "schema.sql"


# ==========================================
# INITIALIZE DATABASE
# ==========================================

def initialize_database():

    connection = sqlite3.connect(DATABASE_PATH)

    with open(
        SCHEMA_PATH,
        "r",
        encoding="utf-8"
    ) as schema_file:

        schema = schema_file.read()

    connection.executescript(schema)

    connection.commit()

    connection.close()

    print("BioTrack database initialized successfully.")


# ==========================================
# RUN
# ==========================================

if __name__ == "__main__":

    initialize_database()