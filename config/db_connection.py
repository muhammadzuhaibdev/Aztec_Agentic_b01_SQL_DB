from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DB_URI=""

engine = create_engine(DB_URI)
SessionLocal = sessionmaker(bind=engine)