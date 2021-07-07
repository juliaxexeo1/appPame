from app.extensions import db

class Receita(db.Model):
    __tablename__='receita'
    id=db.Column(db.Integer, primary_key=True)
    prescrição=db.Column(db.String(100))
    data=db.Column(db.Integer)

    
    consulta_id = db.Column(db.Integer,db.ForeignKey('consulta.id')) 