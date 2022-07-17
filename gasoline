"""Finding out how expensive and what gasoline can do"""

gallons = float(input('Please enter the number of gallons of gasoline: '))
print('Original number of gallons is: ' + str(gallons))
liters = gallons * 3.7854
barrel_of_oil = gallons / 42
barrel_producing_gas = barrel_of_oil * 19.5
gas_producing_co2 = barrel_producing_gas * 20
gas_producing_BTU = barrel_producing_gas * 115000
gallons_of_ethanol = gas_producing_BTU / 75700
price = gallons * 4.00

print(f'{str(gallons)} gallons is the equivalent of {liters} liters')
print(f'{str(gallons)} gallons of gasoline requires {barrel_of_oil} barrels of oil')
print(f'{str(gallons)} gallons of gasoline produces {gas_producing_co2} pound of C02')
print(f'{str(gallons)} gallons of gasoline is energy equivalent to {gallons_of_ethanol} gallons of ethanol')
print(f'{str(gallons)} gallons of gasoline requires {price} US dollars')
print('Thanks for playing')
