def bubble_sort(inp):
    i = 0
    j = i+1
    n = len(inp)
    while (i < n-1):
        while (j < n):
            if inp[i] > inp[j]:
                temporary = inp[i]
                inp[i] = inp[j]
                inp[j] = temporary
            j += 1
        i += 1
        j = i+1
    return (inp)

inp1 = [-2, 5, 4, 3, 0]
print(inp1)
inp2 = bubble_sort(inp1)
print(inp2)
