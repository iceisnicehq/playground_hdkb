z = 1400000.0
c = 0
a = float(input("a = "))
k = float(input("k = "))
print(a*0.8)
print(a*0.2)
print(k*a)
print(k*0.4*a)
print((0.8+0.2+k+k*0.4)*a+a)
sum = (0.8+0.2+k+k*0.4)*a+a
with open("py.py", "a+") as code:
	code.write("c"+"+="+str(sum)+"\n")	
c+=2644026.0
c+=216716.0
c+=17407682.799999997
c+=477360.0
c+=620505.6000000001
