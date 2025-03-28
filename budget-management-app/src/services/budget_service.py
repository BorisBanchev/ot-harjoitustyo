from entities.user import User
from repositories.user_repository import user_repository

class UsernameExistsError(Exception):
    pass

class BudgetService:
    def __init__(self, user_repository):
        self._user = None
        self._user_repository = user_repository
    
    def create_user(self, username: str, password: str):
    
        existing_user = self._user_repository.get_user_by_name(username)

        if existing_user:
            raise UsernameExistsError(f"Username {username} already exists!")
        
        user = self._user_repository.create_user(User(username, password))

        return user

budget_service = BudgetService(user_repository)
