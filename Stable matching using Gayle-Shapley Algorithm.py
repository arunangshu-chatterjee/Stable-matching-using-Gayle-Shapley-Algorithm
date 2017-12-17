__author__      = "Arunangshu Chatterjee"
# Pre-requisite 1: A list of n women and n men
# Pre-requisite 2: Preference lists of each of those n women and n men
# Assumption 1: I consider 10 women and 10 men and each of their preferences
# Assumption 2: I consider men propose women in the order of their preference list
# Assumption 3: One man cannot propose the same woman more than once

import copy as cp

lm = ['Mark', 'Timothy', 'Brian', 'George', 'Shawn', 'Lance', 'Brendan', 'David', 'Greg', 'Jason'] # list of 10 men
lw = ['Candice', 'Michelle', 'Martha', 'Laura', 'Dianne', 'Emily', 'Sophia', 'Emma', 'Isabelle', 'Abigail'] # list of 10 women

pref_Candice  = [lm[3], lm[7], lm[4], lm[5], lm[0], lm[2], lm[1], lm[9], lm[6], lm[8]] # Preference list of Candice
pref_Michelle = [lm[2], lm[4], lm[6], lm[8], lm[0], lm[1], lm[3], lm[5], lm[7], lm[9]] # Preference list of Michelle
pref_Martha   = [lm[3], lm[4], lm[5], lm[0], lm[1], lm[2], lm[6], lm[7], lm[9], lm[8]] # Preference list of Martha
pref_Laura    = [lm[0], lm[1], lm[2], lm[3], lm[4], lm[5], lm[6], lm[7], lm[8], lm[9]] # Preference list of Laura
pref_Dianne   = [lm[9], lm[8], lm[7], lm[6], lm[5], lm[4], lm[3], lm[2], lm[1], lm[0]] # Preference list of Dianne
pref_Emily    = [lm[4], lm[5], lm[2], lm[1], lm[0], lm[3], lm[6], lm[8], lm[7], lm[9]] # Preference list of Emily
pref_Sophia   = [lm[1], lm[9], lm[4], lm[8], lm[6], lm[7], lm[0], lm[5], lm[3], lm[2]] # Preference list of Sophia
pref_Emma     = [lm[8], lm[0], lm[4], lm[2], lm[9], lm[7], lm[5], lm[1], lm[6], lm[3]] # Preference list of Emma
pref_Isabelle = [lm[7], lm[2], lm[9], lm[6], lm[3], lm[4], lm[8], lm[5], lm[1], lm[9]] # Preference list of Isabelle
pref_Abigail  = [lm[6], lm[9], lm[3], lm[0], lm[2], lm[1], lm[5], lm[4], lm[8], lm[7]] # Preference list of Abigail

pref_Mark    = [lw[0], lw[3], lw[5], lw[9], lw[7], lw[2], lw[1], lw[4], lw[6], lw[8]] # Preference list of Mark
pref_Timothy = [lw[4], lw[2], lw[9], lw[8], lw[0], lw[3], lw[6], lw[7], lw[1], lw[8]] # Preference list of Timothy
pref_Brian   = [lw[7], lw[9], lw[1], lw[6], lw[4], lw[5], lw[2], lw[0], lw[8], lw[3]] # Preference list of Brian
pref_George  = [lw[5], lw[4], lw[7], lw[3], lw[1], lw[6], lw[2], lw[0], lw[8], lw[9]] # Preference list of George
pref_Shawn   = [lw[1], lw[0], lw[6], lw[4], lw[2], lw[1], lw[3], lw[8], lw[9], lw[7]] # Preference list of Shawn
pref_Lance   = [lw[2], lw[5], lw[3], lw[7], lw[8], lw[6], lw[9], lw[1], lw[4], lw[0]] # Preference list of Lance
pref_Brendan = [lw[6], lw[7], lw[0], lw[5], lw[2], lw[1], lw[8], lw[3], lw[6], lw[4]] # Preference list of Brendan
pref_David   = [lw[3], lw[8], lw[4], lw[0], lw[6], lw[2], lw[7], lw[9], lw[5], lw[1]] # Preference list of David
pref_Greg    = [lw[9], lw[1], lw[8], lw[2], lw[0], lw[5], lw[4], lw[7], lw[6], lw[3]] # Preference list of Greg
pref_Jason   = [lw[8], lw[6], lw[2], lw[1], lw[9], lw[4], lw[3], lw[0], lw[7], lw[5]] # Preference list of Jason

free_men = cp.deepcopy(lm)   # List of free men. Initially all men are free
free_women = cp.deepcopy(lw) # List of free women. Initially all women are free
stable_matching = {}

def findPrefMen(i): # Returns the preference list of the free man
	if(i==0):
		return pref_Mark
	elif(i==1):
		return pref_Timothy
	elif(i==2):
		return pref_Brian
	elif(i==3):
		return pref_George
	elif(i==4):
		return pref_Shawn
	elif(i==5):
		return pref_Lance
	elif(i==6):
		return pref_Brendan
	elif(i==7):
		return pref_David
	elif(i==8):
		return pref_Greg
	elif(i==9):
		return pref_Jason

def findPrefWomen(j): # Returns the preference list of the free woman
	if(j=='Candice'):
		return pref_Candice
	elif(j=='Michelle'):
		return pref_Michelle
	elif(j=='Martha'):
		return pref_Martha
	elif(j=='Laura'):
		return pref_Laura
	elif(j=='Dianne'):
		return pref_Dianne
	elif(j=='Emily'):
		return pref_Emily
	elif(j=='Sophia'):
		return pref_Sophia
	elif(j=='Emma'):
		return pref_Emma
	elif(j=='Isabelle'):
		return pref_Isabelle
	elif(j=='Abigail'):
		return pref_Abigail

while len(free_men) != 0:                          # While there is a free man in the list
	i = lm.index(free_men[0])                      # Choose the first man in the free men list
	pref_man = findPrefMen(i)                      # Find the first preference of the free man
	if(pref_man[0] in free_women):                 # If the first preference of the free man is also free
		stable_matching[free_men[0]] = pref_man[0] # The free man and the free woman get engaged
		free_men.remove(free_men[0])               # The free man no longer remains in the list of the free men
		free_women.remove(pref_man[0])             # The free woman no longer remains in the list of the free women
		pref_man.remove(pref_man[0])               # Remove the woman from his preference list as this man will never propose her again
	else:                                          # If the woman is engaged
		pref_woman = findPrefWomen(pref_man[0])    # Find the preference list of the woman
		i = pref_woman.index(free_men[0])          # Find the index of this particular man in her list
		j = pref_woman.index((list(stable_matching.keys())[list(stable_matching.values()).index(pref_man[0])])) # Find the index of the man she is engaged with
		if(i<j):                                   # If the man who proposed is higher than her current partner in her preference list
			del stable_matching[(list(stable_matching.keys())[list(stable_matching.values()).index(pref_man[0])])] # The woman breaks her current engagement 
			stable_matching[free_men[0]] = pref_man[0] #  The woman gets engaged to the new man
			free_men.remove(free_men[0]) # The free man no longer remains in the list of the free men
			free_men.append((list(stable_matching.keys())[list(stable_matching.values()).index(pref_man[0])])) # The man whose engagement gets broken becomes free again
			#free_women.remove(pref_man[0])
			pref_man.remove(pref_man[0])           # Remove the woman from his preference list as this man will never propose her again
		else:                                      # If the man who proposed is lower than her current partner in her preference list
			pref_man.remove(pref_man[0])           # The woman retains her current engagement. Remove the woman from his preference list as this man will never propose her again

print(stable_matching)                             # Return the stable matching