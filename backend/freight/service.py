from backend.freight.repertory import get_freight_by_id
from backend.database.database import db
from datetime import datetime
from backend.freight.model import Freight

def update_freight_with_data(freight_id, data):
    try:
        freight = get_freight_by_id(freight_id)
        if freight:
            freight.date = data['date'] if 'date' in data else None
            freight.number = data['number'] if 'number' in data else None
            freight.name = data['name'] if 'name' in data else None
            freight.piece = data['piece'] if 'piece' in data else None
            freight.cube = data['cube'] if 'cube' in data else None
            freight.weight = data['weight'] if 'weight' in data else None
            freight.imprest = data['imprest'] if 'imprest' in data else None
            freight.package_number = data['package_number'] if 'package_number' in data else None
            freight.room = data['room'] if 'room' in data else None
            freight.update_at = datetime.utcnow()
        else:
            freight = Freight()
            print(freight)
            freight.date = data['date'] if 'date' in data else None
            freight.number = data['number'] if 'number' in data else None
            freight.name = data['name'] if 'name' in data else None
            freight.piece = data['piece'] if 'piece' in data else None
            freight.cube = data['cube'] if 'cube' in data else None
            freight.weight = data['weight'] if 'weight' in data else None
            freight.imprest = data['imprest'] if 'imprest' in data else None
            freight.package_number = data['package_number'] if 'package_number' in data else None
            freight.room = data['room'] if 'room' in data else None
            freight.update_at = datetime.utcnow()
            db.session.add(freight)
    except Exception as err:
        print("update failed err:", str(err))
        return False
            
    db.session.commit()
    return True

def delete_freight_with_id(freight_id):
    freight = get_freight_by_id(freight_id)
    if freight:
        freight.deleted = True
        freight.update_at = datetime.utcnow()
        db.session.commit()
        return True
    return False