from basics import *



print(add(2, 1))

print(subtract(3, 4))

print(multiply(7, 8))

print(divide(8, 4))

print('-------------------')

print(inFahrenheit(1))

print('-------------------')

print(inCelsius(100))

print('-------------------')

# zahl = input("Gib eine Zahl ein, um zu überprüfen, ob sie gerade ist")
# zahl = int(zahl)
# if isEven(zahl) == True:
#     print(str(zahl) + ' ist gerade.')
# else:
#     print(str(zahl) + ' ist ungerade.')

# print('-------------------')

# num2 = input("Gib eine Zahl ein, um zu überprüfen, ob sie ungerade ist")
# num2 = int(num2)
# if isOdd(num2) == True:
#     print(str(num2) + ' ist ungerade.')
# else:
#     print(str(num2) + ' ist nicht ungerade.')

# print('-------------------')

# monat = input("Den wievielten Monat haben wir gerade? ")
# monat = int(monat)
# antwort = jahreszeit(monat)
# print("Es ist gerade " + antwort + ".")

print('-------------------')

print(umsatzsteuer(19000, 2023))

print('-------------------')


fizzbuzz(20)

print('-------------------')
    
for i in range(0, 10):
    print(fibonacci(i))
