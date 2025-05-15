from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    # created_at = db.Column(db.DateTime, default=datetime.utcnow)
    # basic_info = db.relationship('BasicInfo', backref='user', lazy=True)
    # document_submission = db.relationship('DocumentSubmission', backref='user', lazy=True)

    def __repr__(self):
        return f"<User {self.name}>"

class BasicInfo(db.Model):
    __tablename__ = 'basic_info'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    middle_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50), nullable=False)
    dob = db.Column(db.Date)
    guardian_name = db.Column(db.String(100), nullable=False)
    
    # Contact Information
    email = db.Column(db.String(120), unique=True, nullable=False)
    mobile_number = db.Column(db.String(15), nullable=False)
    
    # Address Information
    permanent_address = db.Column(db.String(200), nullable=False)
    permanent_district = db.Column(db.String(50), nullable=False)
    permanent_state = db.Column(db.String(50), nullable=False)
    permanent_pincode = db.Column(db.String(10), nullable=False)
    
    temporary_address = db.Column(db.String(200))
    temporary_district = db.Column(db.String(50))
    temporary_state = db.Column(db.String(50))
    temporary_pincode = db.Column(db.String(10))
    is_same_as_permanent = db.Column(db.Boolean, default=False)
    
    employment_status = db.Column(db.String(20), nullable=False)
    category = db.Column(db.String(10), nullable=False)  # Changed to only ECR/Non-ECR
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<BasicInfo {self.first_name} {self.last_name}>"

class DocumentSubmission(db.Model):
    __tablename__ = 'document_submission'
    id = db.Column(db.Integer, primary_key=True)
    address_proof = db.Column(db.String(200))
    dob_proof = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<DocumentSubmission {self.id}>"
