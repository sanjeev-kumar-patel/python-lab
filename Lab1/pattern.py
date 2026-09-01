n = int(input("Enter the number of rows of the pattern you want."))
for i in range(1, n+1):
    for j in range(0,i):
        print("*", end="")
    print("\n")