# Analiza vpliva zakonodaj na onesnaženost zraka v Sloveniji (1997-2023)

## Pregled

Ta projekt predstavlja sistematično analizo učinkovitosti evropskih okoljskih direktiv NECD (2001/81/ES) in Direktive o kakovosti zraka (2008/50/ES) pri zmanjševanju onesnaženosti zraka v Sloveniji. Raziskava temelji na analizi podatkov o SO₂, PM₁₀ in NO₂ iz obdobja 2002-2022 po statističnih regijah z uporabo neparametričnih testov, analize prekinjenih časovnih vrst (ITSA) in panelne regresije.

## Teoretski okvir

Raziskava združuje tri teoretske pristope:

- **Teorija trajnostnega razvoja**: Konceptualni okvir za družbeni in gospodarski napredek brez ogrožanja prihodnjih generacij
- **Teorija regulacije**: Preučuje nastanek regulativnih predpisov in njihove učinke
- **Teorija zdravja prebivalstva**: Osredotoča se na izboljšanje zdravja celotnih populacij

## Raziskovalna vprašanja in hipoteze

### Glavna raziskovalna vprašanja
1. Ali so stopnje onesnaženosti zraka močno upadle po uvedbi regulacij?
2. Ali obstaja variabilnost med statističnimi regijami pri spremembah?
3. Ali se je umrljivost zaradi respiratornih bolezni spremenila?

### Hipoteze
- **H1**: Koncentracije onesnaževal so se po uvedbi direktiv statistično značilno zmanjšale
- **H2**: Obstajajo značilne regionalne razlike v učinkovitosti implementacije
- **H3**: Zdravstveni učinki so opazni z zamikom in varirajo po regijah

## Podatki in metodologija

### Viri podatkov
- **Onesnaženost zraka**: Letna poročila Agencije RS za okolje (ARSO), 1997-2023
- **Zdravstveni podatki**: Nacionalni inštitut za javno zdravje (NIJZ) - umrljivost zaradi bolezni dihal po regijah

### Analizirane snovi in omejitve

| Onesnaževalec | Tip omejitve | Mejna vrednost | Leto implementacije |
|---------------|--------------|----------------|-------------------|
| **SO₂** | 1 ura | 350 μg/m³ | 2005 (NECD) |
| **SO₂** | 24 ur | 125 μg/m³ | 2005 (NECD) |
| **PM₁₀** | Letno | 40 μg/m³ | 2005 (NECD) |
| **NO₂** | 1 ura | 200 μg/m³ | 2010 (Direktiva 2008/50/ES) |
| **NO₂** | Letno | 40 μg/m³ | 2010 (Direktiva 2008/50/ES) |

### Regionalno filtriranje
Zaradi neenakomerne razpoložljivosti podatkov smo uporabili različne regije za posamezne onesnaževalce:

- **SO₂**: Koroška, Osrednjeslovenska, Posavska, Savinjska, Zasavska (5 regij)
- **PM₁₀**: Goriška, Osrednjeslovenska, Podravska, Pomurska, Posavska, Savinjska, Zasavska (7 regij)
- **NO₂**: Goriška, Osrednjeslovenska, Podravska, Pomurska, Savinjska, Zasavska (6 regij)

### Statistične metode

1. **Vizualizacija trendov**: Časovne serije z drsečimi povprečji in standardnimi odkloni
2. **Neparametrični testi**: Mann-Whitney U test in permutacijski test za primerjavo obdobij pred/po direktivi
3. **Interrupted Time Series Analysis (ITSA)**: Ocena takojšnjih in trajnih učinkov zakonodajnih intervencij
4. **Panelna regresija**: Analiza povezanosti med onesnaženostjo in umrljivostjo z 2-letnimi zamiki

## Struktura projekta

```
├── 1_data_processing.ipynb          # Pridobivanje in čiščenje podatkov
├── 2_visual_analysis.ipynb          # Vizualizacija trendov po regijah
├── 3_deskriptivne_analize.ipynb     # Statistični testi pred/po direktivi
├── 4_Interrupted_time_series_analysis.ipynb  # ITSA analiza
├── 5_Panel.ipynb                    # Panelna regresija umrljivosti
├── helpers.py                       # Pomožne funkcije in konstante
├── podatki/                         # Direktorij s podatki
│   ├── df_mesecne.csv              # Mesečno agregirani podatki
│   ├── df_dnevne.csv               # Najvišje dnevne vrednosti
│   ├── df_urne.csv                 # Najvišje urne vrednosti
│   ├── panel_df.csv                # Dataset za panelno analizo
│   └── [onesnaževalec]/            # Surovi podatki po onesnaževalcih
└── README.md                        # Ta datoteka
```

