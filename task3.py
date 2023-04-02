aaa = input("Введите текст: ")
words = aaa.split() 
zzz = {}
for word in words:
    if word in zzz:
        zzz[word] += 1
    else:
        zzz[word] = 1
zzz_word = max(zzz, key=zzz.get)
pinus = max(words, key=len)

print("Самое часто встречающееся ", zzz_word)
print("Самое длинное ", pinus)
