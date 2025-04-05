class Expense:
    def __init__(self, description: str, amount: float, date: str, expense_id: int = None):
        self.expense_id = expense_id
        self.description = description
        self.amount = amount
        self.date = date
