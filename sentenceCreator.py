import random

def generate(strlen):
    result = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    for i in range(strlen):
        result = result + alphabet[random.randrange(27)]
    return result

print(generate(28))

def score(goal, string):
    lettersSame = 0
    for i in range(len(goal)):
        if goal[i] == string[i]:
            lettersSame = lettersSame + 1
    return lettersSame/len(goal)

def main():
    gString = "methinks it is like a weasel"
    nString = generate(28)
    bScore = 0;
    nScore = score(gString,nString)

    while nScore < 1:
        if nScore > bScore:
            print(nScore, nString)
            bScore = nScore;
        nString = generate(28)
        nScore = score(gString, nString)
main()
