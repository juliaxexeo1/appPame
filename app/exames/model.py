from app.extensions import db

class Exame(db.Model):
    __tablename__='Exame'
    id=db.Column(db.Integer, primary_key=True)
    tipodeexame=db.column(db.String(30),nullable=False)
    data=db.column(db.Integer,nullable=False)
    hora=db.column(db.Integer,nullable=False)