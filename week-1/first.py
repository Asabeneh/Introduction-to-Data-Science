fname = "Asabeneh"
age = 100
lname = "Yetayeh"

amISingle = True
amImarried = False

isRaining = False

if (isRaining):
    print("Take an umberalla with you.")

fullname = fname + " " + lname
print(fullname)

for num in range(20):
    print(num)


def zeroToTwenty():
    arr = []
    for i in range(21):
        arr.append(i)
    return arr


print(zeroToTwenty())


def reverseArray(arr):
    newarr = []
    for i in range(len(arr)):
        newarr.append(arr[len(arr) - i - 1])
    return newarr


print(reverseArray([1, 2, 3, 4, 5]))


def writeOnFile():
    f = open('example.txt', 'w')
    f.write("Hello World")
    f.write("This our new text file")
    # f.write(arr)
    f.close()


print(writeOnFile())

# def writeOnFile1(arr):
# f = open('example.txt','r')
# for i in range(len(arr)):
# f.write(str(i))
# f.close()
# print(writeOnFile1([1,2,3,4]))


# 1.4
print("a", "a^2", "a^3")
print(1, 1 ** 1, 1 ** 3)
print(2, 2 ** 1, 2 ** 3)
print(3, 3 ** 1, 3 ** 3)
print(4, 4 ** 1, 4 ** 3)

# 1.9
width = 4.5
height = 7.9
area = width * height
perimeter = 2 * (width + height)

print("Area of the rectangle is ", area)
print("Perimeter of the rectangle is ", perimeter)
# 1.10
distance = 14 / 1.6  # changing killometer to miles
time = (45 + 0.5) / 60  # change the seconds, minutes to hour
speed = distance / time  # in miles/hour
print("The average speed of the runner is ", speed, " miles/hour")


def looping():
    arr = [10,20,30,40,50]
    for i in range(len(arr)):
        print("For index ", i, " the value is " +str(arr[i]))


looping()
