from flask import Blueprint, render_template, jsonify, request
from .models import User  # Importer le modèle User
from . import db

# Définir le Blueprint
main = Blueprint('main', __name__)

# Route pour obtenir tous les utilisateurs
@main.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    users_data = [{"id": user.id, "username": user.username, "email": user.email} for user in users]
    return jsonify(users_data)

# Route pour ajouter un utilisateur
@main.route('/api/users', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = User(username=data['username'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User added successfully"}), 201
