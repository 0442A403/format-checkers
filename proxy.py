from os import environ

import requests
from flask import Flask, request, Response

app: Flask = Flask(__name__)

format_to_host = {
    format_json.split('=')[0]: format_json.split('=')[1]
    for format_json in environ['HOSTS'].split(":")
}


@app.route('/get_result/', methods=['GET'])
def get_result():
    if 'check-format' not in request.headers \
            or request.headers['check-format'] not in format_to_host:
        return Response('Bad check-format header', status=400)

    response = requests.get(format_to_host[request.headers['check-format']],
                            data=request.data,
                            headers={
                                key: value for key, value in request.headers
                            })

    return Response(
        response.raw,
        status=response.status_code
    )


if __name__ == "__main__":
    app.run()
