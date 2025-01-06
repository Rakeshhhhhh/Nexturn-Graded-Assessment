from app import create_app, db

def create_database():
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
        print("Database tables created successfully!")

app = create_app()

if __name__ == "__main__":
    create_database()  
    app.run(debug=True)