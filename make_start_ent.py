import wordle_help
import pandas as pd

df = pd.read_csv("start_entropy.csv",index_col=0)

with open('low.txt', 'r') as f:
    all = [line.strip() for line in f.readlines()]

with open('listofwordlewords.txt','r') as f2:
    wordles_ans = [line.strip() for line in f2.readlines()]

#print(wordles_ans[0:20])

df2 = wordle_help.update_entropy(df,wordles_ans)

df2.to_csv("start_entropyv2.csv")

