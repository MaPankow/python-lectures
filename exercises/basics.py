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
def umsatzsteuer(umsatz, steuerjahr = 2024):
    '''
    :param umsatz: Umsatz im Steuerjahr
    :type umsatz: float
    :param steuerjahr: Steuerjahr
    :type steuerjahr: int

    :return: Umsatzsteuer
    :rtype: float
    '''
    pass

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
def area (shape, params):
    '''
    :param shape: Shape
    :type shape: string
    :param params: Parameters of the shape
    :type params: dict

    :return: Area of the shape
    :rtype: float
    '''
    import math
    pass

# loops

'''
Schreibe eine Funktion, die alle Karten eines Kartenspiels jeweils mit ihrer
Farbe (Clubs, Spades, Hearts, Diamonds) und ihrem Wert (2 - 10, J, K, Q, A)
erzeugt.
Die Karten werden als Tupel bestehend aus Farbe und Wert dargestellt und alle
Karten in einer Liste gesammelt zurückgegeben.
'''
def deckOfCards():
    pass

'''
Schreibe eine Funktion, die die ersten N Antworten für das FizzBuzz-Spiel
erzeugt und auf der Konsole ausgibt.

Siehe auch https://de.wikipedia.org/wiki/Fizz_buzz
'''
def fizzbuzz(n):
    pass

# recursion

'''
Schreibe eine rekursive Funktion, die die N-te Fibonacci-Zahl berechnet.

Siehe auch https://de.wikipedia.org/wiki/Fibonacci-Folge
'''
def fibonacci(n):
    '''
    :type n: int
    
    :return: n-th Fibonacci number
    :rtype: int
    '''
    pass