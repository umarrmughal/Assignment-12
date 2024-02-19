temperture = input("enter in which you want to Convert C or F:")
temperature_input = int(input("enter temperature :"))
Celcius =(temperature_input - 32) * 5/9
Farenhiet = (temperature_input * 9/5) + 32
if temperture == "c":
    print(Farenhiet)
elif temperture == "f" :
    print(Celcius)

temperature_convert = {
    "celcius" : Celcius,
    "farenhiet" : Farenhiet
}
print(temperature_convert)