import wordle_help
import pandas as pd



with open('low.txt', 'r') as f:
    all = [line.strip() for line in f.readlines()]

zeros = [1.01 for i in all]
dict = {"Expected entropy": zeros}
df = pd.DataFrame(dict, index = all)

with open('listofwordlewords.txt','r') as f2:
    wordles_ans = [line.strip() for line in f2.readlines()]

#print(wordles_ans[0:20])

df2 = wordle_help.update_entropy(df,wordles_ans)

df2.to_csv("start_entropyv2.csv")

