S = input()

for i in range(97, 123):
    # try:   
    #     i = chr(i)
    #     print(S.index(i), end=" ")
    # except:
    #     print(-1, end=" ")
    print(S.find(chr(i)), end=" ")