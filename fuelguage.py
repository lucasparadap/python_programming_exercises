'''
Implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, 
and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. 

If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.
'''

fuel_level = input("Fraction: ")
fuel_list = []

# Converts fraction into usable percentage
def fuel_conversion(fuel_level):
    for i in fuel_level:
        fuel_list.append(i)
        
    a = int(fuel_list[0])
    b = int(fuel_list[2])
    percentage = (a / b) * 100
    percentage = round(percentage)
    return percentage


# Spits out fuel level as a percentage, or E for empty / F for full, and accounts for errors
def fuel_guage(fuel_level):
    try:
        if 99 > fuel_conversion(fuel_level) > 1:
            print(str(fuel_conversion(fuel_level)) + "%")
        elif fuel_conversion(fuel_level) >= 99:
            print("F")
        else:
            print("E")
    except (ValueError):
        print("Not a number, try again.")
    except (ZeroDivisionError):
        print("E")


fuel_guage(fuel_level)
