from app import app, db
from models import User

with app.app_context():
    # Create database tables
    db.create_all()
    
    # Create admin user
    admin = User(
        username='admin',
        special_code='CIS-ADMIN-2024'
    )
    admin.set_password('admin2024')
    
    # Create investigator
    investigator = User(
        username='investigator1'
    )
    investigator.set_password('secure123')
    
    # Add to database
    db.session.add(admin)
    db.session.add(investigator)
    db.session.commit()
    
    print("Users created successfully!")
    print("Admin: admin / admin2024 (Special: CIS-ADMIN-2024)")
    print("Investigator: investigator1 / secure123")
