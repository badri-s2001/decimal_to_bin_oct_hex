def print_binary(n):

    if n == 0:
        print(0)
        return

    ans = ""
    l = []
    while n > 0:
        rem = n % 2
        n = n // 2
        l.append(str(rem))

    for i in l[::-1]:
        ans += i

    print(ans)


def print_octal(n):

    if n == 0:
        print(0)
        return

    ans = ""
    l = []
    while n > 0:
        rem = n % 8
        n = n // 8
        l.append(str(rem))

    for i in l[::-1]:
        ans += i

    print(ans)


def print_hexa(n):

    if n == 0:
        print(0)
        return

    ans = ""
    l = []
    while n > 0:
        rem = n % 16
        n = n // 16
        if rem == 10:
            l.append('A')
        elif rem == 11:
            l.append('B')
        elif rem == 12:
            l.append('C')
        elif rem == 13:
            l.append('D')
        elif rem == 14:
            l.append('E')
        elif rem == 15:
            l.append('F')
        else:
            l.append(str(rem))

    for i in l[::-1]:
        ans += i

    print(ans)


while True:
    try:
        num = int(input("Enter a decimal number: "))
    except ValueError as err:
        print("Please enter a number")
    else:
        if num < 0:
            print("Please enter a  non negative number")
        else:
            print("Binary:")
            print_binary(num)
            print("Octal:")
            print_octal(num)
            print("Hexadecimal:")
            print_hexa(num)
