import itertools as it
import math
import pandas as pd

#Get all permutation of length 4
with open('low.txt', 'r') as f:
    all = [line.strip() for line in f.readlines()]

remaining = all

df = pd.read_csv("start_entropy.csv",index_col=0)




#check for the number of common numbers
def checkcommon(inn,ans):
    temp = list(ans)
    out = list('bbbbb')
    for l in range(5): 
        if inn[l] == temp[l]:
            out[l] = 'g'
            temp[l] = '0'
        elif inn[l] in temp:
            out[l] = 'y'
            temp[temp.index(inn[l])] = '0'
    return ''.join(out)
            


#compute expected entropy from the possible outcome
def expected_entropy(dict,remaining):
    result = 0.0
    for i in dict:
        result = result + dict[i]/len(remaining)*math.log2(1/dict[i])
    return result

#compute current entropy
def entropy(remaining):
    ent = math.log2(1./len(remaining))
    return ent


#We keep track of 2 data
# remaining =  *list* of possible answers
# df = *data frame* of expected entropy

#after playing, we can update the entropy list to see what to choose next
def update_entropy(df,remaining):
    outdf = df
    for nextguess in all:
        tally = {}
        for ans in remaining:
            colorresult = checkcommon(nextguess,ans)
            if colorresult in tally.keys():
                tally[colorresult] = tally[colorresult]+1
            else:
                tally[colorresult] = 1
        #print(f"{nextguess} gives {tally}")
        outdf['Expected entropy'][nextguess] = expected_entropy(tally,remaining)

    outdf.sort_values(by='Expected entropy',inplace=True,ascending=False)
    return outdf
    #dfremain = df.loc[remaining].sort_values(by='Expected entropy',ascending=False)


#call it when you want to play the game
def play_and_update_remaining(guess,result,remaining):
    # guess = input("What is your guess: ")
    # result = input("What is your result: ")

    newl = []

    for ans in remaining:
        tryresult = checkcommon(guess,ans)
        if tryresult == result:
            newl.append(ans)

    return newl

# def report_all_remaining(remaining):
#     print("List of top remaining possible answers")
#     print(dfremain.head())

#get report
def report(df,remaining):
    possibleanswers =len(remaining)
    print()
    print("################################")
    print("##### Current game report ######")
    print("################################")
    print()
    print(f"There are {possibleanswers} possible answers left.")
    ent = entropy(remaining)
    print(f"Current entropy = {ent}")
    print("Here is the top expected entropy for the next guess")
    print(df.head())
    # report_all_remaining()
    print("################################")
    print("#####End of the report##########")
    print("################################")

# def reset():
#     global remaining
#     global df
#     df = pd.read_csv("start_entropy.csv",index_col=0)
#     remaining = all


# report()

# while True:
#     play_and_update_remaining()
#     update_entropy()
#     report()


    
