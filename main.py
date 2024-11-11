num = int(input("Enter a number: "))
t = num
numlen = 0

while t > 0 :
    numlen = numlen + 1
    t = int(t / 10)

if numlen >= 4 :
    numlen = numlen // 2
    chk = 0
    while num > 0 :
        rem = num % 10
        if chk == numlen :
            midone = rem
        elif chk == (numlen - 1) :
            midtwo = rem
        num = num // 10
        chk = chk + 1
    prod = midone * midtwo

    print(prod)
else :
    print("Number is less than 4")