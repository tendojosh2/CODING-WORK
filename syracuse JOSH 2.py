def syracuse_sequence(x):
    print("Syracuse sequence starting with", x, ":")
    while x != 1:
        print(x, end=" ")
        if x % 2 == 0:
            x = x // 2
        else:
            x = 3 * x + 1
    print(1)

start_value = int(input("Enter the starting value for the Syracuse sequence: "))
syracuse_sequence(start_value)
