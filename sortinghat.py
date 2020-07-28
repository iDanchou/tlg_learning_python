#! /usr/bin/python3
Hufflepuff = 0
Ravenclaw = 0
Slytherin = 0
Gryffindor = 0

print('~~~~~~~~~Welcome to Hogwarts. Please sit and receive the Sorting Hat. ~~~~~~~~~')
student = input('Enter your name: ')

print(f'Nice to meet you {student}, I will begin asking questions to determine which house would present the best fit for someone of your skill and personality level.')

input('What do you consider to be the most important quality? \n A: Wisdom \n B: Honesty \n C: Power \n D: Friendship \n:')

if input == 'A':
    Ravenclaw + 1
elif input == 'B':
    Gryffindor + 1
elif input == 'C':
    Slytherin + 1
else:
    Hufflepuff + 1

input('What kind of instrument most pleases your ear? \n A: Violin \n B: Drums \n C: Piano \n D: Trumpet \n:')

if input == 'C':
    Ravenclaw + 1
elif input == 'D':
    Gryffindor + 1
elif input == 'A':
    Slytherin + 1
else:
    Hufflepuff + 1

input('Four goblets are placed before you. Which would you choose to drink? \n A: The foaming, frothing, silvery liquid that sparkles as though containing ground diamonds. \n B: The smooth, thick, richly purple drink that gives off a delicious smell of chocolate and plums. \n C: The golden liquid so bright that it hurts the eye, and which makes sunspots dance all around the room \n D: The mysterious black liquid that gleams like ink, and gives off fumes that make you see strange visions. \n:')

if input == 'A':
    Ravenclaw + 1
elif input == 'B':
    Gryffindor + 1
elif input == 'D':
    Slytherin + 1
else:
    Hufflepuff + 1

print('Hmm...Difficult, Very difficult. We will continue with more questions to narrow it down.')

input('Which would you rather be? \n A: Trusted \n B: Praised \n C: Envied \n D: Feared \n:')

if input == 'C':
    Ravenclaw + 1
elif input == 'A':
    Gryffindor + 1
elif input == 'D':
    Slytherin + 1
else:
    Hufflepuff + 1

input('Which road tempts you most? \n A: The wide, sunny, grassy lane \n B: The narrow, dark, lantern-lit alley \n C: The twisting, leaf-strewn path through the woods \n D: The cobbled street lined with ancient buildings \n:')

if input == 'D':
    Ravenclaw + 1
elif input == 'C':
    Gryffindor + 1
elif input == 'B':
    Slytherin + 1
else:
    Hufflepuff + 1

input('Which nightmare would frighten you most? \n A: Standing on top of something very high and realizing suddenly that there are no hand- or footholds, nor any barrier to stop you falling \n B: An eye at the keyhole of the dark, windowless room in which you are locked \n C: Waking up to find that neither your friends nor your family have any idea who you are. \n D: Being forced to speak in such a silly voice that hardly anyone can understand you, and everyone laughs at you \n:')
if input == 'B':
    Ravenclaw + 1
elif input == 'C':
    Gryffindor + 1
elif input == 'D':
    Slytherin + 1
else:
    Hufflepuff + 1

input('Dawn or Dusk? \n A: Dawn \n B: Dusk \n')

if input == 'A':
    Ravenclaw + 1, Slytherin + 1
else:
    Hufflepuff + 1, Gryffindor + 1 

input('Moon or stars? \n A: Moon \n B: Stars \n')

if input == 'A':
    Ravenclaw + 1, Slytherin + 1
else:
    Hufflepuff + 1, Gryffindor + 1

if Gryffindor > Hufflepuff and Gryffindor > Ravenclaw and Gryffindor > Slytherin:
    print(f"I've got it, {student} you'd be a perfect fit for the house of Gryffindor!")
elif Hufflepuff > Gryffindor and Hufflepuff > Ravenclaw and Hufflepuff > Slytherin:
    print(f"I've got it, {student} you'd be a perfect fit for the house of Hufflepuff!")
elif Ravenclaw > Gryffindor and Ravenclaw > Slytherin and Ravenclaw > Hufflepuff:
    print(f"I've got it, {student} you'd be a perfect fit for the house of Ravenclaw!")
else:
    print(f"I've got it, {student} you'd be a perfect fit for the house of Slytherin!")
