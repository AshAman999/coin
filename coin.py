import random
toss = "t"
while(toss == "t"):
    toss = input("press t to toss\n")
    x = random.randint(1,2)
    if x == 1:
        print ("HEADS")
    else:
        print ("TAILS")