import this
a = 969
b = 882
(a**2+b**2)
s= "26HZ92SpKx91Eulabeia69V2MssXwRkaMwiu2SBKR3MsAapGlq0hoAJTbjzGgc7V8ZPafRmfOHzsgp5KDAMXoCJt1EP98dYTEesOx2bnWLH6Ox5CXGtqcastusUBZbKZZ2mr0GV0PHBpZvD9iFfXlDdnmiweQkN28CvD5mOlRh8GqsFbcbfBTPTBuj."

first = s[12:19]
print(first)
second = s[67:74]
print(second)
third= s[74:113]
print(third)
fourth=s[113:117]
print(fourth)'
print(s[97])
s="HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain."
a = 22
b = 27
c = 97
d = 102
print(s[a:b+1] + " " + s[c:d+1])


s = "otM6TPEXoDy8QymKNgHhWYxKDhMNmpDf7r73r0TgghUQN4nkyxhhhjlkMTDtXndWSSRdshJMtf88rgQU08iaTLaGVBPituophisQzndXRkhNbGfqPEIS370ZO7YOZRgc6aawalbopillosumgGVSGmlBHWjWdFNCCS06RMfYItejkwryYiuywmR2q."
a = 90 
b = 98 
c = 132 
d = 143
x = s[a:b+1]
y = s[c:d+1]
m = x + " " + y
print(m)

a = 4660 
b = 9631
x = 0
for i in range(a,b+1):
    if i%2 == 1:
        x += i
        print(x)

# working with files 
f = open('rosalind_ini5.txt', 'r')

for line in f:
    print(line)

#splitting lines 

f = open('rosalind_ini5.txt', 'r')
for line in f.readlines(): 
    i = 1
    if i%2 == 0: 
        print(line)
        i += 1
f.close()

