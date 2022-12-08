from flask import request, jsonify, Blueprint
from marshmallow import ValidationError

from lesson23_project_source.builder import query_builder
from lesson23_project_source.models import RequestParams, BatchRequestParams

main_bp = Blueprint('main', __name__)


@main_bp.route("/perform_query", methods=['POST'])
def perform_query():
    try:
        params = BatchRequestParams().load(data=request.json)
    except ValidationError as r:
        return jsonify(r.messages), 400
    result = None
    for query in params['queries']:
        result = query_builder(
            cmd=query['cmd'],
            value=query['value'],
            data=result,
        )
    return jsonify(result)
