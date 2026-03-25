import hashlib

def convert_hash(text):
    text = text.encode('utf-8')
    t = hashlib.sha256(text)
    return t.hexdigest()