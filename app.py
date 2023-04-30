from typing import Dict, Type, Any

from flask import Flask, request, Response
from os import environ

from checkers.apache_avro_checker import ApacheAvroChecker
from checkers.checker import Checker
from checkers.json_checker import JsonChecker
from checkers.message_pack_checker import MessagePackChecker
from checkers.pickle_checker import PickleChecker
from checkers.xml_checker import XmlChecker
from checkers.yaml_checker import YamlChecker

app: Flask = Flask(__name__)

CHECKER_CLASSES: Dict[str, Type] = {
    "json": JsonChecker,
    "pickle": PickleChecker,
    "xml": XmlChecker,
    "message_pack": MessagePackChecker,
    "yaml": YamlChecker,
    "apache_avro": ApacheAvroChecker,
}
MAX_DATA_SIZE: int = 1000

format: str = environ['CHECK_FORMAT']
if format not in CHECKER_CLASSES:
    raise Exception("Inappropriate format")
CheckerClass: Type = CHECKER_CLASSES[format]


@app.route('/get_result/', methods=['POST'])
def get_result():
    data: bytes = request.data

    if not data \
            or 'check-format' not in request.headers \
            or request.headers['check-format'] != format \
            or (CheckerClass.need_schema and 'schema' not in request.headers):
        return Response("Bad input", status=400)

    checker: CheckerClass
    if CheckerClass.need_schema:
        checker = CheckerClass(request.headers['schema'])
    else:
        checker = CheckerClass()

    print(str(data))
    result = checker.validate_data(data)

    if result:
        return Response("Ok")
    else:
        return Response("Bad format")

if __name__ == "__main__":
    app.run()