## Ključni rezultati

### Učinkovitost direktiv po onesnaževalcih

**SO₂ (NECD 2005)** - Najuspešnejša intervencija:
- Dramatični takojšnji učinki: do -291 μg/m³ v industrijskih regijah (Zasavska, Posavska)
- 70-85% zmanjšanje povprečnih koncentracij
- Statistično značilni učinki v vseh regijah (p<0.001)
- Kombinacija takojšnjih in trajnih izboljšav

**PM₁₀ (NECD 2005)** - Zmerna učinkovitost:
- Postopen upad z doseganjem mejnih vrednosti do 2010
- Večinsko trajni učinki (0.3-0.6 μg/m³/mesec)
- Največje izboljšave v industrijskih regijah
- Statistično značilen zdravstveni učinek z 2-letnim zamikom

**NO₂ (Direktiva 2008/50/ES 2010)** - Šibkejši odziv:
- Najkompleksnejši vzorci odziva
- Mešani pozitivni in negativni učinki po regijah
- Urbane regije (Osrednjeslovenska) brez značilnih izboljšav
- Odraža kompleksnost prometnih virov onesnaževanja

### Regionalne razlike (H2 potrjena)

**Industrijske regije** (Zasavska, Savinjska, Posavska):
- Največje absolutne izboljšave pri SO₂ in PM₁₀
- Močni takojšnji učinki NECD direktive
- Uspešna regulacija centraliziranih virov emisij

**Urbane regije** (Osrednjeslovenska):
- Manjše izboljšave pri NO₂ zaradi prometnih obremenitev
- Potrebni specializirani ukrepi za prometno onesnaževanje

**Manjše regije** (Goriška, Pomurska):
- Že nizke izhodiščne vrednosti
- Stabilno nizke ravni skozi celotno obdobje

### Zdravstveni učinki (H3 delno potrjena)

Panelna regresija z 2-letnimi zamiki:
- **PM₁₀**: Povečanje za 1 μg/m³ → +1.51% umrljivost zaradi bolezni dihal
- **NECD direktiva**: Zmanjšanje škodljivega učinka PM₁₀ za 1.20% po letu 2005
- **SO₂ in NO₂**: Brez statistično značilnih zdravstvenih učinkov

## Zaključne ugotovitve

### Potrjene hipoteze
- **H1** (v celoti): Koncentracije onesnaževal statistično značilno zmanjšane
- **H2** (v celoti): Jasne regionalne razlike v implementaciji
- **H3** (delno): Zdravstveni učinki opazni le pri PM₁₀ z 2-letnim zamikom

### Teoretski prispevek
Raziskava zagotavlja empirično podlago za teorijo regulativnih učinkov in potrjuje uspešnost EU okoljskega regulativnega okvira. Izkazuje pomembnost prilagojenih pristopov glede na tip onesnaževalca in regionalne značilnosti.

### Praktični pomen
Rezultati podpirajo nadaljevanje in krepitev okoljskih politik EU ter nakazujejo potrebo po:
- Specializiranih ukrepih za NO₂ v urbanih območjih
- Sistematičnem spremljanju zdravstvenih učinkov
- Ciljno usmerjenih politikah glede na regionalne posebnosti

### Omejitve raziskave
- Skriti dejavniki (gospodarske krize, tehnološki napredek, vremenske spremembe)
- Omejen časovni zamik zdravstvenih učinkov (2 leti)
- Regionalni agregirani podatki ne zajemajo lokalne heterogenosti
- Neenakomerna pokritost regij po onesnaževalcih

## Priporočila za prihodnje raziskovanje

1. Podrobnejša analiza NO₂ trendov z vključitvijo prometnih podatkov
2. Daljši časovni zamiki za zdravstvene učinke (5-10 let)
3. Lokalna raven analize za urbane izzive
4. Stroškovno-koristna analiza regulativnih ukrepov
5. Vpliv podnebnih sprememb na učinkovitost politik

---

*Raziskava dokazuje, da so EU okoljske direktive učinkovit instrument za izboljšanje kakovosti zraka in javnega zdravja, vendar zahtevajo prilagoditve glede na lokalne značilnosti in vrste onesnaževal.*
