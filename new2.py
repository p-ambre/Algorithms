def reverse(stri, startindex, endindex):

    i = len(stri) - 1
    new3 = ''
    while i >= 0:
        if i > endindex:
            i -= 1
            continue
        if i >= startindex:
            new3 += (stri[i])
            i -= 1
        if i < startindex:
            break
    return new3

stri = "Hi How are you"

print(reverse(stri, 3, 5))
