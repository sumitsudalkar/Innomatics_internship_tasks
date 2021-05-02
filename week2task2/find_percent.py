import statistics as stat
if __name__ == '__main__':
    n = int(input())
    stu_marks = {}
    for _ in range(n):
        name, *line = input().split()
        myscores = list(map(float, line))
        stu_marks[name] = myscores
        
    query_name = input()
    avg = stat.mean(stu_marks[query_name])
    print(format(avg, '.2f'))
