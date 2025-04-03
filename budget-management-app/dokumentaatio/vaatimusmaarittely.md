# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus on budjetin hallinnointi järjestelmä, jossa käyttäjät voivat kirjautua sovellukseen ja seurata omia päivittäisiä kulujaan sen hetkisenä kuukautena. Käyttäjä voi luoda uusia kuluja,
jotka tallennetaan tietokantaan, muodossa (kulun id, kulun/ostoksen nimi, kulun summa, kulun päivämäärä). Käyttäjä voi asettaa itselleen oman budjetin.
Oman budjetin tilanne päivittyy, jos kuluja muokataan tai poistetaan.

## Käyttäjät

Sovelluksessa on käytössä vain yksi käyttäjärooli eli ei ole admin käyttäjää

## Sovelluksen perusversion tarjoama toiminnallisuus

### Ennen kirjautumista

- Käyttäjä voi luoda itselleen käyttäjätunnuksen, joka on uniikki ja pituudeltaan vähintään 4 merkkiä (salasanan oltava vähintään 4 merkkiä)
- Käyttäjä voi kirjautua sovellukseen omalla tunnuksellaan
  - Kirjautuminen onnistuu kirjoittamalla voimassa oleva käyttäjätunnus ja oikea salasana kirjautumislomakkeeseen
  - Virheellisen käyttäjätunnuksen tai salasanan antamisesta järjestelmä antaa sopivan virheviestin

### Kirjautuneena

- Käyttäjä voi asettaa itselleen kuukauden budjetin
- Käyttäjä voi luoda uuden kulun lomakkeelta täyttämällä tiedot ja painamalla nappia "add expense"
- Käyttäjä voi mennä kulujen näkymään painamalla nappia "show expenses"
- Käyttäjä voi poistaa omia kulujaan painamalla nappia "Delete Expense", muokata niitä klikkaamalla haluttua kulua ja painamalla "Update Expense". Budjetti päivittyy näiden yhteydessä
- Käyttäjä voi kirjautua ulos sovelluksesta

## Jatkokehitysideoita

Perusversion jälkeen voidaan ajan salliessa seuraavia ominaisuuksia sovellukseen:

- Kulujen järjestäminen summan mukaisesti tärkeysjärjestykseen
- Admin käyttäjä, joka voi valita käyttäjän ja näkee hänen kaikki kulut listattuna
- Admin käyttäjä voi muokata muiden käyttäjien budjettia
- Kuluihin kenttä, joka sisältää tarkemman kuvauksen kuluun liittyen
- Käyttäjä voi muokata omaa käyttäjätunnusta ja salasanaa
