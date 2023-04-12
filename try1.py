import pandas as pd

df = pd.DataFrame(data = [],columns = ['Guess','Result'])

df = df.append({'Guess':"guess 1" , 'Result' :"result 1"},ignore_index=True)

print(df)