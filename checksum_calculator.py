import hashlib

def calculate_checksum(file_path, algorithm="sha256"):
    hash_func = hashlib.new(algorithm)
    
    with open(file_path, "rb") as f:
        while chunk := f.read(8192):  # Read in chunks
            hash_func.update(chunk)
    
    return hash_func.hexdigest()


file_path = "example.txt"
checksum = calculate_checksum(file_path, "sha256")
print(f"SHA-256 Checksum: {checksum}")
