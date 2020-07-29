#! /usr/bin/python3
huff = 0
rave = 0
sly = 0
gry = 0

print('~~~~~~~~~Welcome to Hogwarts. Please sit and receive the Sorting Hat. ~~~~~~~~~')
student = input('Enter your name: ')

print(f'Nice to meet you {student}, I will begin asking questions to determine which house would present the best fit for someone of your skill and personality level.')

q1 = input('What do you consider to be the most important quality? \n A: Wisdom \n B: Honesty \n C: Power \n D: Friendship \n:')

if q1 == 'a':
    rave += 1
elif q1 == 'b':
    gry += 1
elif q1 == 'c':
    sly += 1
elif q1 == 'd':
   huff += 1
else:
    print("Sorry, I don't understand that answer") 

q2 = input('What kind of instrument most pleases your ear? \n A: Violin \n B: Drums \n C: Piano \n D: Trumpet \n:')

if q2 == 'c':
    rave += 1
elif q2 == 'd':
    gry += 1
elif q2 == 'a':
    sly += 1
elif q2 == 'b':
    huff += 1
else:
    print("Sorry, I don't understand that answer")

q3 = input('Four goblets are placed before you. Which would you choose to drink? \n A: The foaming, frothing, silvery liquid that sparkles as though containing ground diamonds. \n B: The smooth, thick, richly purple drink that gives off a delicious smell of chocolate and plums. \n C: The golden liquid so bright that it hurts the eye, and which makes sunspots dance all around the room \n D: The mysterious black liquid that gleams like ink, and gives off fumes that make you see strange visions. \n:')

if q3 == 'a':
    rave += 1
elif q3 == 'b':
   gry += 1
elif q3 == 'd':
   sly += 1
elif q3 == 'c':
    huff += 1
else:
    print("Sorry, I don't understand that answer")

print('Hmm...Difficult, Very difficult. We will continue with more questions to narrow it down.')

q4 = input('Which would you rather be? \n A: Trusted \n B: Praised \n C: Envied \n D: Feared \n:')

if q4 == 'c':
    rave += 1
elif q4 == 'a':
    gry += 1
elif q4 == 'd':
   sly += 1
elif q4 == 'b':
   huff += 1
else:
    print("Sorry, I don't understand that answer")

q5 = input('Which road tempts you most? \n A: The wide, sunny, grassy lane \n B: The narrow, dark, lantern-lit alley \n C: The twisting, leaf-strewn path through the woods \n D: The cobbled street lined with ancient buildings \n:')

if q5 == 'd':
    rave += 1
elif q5 == 'c':
    gry += 1
elif q5 == 'b':
    sly += 1
elif q5 == 'a':
    huff += 1
else:
    print("Sorry, I don't understand that answer")

q6 = input('Which nightmare would frighten you most? \n A: Standing on top of something very high and realizing suddenly that there are no hand- or footholds, nor any barrier to stop you falling \n B: An eye at the keyhole of the dark, windowless room in which you are locked \n C: Waking up to find that neither your friends nor your family have any idea who you are. \n D: Being forced to speak in such a silly voice that hardly anyone can understand you, and everyone laughs at you \n:')

if q6 == 'b':
    rave += 1
elif q6 == 'c':
   gry += 1
elif q6 == 'd':
    sly += 1
elif q6 == 'a':
    huff += 1
else:
    print("Sorry, I don't underand that answer")

q7 = input('Dawn or Dusk? \n A: Dawn \n B: Dusk \n')

if q7 == 'a':
    rave += 1
    sly += 1
elif q7 == 'b':
   huff += 1
   gry += 1
else:
    print("Sorry, I don't understand that answer")

q8 = input('Moon or stars? \n A: Moon \n B: Stars \n')

if q8 == 'a':
    rave += 1
    sly += 1
elif q8 == 'b':
    huff += 1
    gry += 1
else:
    print("Sorry, I don't understand that answer")

if gry > rave and gry > huff and gry > sly:
    print(f"I've got it, {student} you are GRYFFINDOR!")
elif huff > rave and huff > sly and huff > gry:
    print(f"I've got it, {student} you are HUFFLEPUFF!")
elif rave > huff and rave > sly and rave > gry:
    print(f"I've got it, {student} you are RAVENCLAW!")
else:
    print(f"I've got it, {student} you are SLYTHERIN!")

houses = []

if gry > 2:
    houses.append('Gryffindor')
if huff > 2:
    houses.append('Hufflepuff')
if sly > 2:
    houses.append('Slytherin')
if rave > 2:
    houses.append('Ravenclaw')

print('With your score, there was potential to study under these houses...')
for house in houses:
    print(house)
