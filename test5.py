a=range(10)
print(a)

add=0
for j in range(1,11):
    add+j
    print(j,add)

print(add)

for j in range(2,10):
    for k in range(2,10):
        print(j,'*',k,'=',j*k)
        #print(j*k,end=", ")
    print()

#for문 연습문제
A=[70,60,55,75,95,90,80,80,85,100]
total=0
for score in A:
    total+=score
average=total/len(A)
print(average)

#diamond 그리기
diamond=5
a=0
for j in range(diamond):
    space=abs(j-(diamond//2))
    star=diamond-2*space
    print(' '*space,'*'*star)
