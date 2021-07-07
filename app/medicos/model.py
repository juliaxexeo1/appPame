from app.extensions import db

class Medico(db.Model):
    __tablename__='medico'
    id=db.Column(db.Integer, primary_key=True)
    nome=db.Column(db.String(30),nullable=False)
    especialidade=db.Column(db.String(30),nullable=False)
    crm=db.Column(db.Integer,nullable=False)

    consultas=db.relationship('Consulta',backref='medico')