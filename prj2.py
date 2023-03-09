
n = int(input("ente number to print satr"))
def pypart(n):

  for i in range(0, n):
    if(n==4):
     for j in range(0, i+1):
      print(" *", end="")
     print("\r")
    else:
        def pattern(n):
            for i in range(n):
                for j in range(n - i - 1):
                    # print star
                    print("* ", end="")
                print(" ")

        # take input
       # n = int(input('Enter the number of rows: '))

        # calling function
        pattern(n)

pypart(n)



