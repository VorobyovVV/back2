from database import Base,engine
from models import car

print("Creating database ....")

Base.metadata.create_all(engine)
