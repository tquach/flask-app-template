import os
from flask import Flask

app = Flask(__name__)
app_env = os.getenv('FLASK_ENV')
app.config.from_object(f'service.settings.{app_env}')

from service.apps.system.views import system_bp
app.register_blueprint(system_bp, url_prefix='/v1/')

from service.apps.auth.views import auth_bp
app.register_blueprint(auth_bp, url_prefix='/v1/auth')
