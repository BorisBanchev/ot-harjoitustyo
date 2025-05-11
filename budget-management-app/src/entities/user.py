class User:
    ''' Luokka kuvaa yksittäistä käyttäjäää ohjelmassa

    Attributes: 
        username: Merkkijonoarvo, kuvaa käyttäjän käyttäjätunnusta ohjelmaan
        password: Merkkijonoarvo, kuvaa käyttäjän salasanaa ohjelmaan
        monthly_budget: Kokonaislukuarvo, kuvaa käyttäjäkohtaista kuukausibudjettia
        user_id:: Kokonaislukuarvo kuvaa käyttäjän id:tä
    '''

    def __init__(self, username: str, password: str, monthly_budget: float = None,
                  user_id: int = None):
        ''' Luokan konstruktori luo uuden käyttäjän

        Args:
            username: Merkkijonoarvo, kuvaa käyttäjän käyttäjätunnusta ohjelmaan
            password: Merkkijonoarvo, kuvaa käyttäjän salasanaa ohjelmaan
            monthly_budget: Desimaaliarvo, kuvaa käyttäjäkohtaista kuukausibudjettia
            user_id:: Kokonaislukuarvo kuvaa käyttäjän id:tä
        '''
        self.username = username
        self.password = password
        self.monthly_budget = monthly_budget
        self.user_id = user_id
