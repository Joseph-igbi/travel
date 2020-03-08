

from application import db


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return ''.join(['ID: ',  self.id, '\r\n', 'City: ', self.city_name])
        
