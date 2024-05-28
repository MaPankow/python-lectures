def user_input():
    return input("Erzähle uns, was dich am Programmieren interessiert!\n> " )



def wordcount(text):
    text = text.lower()
    for char in ".!-,\n":
        text = text.replace(char, ' ')
    words = text.split() 
    return len(words), words  #returns tupel

# text = user_input()
# print(wordcount(text))

def word_frequency(words):
    frequency = {} #Parameter "words" setzt schon mal den Key ins Dictionary,
                    # Schleife ist für den Value
    for word in words:
        if word in frequency:
            frequency[word] += 1 #Schleife überprüft, ob Wort noch einaḿal drin ist
        else:                      #wir schreiben die 1 und rechnen daruf, weil sonst index 0 wäre
                                    #fügt den Wert 1 in den Value ein
            frequency[word] = 1
    return frequency
    
def longest_word(words):
    max_word = ""
    for word in words:
        #das erste Wort wird direkt eingetragen als max_word
        if len(word) > len(max_word):
            max_word = word
    return max_word, len(max_word)
        #wenn die Schleife durch ist, ist das längste Wort drin
        #gibt kürzere Varianten, dafür braucht es eine andere Schleife
  

def average_word_length(words):
        total_length = sum(len(word) for word in words)
        return total_length / len(words)
    

def main():
    text = user_input()
    word_count_result, words = wordcount(text)
    frequency = word_frequency(words)
    max_word = longest_word(words)
    average_length = average_word_length(words)

    print("\nNumber of words:", word_count_result)
    print("\nWord frequency:")
    for word, count in frequency.items():
        print(" {}: {}".format(word, count))
    print("\nLongest Word :", max_word)
    print("\nAverage word length:", average_length)

main()

    #You would say anything and you would try anything to escape your meaningless and your insignificance


'''
Eingabetext zum Kopieren: Ich finde Programmieren spannend, weil es eine Herausforderung ist und einfach cool klingt, wenn ich erzähle, dass ich code. 
'''

