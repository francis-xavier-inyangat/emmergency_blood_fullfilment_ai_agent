from app import db
from datetime import datetime
import uuid

def generate_uuid():
    return str(uuid.uuid4())

class Patient(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    name = db.Column(db.String(100), nullable=False)
    blood_type = db.Column(db.String(5), nullable=False)
    contact = db.Column(db.String(20))
    location = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    requests = db.relationship('BloodRequest', backref='patient', lazy=True)

class Hospital(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(200))
    contact = db.Column(db.String(20))
    inventory = db.relationship('BloodInventory', backref='hospital', lazy=True)

class BloodBank(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(200))
    contact = db.Column(db.String(20))
    inventory = db.relationship('BloodInventory', backref='blood_bank', lazy=True)

class BloodInventory(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    blood_type = db.Column(db.String(5), nullable=False)
    quantity = db.Column(db.Integer, default=0)
    hospital_id = db.Column(db.String(36), db.ForeignKey('hospital.id'))
    blood_bank_id = db.Column(db.String(36), db.ForeignKey('blood_bank.id'))
    last_updated = db.Column(db.DateTime, default=datetime.utcnow)

class BloodRequest(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    patient_id = db.Column(db.String(36), db.ForeignKey('patient.id'))
    blood_type = db.Column(db.String(5), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    urgency = db.Column(db.String(20), default='normal')
    status = db.Column(db.String(20), default='pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow) 