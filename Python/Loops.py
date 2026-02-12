#For Loop
#While Loop
#Break Continue Statements

# for i in range(1, 5, 2):
#     print(i)


while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    # except Exception as e:
    #     print("Something went wrong:", e)