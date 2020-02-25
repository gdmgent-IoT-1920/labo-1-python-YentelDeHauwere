import random

print("LINGO-BINGO Welkom bij het kip en eieren spel!")

randomNumber = random.randint(1000,9999)

randomNumber = str(randomNumber)

inp = ''
counter = 0

while inp != randomNumber:

	correct = 0
	contains = 0

	if counter != 0:
		i=0
		for x in randomNumber:
			if randomNumber[i] == inp[i]:
				correct+=1
			if randomNumber[i] in inp and randomNumber[i] != inp[i]:
				contains+=1
			i+=1


		if correct == 1:
			print(str(correct) + " kip", end=', ')
		else:
			print(str(correct) + " kippen", end=', ')


		if contains == 1:
			print(str(contains) + " ei")
		else:
			print(str(contains) + " eieren")


	inp = input("Geef een viercijferig nummer in: ") 
	counter+=1

print("Je hebt gewonnen! Pogingen: " + str(counter))