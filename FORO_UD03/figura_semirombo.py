altura = 5
for i in range(1,altura):
        if(i==1):
            print(" "*altura,end="")
            print("*")
        else:
            print(" "*(altura - i) + "*" + " "*(i - 1) + "*")

for i in range(altura, 0, -1):
            print(" "*(altura - i) + "*" + " "*(i - 1) + "*")
        
print(" "*altura,end="")
print("*")