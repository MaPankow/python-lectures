from datetime import datetime
import math

'''
Schreibe je eine Funtion add, subtract, multiply, divide, die die
jeweilige Grundrechenart auf die beiden übergebenen Parameter A und B
anwendet.
'''
def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


'''
Schreibe eine Funktion, die eine Temperatur in Celsius in eine Temperatur in
Fahrenheit umrechnet.
'''
def inFahrenheit(celsius):
    '''
    :param celsius: Temperature to convert in Celsius
    :type celsius: float

    :return: Converted temperature in Fahrenheit
    '''

    fahrenheit = celsius * 1.8 + 32
    return fahrenheit

'''
Schreibe eine Funktion, die eine Temeratur in Fahrenheit in eine Temperatur
in Celsius umrechnet.
'''
def inCelsius(fahrenheit):
    '''
    :param fahrenheit: Temperature to convert in Fahrenheit
    :type fahrenheit: float

    :return: Converted temperature in Celsius
    :rtype: float
    '''
    celsius = (fahrenheit - 32) / 1.8
    return celsius

'''
Schreibe eine Funktion, die prüft, ob eine Zahl gerade ist.
'''
def isEven(num):
    '''
    :param num: Number to test
    :type num: int

    :rtype: bool
    '''
    if num % 2 == 0:
        return True


'''
Schreibe eine Funktion, die prüft, ob eine Zahl ungerade ist.
'''
def isOdd(num2):

    if num2 % 2 != 0:
        return True
    '''
    :param num: Number to test
    :type num: int

    :rtype: bool
    '''
    

# Kontrollfluss

# if

'''
Schreibe eine Funkntion, die abhängig von dem als Zahl eingegebenen Monat die
passende Jahreszeit zurückgibt. Und zwar

"Frühling" für die Monate März, April, Mai
"Sommer" für die Monate Juni, Juli, August
"Herbst" für die Monate September, Oktober, November und
"Winter" für die Monate Dezember, Januar und Februar.
'''
def jahreszeit(monat):
    '''
    :type monat: int
    :return: Jahreszeit
    :rtype: string
    '''
    match monat:
        case 3 | 4 | 5:
            return "Frühling"
        case 6 | 7 | 8:
            return "Sommer"
        case 9 | 10 | 11:
            return "Herbst"
        case 12 | 1 | 2:
            return "Winter"
        case _:
            return "Invalid input"

'''
Schreibe eine Funktion, die die Umsatzsteuer anhand des Umsatzes und des
Steuerjahres berechnet. Der Steuersatz beträgt 19%. Liegt der Umsatz unter
der Freigrenze von 17.500 EUR (für die Steuerjahre 2003-2019) bzw. 22.000 EUR
(für die Steuerjahre ab 2020) soll die Kleinunternehmerregelung angewendet
und keine Umsatzsteuer berechnet werden. Der Rückgabewert ist dann 0.
'''
def umsatzsteuer(umsatz, steuerjahr):
    steuersatz = umsatz / 100 * 19
    current_year = datetime.now().year
    if steuerjahr >= 2003 and steuerjahr <= 2019:
        if umsatz <= 17500:
            return 0
        else: return steuersatz
    if steuerjahr > 2019 and steuerjahr < current_year:
    # if steuerjahr > 2019 and steuerjahr < 2024:
        if umsatz <= 22000:
            return 0
        else: return steuersatz
    else:
        return "Invalid input"

    

# match

'''
Schreibe eine Funktion, die den Flächeninhalt verschiedener geometrischer
Formen berechnet. Die Funktion soll zwei Argumente erhalten:
Den Namen der geometrischen Form (circle, triangle, rectangle), sowie die
dafür relevanten Parameter als ein Dictionary.
Für die Berechnung eines Kreises wird der Radius (radius) benötigt.
Für die Berechnung eines Dreieckes sowie eines Rechteckes werden die Länge
der Grundseite (base) sowie die Höhe (height) benötigt.

Beispiele für den `params` Parameter:

{ 'radius': 1.0 }
{ 'base': 2, 'height': 1 }

'''
params = {
   
    "radius": 1.0,
    "base": 2,
    "height": 1.8
}

def area (shape, params):
    match shape:
        case "circle":
            return math.pi * (params["radius"] ** 2)
        case "triangle":
            return (params["base"] * params["height"]) / 2
        case "rectangle":
            return(params["base"]) * params["height"]

    

# loops

'''
Schreibe eine Funktion, die alle Karten eines Kartenspiels jeweils mit ihrer
Farbe (Clubs, Spades, Hearts, Diamonds) und ihrem Wert (2 - 10, J, K, Q, A)
erzeugt.
Die Karten werden als Tupel bestehend aus Farbe und Wert dargestellt und alle
Karten in einer Liste gesammelt zurückgegeben.
'''
def deckOfCards():
    colours = ['Clubs', 'Spades', 'Hearts', 'Diamonds']
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'K', 'Q', 'A']
    for item in colours:
        for card in cards:
            print(item + ' - ' + card)
        
    

'''
Schreibe eine Funktion, die die ersten N Antworten für das FizzBuzz-Spiel
erzeugt und auf der Konsole ausgibt.

Siehe auch https://de.wikipedia.org/wiki/Fizz_buzz
'''
def fizzbuzz(n):
    for i in range(0, n):
        i = i + 1
        if i % 15 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

# recursion

'''
Schreibe eine rekursive Funktion, die die N-te Fibonacci-Zahl berechnet.

Siehe auch https://de.wikipedia.org/wiki/Fibonacci-Folge
'''
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


    

