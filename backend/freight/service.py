from backend.freight.repertory import get_freight_by_id
from backend.database.database import db
from datetime import datetime

def update_freight_with_data(freight_id, data):
    freight = get_freight_by_id(freight_id)
    if freight:
        freight.date = data['date'] or None
        freight.number = data['number'] or None
        freight.number = data['number'] or None
        freight.name = data['name'] or None
        freight.piece = data['piece'] or None
        freight.cube = data['cube'] or None
        freight.weight = data['weight'] or None
        freight.imprest = data['imprest'] or None
        freight.package_number = data['package_number'] or None
        freight.room = data['room'] or None
        freight.update_at = datetime.utcnow()
        db.session.commit()
        return True
    return False