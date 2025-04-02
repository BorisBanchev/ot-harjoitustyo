import unittest
from entities.user import User
from repositories.user_repository import user_repository


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all_users()
        self.user_paavo = User("paavo", "1234")
        self.user_ville = User("ville", "1234")

    def test_create(self):
        user_repository.create_user(self.user_paavo)
        users = user_repository.get_all_users()
        self.assertEqual(len(users), 1)

        self.assertEqual(users[0].username, self.user_paavo.username)

    def test_get_all_usernames(self):
        user_repository.create_user(self.user_paavo)
        user_repository.create_user(self.user_ville)
        users = user_repository.get_all_users()

        self.assertEqual(len(users), 2)
        self.assertEqual(users[0].username, self.user_paavo.username)
        self.assertEqual(users[1].username, self.user_ville.username)

    def test_find_by_username(self):
        user_repository.create_user(self.user_ville)

        user_by_name = user_repository.get_user_by_name("ville")
        self.assertEqual(user_by_name.username, self.user_ville.username)
