# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

#opdracht part 1
scorer0="Gullit"
scorer1="Van Basten"
goal_0=32
goal_1=54
report= str(scorer0)+" scored in the "+str( goal_0)+"nd minute." +'\n'+ str(scorer1)+" scored in the "+str( goal_1)+"th minute."
print(report)

#opdracht part 2
player="Jan Wouters"

first_name_find= player.find(' ')           #geeft 3
first_name= player[:first_name_find]        #geeft naam VOOR de spatie
last_name= player[first_name_find:]         #geeft achternaam NA de spatie
last_name_len= len(last_name)               #geeft lengte van achternaam

name_short=first_name[:1]+"." + last_name   #geeft naam van player eerste letter met punt plus achternaam.

chant= (first_name+"! ")*first_name_find    #geeft chant van voornaam met !en spatie maal aantal letters uit first_name_find
print(chant)
