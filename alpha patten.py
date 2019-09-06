n = int(input())
i = 1
while i <=n:
    j = 1
    sep_char = chr(ord('A') + i -1)
    while j <= i:
        print(sep_char, end="")
        j = j+1
    print()
    i = i + 1