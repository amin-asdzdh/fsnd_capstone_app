from flask import Blueprint, jsonify

from app.auth import requires_auth
from ..models import Movie

movies_bp = Blueprint('movies', __name__)


@movies_bp.route('/', methods=['GET'])
@requires_auth("get:movies")
def movies_get():
    movies = Movie.query.all()
    return jsonify({"success": True, "movies": [m.format() for m in movies]})
