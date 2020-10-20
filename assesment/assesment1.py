#define locate function
def locate():
    print("Where are you?")
    location = input()
    print("You are in a {}".format(location))
    print("You must use your hair to escape!")

#sample run to test locate function
#locate()

#define escape function
def escape(metres):
    if metres >=5:
        print("You will need your hair to escape!")
    else:
        print("You may be able to jump to escape!")

#sample run to test escape function
#escape(7)
#escape(2)

#define untangle function
def untangle(num_brushes):
    while num_brushes != 0:
        print("Brushing hair...")
        num_brushes = num_brushes-1
        if num_brushes == 0:
            print("The hair is now untangled!")

#sample run to test untangle function
#untangle(9)