l = [4,5,1,2,9,7,10,8]
print("original List :", l)

count= 0

for i in l:
    count = count+i
    
avg = count/len(l)

print("Sum =", count)
print("average =", avg)

l.sort()
print()

print("Smallest element is:", l[0])
print("Largest element is:", l[-1])
