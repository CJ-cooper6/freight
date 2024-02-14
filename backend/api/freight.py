from backend.freight.repertory import get_freight_all, get_freight_items_by_page
from backend.freight.service import update_freight_with_data
from backend.response_helper import success, bad_request_with_data
from backend.api import bp
from backend.request_helper import get_pagination
from flask import request


@bp.route("/freight", methods=["GET"])
def get_freight():
    current_page, page_size = get_pagination()
    items = get_freight_items_by_page(current_page, page_size)
    serialized_items = [item.to_dict() for item in items.items]
    return success({"total": items.total, "freight_items": serialized_items})


@bp.route("/freight/<int:freight_id>", methods=["PUT"])
def update_freight(freight_id):
    data = request.get_json()
    print(data)
    if update_freight_with_data(freight_id, data):
        return success({"message": "ok"})
    return bad_request_with_data({"error": "Freight update failed"}, 404)
