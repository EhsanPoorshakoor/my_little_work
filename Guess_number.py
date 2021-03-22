# computer guess number by chance
import random
aval = 1
akhar = 99
hads = random.randint(aval,akhar)
print("I guess",hads)

# check its answer by asking
javab = input("Is it ture ?  ")

# b = bigger ,, k = smaller ,, d = correct
while javab != 'd':
    if javab == 'b':
        aval = hads
        hads = random.randint(aval,akhar)
        print("I guess",hads)
        javab = input("Is it ture ?  ")
    elif javab == 'k':
        akhar = hads
        hads = random.randint(aval,akhar)
        print("I guess",hads) 
        javab = input("Is it ture ?  ")
    else:
        exit

print("your number is:")            
print(hads)