# add_ten = lambda a: a + 10
# print(add_ten(7))

# def call_function(func, *args):
#     return func(*args)

# def add(x, y):
#     return x + y

# def subt_ten(x):
#     return x - 10

# result1 = call_function(add, 2, 7)
# result2 = call_function(subt_ten, 12)

# print(result1 + result2)

# Funktion, die 3 und 4 multipliziert:
# def multiply(a, b):
#     return a * b

# result1 = multiply(3, 4)

# Lambda-fkt, die 5 hoch 2 nimmt

# a = 5
# result2 = lambda a: a ** 2
# print(result2(5))

# Fukt. die eine andere Fkt als Argument nimmt
# import math

# def call_function(func, *args):
#     return func(*args)

# def circle(r):
#     return math.pi * (r ** 2)

# result3 = call_function(circle, 3)
# print(result3)


# Aufgabe Zahlenratespiel
import random
# def call_function(func):
#     return func()
    
def zufallszahl_generieren():
    return random.randint(1, 100)
    
    
def benutzereingabe():
    return int(input("Gib deinen Tipp ein! "))
    
    

def vergleichen(geratene_zahl, zufallszahl):
    
    if(geratene_zahl < zufallszahl):
        print("Die Zahl ist zu niedrig. Versuche es erneut!")
        return False
    elif(geratene_zahl > zufallszahl):
        print("Die Zahl ist zu hoch. Versuche es erneut!")
        return False
    else:
        
        return True


def spiel():
    n = 0
    zufallszahl = zufallszahl_generieren()
    erraten = False

    while not erraten:
        geratene_zahl = benutzereingabe()
        erraten = vergleichen(geratene_zahl, zufallszahl)
        n = n + 1
        
    print(f'Glückwunsch! {zufallszahl} ist richtig! \n\
          Du hast {n} Versuche gebraucht!')
    
    
    
spiel()

