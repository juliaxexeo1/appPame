from app.extensions import db

class Consulta(db.Model):
    __tablename__='consulta'
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Integer ,nullable=False)
    hora = db.Column(db.Integer,nullable=False)

    medico_id = db.Column(db.Integer,db.ForeignKey('medico.id'))
    paciente_id = db.Column(db.Integer,db.ForeignKey('paciente.id')) 
    receitas=db.relationship('Receita',backref='consulta')
    
