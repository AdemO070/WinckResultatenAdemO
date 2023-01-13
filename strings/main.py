# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

#opdracht part 1
scorer0="Ruud Gullit"
scorer1="Marco Van Basten"
goal_0=32
goal_1=54
scorers= scorer0 + " " + str(goal_0) + ", " + scorer1 + " " + str(goal_1)           #wincpy geef fout aan, maar resultaat is wel goed.
report= str(scorer0)+" scored in the "+str( goal_0)+"nd minute." +'\n'+ str(scorer1)+" scored in the "+str( goal_1)+"th minute."
print(report)

#opdracht part 2
player="Jan Wouters"

first_name_find= player.find(' ')           #geeft aantal letter van naam voor de spatie naar achter = 3 voor Jan
first_name= player[:first_name_find]        #geeft naam VOOR de spatie
last_name= player[first_name_find:]         #geeft achternaam NA de spatie
last_name_len= len(last_name)               #geeft lengte van achternaam

name_short=first_name[:1]+"." + last_name   #geeft naam van player eerste letter met punt plus achternaam.

chant= (first_name+"! ") * (first_name_find-1)+(first_name+"!")   #geeft chant van voornaam met "! " maal aantal letters uit first_name_find -1 en 
                                                                #daarna nog een keer zonder spatie achter de "!"
print(chant)

#lengte van chant = (letters in naam) x aantal letters in naam - 1(de laatste spatie die weg is gehaald)
space_in_chant=len(chant)                                      #lengte wat chant is.
good_chant_lenght=((first_name_find+2)*first_name_find)-1      #lengte wat chant moet zijn
good_chant=space_in_chant == good_chant_lenght                 #vergelijkt bovenstaande twee met True of False resultaat
print(good_chant)     
