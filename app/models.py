from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app import db


class Movie(db.Model):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    title = Column(String(120), nullable=False)
    release_date = Column(DateTime, nullable=False)

    actors = relationship(
        "Actor",
        back_populates="movie",
        cascade="all, delete-orphan",
        lazy="selectin"
    )

    def format(self):
        return {
            "id": self.id,
            "title": self.title,
            "release_date": self.release_date.isoformat() if self.release_date else None,
            "actors": [actor.format() for actor in self.actors]
        }

    def __repr__(self):
        return f"<Movie {self.id} - {self.title}>"


class Actor(db.Model):
    __tablename__ = "actors"

    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String(16), nullable=False)

    movie_id = Column(Integer, ForeignKey("movies.id", ondelete="CASCADE"), nullable=True)
    movie = relationship("Movie", back_populates="actors")

    def format(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "movie_id": self.movie_id
        }

    def __repr__(self):
        return f"<Actor {self.id} - {self.name}>"
