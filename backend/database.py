# ==========================================
# IMPORTS
# ==========================================

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# ==========================================
# DATABASE CONFIGURATION
# ==========================================

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_URL = f"sqlite:///{BASE_DIR / "database" / "biotrack.db"}"


# ==========================================
# ENGINE
# ==========================================

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)


# ==========================================
# SESSION FACTORY
# ==========================================

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# ==========================================
# DATABASE SESSION DEPENDENCY
# ==========================================

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()