from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import uvicorn

# Configure the database connection
DATABASE_URL = "sqlite:///C:\\Users\\User\\Desktop\\Test.db"
engine = create_engine(DATABASE_URL, echo=True)  # Set echo to True for database logging

# Define SQLAlchemy models
Base = declarative_base()


class Cars(Base):
    __tablename__ = "Cars"

    id = Column(Integer, primary_key=True, index=True)
    mark = Column(String, index=True)
    date = Column(String)


# Create the FastAPI app
app = FastAPI()

# SQLAlchemy session setup
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@app.get("/")
async def read_root():
    print(1, flush=True)
    db = SessionLocal()
    print(2, flush=True)
    cars = db.query(Cars).all()
    print(3, flush=True)
    print(cars, flush=True)
    db.close()
    return cars


@app.get("/cars")
async def list_cars():
    print(1, flush=True)
    db = SessionLocal()
    print(2, flush=True)

    cars = db.query(Cars).all()
    print(cars, flush=True)
    db.close()
    return {'aa': "asssssss"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
