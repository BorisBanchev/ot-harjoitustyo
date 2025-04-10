# Ohjelmistotekniikka, Harjoitustyö

## Budget managing App

Projekti kirjoitetaan _python-kielellä_ ja se tulee käyttämään _tietokantana_ **SQLite**. Riippuvuuksien hallintana käytetään **Poetryä**.
Käyttäjät voivat kirjautuneena sovellukseen hallinnoida omia päivittäisiä kulujaan.

## Dokumentaatio

- [vaatimusmäärittely](https://github.com/BorisBanchev/ot-harjoitustyo/tree/main/budget-management-app/dokumentaatio/vaatimusmaarittely.md)
- [työaikakirjanpito](https://github.com/BorisBanchev/ot-harjoitustyo/tree/main/budget-management-app/dokumentaatio/tyoaikakirjanpito.md)
- [changelog](https://github.com/BorisBanchev/ot-harjoitustyo/tree/main/budget-management-app/dokumentaatio/changelog.md)
- [arkkitehtuuri](https://github.com/BorisBanchev/ot-harjoitustyo/tree/main/budget-management-app/dokumentaatio/arkkitehtuuri.md)

## Asennus

**Huom!** Kloonaa ensin repositorio koneellesi:

```bash
git clone
```

Navigoi hakemistoon _budget-management-app_:

```bash
cd budget-management-app
```

Luo .env - tiedosto projektin juureen seuraavalla sisällöllä:

```bash
DATABASE_FILENAME=<tietokanta-tiedoston-nimi> # esim. database.sqlite
```

Tämän jälkeen suorita seuraavat asiat:

1. Asenna riippuvuudet:

```bash
poetry install
```

2. Suorita tietokannan alustus:

```bash
poetry run invoke build
```

3. Käynnistä sovellus:

```bash
poetry run invoke start
```

## Komentorivikomennot

### Ohjelman suorittaminen

Ohjelma suoritetaan komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit voidaan ajaa komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Generoi testikattavuusraportti komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoidaan htmlcov-hakemistoon

### Pylint
Ohjelman suorittamat koodin tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke pylint
```
