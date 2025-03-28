class User:
    def __init__(self, username: str, password: str, budget: int = None, id: int = None):
        self.username = username
        self.password = password
        self.budget = budget
        self.id = id