def compare(s1, s2, n):
    c = 0
    for i in range(0, n):
        if s1[i] != s2[i]:
            return False
        else:
            c = c+1
    if c == n:
        return True
s1 = input("Enter 1st string:")
s2 = input("Enter 2nd string:")
n = int(input("Enter the number:"))
result = compare(s1, s2, n)
if result == True:
    print("The first", n, "characters are same.")
else:
    print("The first", n, "characters are not same.")