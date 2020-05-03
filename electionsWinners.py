def electionsWinners(votes, k):
    count = 0
    max_vote = max(votes)
    if votes.count(max_vote) >= 2 and k == 0:
        return 0

    for i in votes:
        if i + k >= max_vote:
            count += 1
            
    if count == 0 and k == 0:
        return 1
    return count

votes = [5, 3, 3, 1, 1]
k = 0
print(electionsWinners(votes, k))