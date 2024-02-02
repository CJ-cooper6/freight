from backend.freight.model import Freight

def get_freight_all():
    return Freight.query.all()