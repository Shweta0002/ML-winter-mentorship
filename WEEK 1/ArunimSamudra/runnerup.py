input()
a = [int(k) for k in input().split(' ')]
a.sort()
a.reverse()
for i in range(len(a)):
    if a[i] != a[0]:
        print(a[i])
        break
      
