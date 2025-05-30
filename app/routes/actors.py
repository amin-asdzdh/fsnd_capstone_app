from flask import Blueprint, jsonify, request, abort
from sqlalchemy.exc import IntegrityError

from app.auth import requires_auth

from ..models import Actor, db

actors_bp = Blueprint('actors', __name__)


@actors_bp.route('/', methods=['GET'])
@requires_auth("get:actors")
def actors_get():
    actors = Actor.query.all()
    return jsonify({"success": True, "actors": [a.format() for a in actors]})


@actors_bp.route('/', methods=['POST'])
@requires_auth("post:actors")
def actors_post():
    data = request.get_json()
    if not data:
        # malformed/missing JSON
        abort(400)
    try:
        actor = Actor(**data)
        db.session.add(actor)
        db.session.commit()
        return jsonify({"success": True, "actor": actor.format()})
    except IntegrityError:
        db.session.rollback()
        abort(422)
    except Exception:
        db.session.rollback()
        abort(400)

@actors_bp.route('/<int:actor_id>', methods=['DELETE'])
@requires_auth("delete:actors")
def actors_delete(actor_id):
    actor = Actor.query.get(actor_id)
    if not actor:
        abort(404)

    try:
        db.session.delete(actor)
        db.session.commit()
        return jsonify({"success": True, "deleted": actor_id})
    except Exception:
        db.session.rollback()
        abort(500)

@actors_bp.route('/<int:actor_id>', methods=['PATCH'])
@requires_auth("patch:actors")
def actors_patch(actor_id):
    actor = Actor.query.get(actor_id)
    if not actor:
        abort(404)

    data = request.get_json()
    try:
        if "name" in data:
            actor.name = data["name"]
        if "age" in data:
            actor.age = data["age"]
        if "gender" in data:
            actor.gender = data["gender"]

        db.session.commit()
        return jsonify({"success": True, "actor": actor.format()})
    except Exception:
        db.session.rollback()
        abort(400)