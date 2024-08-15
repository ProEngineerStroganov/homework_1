def solution(request):
    answer = []
    for i in range(1, request):
        for j in range(i + 1, request):
            if request % (i + j) == 0:
                answer.append(str(i))
                answer.append(str(j))
    print(''.join(answer))


for i in range(3, 21):
    solution(i)
