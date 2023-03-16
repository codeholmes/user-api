class User:
    """User module. Methods: create_user()"""

    @staticmethod
    def create_user(user):
        """This function creates a new user"""
        temp_users = []
        temp_users.append(
            {
                "id": user["id"],
                "name": user["name"],
                "email": user["email"],
                "password": user["password"],
            }
        )
        return temp_users
