from random import random
data = []
for j in range (10) :
	data.append(int(random()*10))
print(data)

s = []
for i in data:
	if data.count(i) == 1:
		s.append(i)
print(s)