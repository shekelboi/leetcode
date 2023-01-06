def numTeams(rating):
    solutions = []
    for i in range(len(rating)):
        for j in range(i, len(rating)):
            for k in range(j, len(rating)):
                if rating[i] > rating[j] > rating[k] or rating[i] < rating[j] < rating[k]:
                    solutions.append([rating[i], rating[j], rating[k]])
    return len(solutions)


rating = [1, 2, 3, 4]
print(numTeams(rating))
