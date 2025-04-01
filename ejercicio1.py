temp_fah=float(input("Ingrese la temperatura en Fahrenheit: "))
temp_cel=((temp_fah-32)*5/9)
temp_kel=temp_cel+273.15
print(f"La temperatura en Celsius es: {temp_cel: .2f}")
print(f"La temperatura en Kelvin es: {temp_kel: .2f}")