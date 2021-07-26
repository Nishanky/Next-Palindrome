def is_palindrome(n):
    return str(n) == str(n)[::-1]

def next_palindrome(n):
    n += 1
    while not is_palindrome(n):
        n += 1
    return n

if __name__ == '__main__':
    org_num = []
    testcase = 0
    try:
        testcase = int(input("Enter the number of test cases you want to check"))
        if testcase > 10:
            print("Test Cases should be less than 10!!")
            exit()

        for i in range(testcase):
            org_num.append(int(input(f"Enter test case {i + 1}:")))
    except ValueError:
        print("Only integers are allowed..")
        exit()


    for i in range(testcase):
        print(f"\nNext palindrome for {org_num[i]} is {next_palindrome(org_num[i])}")
