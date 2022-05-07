n=int(input())
l=[]
d={}
for i in range(n):
	x=int(input())
	l.append(x)
for i in l:
	if i%2==0:
		d[i]='yes'
	else:
		d[i]='no'
print(d)
