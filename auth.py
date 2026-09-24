from passlib.context import CryptContext
from user import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def signup(user_id, email, plain_password):
    hashed_password = pwd_context.hash(plain_password)
    new_user = User(user_id, email, hashed_password)
    return new_user