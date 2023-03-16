from bson import ObjectId
from flask import jsonify
from utils.db import db


class User:
    """User module. Methods: create_user()"""

    def __init__(self, name, email, password) -> None:
        self.name = name
        self.email = email
        self.password = password

    def create_user(self, user):
        """This function creates a new user"""
        user = User(name=user["name"], email=user["email"], password=user["password"])
        result = db.users.insert_one(user.__dict__)
        user._id = str(result.inserted_id)
        return user.__dict__

    def get_all_users(self):
        """This function list all the users"""
        users = db.users.find()
        user_list = []
        for user in users:
            user["_id"] = str(user["_id"])
            user_list.append(user)
        return jsonify(user_list)

    def get_user(self, id):
        """This function get specific user using id"""
        user = db.users.find_one({"_id": ObjectId(id)})
        if user is None:
            return jsonify({"error": "User not found"}), 404
        user["_id"] = str(user["_id"])
        return jsonify(user), 200

    def update_user(self, id, new_data):
        """This function update a specific user data"""
        user = db.users.find_one({"_id": ObjectId(id)})
        if user is None:
            return jsonify({"error": "User not found"}), 404
        result = db.users.update_one({"_id": ObjectId(id)}, {"$set": new_data})
        if result.modified_count == 1:
            return jsonify({"message": "User updated successfully"}), 200
        else:
            return jsonify({"message": "User update failed"}), 201

    def delete_user(self, id):
        result = db.users.delete_one({"_id": ObjectId(id)})
        if result.deleted_count == 1:
            return jsonify({"message": "User deleted successfully"}), 200
        else:
            return jsonify({"error": "User not found"}), 404
