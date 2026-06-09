from datetime import datetime, timedelta, timezone
import jwt

SECRET_KEY = "temp"
ALGORITHM = "HS256"

def encode_token(data : dict):
    payload = data.copy()
    payload["exp"] = datetime.now(timezone.utc) + timedelta(hours=1)
    encode_jwt = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
    
    return encode_jwt

def decode_token(data : dict):
    return jwt.decode(
        data['token'],
        SECRET_KEY,
        algorithms=ALGORITHM
        )