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

    def get_all_users(self):
        users = self.user_repository.find_all()
        return [UserDTO(user.idUser, user.idCard, user.names, user.surnames, user.email, user.password, user.score) for user in users]

    def get_user_by_id(self, user_id):
        user = self.user_repository.find_by_id(user_id)
        if user:
            return UserDTO(user.idUser, user.idCard, user.names, user.surnames, user.email, user.password, user.score)
        return None

    def create_user(self, user_dto: UserDTO):
        encrypted_password = self._encrypt_password(user_dto.password)
        user_dto.password = encrypted_password
        return self.user_repository.create_user(user_dto)

    def update_user(self, user_id, user_dto: UserDTO):
        if user_dto.password:
            user_dto.password = self._encrypt_password(user_dto.password)
        return self.user_repository.update_user(user_id, user_dto)

    def delete_user(self, user_id):
        self.user_repository.delete(user_id)

    def verify_password(self, user_id: int, provided_password: str) -> bool:
        user = self.user_repository.get_user_by_id(user_id)
        if user:
            stored_password = self._decrypt_password(user.password)
            return stored_password == provided_password  # Comparar las contraseñas
        return False