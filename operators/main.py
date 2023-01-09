# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line

#data Zwitserland
religion_Switzerland= "Roman-Catholic"
language_Switzerland= "German"                      
capital_Switzerland= "Bern"
GDP_Switzerland_billion_dollar= 590.7 
population_growth_Switzerland= 0.65
population_total_Switzerland= 8508698

#data Spanje
religion_Spain= "Roman-Catholic"
language_Spain= "Castilian-Spanish"                 
capital_Spain= "Madrid"
GDP_Spain_billion_dollar= 1.715 
population_growth_Spain= 0.13
population_total_Spain= 47163418

#The language spoken the most in Switzerland is the same as in Spain.
language_spoken_same=(language_Switzerland==language_Spain)
print("Same language spoken =",language_spoken_same)

#The most prevalent religion in Switzerland is the same as in Spain.
religion_same=(religion_Switzerland==religion_Spain)
print("Same religion =",religion_same)

#The name length of Spain's capital does not equal that of Switzerland.
lengte_capital_name_Switzerland=len(capital_Switzerland)        #geeft 4
lengte_capital_name_Spain=len(capital_Spain)                    #geeft 6
print("Lengte of Swiss capital name equal to Spains = ",lengte_capital_name_Spain==lengte_capital_name_Switzerland)

#Switzerland's GDP is greater than Spain's GDP.
print("GDP of Zwisterland is greater than Spains GDP = ",(GDP_Switzerland_billion_dollar>GDP_Spain_billion_dollar))

#The population growth is less than 1% in Switzerland and Spain
print("Population growth in both countries is less than 1% =",(population_growth_Switzerland<1 and population_growth_Spain<1))

#At least one of the two countries has a population count of over 10 million.
lim=10000000
print("Population in at least one country is more than 10 Million =",(population_total_Switzerland>lim) or (population_total_Spain>lim))

#Exactly one of the two countries has a population count of over 10 million.

