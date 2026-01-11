from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import bcrypt

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), default='investigator')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    special_code = db.Column(db.String(50), unique=True)
    
    def set_password(self, password):
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))

class Criminal(db.Model):
    __tablename__ = 'criminals'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    crime_type = db.Column(db.String(100))
    crime_severity = db.Column(db.String(20))  # Low, Medium, High
    prior_convictions = db.Column(db.Integer, default=0)
    last_known_location = db.Column(db.String(200))
    status = db.Column(db.String(20), default='Wanted')  # Wanted, Arrested, Released
    photo_path = db.Column(db.String(300))
    fingerprint_path = db.Column(db.String(300))
    facial_features = db.Column(db.Text)  # JSON string of facial features
    fingerprint_template = db.Column(db.Text)  # Fingerprint template data
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    
    # Additional biometric data
    height = db.Column(db.Float)
    weight = db.Column(db.Float)
    eye_color = db.Column(db.String(20))
    hair_color = db.Column(db.String(20))
    scars_marks = db.Column(db.Text)
    dna_sample_id = db.Column(db.String(50))
    
    # Prediction features
    recidivism_score = db.Column(db.Float)
    danger_level = db.Column(db.String(20))
    predicted_crime_type = db.Column(db.String(100))