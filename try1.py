import pandas as pd

df = pd.DataFrame(data = [],columns = ['Guess','Result'])

for i in range(10):
    df = df.append({'Guess':f"guess {i}" , 'Result' :f"result {i}"},ignore_index=True)

print(df.loc[[1,2,3,11]])