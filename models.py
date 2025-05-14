from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<User {self.name}>"

class BasicInfo(db.Model):
    __tablename__ = 'basic_info'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    middle_name = db.Column(db.String(100), nullable=True)
    last_name = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    guardian_name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    district = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    pincode = db.Column(db.String(10), nullable=False)
    employment_status = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<BasicInfo {self.first_name} {self.last_name}>"

class DocumentSubmission(db.Model):
    __tablename__ = 'document_submission'
    id = db.Column(db.Integer, primary_key=True)
    address_proof = db.Column(db.String(200), nullable=True)  # Path to uploaded file
    dob_proof = db.Column(db.String(200), nullable=True)      # Path to uploaded file
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<DocumentSubmission {self.id}>"