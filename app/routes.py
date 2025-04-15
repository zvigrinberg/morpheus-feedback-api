from flask import Blueprint, request, jsonify
from .sdk import process_request

api_blueprint = Blueprint('api', __name__, url_prefix='/api')


@api_blueprint.route('/process', methods=['POST'])
def process():
    data = request.get_json()  # Retrieve incoming feedback data
    result = process_request(data)  # Process data with Argilla SDK helper
    return jsonify(result)


def register_routes(app):
    app.register_blueprint(api_blueprint)
