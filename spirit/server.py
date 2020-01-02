from flask import Flask, jsonify, request
from .utils import fetcher
from . import parsers
import jsonpickle


app = Flask(__name__)


def run_server(host, port, data_dir):
    app.run(host=host, port=port)


@app.route("/get_parsers")
def available_parsers_names():
    return jsonify([parser.field.lower()
                    for parser in get_all_parsers()])


@app.route("/upload_snapshot", methods=['POST'])
def handle_snapshot():
    snapshot = jsonpickle.decode(request.get_json())
    return ""


def get_all_parsers():
    return get_all_class_parsers()+get_all_func_parsers()


def get_all_class_parsers():
    available_parsers = [cls
                         for cls in fetcher.get_all_classes(parsers)
                         if "parse" in cls.__name__.lower()]
    return available_parsers


def get_all_func_parsers():
    available_parsers = [f
                         for f in fetcher.get_all_funcs(parsers)
                         if "parse" in f.__name__.lower()]
    return available_parsers
