number = [0,1,2,3,4,5,6,7]

for i in range (len (number)):
    number[i]=(-number[i]-1)%8
print(str(number) +"hello")

for i in range (len (number)):
    number[i]=(-number[i])%8
print(number)

x="s"
x+1
print(x)
