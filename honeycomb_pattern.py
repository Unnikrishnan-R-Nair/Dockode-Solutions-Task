ins = input('inputs :- ').split(" ")
row, col = int(ins[0]), int(ins[1])
# print(row, col)

li = ['___', '/', '\\']

for i in range(row):

    if i==0:
        for c in range(col):
            if c==0:
                print(f' {li[0]}', end="")
            elif c%2==0:
                print(f"{li[0]}", end="")
            elif c%2==1:
                print(" "*5, end="")
        print()
        for c in range(col):
            if c%2==0:
                print(f"{li[1]}{" "*len(li[0])}{li[2]}", end="")

            elif c%2==1:
                print(f"{li[0]}", end="")
        print()
        for c in range(col):
            if c%2==0:
                print(f"{li[2]}{li[0]}{li[1]}", end="")
            elif c%2==1:
                print(" "*3, end="")
        

    elif i%2==0:
        
        for c in range(col):
            if c==0:
                print(f' {" "*len(li[0])}', end="")
                pass
            elif c%2==0:
                print(f"{" "*len(li[0])}", end="")
                pass
            elif c%2==1:
                print(" "*5, end="")
        print()
        for c in range(col):
            if c%2==0:
                print(f"{li[1]}{" "*len(li[0])}{li[2]}", end="")

            elif c%2==1:
                print(f"{li[0]}", end="")
        print()
        for c in range(col):
            if c%2==0:
                print(f"{li[2]}{li[0]}{li[1]}", end="")
            elif c%2==1:
                print(" "*3, end="")

    else:
              
        for c in range(col):
            if c==0:
                print(f' {" "*len(li[0])}', end="")
                pass
            elif c%2==0:
                print(f"{" "*len(li[0])}", end="")
                pass
            elif c%2==1:
                print(" "*5, end="")
        print()
        for c in range(col):
            if c%2==0:
                print(f"{li[1]}{" "*len(li[0])}{li[2]}", end="")

            elif c%2==1:
                print(f"{li[0]}", end="")
        print()
        for c in range(col):
            if c%2==0:
                print(f"{li[2]}{li[0]}{li[1]}", end="")
            elif c%2==1:
                print(" "*3, end="")

print()
        
    



    
        
            
