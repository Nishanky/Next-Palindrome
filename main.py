print("This program will print a next palindrome corresponding to given number..")
org_num = []
testcase = 0

try:
    testcase = int(input("Enter the number of test cases you want to check"))
    if testcase > 10:
        print("Test Cases should be less than 10!!")
        exit()

    for i in range(testcase):
        org_num.append(int(input(f"Enter test case {i+1}:")))
except ValueError:
    print("Only integers are allowed..")
    exit()


i=0
num = org_num[i]
temp = num
rev = 0

while i < testcase:
    while(temp > 0):
        dig = temp % 10
        rev = rev * 10 + dig
        temp = temp // 10

    if(num == rev):
        print(f"\nNext palindrome for {org_num[i]} is {num}")
        i += 1
        if i < testcase:
            num = org_num[i]
    else:
        num += 1
        temp = num
        rev = 0










