from wonderwords import RandomWord
import random

r = RandomWord()

f = open("testcases.txt", "a")

for i in range(1000):
    text = ""

    for j in range(random.randint(4, 20)):
        text += r.word() + ";"

    print("Test Case " + str(i + 1) + " Written!")
    f.write(text + "\n")

f.close()