from passlib.context import CryptContext
from user import User
import jwt
from datetime import datetime, timedelta

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def signup(user_id, email, plain_password):
    hashed_password = pwd_context.hash(plain_password)
    new_user = User(user_id, email, hashed_password)
    return new_user

def login(email, plain_password, stored_user):
    if email == stored_user.email:
        if pwd_context.verify(plain_password, stored_user.hashed_password):
            return "Login Successful"
        else:
            return "Login Failed"
    else:
        return "Login failed"

SECRET_KEY = "this-is-a-placeholder-change-it-later"

def create_token(user_id):
    payload = {
        "user_id" : user_id,
        "exp" : datetime.now() + timedelta(hours=24)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

def verify_token(token):
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return decoded
    except jwt.InvalidTokenError:
        return None