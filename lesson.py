from random import random
data = []
for j in range (10) :
	data.append(int(random()*10))
print(data)

f = []
for k in data:
	b = 0
	for h in data:
		if k==h:
			b += 1
	if b == 1:
		f.append(k)
print(f)