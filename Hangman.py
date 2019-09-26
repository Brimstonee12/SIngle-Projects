import random
import time
liczba_skuc = 0
haslo1 = ['tennis','mercury','paris','kefir','cow']

x=[]
x2=[]
w = '-'
x3=[]
print("WELCOME TO HANGMAN!")
haslo = random.choice(haslo1)

def start():
    print("LETS BEGIN!")
    time.sleep(2)
    print("KEY WORDS CONTAINS ONLY LOWER CASE LETTERS))")
    time.sleep(2)
    print("YOU CAN ONLY MAKE MISTAKE THREE TIMES" '\n')
    time.sleep(5)

    if haslo is 'tennis':
        print("A sport in which you fight with an opponent but do not touch him")
    if haslo is 'mercury':
        print("which is the smallest planet in the solar system?")
    if haslo is 'paris':
        print("Fryderyk Chopin is buried in?")
    if haslo is 'kefir':
        print("Dairy product with bacteria")
    if haslo is 'cow':
        print("Which animal can you meet while walking through the fields?")

start()

for a,i in enumerate(haslo):
    x.append(i)

def func():
    x2.append(w)

pas_len = len(x)

for i in range(0,pas_len):
    func()
print(x2)

liczba_skuc = 0

def engine():
    global liczba_skuc
    li = input("Type a letter or if you know what a key-word is type(W): ")
    if li in x:
        a=(x.index(li))
        x2[a]=li
        print(x2)
        print("Mistakes:",liczba_skuc)
    if li is 'W':
        li2 = input("Give me key word: ")
        if li2 == haslo:
            print("Congratulations you guessed it")
            exit()
        elif li2 is not haslo:
            print("Wrong, You lose!")
            print("Mistakes:",liczba_skuc)
            exit()
    elif li not in x:
        print("Wrong letter")
        print("Key-Word containes only lower case letters"'\n')
        liczba_skuc += 1
        print("Mistakes:",liczba_skuc)
    if liczba_skuc > 3:
        print("You lose!")
        exit()
    if x2 == x:
        print("Congratulations you won!")



for i in range(20):

    engine()
