import os

# from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


db.execute("CREATE TABLE users (id SERIAL PRIMARY KEY, user VARCHAR NOT NULL, password VARCHAR NOT NULL")


db.execute("INSERT INTO passengers (name, flight_id) VALUES (:name, :flight_id)",
        {"name": name, "flight_id": flight_id})
db.commit()
