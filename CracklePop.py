def cracklePop():
    for y in range(1,101,1):
        if y % 3 == 0 and y % 5 == 0:
            print("CracklePop")
        elif y % 3 == 0:
            print("Crackle")
        elif y % 5 == 0:
            print("Pop")
        else:
            print(y)
            
cracklePop();