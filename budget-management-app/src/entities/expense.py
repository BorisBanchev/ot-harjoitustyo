class Expense:
    ''' Luokka, joka kuvaa yksittäistä kulua ohjelmassa
    
    Attributes: 
        description: Merkkijonoarvo, joka on kuvaus kulusta
        amount: Desimaaliarvo, joka määrittelee kulun summan arvon
        date: Merkkijonoarvo, joka määrittelee kulun päivämäärän
        expense_id: Kokonaislukuarvo, joka kertoo kulun id:n
    '''
    def __init__(self, description: str, amount: float, date: str, expense_id: int = None):
        ''' Luokan konstruktori, joka luo uuden käyttäjän kulun

        Args:
            description: Merkkijonoarvo, joka on kuvaus kulusta
            amount: Desimaaliarvo, joka määrittelee kulun summan arvon
            date: Merkkijonoarvo, joka määrittelee kulun päivämäärän
            expense_id: Kokonaislukuarvo, joka kertoo kulun id:n
        '''
        self.expense_id = expense_id
        self.description = description
        self.amount = amount
        self.date = date
