from app import db

class users(db.Model):
    uuid = db.Column(db.String(36), primary_key=True, nullable=False, unique=True)
    name = db.Column(db.String(20), nullable=False)
    fancyname = db.Column(db.String(20), nullable=False)
    document = db.Column(db.String(11), nullable=False, unique=True)
    phone = db.Column(db.String(11), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(30), nullable=False, unique=True)

    def to_json(self):
        return {
            "uuid": self.uuid,
            "name": self.name,
            "fancyname": self.fancyname,
            "document": self.document,
            "phone": self.phone,
            "password": self.password
        }