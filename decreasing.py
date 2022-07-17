large_number = str(input('Input a large whole number: '))
splitt = int(input('Input the split (whole number): '))
new_string = []

if int(large_number) <= 0:
    print('Try again, must be positive')
elif len(large_number) % splitt != 0:
    print('Try again, must be divisible')
else:
    large_number = str(large_number)
    for i in range(0, len(large_number), splitt):
        new_string.append(int(large_number[i:i+splitt]))
    print(new_string)

if new_string[0] < new_string[1] and new_string[1] < new_string[2]:
    print('This sequence is increasing')
else:
    print('This sequence is decreasing')
