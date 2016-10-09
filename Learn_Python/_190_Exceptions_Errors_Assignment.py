try:
    for i in ['a','b','c']:
        print i**2
except:
    print("Fuck off")

try:
    x = 5
    y = 0

    z = x/y
except:
    print("Fuck you, something happened!")
finally:
    print("And now go fuck yourself")

def square_int():
    while True:
        try:
            i = int(raw_input("Please enter an Integer: "))
            i**= 2
        except:
            print("Come on! Enter a fucking integer")
            continue
        else:
            print("Thank you cabron!")
            break
        finally:
            print("I wanna go to bed")
    print i

square_int()