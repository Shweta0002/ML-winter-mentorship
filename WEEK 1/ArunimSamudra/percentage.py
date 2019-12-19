if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    sum = 0.00
    avg = 0.00
    for i in range(3):
        sum = sum +  student_marks[query_name][i]
    avg = sum/3
    print('%.2f'%avg)
