while True:
    customer_code = input('Enter customer code: ')
    customer_code = customer_code.lower()
    start_meter = int(input('Enter beginning meter reading: '))
    end_meter = int(input('Enter ending meter reading: '))
    if start_meter < 0 or end_meter <0:
        print('Must be positive')
        break
    difference = end_meter - start_meter
    if end_meter < start_meter:
        difference = (1000000000 + end_meter) - start_meter



    if customer_code == 'r':
        price = (0.0005 * difference) + 5
    elif customer_code == 'c':
        if difference <= 4000000:
            price = 1000
        else:
            dif_mil = difference - 4000000
            price = 1000 + (0.00025 * dif_mil)
    elif customer_code == 'i':
        if difference < 4000000:
            price = 1000
        elif difference > 4000000 and difference < 10000000:
            price = 2000
        elif difference > 10000000:
            dif_mil = difference - 10000000
            price = 2000 + (dif_mil * 0.00025)
    else:
        break


    print()
    print(f'Customer code: {customer_code}')
    print(f'Beginning meter reading: {start_meter}')
    print(f'Ending meter reading: {end_meter}')
    print(f'Gallons of water used: {difference/10}')
    print(f'Amount billed: ${round(price, 2)}')
