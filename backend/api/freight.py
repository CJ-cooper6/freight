from backend.freight.repertory import get_freight_all
from backend.response_helper import success
from backend.api import bp


@bp.route('/freight', methods=["GET"])
def get_all_freight():
    result = get_freight_all()
    return success(result)
