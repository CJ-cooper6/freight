from backend.freight.repertory import update_freight
from backend.database.database import db

def update_freight_with_data(freight_id, data):
    freight = update_freight(freight_id, data)
    if freight:
        db.session.commit()
        return True
    return False