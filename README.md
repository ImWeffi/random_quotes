# Random Citātes
Programma, kas ļauj lietotājam izvēlēties tēmu, skatīt nejaušas citātus no vietnes https://quotes.toscrape.com, un pēc izvēles tos saglabāt Excel failā.
Programmas darbības: skatīt citātu, saglabāt citātu, mainīt tēmu vai iziet no programmas.

## Izmantotās bibliotēkas

+ requests – lai iegūtu HTML saturu no tīmekļa vietnes.
+ BeautifulSoup - lai parsētu (izvilktu) datus no HTML dokumenta.
+ random - lai izvēlētos nejaušu citātu no saraksta.
+ datetime - lai pierakstītu datuma un laika zīmogu Excel failā
+ os – lai pārbaudītu, vai Excel fails jau eksistē.
+ openpyxl – lai lasītu un rakstītu .xlsx failus

## Galvenās funkcijas

+ paradi_darbibas() - Atgriež pieejamo darbību sarakstu (skatīt citātu, saglabāt, cita tēma, iziet).
+ paradi_temas() - Izvada visus iespējamos tēmu tagus, no kuriem izvēlēties (top_tags).
+ iegut_citatus(tag) - Veic HTTP pieprasījumu uz https://quotes.toscrape.com/tag/<tag>/. Atgriež sarakstu ar (citāts, autors) pāriem.
+ saglabat_excel(autors, citats, tema) - Pārbauda, vai Citati.xlsx fails jau eksistē. Pārbauda, vai šāds citāts jau eksistē, lai izvairītos no dublikātiem.
  Ja nav dublikāts – saglaba autoru, citatu, temu un datumu .xlsx faila.
+ izveleties_temu() - Ļauj lietotājam izvēlēties tēmas indeksu no saraksta un pārbaude ievadi.

## Lietotāja darbības
1. Skatīt citātu - Parāda tēmas un prasa ievadi, pec ievadi parāda citātu.
2. Saglabāt citātu - Saglabā izvēlēto citātu.
3. Izvēlēties citu citātu - Ļauj izvēlēties jaunu tēmu.
4. Iziet no programmas - Pārtrauc programmu

## Bibliotēku instalēšana
```
pip install requests beautifulsoup4 openpyxl

```
