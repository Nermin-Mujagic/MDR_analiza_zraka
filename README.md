# MDR Analiza zraka

[Prompt za AI]
We're working on a data analysis project. The gist of it is that we're looking at data about air pollution in Slovenia. We have data for our statistical regions, more precisely from measuring stations. What we are determining primarily is whether EU legislation (ex. NECD) had an impact on air pollutant levels (ex. SO2, PM10,...). We would like to achieve this is showing graphs on how trends per pollutant changed over certain critical points (directives), calculating statistics around this. Then we'll focus on a panel data regression, to see if the air pollution levels had an impact on MRD (mortality due to respiratory diseases). 
The analysis mostly consists of exploring data analysis on a per pollutant basis, where for the pollutant we are exploring we have a pre-defined function which filters our master df by only selecting that pollutant and selecting only the years and regions which have the most complete data for this selection. (filter_region_year - Args: full_df(pd.Dataframe): Input DataFrame with air pollution data, snov (str): Pollutant to filter for (e.g. "SO2"). Returns: pd.DataFrame Filtered DataFrame with 'Regija', 'Datum', and snov columns.)

[Popravki za hipoteze/vprašanja]
- V1: Ali je implementacija NECD(2005, 2010) vodila k statistično značilnemu padcu pri onesnaževanju posameznih snovi ? 
- H2: Ali so značilne razlike med posameznimi regijami. (nekatere bolj ali manj uspešne) ?
- V3: Katere regije so največkrat prekršile dane omejitve?
- V4: Ali obstaja korelacija z zmanjšanjem onesnaževanja zraka in umrljivosti zaradi bolezni dihal?

- H1a: NECD direktiva je vodila k statistično značilnemu padcu onesnaževanja SO2 v vseh regijah.
- H1b: NECD direktiva je  vodila k statistično značilnemu padcu onesnaževanja PM10 v vseh regijah.
- H1c: NECD direktiva je vodila k statistično značilnemu padcu onesnaževanja NO2 v vseh regijah.
- H2: 

[Sestavine analize]
 *Zbiranje podatkov*:
 - zbrani iz letnih poročil (1997-2023)
 - oblikovanje skupne široke tabele
 - zajemajo vse snovi


 - Analiza poteka v dveh delih:
    - 1. Del: za vsako snov posebej izvedemo analizo po enakem receptu. Pregledamo trende (vizualizacija), naredimo formalne statistične teste, autokorelacija in na koncu Interrupted Time Series analiza.
    - 2. Del: Za skupno tabelo pregledamo korelacijsko matriko med snovi, učinki z zamikom in panelna regresija, ki pove če direktiva -> vpliv na ravni onesnaževanja -> vpliv na umrljivost zaradi bolezni dihal

 *Filtriranje*:
- region_filter_year funkcija, prejme celotno tabelo, snov in leto, nato vrne podmnožico, ki vključuje le podatke o izbrani snovi, od podanega začetnega leta in le regije, za katere smo videli da imajo najbolj popolne podatke za to snov. 
 - Zakaj? Ker tako lahko nardimo poglobljeno analizo za vsako snov posebej in ne žrtvujemo količine podatkov. (Če bi gledali samo skupni presek bi imeli 1/20 podatkov). 
 
 

[Direktive in omejitve]
NECD:
- SO2:
    - 350μg/m3 (1 ura, 2005)[X]
    - 125μg/m3 (24 ur, 2005)[X]
 
- PM10:
    -̶ ̶5̶0̶μ̶g̶/̶m̶3̶ ̶(̶2̶4̶ ̶u̶r̶,̶ ̶2̶0̶0̶5̶)̶ (ni podatkov za dnevna preseganja)
    - 40μg/m3 (leto, 2005)[X]

- NO2:
    - 200μg/m3 (1 ura, 2010)[X]
    - 40μg/m3 (leto, 2010)[X]
 
 https://environment.ec.europa.eu/topics/air/air-quality/eu-air-quality-standards_en
 
 
[Kontekst statističnih metod, ki smo uporabili]
0. Vizualizacija trendov:
Prikažemo gibanje ravni za posamezno snov. Dodana je prelomnica (direktiva) in letna omejitev ki je določena. Pomagamo si tudi da prikažemo št. prekoračitev za urno in/ali dnevno omejitev, da identificiramo katere regije so bile največ/najmanj v prekršku.

*Rollin mean/ drseče povprečje*
 Drseče povprečje je statistična metoda, kjer za vsak trenutek v časovni seriji izračunamo povprečje vrednosti v določenem časovnem oknu pred (ali okoli) tega trenutka. Na primer, če imamo mesečne podatke in uporabimo 12-mesečno drseče povprečje, to pomeni, da za vsak mesec vzamemo povprečje vrednosti iz zadnjih 12 mesecev.
 - zgladi podatke - odstrani kratkoročne nihaje in pokaže dolgoročne trende
 - pomaga prepoznati vzorce, sezonskost ali spremembe v vedenju podatkov

Rolling std / drseči standardni odklon*
 Drseči standardni odklon meri, kako zelo se podatki znotraj istega časovnega okna razlikujejo od povprečja. To nam pove, koliko "variabilnosti" ali "nestanovitnosti" je v podatkih v določenem obdobju.
 - Omogoča spremljanje sprememb v razpršenosti podatkov skozi čas.
 - Pomaga identificirati nestabilna obdobja, ko so vrednosti močno nihale (npr. izbruhi onesnaženja).
 - Dopolnjuje drseče povprečje – če je povprečje stabilno, a standardni odklon velik, to pomeni, da so nihanja prisotna, a uravnotežena.

1. Permutacijski test:


3.Mann-Whitney U test:
Neparametrični test, ki primerja mediane dveh neodvisnih vzorcev (pred in po zakonodaji). Pokaže nam, ali se je distribucija onesnaženja pomembno premaknila – kar nam pomaga potrditi učinek zakonodaje tudi, če podatki niso normalno porazdeljeni.

To smo uporabili namesto t-testov, saj nimamo normalno porazdeljenih podatkov


5. Interrupted time series analysis (ITSA):
Ta analiza nam bo omogočila kvantificirati učinek zakonodajnega "posega" v času – torej, ali se je trend onesnaženja po sprejetju zakonodaje bistveno spremenil. Ključno za oceno dejanskega vpliva NECD ali podobnih direktiv.
V ozadju so pravzaprav dve linearne regresije. Pred in po direktivi. Vizualiziramo 
https://en.wikipedia.org/wiki/Interrupted_time_series
https://ds4ps.org/pe4ps-textbook/docs/p-020-time-series.html

 
[Pomožni prompt naših hipotez]
What are the ways in which we can use data analysis to show the impact of legislations. We can't really use linear regression to determine how the year for example 2005 (when NECD became legally binding) impacted  our data. Since this is just a constant, we have to find ways to show the statistics. One that comes to mind is ranking an annual change for each region past year 2005. To help you out i'll write our  hypothesis' so you can get a better idea: H1: Stopnje onesnaženosti zraka so se znižale v vseh regijah po uvedbi regulacij. H2:  Spremembe po uvedbi regulacij so visoko variabilne med regijami (različna skladnost z zakonodajo). H3:     Vpliv zakonodaje na kakovost zraka se izraža z določenim časovnim zamikom, kar pomeni, da se učinki zakonodajnih sprememb ne pokažejo takoj, temveč šele po nekaj letih (This one can be changed a bit, since it's quite vague, but it obviously tied with our panel regression)