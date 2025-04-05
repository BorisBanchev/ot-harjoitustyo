class User:
    def __init__(self, username: str, password: str, monthly_budget: int = None, user_id: int = None):
        self.username = username
        self.password = password
        self.monthly_budget = monthly_budget
        self.user_id = user_id
