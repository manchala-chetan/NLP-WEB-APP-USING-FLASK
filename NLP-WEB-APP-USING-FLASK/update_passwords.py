import json
import hashlib
import os

def hash_password(password):
    """Hash a password for storing."""
    return hashlib.sha256(password.encode()).hexdigest()

def update_passwords():
    filename = 'users.json'
    
    # Check if file exists
    if not os.path.exists(filename):
        print(f"Error: {filename} not found")
        return
    
    # Read existing users
    with open(filename, 'r') as f:
        try:
            users = json.load(f)
        except json.JSONDecodeError:
            print(f"Error: {filename} contains invalid JSON")
            return
    
    # Update passwords with hashed versions
    for email, user_data in users.items():
        if len(user_data) >= 2:
            plain_password = user_data[1]
            hashed_password = hash_password(plain_password)
            user_data[1] = hashed_password
            print(f"Updated password for {email}")
    
    # Write back to file
    with open(filename, 'w') as f:
        json.dump(users, f, indent=4)
    
    print(f"Successfully updated passwords in {filename}")

if __name__ == "__main__":
    update_passwords()
