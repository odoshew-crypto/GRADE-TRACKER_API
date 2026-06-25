from sqlalchemy.orm import sessionmaker # is a function that creates a new SQLAlchemy sessionmaker instance, which is used to create new database sessions.
from sqlalchemy import create_engine # is a function that creates a new SQLAlchemy engine instance, which is used to connect to the database.
from sqlalchemy.ext.declarative import declarative_base # is a function that creates a new SQLAlchemy declarative base class, which is used to define the database models.

DATABASE_URL = "sqlite:///./grade.db"
# the engine is the actual connection to the dayabase, and it is created using the create_engine function from SQLAlchemy. The DATABASE_URL variable specifies the location of the SQLite database file, which is located in the current directory and named grade.db.
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False}) # creates a new SQLAlchemy engine instance that connects to the SQLite database specified by DATABASE_URL. The connect_args parameter is used to specify additional connection arguments, in this case, to allow multiple threads to access the database.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # creates a new SQLAlchemy sessionmaker instance that is bound to the engine.
Base = declarative_base() # creates a new SQLAlchemy declarative base class that is used to define the database models.


def get_db(): # is a function that returns a new database session. It is used to create a new session for each request to the API.
    db = SessionLocal() # creates a new database session using the SessionLocal instance.
    try:
        yield db # yields the database session to the caller.
    finally:
        db.close() # closes the database session when the request is complete.