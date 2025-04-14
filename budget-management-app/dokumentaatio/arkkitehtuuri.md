# Arkkitehtuurikuvaus

## Ohjelman Rakenne

Ohjelman rakenne muodostuu kerrosarkkitehtuurista, jota kuvaa seuraava pakkauskaavio:

![Pakkausrakenne](./kuvat/kerrosarkkitehtuurikaavio.png)

_UI_ pakkaus huolehtii käyttöliittymään liittyvästä koodista, _services_ sovelluslogiikasta, _repositories_ käyttäjien ja kulujen tietojen tallennuksesta sekä _entities_ esittää ohjelmassa yksittäistä käyttäjää ja kulua.

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
