from backend.freight.repertory import get_freight_all, get_freight_items_by_page
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


# @bp.route("/freight", methods=["PUT"])
# def update_freight():
#     data = request.get_json()
#     updated_todo = update_todo(todo_id, title=data.get("title"), completed=data.get("completed"))
#     if updated_todo:
#         return success({"updated_todo": updated_todo})
#     return bad_request_with_data({"error": "Todo not found"}, 404)
