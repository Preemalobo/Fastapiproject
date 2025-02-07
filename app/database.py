from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base


DATABSE_URL="sqlite:///items.db"
engine=create_engine(DATABSE_URL) #Connects to the Database

#Sessions are like helper, where we are setting the rules , how it should work
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

#This which creates a fresh session for interacting with the database
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:  #clses the session after using to avoid data leakage
        db.close()

#   Base is like a blueprint for database tables, and creates the tables accordingly.
Base.metadata.create_all(bind=engine)

"""
    engine=create_engine(DATABASE_URL) → Creates a library (database).
    SessionLocal=sessionmaker(...) → Prepares librarians (sessions) to manage books.
    get_db() → Gives a librarian whenever someone needs a book.
    Base.metadata.create_all(bind=engine) → Sets up bookshelves (tables) in the library.

"""