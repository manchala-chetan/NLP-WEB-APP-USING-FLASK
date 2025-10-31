import hashlib

def hash_password(password):
    """Hash a password for storing."""
    return hashlib.sha256(password.encode()).hexdigest()

# Test with a known password
password = "1234"
hashed = hash_password(password)
print(f"Password: {password}")
print(f"Hashed: {hashed}")

# Compare with the stored hash for bhanutejasubbara@gmail.com
stored_hash = "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4"
print(f"Stored hash: {stored_hash}")
print(f"Match: {hashed == stored_hash}")

# Let's also try with some variations
print("\nTesting variations:")
variations = ["1234 ", " 1234", "1234\n", "1234\r", "1234\t"]
for var in variations:
    var_hash = hash_password(var)
    print(f"'{var}' -> {var_hash}")
    print(f"Match: {var_hash == stored_hash}")
