points = []
def Olympics():
    for i in range(5):
        point = int(input("Enter the points you scored in the competition: "))
        points.append(point)
Olympics()
ranking = [0] * len(points)
for i in range(len(points)):
    rank = 1 
    for j in range(len(points)):
        if points[j] > points[i]:
            rank += 1
    ranking[i] = rank
print("Competition ranking: ", ranking)
