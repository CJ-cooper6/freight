from datetime import datetime
from backend.database import db


class Freight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))  # 品名
    piece = db.Column(db.DECIMAL(10, 4))  # 件数
    cube = db.Column(db.DECIMAL(10, 4))  # 立方
    weight = db.Column(db.DECIMAL(10, 4))  # 重量
    imprest = db.Column(db.DECIMAL(10, 4))  # 垫付款
    package_number = db.Column(db.Integer)  # 包装数
    room = db.Column(db.String(255))  # 房间
    deleted = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    update_at = db.Column(db.DateTime, default=datetime.utcnow)
