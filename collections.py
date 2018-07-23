#Exercise 1
#1
a = [1, 3, 5]
b = [2, 4, 6]

#2
c = a + b
#print(c)

#3
d = sorted(c)
#print(c)
#print(d)   

#4
d.reverse()
#print(d) 

#5
c[3] = 42
#print(c)

#6
d.append(10)

#7
c.extend([7, 8, 9])
print(c)

#8
print(c[:3])

#9
print(d[-1])

#10
print(len(d))


#Exercise2
#1
a = (2, 4, 6, 8)
b = (10, 12, 14, 16)

#2
c = a + b
print(c)

#3
d = sorted(c)
print(d)

#4
print(d[2])

#5
print(d[-3:])

#6
print(len(d))


#Exercise3
#1
a = {2, 4, 6, 8}
b = {1, 3, 5, 7}

#2 combines all the numbers which are in a or b (or both)
c = (a | b)

#3 contains all the numbers in a but not in b
d = (a - b)

#4 contains all the numbers in b but not in a
e = (b - a)

#5 contains all the numbers which are both in a and in b
f = (a & b)

#6 contains all the numbers which are either in a or in b but not in both
g = (a ^ b)

#7
print(len(c))


#Exercise4
#1
print(list(range(20)))

#2
print(list(range(3, 13)))

#3
print(list(range(2, 51, 3)))


#Exercise5
#1
dict = {"Jane Doe": "+27 555 5367", "John Smith": "+27 555 6254", "Bob Stone": "+27 555 5689"}

#2
dict["Jane Doe"] = "+27 555 1024"

#3
dict["Anna Cooper "] = "+27 555 3237"

#4
print(dict["Bob Stone"])

#5
print(dict.get("Bob Stone", None))

#6
print(dict.keys())

#7
print(dict.values())


#Exercise6
#1
a = tuple([1, 1, 2, 3, 3])

#2
b = list(a)
print(len(b))

#3
c = set(b)
print(len(c))

#4
d = list(c)
print(len(d))

#5
e = list(range(1, 11))

#6
dict = {"Jane Doe": "+27 555 5367", 
        "John Smith": "+27 555 6254", 
        "Bob Stone": "+27 555 5689"}
t = list(dict.items())

#7
v = list(dict.values())

#8
k = list(dict)

#9
s = sorted("antidisestablishmentarianism")
print(type(s))
s2 = "".join(s)
print(s2)

#10
w = "the quick brown fox jumped over the lazy dog".split()
print(w)


#Exercise7
#1
a = [1, [2, 3,], [4, 5, 6]]

#2
print(a[1][1])

#3
b = [[1, 2, 3, 4,], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(b[0][-2:])