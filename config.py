import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'criminal-investigation-secret-key-2024')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///../database/criminals.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'jwt-secret-key-2024')
    UPLOAD_FOLDER = '../uploads'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    
    # ML Model paths
    DECISION_TREE_MODEL = 'ml_models/decision_tree.pkl'
    NAIVE_BAYES_MODEL = 'ml_models/naive_bayes.pkl'
    
    # Biometric thresholds
    FACE_MATCH_THRESHOLD = 0.6
    FINGERPRINT_MATCH_THRESHOLD = 0.7