stu = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        stu.append([name, score])

    stu = sorted(stu, key = lambda x: x[1])
    second_lowest_score = sorted(list(set([x[1] for x in stu])))[1]
    desired_stu = []
    for stu in stu:
        if stu[1] == second_lowest_score:
            desired_stu.append(stu[0])
    print("\n".join(sorted(desired_stu)))
