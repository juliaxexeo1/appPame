from app.extensions import db

class Paciente(db.Model):
    __tablename__='paciente'
    id=db.Column(db.Integer, primary_key=True)
    nome=db.Column(db.String(30),nullable=False)
    cpf=db.Column(db.Integer,nullable=False)
    temperatura=db.Column(db.Integer,nullable=False)
    pressao=db.Column(db.Integer,nullable=False)
    data_de_nascimento=db.Column(db.DateTime,nullable=False)
    
    consultas=db.relationship('Consulta',backref='paciente')
    exames=db.relationship('Exame',backref='paciente')

