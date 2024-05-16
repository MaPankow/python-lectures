#!/usr/bin/python3

# while True:
#     eingabe = input('Gib mir eine Zahl! ')
#     try:
#         zahl = int(eingabe)
#         break
#     except ValueError:
#         print('Das war wohl nichts: ' + eingabe)

def input_int(prompt):
    while True:
        eingabe = input(prompt)
        try:
            return int(eingabe)
        except ValueError:
            print('Das war wohl nichts: ' + eingabe)

if __name__ == '__main__':
    
    x = input_int('Gib mir eine Zahl! ')
    y = input_int('Gib mir noch eine Zahl! ')
    z = input_int('Gib mir noch eine Zahl! ')

    print(x, y, z)