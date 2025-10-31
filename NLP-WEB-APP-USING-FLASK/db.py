import json
import os
import hashlib
from config import Config

class Database:
    def __init__(self):
        self.filename = Config.DB_FILENAME

        # Create file with empty dict if it doesn't exist or is empty
        if not os.path.exists(self.filename) or os.path.getsize(self.filename) == 0:
            with open(self.filename, 'w') as f:
                json.dump({}, f, indent=4)

    def hash_password(self, password):
        """Hash a password for storing."""
        return hashlib.sha256(password.encode()).hexdigest()

    def insert(self, name, email, password):
        try:
            # Read existing users
            with open(self.filename, 'r') as f:
                try:
                    users = json.load(f)
                except json.JSONDecodeError:
                    users = {}

            # Check if email already exists
            if email in users:
                return 0

            # Hash the password before storing
            hashed_password = self.hash_password(password)

            # Add new user
            users[email] = [name, hashed_password]

            # Write back to file
            with open(self.filename, 'w') as f:
                json.dump(users, f, indent=4)
            return 1

        except Exception as e:
            print(f"Error in insert: {str(e)}")
            return 0

    def search(self, email, password):
        try:
            # Read existing users
            with open(self.filename, 'r') as f:
                try:
                    users = json.load(f)
                except json.JSONDecodeError:
                    users = {}

            # Check credentials
            if email in users:
                # Hash the provided password and compare with stored hash
                hashed_password = self.hash_password(password)
                if users[email][1] == hashed_password:
                    return 1
            return 0

        except Exception as e:
            print(f"Error in search: {str(e)}")
            return 0
