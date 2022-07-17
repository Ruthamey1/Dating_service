print('Guess a six-digit number SLAYER so that the following equation is true,\nWhere each letter stands for th digit in the position shown:')
print()
print('SLAYER + SLAYER + SLAYER = LAYERS')
print()
guess = int(input('Enter your guess for slayer: '))
slayer = 142857
if len(str(guess)) != 6:
    print('Your guess is incorrect: \nSLAYER must be a 6-digit number. \nThanks for playing')
elif guess == slayer:
    print('Your guess is correct: \nSLAYER + SLAYER + SLAYER = 428571 \nLAYERS = 428571 \nThanks for playing.')
else:
    layers = guess * 3
    print(f'Your guess is incorrect: \nSLAYER + SLAYER + SLAYER = {layers} \nlayers = {guess} \nThanks for playing.')
