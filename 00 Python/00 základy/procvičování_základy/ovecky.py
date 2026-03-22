def animals(n):
    for x in range(n):
        print(x, "ovecka")
    print("pes")

animals(7)

def animals2(n):
    if n > 10: 
        for x in range(n):
            print(x, "ovečka")
        print("růžová ovečka")
        print("pes")
    else:
        for x in range(n):
            print(x, "ovecka")
        print("pes")


animals2(11)