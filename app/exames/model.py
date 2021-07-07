from app.extensions import db
#ghasla

class Exame(db.Model):
    __tablename__='Exame'
    id=db.Column(db.Integer, primary_key=True)
    tipodeexame=db.Column(db.String(30),nullable=False)
    data=db.Column(db.Integer,nullable=False)
    hora=db.Column(db.Integer,nullable=False)

    paciente_id = db.Column(db.Integer,db.ForeignKey('paciente.id'))