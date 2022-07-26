from ntpath import join

file = open('hw4.txt', "w", encoding = 'utf-8')
file.write("Мама сшила м0не штаны и7з бере9зовой кор45ы 893.")
file.close()

file = open('hw4.txt', "r", encoding = 'utf-8')
data = file.read().split()
sort = []

for words in data:
    if words.isalpha():
        sort.append(words)
file.close()        

print(' '.join(sort))

