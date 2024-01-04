def solution(friends, gifts):
    answer = 0
    friendList = {}
    giftsMax = 0
    for i in friends:
        give = 0
        receive = 0
        friendList[i] = {_: 0 for _ in friends}
        for j in gifts:
            to = j.split()
            if to[0] == i:
                friendList[i][to[1]] += 1
                give += 1
            else:
                receive += 1

        friendList[i]["give"] = give
        friendList[i]["receive"] = receive
        friendList[i]["prsent"] = give - receive

    for i in friends:
        perznt = 0
        gcnt = 0
        for j in friends:
            if i == j:
                continue
            else:
                if " ".join([i, j]) in gifts and " ".join([j, i]) in gifts:
                    if friendList[i][j] > friendList[j][i]:
                        perznt += 1
                    else:
                        if friendList[i]["prsent"] != friendList[j]["prsent"]:
                            if friendList[i]["prsent"] > friendList[j]["prsent"]:
                                perznt += 1

        if gcnt == len(friends) - 1:
            print("++=")
            perznt += 1
        print(perznt)
        if answer < perznt:
            answer = perznt
    return answer