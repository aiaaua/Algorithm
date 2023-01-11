N = int(input())
channels = [input() for _ in range(N)]
solution = str()

idx1 = channels.index("KBS1")
solution += '1' * idx1 + '4' * idx1

channels.pop(idx1)
channels.insert(0, "KBS1")

idx2 = channels.index("KBS2")
solution += '1' * idx2 + '4' * (idx2 - 1)

print(solution)
