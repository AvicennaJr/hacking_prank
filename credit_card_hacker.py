import math
import time


def progress_bar(progress, total):
    percent = 100 * (progress / float (total))
    bar = '█' *int( percent)  + '-' * (100-int(percent))
    print(f"\r|{bar}| {percent: .2f}% Searching", end="\r")




print('''****Credit Card Hacking Tool****

Made By Avi - the Dark Web Lord

!!!!I WILL NOT BE RESPONSIBLE FOR ANY ILLEGAL ABUSE!!!!

''')

input("Credit Card Number: ")

print("\nSearching For Owner\n")

numbers = [x * 5 for x in range(2000, 3000)]
result = []

progress_bar(0, len(numbers))

for i, x in enumerate(numbers):
    result.append(math.factorial(x))
    progress_bar(i + 1, len(numbers))


print("\n\n Credit Card Owner Found: ************")

input("Please input the Account's SORT CODE: ")

time.sleep(3)

input("\nSort Code Error. Please try again: ")
time.sleep(3)
print("\n")
numbers = [x * 5 for x in range(1000, 2000)]
result = []

progress_bar(0, len(numbers))

for i, x in enumerate(numbers):
    result.append(math.factorial(x))
    progress_bar(i + 1, len(numbers))

print("\n\n Total Cash: $34550\n")

input("Begin Cash Transfer (Yes/ No): ")

print("\n")
def progress_bar(progress, total):
    percent = 100 * (progress / float (total))
    bar = '█' *int( percent)  + '-' * (100-int(percent))
    print(f"\r|{bar}| {percent: .2f}% Transfered", end="\r")
    
numbers = [x * 5 for x in range(4000, 5000)]
result = []

progress_bar(0, len(numbers))

for i, x in enumerate(numbers):
    result.append(math.factorial(x))
    progress_bar(i + 1, len(numbers))
    
print("\n\n\n TRANSFER COMPLETE WITH ZERO ERRORS. HAPPY HACKING!")
