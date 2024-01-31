from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class HashPassword:
    def create_hash(self, password: str):
        return pwd_context.hash(password)

    def verify_hash(self, plain_passwod: str, hashed_password: str):
        return pwd_context.verify(plain_passwod, hashed_password)
        



