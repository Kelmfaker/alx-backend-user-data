#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, Blueprint, abort
from api.v1.views import app_views

app_views = Blueprint('app_views', __name__)


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ GET /api/v1/status
    Return:
      - the status of the API
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """ GET /api/v1/stats
    Return:
      - the number of each objects
    """
    from models.user import User
    stats = {}
    stats['users'] = User.count()


@app_views.route('/api/v1/unauthorized', methods=['GET'])
def unauthorized_endpoint():
    """
    Get method
    """
    abort(401)


@app_views.route('/api/v1/forbidden', methods=['GET'])
def forbidden_endpoint():
    """
    Get method
    """
    abort(403)
