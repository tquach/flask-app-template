from flask import Blueprint, make_response, request

from service.apps.auth.models import Account

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/')
def login():
    return {'records': Account.query.all()}


