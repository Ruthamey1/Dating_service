years = int(input('How many years: '))
current = 307357870
seconds_in_a_year = years * (60*60*24*365)
births_in_a_year = seconds_in_a_year/7
deaths_in_a_year = seconds_in_a_year/13
new_immigrant = seconds_in_a_year/35
change = births_in_a_year - deaths_in_a_year + new_immigrant
in_a_year = current - int(change)

print(f'New population in {years} years will change by {change} to be {in_a_year}')


