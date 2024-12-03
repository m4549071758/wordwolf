from flask import Flask, request, jsonify
from flask_json import FlaskJSON
from flasgger import Swagger
from flasgger.utils import swag_from
from uuid_extensions import uuid7str
from werkzeug.middleware.proxy_fix import ProxyFix
import os

app = Flask(__name__)
URL_PREFIX = "/api"

FlaskJSON(app)
app.config["JSON_AS_ASCII"] = False

app.config["SWAGGER"] = {
    "title": "ワードウルフ API",
    "uiversion": 3,
    "version": "1.0.0",
}
swagger = Swagger(app)

app.wsgi_app = ProxyFix(app.wsgi_app)