from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Meeting(db.Model):
    __tablename__ = 'meeting'  # Name of the table in the database

    id = db.Column(db.Integer, primary_key=True)
    start_hour = db.Column(db.DateTime, nullable=False)
    end_hour = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.String(255), nullable=True)
    mail = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    color = db.Column(db.String(255), nullable=True)

    def __init__(self, start_hour, end_hour, description, mail,title,color):
        self.start_hour = start_hour
        self.end_hour = end_hour
        self.description = description
        self.mail = mail
        self.title = title
        self.color = color
