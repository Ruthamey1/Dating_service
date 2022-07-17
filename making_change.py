print('Welcome to the vending machine change maker program')
print('Change maker initialized.')


while True:

    coins = input('Enter the purchase price (xx.xx) or \'q\' to quit: ')
    if not coins == 'q':
        coin = float(coins)
        payment = round(coin*100)
        if payment <= 0 or payment%5 != 0:
            print('Illegal price: Must be a non-negative multiple of 5 cents.')
            break
    else:
        break

    
    print()
    print('Menu for deposits:\n\t\'n\' - deposit a nickel\n\t\'d\' - deposit a dime\n\t\'q\' - deposit a quarter\n\t\'o\' - deposit a one dollar bill\n\t\'f\' - deposit a five dollar bill\n\t\'c\' - cancel the purchase')
    print()
    while payment > 0:
        try:
            dollars = int(payment//100)
        except ZeroDivisionError:
            dollars = 0
        payment = str(payment)
        print(f'Payment due: {dollars} dollars and {payment[-2:]} cents')
       
        payment= int(payment)
    
        try:
            deposit = str(input('Indicate your change: '))
            if deposit == 'n':
                payment = payment - 5
            elif deposit == 'd':
                payment = payment - 10
            elif deposit == 'q':
                payment = payment - 25
            elif deposit == 'o':
                payment = payment - 100
            elif deposit == 'f':
                payment = payment - 500
            if deposit == 'c':
                print(f'You still owe ${float(payment/100)}') 
                break
        except ValueError:
            pass
        
