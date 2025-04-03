"""Initialize the database tables."""

# init_db.py

from database import Base, engine
from models import OAuthToken  # <-- Explicitly import your model

print("Creating database tables...")
Base.metadata.create_all(bind=engine)
print("Tables created successfully!")
