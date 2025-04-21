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
- Lisätty testejä luokille ExpenseRepository sekä UserService

## Viikko 5

- Käyttäjä voi kirjautua ulos sovelluksesta add_expense, update_expense ja show_expenses sivuilta painamalla nappia **Logout**
- Lisätty näkymä update_expense_view, jossa käyttäjä voi muokata kulun kenttiä amount, description tai date
- Käyttäjä voi scrollata kuluja taulukossa, jos niitä on paljon
- Testattu UserService luokan logout funktiota ja ExpenseRepositoryn update_expense funktiota

## Viikko 6

- Käyttäjä näkee nyt show_expenses_view kulut näiden summan mukaisessa järjestyksessä
- Testattu ExpenseServicen luokan funktioita add_expense ja update_expense TestExpenseService-luokalla
- Korjattu Käyttäjän kuukausibudjetti toimimaan desimaaliarvoilla
- Lisätty sekvenssikaavio uuden käyttäjän luomisesta
