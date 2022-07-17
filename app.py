import os
import mypy
from flask import Flask, request, Response
from flask_restx import abort

from functions import make_query

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.post("/perform_query")
def perform_query() -> Response:
    # нужно взять код из предыдущего ДЗ
    # добавить команду regex
    # добавить типизацию в проект, чтобы проходила утилиту mypy app.py
    cnd_1 = request.args.get('cnd_1')
    val_1 = request.args.get('val_1')
    cnd_2 = request.args.get('cnd_2')
    val_2 = request.args.get('val_2')
    file_name = request.args.get('file_name')
    if not (cnd_1 and file_name):
        abort(400)
    file_path = os.path.join(DATA_DIR, str(file_name))
    if not os.path.exists(file_path):
        return abort(400)
    if cnd_1 not in ["filter", "map", "unique", 'sort', "limit"]:
        return abort(400)
    with open(file_path) as file:
        res = make_query(cnd_1, str(val_1), file)
        if cnd_2 and cnd_2 not in ["filter", "map", "unique", 'sort', "limit"]:
            return abort(400)
        res = make_query(str(cnd_2), str(val_2), iter(res))
    return app.response_class("\n".join(res), content_type="text/plain")
