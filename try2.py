with open('listofwordlewords.txt', 'r') as f:
        list1 = [line.strip() for line in f.readlines()]

with open('low.txt', 'r') as f:
        list2 = [line.strip() for line in f.readlines()]

for word in list1:
    if not(word in list2):
        print(word)
        
