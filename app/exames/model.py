from app.extensions import db


class Exame(db.Model):
    __tablename__='Exame'
    id=db.Column(db.Integer, primary_key=True)
    tipo_de_exame=db.Column(db.String(70),nullable=False)
    atestado_medico=db.Column(db.String(100),nullable=False)
    data=db.Column(db.DateTime,nullable=False)
    hora=db.Column(db.DateTime,nullable=False)

    paciente_id = db.Column(db.Integer,db.ForeignKey('paciente.id'))

        