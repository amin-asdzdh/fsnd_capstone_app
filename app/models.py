from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
from app import db


actor_movie = db.Table(
    "actor_movie",
    db.Column("actor_id", db.Integer, db.ForeignKey("actors.id", ondelete="CASCADE"), primary_key=True),
    db.Column("movie_id", db.Integer, db.ForeignKey("movies.id", ondelete="CASCADE"), primary_key=True),
)


class Movie(db.Model):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    title = Column(String(120), nullable=False)
    release_date = Column(DateTime, nullable=False)

    actors = relationship(
        "Actor",
        secondary=actor_movie,
        back_populates="movies",
        lazy="selectin"
    )

    def format(self):
        return {
            "id": self.id,
            "title": self.title,
            "release_date": self.release_date.isoformat(),
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

    movies = relationship(
        "Movie",
        secondary=actor_movie,
        back_populates="actors",
        lazy="selectin"
    )

    def format(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "movies": [movie.id for movie in self.movies]
        }

    def __repr__(self):
        return f"<Actor {self.id} - {self.name}>"
