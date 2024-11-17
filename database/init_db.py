import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app, db  # Importer `app` et `db` depuis `__init__.py`
from app.models import User, Team, Match  # Importer les modèles nécessaires

def create_tables():
    with app.app_context():  # Utilisez le contexte d'application
        db.create_all()

if __name__ == '__main__':
    create_tables()
