class Expense:
    def __init__(self, description: str, amount: float, date: str, id: int = None):
        self.id = id
        self.description = description
        self.amount = amount
        self.date = date
    
