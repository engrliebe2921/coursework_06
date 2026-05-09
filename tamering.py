from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

data = b"napier123"

token = cipher.encrypt(data)
original = cipher.decrypt(token)

tampered_token = token[:-1] + b'0'

try:
    cipher.decrypt(tampered_token)
    print("Tampered token decrypted (unexpected)")
except:
    print("Decryption failed (expected)")
