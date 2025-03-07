"""temperatures = ["Label", 32, 50, 77, 104]

def f2c(temperatures):
    answer = []

    for num in temperatures[1:]:
        celsius = (5 / 9) * (num - 32)
        answer.append(celsius)

    return answer

result = f2c(temperatures)
print(result)"""

temperatures = ["Label", 32, 50, 77, 104]

answer = list(map(lambda x: (5 / 9) * (x - 32), temperatures[1:]))

print(answer)




