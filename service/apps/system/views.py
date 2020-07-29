from flask import Blueprint, make_response, request

system_bp = Blueprint('system', __name__)


@system_bp.route('/ping')
def ping() -> dict:
    return {'message': 'PONG'}


@system_bp.route('/healthcheck')
def health_check() -> dict:
    return {'message': 'OK'}
