def tempratureConverter(temp, unitToConvert):
    if unitToConvert == 1:
        return ((temp * 9/5) + 32)
    elif unitToConvert == 2:
        return ((temp - 32) * 5/9)
    else:
        return "Invalid unit to convert"
    
choice = int(input(f'1)Celsius to Fahrenhiet\n2)Fahrenheit to Celsius\nEnter what you want to convert (Enter option 1 or 2): '))
if  choice == 1 or choice == 2:
    temp = float(input('Enter temperature: '))
    print("Converted Temprature is: ", tempratureConverter(temp, choice))
else:
    print('Invalid choice')