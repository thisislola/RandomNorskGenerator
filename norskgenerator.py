import random

with open("adjektive.txt","r") as adj_file:
    adj = adj_file.readlines()
    length = len(adj)
    for i in range(length):
        adj[i]=adj[i].rstrip()    # rms line from txt file
    with open("substantive.txt","r") as sub_file:
        sub = sub_file.readlines()
        length = len(sub)
        for i in range(length):
            sub[i]=sub[i].rstrip()

print(random.choice(adj), random.choice(sub))
