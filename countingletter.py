dictionary = {}
n = str(input("Input String: "))
for i in n:
    dictionary[i] = dictionary.get(i, 0) + 1
    after = sorted(dictionary.items())
for i in after:
    print(i)

