letters = "ABCDEFGHI"
n =len(letters)
for i in range(n,0,-2):
    for j in range(0,i):
        print(letters[j],end="\t")
    print(end="\n")