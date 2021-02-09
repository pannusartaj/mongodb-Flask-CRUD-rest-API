from flask import Flask, jsonify, render_template, request

from crud import MongoCRUD
from error import UnsupportedRequestError

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config["APPLICATION_ROOT"] = "/api/"

VALID_FORMAT = ("song", "podcast", "audio_book")


@app.route('/healthcheck')
def healthcheck():
    return 'OK'


@app.route('/crud/<audi_file_type>/', methods=["GET", "POST"])
@app.route('/crud/<audi_file_type>/<audi_file_id>', methods=["GET", "DELETE", "PUT"])
def api_crud(audi_file_type=None, audi_file_id=None):
    try:
        if audi_file_type not in VALID_FORMAT:
            raise UnsupportedRequestError(
                "Only formats {} are allowed".format(", ".join(VALID_FORMAT)))
        request_method = request.method

        if request_method == "GET":
            data_obj = MongoCRUD(audi_file_type, id=audi_file_id)
            return jsonify(data_obj.read())

        if request_method == "DELETE":
            data_obj = MongoCRUD(audi_file_type, id=audi_file_id)
            return jsonify(data_obj.delete())

        if request_method == "PUT":
            data = request.json
            data_obj = MongoCRUD(audi_file_type, id=audi_file_id, data=data)
            return jsonify(data_obj.update())

        if request_method == "POST":
            data = request.json
            data_obj = MongoCRUD(audi_file_type, id=audi_file_id, data=data)
            return jsonify(data_obj.create())

    except UnsupportedRequestError as error:
        return {"result": {"error": error.message}}, 422

    except Exception as exc:
        return {"result": {"error": str(exc)}}, 500
