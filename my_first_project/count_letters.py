def letter_count(s,l):
    acc = 0
    for i in s:
        if i==l:
            acc += 1
    return acc

print(letter_count("The quick brown fox jumped over the lazy dogs.",'e'))