from flask import Blueprint, request, jsonify
from .sdk import process_feedback

api_blueprint = Blueprint('api', __name__, url_prefix='/api')

@api_blueprint.route('/feedback', methods=['POST'])
def feedback():
    """
    Receives user feedback from the Quarkus app and
    submits it to Argilla via the SDK.
    """
    data = request.get_json()
    result = process_feedback(data)
    return jsonify(result)


def register_routes(app):
    app.register_blueprint(api_blueprint)
