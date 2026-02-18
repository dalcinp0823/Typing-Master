import random
print("Welcome to Typing Master")
print("Good luck!")
words = [
    "El Alfa", "Rochy RD", "Juan Soto", "Jeudry", "Computadora",
    "Flauta", "Arroz", "Bandera Dominicana", "Celular", "Facil",
    "Salsa", "Baul", "Ferrari", "Bachata", "Dal Cin"
]

random.shuffle(words)

mistakes = 0
correct = 0
total_words = len(words)

for word in words:
    print("Type this word:", word)
    user = input()

    if user == word:
        print("Correct!")
        correct += 1
    else:
        print("Incorrect!")
        mistakes += 1

    print("Progress:", correct + mistakes, "/", total_words)
    print("----------------------")

print("Game Over")
print("Correct words:", correct)
print("Mistakes:", mistakes)




