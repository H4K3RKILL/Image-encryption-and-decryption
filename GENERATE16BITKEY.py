import hashlib
import os
# Generate a random string of 32 characters
random_string = os.urandom(32).hex()

# Hash the random string with MD5 to create a 16-byte digest
key_hash = hashlib.md5(random_string.encode('ascii')).digest()

# Ensure the key is 16 bytes long
key = key_hash[:16]

print(f"Generated 16-byte key: {key.hex()}")