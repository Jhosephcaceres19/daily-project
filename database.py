from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Ajusta con TU password real de la base de datos de Supabase
DATABASE_URL = (
    "postgresql://postgres.lwnseeoefwfwwwajloxy:daily"
    "@aws-1-us-east-2.pooler.supabase.com:6543/postgres"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
