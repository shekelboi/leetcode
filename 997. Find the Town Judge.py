def findJudge(n, trust):
    all_people = {i + 1 for i in range(n)}
    trust_dict = {k: set() for k in all_people}
    for t in trust:
        trust_dict[t[1]].add(t[0])

    print(trust_dict)

    for k, v in trust_dict.items():
        if v == (all_people - {k}):
            if not any(trust_dict[key] for key in trust_dict.keys() if key != k and k in trust_dict[key]):
                return k
    return -1


n = 2
trust = [[1, 2]]
print(findJudge(n, trust))
