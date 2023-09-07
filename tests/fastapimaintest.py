from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Configure the database connection
DATABASE_URL = "sqlite:///C:\\Users\\User\\Desktop\\test.db"
engine = create_engine(DATABASE_URL, echo=True)  # Set echo to True for database logging

# Define SQLAlchemy models
Base = declarative_base()

class Cars(Base):
    __tablename__ = "Cars"

    id = Column(Integer, primary_key=True, index=True)
    mark = Column(String, index=True)
    date = Column(Date)

# Create the FastAPI app
app = FastAPI()

# SQLAlchemy session setup
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/cars/")
async def list_cars():
    db = SessionLocal()
    cars = db.query(Cars).all()
    db.close()
    return cars

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
