from backend.freight.model import Freight

def get_freight_all():
    return Freight.query.all()



def get_freight_items_by_page(current_page, page_size):
    return Freight.query.paginate(current_page, page_size, error_out=False)


def get_freight_by_id(id):
    return Freight.query.filter(Freight.id == id).first()

def update_freight(id, data):
    return Freight.query.filter(Freight.id == id).update(data)