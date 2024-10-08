# Keskustelusovellus

Sovelluksessa näkyy keskustelualueita, joista jokaisella on tietty aihe. Alueilla on keskusteluketjuja, jotka muodostuvat viesteistä. Jokainen käyttäjä on peruskäyttäjä tai ylläpitäjä.

Sovelluksen ominaisuuksia:

* Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen.
* Käyttäjä näkee sovelluksen etusivulla listan alueista sekä jokaisen alueen ketjujen ja viestien määrän ja viimeksi lähetetyn viestin ajankohdan.
* Käyttäjä voi luoda alueelle uuden ketjun antamalla ketjun otsikon ja aloitusviestin sisällön.
* Käyttäjä voi kirjoittaa uuden viestin olemassa olevaan ketjuun.
* Käyttäjä voi muokata luomansa ketjun otsikkoa sekä lähettämänsä viestin sisältöä. Käyttäjä voi myös poistaa ketjun tai viestin.
* Käyttäjä voi etsiä kaikki viestit, joiden osana on annettu sana.
* Ylläpitäjä voi lisätä ja poistaa keskustelualueita.
* Ylläpitäjä voi luoda salaisen alueen ja määrittää, keillä käyttäjillä on pääsy alueelle.

Aiheen lähde:
https://hy-tsoha.github.io/materiaali/aiheen_valinta/

Ylläpitäjä luodaan sovelluksen käynnistyksen yhteydessä. Sovelluksen nykyinen tilanne on se, että kaikki yllä mainitut ominaisuudet on toteutettu.

Käynnistysohjeet:

Käynnistysohjeet ovat pääosin samat kuin sivulla https://hy-tsoha.github.io/materiaali/aikataulu/ kohdassa "esimerkki käynnistysohjeista" olevat käynnistysohjeet (nämä ohjeet on kopioitu tämän README:n loppuun), mutta erona on se, että täytyy vielä lisätä käynnistysohjeissa mainittuun .env-tiedostoon yksi ylimääräinen ympäristömuuttuja nimeltä ADMIN_PASSWORD, jonka arvoksi tallennetaan haluamasi ylläpitäjän salasanan hajautusarvo, joka on luotu moduulin werkzeug.security funktiolla generate_password_hash. Voit luoda hajautusarvon esim. näin: 1. seuraa ensin sivun https://hy-tsoha.github.io/materiaali/aikataulu/ käynnistysohjeita (nämä ohjeet on kopioitu tämän README:n loppuun), 2. pysy vielä komentorivillä samassa virtuaaliympäristössä, joka mainittiin käynnistysohjeissa (pitää lukea venv rivin alussa), 3. suorita komentorivillä komento python3 python-tulkin käynnistämiseksi, 4. suorita tulkissa komento: "from werkzeug.security import generate_password_hash" ilman sulkeita, jotta voidaa suorittaa seuraava komento. 5. suorita hajautusarvon saamiseksi tulkissa komento generate_password_hash("haluamasi_salasana"), jossa kohdassa haluamasi_salasana on valitsemasi salasana (sisällytä sulkeet). Nyt pitää siis vielä tallentaa saamasi hajautusarvo .env tiedostoon muuttujan ADMIN_PASSWORD arvoksi. Kaiken jälkeen .env tiedoston tulee olla muotoa:

```
DATABASE_URL=tietokannan-paikallinen-osoite  
SECRET_KEY=salainen-avain  
ADMIN_PASSWORD=scrypt:...
```

Sovelluksen testaaminen:  
Tarvitset testaamiseen ylläpitäjän käyttäjätunnuksen, joka on admin, ja ylläpitäjän salasanan, joka on käynnistysohjeiden noudattamisen yhteydessä luomasi salasana (valitsit sen kohdassa haluamasi_salasana).

Tässä sivulta https://hy-tsoha.github.io/materiaali/aikataulu/ kohdasta "esimerkki käynnistysohjeista" kopioidut käynnistysohjeet:

Kloonaa tämä repositorio omalle koneellesi ja siirry sen juurikansioon. Luo kansioon .env-tiedosto ja määritä sen sisältö seuraavanlaiseksi:

```
DATABASE_URL=tietokannan-paikallinen-osoite  
SECRET_KEY=salainen-avain
```

Seuraavaksi aktivoi virtuaaliympäristö ja asenna sovelluksen riippuvuudet komennoilla  

```
$ python3 -m venv venv  
$ source venv/bin/activate  
$ pip install -r ./requirements.txt  
```

Määritä vielä tietokannan skeema komennolla
```
$ psql < schema.sql
```

Nyt voit käynnistää sovelluksen komennolla  
```
$ flask run
```