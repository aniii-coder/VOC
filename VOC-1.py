choice = int(input(f'1)Celsius to Fahrenhiet\n2)Fahrenheit to Celsius\nEnter what you want to convert (Enter option 1 or 2): ')
)
if ( choice == 1 ):
    celsius = float(input('Enter temperature in Celsius: '))
    answer = (celsius*(9/5)+32)
    print(f'{celsius}°C is equal to {answer}°F')
elif(choice == 2 ):
    fahrenheit = float(input('Enter temperature in Fahrenheit: '))
    answer = ((fahrenheit-32)*(5/9))
    print(f'{fahrenheit}°F is equal to {answer}°C')
else:
    print('Enter the valid number ')