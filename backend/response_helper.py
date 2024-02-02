from typing import NewType, Tuple, Optional
from flask import jsonify

JsonResponse = NewType("JsonResponse", Tuple[str, int])


def bad_request_with_data(data=None, code=400):
    return jsonify(data or {}), code


def success(data: Optional[dict] = None) -> JsonResponse:
    return JsonResponse((jsonify(data or {}), 200))
