#The Hello world of Hill Climbing
#1. First step is to generate a random solution
import random
import string
def generateRandomSoln(length=5):
    return [random.choice(string.printable) for _ in range(length)]
#The important thing is we know the Goal State and we are generating a random
#state to start off to the Goal State. To know if we are getting near the goal
#state we gotta calculate the distance between the current state and the goal state
def eval(solution):
    target = "hello"
    difference = 0
    for i in range(len(target)):
        s = solution[i]
        #print("SOLUTION===",s)
        t = target[i]
        #print("TARGET=====",t)
        #We need to calculate the difference between our SOLUTION and the TARGET
        difference = difference + abs(ord(s)-ord(t))
        #print("ORD(S)======",ord(s))
        #print("ORD(t)======",ord(t))
        #print("DIFFERENCE=",difference)
    return difference
#Now to continue my algorithm, It needs to be processing.
#Here I will process each and every word in a random pattern
def mutate(solution):
    index = random.randint(0, len(solution)-1)
    solution[index] = random.choice(string.printable)

best_possible_solution = generateRandomSoln()
best_possible_score = eval(best_possible_solution)
while(True):
    print('So far the best solution score is:',best_possible_score,' solution is:',"".join(best_possible_solution))
    #If the solution can o longer be improved then abort
    if best_possible_score == 0:
        break
    #Consider the new solution
    newSolution = list(best_possible_solution)
    mutate(newSolution)
    #Storing the evaluation results
    score = eval(newSolution)
    #If the current evaluation score is quite less that the best possible
    #score we defined then we re-define out best and best score with
    #the new ones.
    if eval(newSolution)<best_possible_score:
        best_possible_solution = newSolution
        best_possible_score = score







'''
expressions in string printable [Source: BCS/Dave StackOverflow]

{'N', 'M', '%', 'q', 'L', '{', 'x', 'E', 'J', '.', 'k', 'A',
 'X', '}', 'n', 'G', '=', '-', "'", '`', '|', ']', '>', 'R', ' ',
 '\x0b', 'H', '(', '\x0c', 'T', '^', '4', '$', '2', '+', ':', 'c',
 \'P', '*', '"', 'I', 'i', 'W', 'D', '[', 'o', 'S', 'm', '7', 'r', 'Q',
 'z', 's', '&', '#', 'U', 'f', 'y', 'e', 'w', '?', '6', 't', 'K', 'd',
 'u', 'Z', 'Y', '\t', '9', '_', '8', ')', 'a', 'p', 'V', '\n', 'v', '0',
 'j', '/', 'l', ',', 'F', ';', '1', '!', 'B', '5', 'C', '\\', 'O', '<', 'g',
 '3', '@', 'h', 'b', '\r', '~'}
>>> len(p)
'''










