# Arkkitehtuurikuvaus

## Ohjelman Rakenne

Ohjelman rakenne muodostuu kerrosarkkitehtuurista, jota kuvaa seuraava pakkauskaavio:

![Pakkausrakenne](./kuvat/Pakkauskaavio-ohte.png)

_UI_ pakkaus huolehtii käyttöliittymään liittyvästä koodista, _services_ sovelluslogiikasta, _repositories_ käyttäjien ja kulujen tietojen tallennuksesta sekä _entities_ esittää ohjelmassa yksittäistä käyttäjää ja kulua.

## Käyttöliittymä

Käyttöliittymä sisältää viisi erilaista näkymää:

- Kirjautuminen sovellukseen
- Uuden käyttäjän luominen
- Budjetin asettaminen sekä uuden kulun luominen (yhteinen näkymä)
- Kulujen näyttämisnäkymä
- Kulun muokkausnäkymä

Nämä on toteutettu erillisinä luokkina. Näkymien näyttäminen annetaan UI-luokan vastuuksi, jossa nämä importataan.

## Sovelluslogiikka

Sovelluksen loogisen tietomallin muodostavat luokat User ja Expense, jotka kuvaavat käyttäjiä ja heidän kulujaan:

```mermaid
classDiagram
    class User {
        username
        password
        monthly_budget
    }

    class Expense {
        expense_id
        description
        amount
        date
    }
    User "1" --> "*" Expense
```

Toiminnallisista kokonaisuuksista vastaa luokan UserService ja ExpenseService oliot. Nämä luokat tarjoavat UI:n toiminnallisuuksia, kuten kirjautumisen, kulujen lisäämisen, poistamisen sekä muokkaamisen. Metodeja ovat esim:

- `login(username, password)`
- `add_expense(description, amount, date, username)`
- `update_expense(expense_id, description, amount, date)`
- `delete_expense(expense_id)`

Sovelluslogiikka käyttää repositories-pakkausta tietojen tallennukseen ja hakemiseen. Käyttäjien tiedoista vastaa UserRepository ja kulujen tiedoista vastaa ExpenseRepository. Näiden avulla Sovelluslogiikka kommunikoi tietokannan kanssa.

## Sovelluksen päätoiminnallisuudet

Sekvenssikaavioita ohjelman oleellisista päätoiminnallisuuksista

### Käyttäjän kirjautuminen

Käyttäjän täytettyä käyttäjätunnuksen ja salasanansa, niin painamalla Login nappia, ohjelman suoritus etenee sekvenssikaavion mukaisesti näin:

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant UserService
  participant UserRepository
  User->>UI: click "Login" button
  UI->>UserService: login("Joonas", "1234")
  UserService->>UserRepository: get_user_by_name("Joonas")
  UserRepository-->>UserService: user
  UserService-->>UI: user
  UI->UI: _show_add_expense_view()
```
