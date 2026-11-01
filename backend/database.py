
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Local SQLite database
DATABASE_URL = "sqlite:///./meals.db"

# Connect to the database
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Create database sessions
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class for database tables
Base = declarative_base()


# Open and close database connections safely
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
