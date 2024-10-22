#Area Calculator project from Codedex
print("====================")
print(" Area Calculator 📐")
print("====================\n")
print("1) Triangle")
print("2) Rectangle")
print("3) Square")
print("4) Circle")
print("5) Quit\n")
while True:
    try:
        shape = int(input("Witch shape: "))
        print("")
        if shape>=1 and shape<=5:
            break
        else:
            print("No Valid Option")
    except:
        print("No Valid Option")
if shape == 1:
    while True:
        try:
            base = int(input("Base: "))
            height = int(input("Height: "))
            print("")
            break
        except:
            print("No valid input, try again.")
    area=(height*base)/2
    print(f"The area is: {area}")
elif shape == 2:
    while True:
        try:
            length = int(input("Length: "))
            width = int(input("Width: "))
            print("")
            break
        except:
            print("No valid input, try again.")
    area=length*width
    print(f"The area is: {area}")
elif shape == 3:
    while True:
        try:
            side = int(input("Side: "))
            print("")
            break
        except:
            print("No valid input, try again.")
    area=side*side
    print(f"The area is: {area}")
elif shape == 4:
    while True:
        try:
            radius = int(input("Radius: "))
            print("")
            break
        except:
            print("No valid input, try again.")
    area=3.1416*radius**2
    print(f"The area is: {area}")
else:
    print("Quit")