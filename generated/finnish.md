# Yhteenveto - Istunto 1: Eprimer-sovelluksen tutkiminen

**Tavoite:** Tutustua Eprimer-sovellukseen ja ymmärtää sen toiminta sekä käyttötarkoitus.

**Mitä tehtiin:**
- Tutkittiin käyttöliittymää ja opittiin, että sovellus auttaa kirjoittamaan englantia välttäen "to be" -verbiä
- Testattiin syöttämällä tekstiä "to be" ja havaittiin, että sovellus värjää "be"-sanan punaiseksi ja laskee sen "ei-suositeltavaksi sanaksi"
- Avattiin linkitetty Wikipedia-sivu oppiaksemme supistumista ja "to be"-verbin eri funktioista
- Kopioitiin koko Wikipedia-sivun sisältö tekstikenttään

**Löydetyt ongelmat:**
- **BUGI:** Vieritys ei toimi, kun tekstikenttään syötetty teksti on pitkä ja vaatisi vierittämistä
- Ei voitu nähdä mitä "mahdolliset rikkomukset" (possible violations) tarkoittavat

**Testitapaus:** 
- Syöte: "To be or not to be" → 2 ei-suositeltavaa sanaa, 6 sanaa yhteensä

**Jatkoideat:**
- Wikipedia-sivun yksityiskohtainen lukeminen ja testiarvojen poiminta
- Vieritysbugiin korjauksen etsiminen
- Lyhyemmän syötteen testaaminen "mahdollisten rikkomusten" selvittämiseksi

**Huomiot:** 
- Sovellus on MIT-lisensoitu ja vaatii attribuution