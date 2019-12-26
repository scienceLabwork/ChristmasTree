n = int(input("Input Length of chritmas tree: "))
ui = n
s = "*"
y = "\/"

#print(" "*(n)+y)
print(" "*(n),"$")
for i in range(1,n):
    n-=1
    o = i + 1
    print(" "*n,s*i+s*o)

for j in range(0,4):
    print(" "*(ui),"||")

print("\n\nChritmas Tree by Rudra Shah")
