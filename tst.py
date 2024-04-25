import hashlib

# Original string
original_string = "Hello, world!"

# Hash the original string using SHA-256
sha256_hash = hashlib.sha256()
sha256_hash.update(original_string.encode('utf-8'))
hashed_value = sha256_hash.hexdigest()

# Later, if you want to check if a new string matches the original
new_string = "Hello, world!"

# Hash the new string
sha256_hash_new = hashlib.sha256()
sha256_hash_new.update(new_string.encode('utf-8'))
hashed_value_new = sha256_hash_new.hexdigest()

# Compare the hashed values
if hashed_value_new == hashed_value:
    print("The new string matches the original.")
else:
    print("The new string does not match the original.")
