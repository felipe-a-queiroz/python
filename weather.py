temperature = float(input("What's the temperature outside now (in C)?\n"))
temperature = (temperature*9/5)+32
print("It's " + str(temperature) +" F")
if temperature > 80:
    print("It's too hot!")
    print("Stay inside!")
elif temperature < 60:
    print("It's too cold!")
    print("Stay inside!")
else:
    print("Enjoy the outdoors!")