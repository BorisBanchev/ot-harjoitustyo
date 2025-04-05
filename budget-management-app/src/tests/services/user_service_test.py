import unittest
from entities.user import User
from entities.expense import Expense
from repositories.user_repository import user_repository
from services.user_service import user_service
from repositories.expense_repository import expense_repository

class TestUserService(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all_users()
        self.valid_user = User("Paavo", "1234")
        self.invalid_user = User("Moi", "123")
        self.expense = Expense("car", 2000, "2025-04-08")

    def test_create_user_succeeds_with_correct_username_and_password(self):
        user = user_service.create_user(self.valid_user.username,self.valid_user.password, self.valid_user.password)

        self.assertEqual(user.username, "Paavo")
        self.assertIsNotNone(user_repository.get_user_by_name("Paavo"))
    
    def test_create_user_fails_with_existing_user(self):
        user = user_service.create_user(self.valid_user.username,self.valid_user.password, self.valid_user.password)
        
        with self.assertRaises(Exception) as context:
            user_service.create_user(self.valid_user.username,self.valid_user.password, self.valid_user.password)
        
        self.assertEqual(str(context.exception), "Username {username} already exists!")
        
    def test_create_user_fails_with_empty_username_or_password(self):
        with self.assertRaises(Exception) as context1:
            user_service.create_user("","1234","1234")        
        self.assertEqual(str(context1.exception), "Username and password must not be empty values!")

        with self.assertRaises(Exception) as context2:
            user_service.create_user("Paavo","","")        
        self.assertEqual(str(context2.exception), "Username and password must not be empty values!")

    def test_create_user_fails_with_unmatching_passwords(self):
        with self.assertRaises(Exception) as context:
            user_service.create_user("Paavo","12345","1234")        
        self.assertEqual(str(context.exception), "Passwords do not match!")
    
    def test_create_user_fails_with_invalid_username_or_password(self):
        with self.assertRaises(Exception) as context1:
            user_service.create_user(self.invalid_user.username,"1234","1234")        
        self.assertEqual(str(context1.exception), "Password and username must have legth of at least 4!")

        with self.assertRaises(Exception) as context2:
            user_service.create_user(self.valid_user.username,self.invalid_user.password,self.invalid_user.password)        
        self.assertEqual(str(context2.exception), "Password and username must have legth of at least 4!")

    def test_login_succeeds_with_correct_credentials(self):
        user_service.create_user(self.valid_user.username, self.valid_user.password, self.valid_user.password)
        user = user_service.login(self.valid_user.username,self.valid_user.password)

        self.assertEqual(user_service._user.username,self.valid_user.username)

    def test_login_fails_with_invalid_username_or_password(self):
        user_service.create_user(self.valid_user.username,self.valid_user.password,self.valid_user.password)
        
        with self.assertRaises(Exception) as context1:
            user_service.login("wrong","1234")        
        self.assertEqual(str(context1.exception), "Invalid username or password")
        
        with self.assertRaises(Exception) as context2:
            user_service.login(self.valid_user.username,self.invalid_user.password)        
        self.assertEqual(str(context2.exception), "Invalid username or password")

    def test_set_budget_sets_a_valid_budget_to_user(self):
        user_service.create_user(self.valid_user.username, self.valid_user.password, self.valid_user.password)
        user = user_service.login(self.valid_user.username,self.valid_user.password)

        user_service.set_budget(user.username,3000)
        self.assertEqual(user_service._user.monthly_budget, 3000)
    
    def test_set_budget_fails_with_negative_or_zero_budget(self):
        user_service.create_user(self.valid_user.username, self.valid_user.password, self.valid_user.password)
        user = user_service.login(self.valid_user.username,self.valid_user.password)

        with self.assertRaises(Exception) as context1:
            user_service.set_budget(user.username,-3000)       
        self.assertEqual(str(context1.exception), "Budget must be a positive number!")

        with self.assertRaises(Exception) as context2:
            user_service.set_budget(user.username,"sdsd")       
        self.assertEqual(str(context2.exception), "Budget must be a valid number!")

    def test_get_current_budget_returns_none_when_no_budget_set(self):
        user_service.create_user(self.valid_user.username, self.valid_user.password, self.valid_user.password)
        user = user_service.login(self.valid_user.username,self.valid_user.password)

        current_budget = user_service.get_current_budget()

        self.assertIsNone(current_budget)
    
    def test_get_current_budget_returns_correct_budget_when_expenses(self):
        user_service.create_user(self.valid_user.username, self.valid_user.password, self.valid_user.password)
        user = user_service.login(self.valid_user.username,self.valid_user.password)
        user_service.set_budget(user.username, 4000)
        self.assertEqual(user_service.get_current_budget(), 4000)
        expense_repository.create_expense(self.expense, user.username)
        
        self.assertEqual(user_service.get_current_budget(), 2000)
        



