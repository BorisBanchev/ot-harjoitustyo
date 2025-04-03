# Changelog

## Viikko 3

- Käyttäjä näkee uuden käyttäjän luomisen lomakkeen ja pystyy luomaan käyttäjän
- Lisätty UserRepository luokka, joka vastaa käyttäjiin liittyvistä tietokantaoperaatioista
- Lisätty BudgetRepository luokka, joka vastaa sovelluslogiikan koodista
- Testattu, että UserRepository palauttaa kaikki käyttäjät, hakee yksittäisen käyttäjän sekä luo tietokantaan käyttäjän oikein

## Viikko 4

- Käyttäjä näkee aloitussivulla kirjautumislomakkeen, voi valita myös uuden käyttäjän luomisen, jos ei ole käyttäjää
- Vaihdettu BudgetService-luokka UserService luokaksi, joka vastaa käyttäjiin liittyvästä sovelluslogiikasta
- Käyttäjä ohjataan omien kulujen alustavaan näkymään onnistuvan kirjautumisen tai uuden käyttäjän luomisen yhteydessä.
- Tietokantaan lisätty expenses taulu tallentamaan käyttäjän kuluja
- Lisätty Expense-luokka, joka kuvaa käyttäjän tietokannassa olevia yksittäisiä kuluja
- Lisätty ExpenseRepository-luokka, joka huolehtii käyttäjän kuluihin liittyvistä tietokantaoperaatioista
- Lisätty ExpenseService-luokka, joka huolehtii kulun validaatiosta ja kutsuu ExpenseRepository luokkaa luodessa uuden kulun
- Lisätty add_expense_view ja show_expenses_view näkymät huolehtimaan käyttöliittymästä kulujen näyttämiseen ja luomiseen
