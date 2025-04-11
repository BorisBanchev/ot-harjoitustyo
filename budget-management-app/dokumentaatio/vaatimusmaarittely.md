# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus on budjetin hallinnointi järjestelmä, jossa käyttäjät voivat kirjautua sovellukseen ja seurata omia päivittäisiä kulujaan sen hetkisenä kuukautena. Käyttäjä voi luoda uusia kuluja,
jotka tallennetaan tietokantaan, muodossa (kulun id, kulun/ostoksen nimi, kulun summa, kulun päivämäärä). Käyttäjä voi asettaa itselleen oman budjetin.
Oman budjetin tilanne päivittyy, jos kuluja muokataan tai poistetaan.

## Käyttäjät

Sovelluksessa on käytössä vain yksi käyttäjärooli eli ei ole admin käyttäjää

## Sovelluksen perusversion tarjoama toiminnallisuus

### Ennen kirjautumista

- Käyttäjä voi luoda itselleen käyttäjätunnuksen, joka on uniikki ja pituudeltaan vähintään 4 merkkiä (salasanan oltava vähintään 4 merkkiä) **"Tehty"**
- Käyttäjä voi kirjautua sovellukseen omalla tunnuksellaan **"Tehty"**
  - Kirjautuminen onnistuu kirjoittamalla voimassa oleva käyttäjätunnus ja oikea salasana kirjautumislomakkeeseen **"Tehty"**
  - Virheellisen käyttäjätunnuksen tai salasanan antamisesta järjestelmä antaa sopivan virheviestin **"Tehty"**

### Kirjautuneena

- Käyttäjä voi asettaa itselleen kuukauden budjetin **"Tehty"**
- Käyttäjä voi luoda uuden kulun lomakkeelta täyttämällä tiedot ja painamalla nappia "add expense" **"Tehty"**
- Käyttäjä voi mennä kulujen näkymään painamalla nappia "show expenses" **"Tehty"**
- Käyttäjä voi poistaa omia kulujaan painamalla nappia "Delete Expense" **"Tehty"**, muokata niitä klikkaamalla haluttua kulua ja painamalla "Update Expense"
- Budjetti päivittyy muutosten yhteydessä **"Tehty"**
- Käyttäjä voi kirjautua ulos sovelluksesta **"Tehty"**

## Jatkokehitysideoita

Perusversion jälkeen voidaan ajan salliessa seuraavia ominaisuuksia sovellukseen:

- Kulujen järjestäminen summan mukaisesti tärkeysjärjestykseen
- Admin käyttäjä, joka voi valita käyttäjän ja näkee hänen kaikki kulut listattuna
- Admin käyttäjä voi muokata muiden käyttäjien budjettia
- Kuluihin kenttä, joka sisältää tarkemman kuvauksen kuluun liittyen
- Käyttäjä voi muokata omaa käyttäjätunnusta ja salasanaa
