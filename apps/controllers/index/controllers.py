from flask import Blueprint

from apps.common.response import ok
from config import Config

app = Blueprint('index', __name__, url_prefix='/')

@app.route('/', methods=['GET'])
def index():
    return ok('Index')
