# MDR Analiza zraka

We're working on a data analysis project. The gist of it is that we're looking at data about air pollution in Slovenia. We have data for our statistical regions, more precisely from measuring stations. What we are determining primarily is whether EU legislation (ex. NECD) had an impact on air pollutant levels (ex. SO2, PM10,...). We would like to achieve this is showing graphs on how trends per pollutant changed over certain critical points (directives), calculating statistics around this. Then we'll focus on a panel data regression, to see if the air pollution levels had an impact on MRD (mortality due to respiratory diseases). 


Please take a moment to fully digest our situation. Then I need you to provide small manageable goals, that will help us achieve this. First i'll tell you our starting point, and our thoughts on potentiall issues. Please help us determine also the order in which should we go about solving our problems that make the most sense. 


We probably need to present a full chapter on descriptive statistics around our data. (here we don't have in-depth knowledge)

What are the ways in which we can use data analysis to show the impact of legislations. We can't really use linear regression to determine how the year for example 2005 (when NECD became legally binding) impacted  our data. Since this is just a constant, we have to find ways to show the statistics. One that comes to mind is ranking an annual change for each region past year 2005. To help you out i'll write our  hypothesis' so you can get a better idea: H1: Stopnje onesnaženosti zraka so se znižale v vseh regijah po uvedbi regulacij. H2:  Spremembe po uvedbi regulacij so visoko variabilne med regijami (različna skladnost z zakonodajo). H3:     Vpliv zakonodaje na kakovost zraka se izraža z določenim časovnim zamikom, kar pomeni, da se učinki zakonodajnih sprememb ne pokažejo takoj, temveč šele po nekaj letih (This one can be changed a bit, since it's quite vague, but it obviously tied with our panel regression)


Direktive in omejitve:
 - SO2 <= 125ug z izjemo 3 dni v letu(2005)
 - NO2 <= 40ug (2010)
 - NOX <= 24ug (2010)
 - PM10 <= 40ug (2005)
 
 https://en.wikipedia.org/wiki/Interrupted_time_series
 Interrupted Time Series