import random

print("-------------------\n-------------------\n-------------------\nBIG TRIVIA QUIZ\n-------------------\n-------------------\n-------------------")
inp = input("\npress enter to start\n")
print("For each correct answer you will be awarded with 10 points")

score = 0
correct_question = 0
def q1():
    global score
    global correct_question
    print("What year was the quarantine?\n")
    print(" A. 2019  B. 2024\nC. 2020  D. 1999 ")
    q1 = input().capitalize()
    if q1 == "C":
        print("this is correct answer")
        score += 10
        correct_question += 1
    else:
        print("\nyour answer is incorrect\n")
def q2():
    global score
    global correct_question
    print("Who is the president of Russia?\n")
    q2 = input().capitalize()
    if q2 == "Putin":
        print("this is correct answer")
        score += 10
        correct_question += 1
    else:
        print("\nyour answer is incorrect\n")

def q3():
    global score
    global correct_question
    print("What is 11*11?\n")
    q3 = int(input())
    if q3 == 121:
        print("this is the correct answer")
        score += 10
        correct_question += 1
    else:
        print("\nyour answer is incorrect\n")

list = [q1, q2, q3]
for i in random.sample(list,k = 3):
    i()
    list.remove(i)
    

    
    

print()
print()
rounded_percentage = round(correct_question / 3 * 100, 2)
print("you got a score of", score)
print(f"you answered {rounded_percentage}% of questions correctly")
print("-------------------\n-------------------\n-------------------\nTHE END OF THE QUIZ\n-------------------\n-------------------\n-------------------")import random

print("-------------------\n-------------------\n-------------------\nBIG TRIVIA QUIZ\n-------------------\n-------------------\n-------------------")
inp = input("\npress enter to start\n")
print("For each correct answer you will be awarded with 10 points")

score = 0
correct_question = 0
def q1():
    global score
    global correct_question
    print("What year was the quarantine?\n")
    print(" A. 2019  B. 2024\nC. 2020  D. 1999 ")
    q1 = input().capitalize()
    if q1 == "C":
        print("this is correct answer")
        score += 10
        correct_question += 1
    else:
        print("\nyour answer is incorrect\n")
def q2():
    global score
    global correct_question
    print("Who is the president of Russia?\n")
    q2 = input().capitalize()
    if q2 == "Putin":
        print("this is correct answer")
        score += 10
        correct_question += 1
    else:
        print("\nyour answer is incorrect\n")

def q3():
    global score
    global correct_question
    print("What is 11*11?\n")
    q3 = int(input())
    if q3 == 121:
        print("this is the correct answer")
        score += 10
        correct_question += 1
    else:
        print("\nyour answer is incorrect\n")

list = [q1, q2, q3]
for i in random.sample(list,k = 3):
    i()
    list.remove(i)
    

    
    

print()
print()
rounded_percentage = round(correct_question / 3 * 100, 2)
print("you got a score of", score)
print(f"you answered {rounded_percentage}% of questions correctly")
print("-------------------\n-------------------\n-------------------\nTHE END OF THE QUIZ\n-------------------\n-------------------\n-------------------")
