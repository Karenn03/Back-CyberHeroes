from cryptography.fernet import Fernet
from dto.userDto import UserDTO
from repositories.userRepository import UserRepository
import os

class UserService:
    def __init__(self, db_session):
        self.user_repository = UserRepository(db_session)
        
        self.key = os.getenv('FERNET_KEY').encode()
        self.cipher_suite = Fernet(self.key)

    def _encrypt_password(self, password: str) -> str:
        encrypted_password = self.cipher_suite.encrypt(password.encode())  # Encriptar la contraseña
        return encrypted_password.decode()  # Convertir a string para almacenamiento

    def _decrypt_password(self, encrypted_password: str) -> str:
        decrypted_password = self.cipher_suite.decrypt(encrypted_password.encode())  # Desencriptar la contraseña
        return decrypted_password.decode()  # Convertir a string

    def _validate_score(self, score: int):
        if not isinstance(score, int) or score < 0:
            raise ValueError(f"Score must be a non-negative integer, got {score}")

    def get_all_users(self):
        try:
            users = self.user_repository.get_all()
            return [UserDTO(user.idUser, user.idCard, user.names, user.surnames, user.email, user.password, user.score) for user in users]
        except Exception as e:
            raise Exception(f"Error retrieving all users: {e}")

    def get_user_by_id(self, user_id):
        try:
            user = self.user_repository.get_by_id(user_id)
            if user:
                return UserDTO(user.idUser, user.idCard, user.names, user.surnames, user.email, user.password, user.score)
            return None
        except Exception as e:
            raise Exception(f"Error retrieving user by ID: {e}")

    def create_user(self, user_dto: UserDTO):
        try:
            self._validate_score(user_dto.score)
            encrypted_password = self._encrypt_password(user_dto.password)
            user_dto.password = encrypted_password
            return self.user_repository.add(user_dto)
        except Exception as e:
            raise Exception(f"Error creating user: {e}")

    def update_user(self, user_id, user_dto: UserDTO):
        try:
            self._validate_score(user_dto.score)
            if user_dto.password:
                user_dto.password = self._encrypt_password(user_dto.password)
            return self.user_repository.update(user_dto)
        except Exception as e:
            raise Exception(f"Error updating user: {e}")

    def delete_user(self, user_id):
        try:
            user = self.user_repository.get_by_id(user_id)
            if user:
                self.user_repository.delete(user)
            else:
                raise Exception("User not found")
        except Exception as e:
            raise Exception(f"Error deleting user: {e}")

    def verify_password(self, user_id: int, provided_password: str) -> bool:
        try:
            user = self.user_repository.get_by_id(user_id)
            if user:
                stored_password = self._decrypt_password(user.password)
                return stored_password == provided_password
            return False
        except Exception as e:
            raise Exception(f"Error verifying password: {e}")