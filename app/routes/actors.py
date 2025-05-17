from flask import Blueprint, jsonify, request, abort
from ..models import Actor, db

actors_bp = Blueprint('actors', __name__)


@actors_bp.route('/', methods=['GET'])
def actors_get():
    actors = Actor.query.all()
    return jsonify({"success": True, "actors": [a.format() for a in actors]})


@actors_bp.route('/', methods=['POST'])
def actors_post():
    data = request.get_json()
    try:
        actor = Actor(**data)
        db.session.add(actor)
        db.session.commit()
        return jsonify({"success": True, "actor": actor.format()})
    except Exception:
        db.session.rollback()
        abort(400)

@actors_bp.route('/<int:actor_id>', methods=['DELETE'])
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