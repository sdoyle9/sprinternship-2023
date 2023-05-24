from __init__ import *
# from models import *

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        # db.drop_all()  # Drop all existing tables
        db.create_all()  # Create new tables according to the current models
    app.run(debug=False)