from app import app, db

if __name__ == '__main__':
    app.app_context().push()
    db.create_all()
    app.run(host='0.0.0.0', port=8000)
else:
    # Creates the database and tables 
    # for the production environment    
    app.app_context().push()
    db.create_all()