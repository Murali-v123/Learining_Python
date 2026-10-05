from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = 'postgresql://postgres:root@localhost:5432/murali'
engine = create_engine(db_url)

# This is what main.py needs to look for
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
