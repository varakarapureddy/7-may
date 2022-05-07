def perfectsquare(h) :
    i = 1
    while(i**2 <= h):
        if ((h%i == 0) and (h/i == i)):
            return True
        i += 1
    return False
n=int(input())
l=[]
d={}
for i in range(n):
	x=int(input())
	l.append(x)
for i in l:
	if perfectsquare(i):
		d[i]='yes'
	else:
		d[i]='no'
print(d)
