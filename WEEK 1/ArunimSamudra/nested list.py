if __name__ == '__main__':
    arr = []
    sc = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        sc.append(score)
        x = [name,score]
        arr.append(x)
    sc.sort(reverse=True)
    max = sc[len(sc)-1]
    max2 = sc[0]
    for i in range(len(sc)):
        if sc[i] < max2 and sc[i] > max:
            max2 = sc[i]
    n = []
    for i in range(len(arr)):
        if arr[i][1] == max2:
            n.append(arr[i][0])
    n.sort()
    for i in range(len(n)):
        print(n[i])

