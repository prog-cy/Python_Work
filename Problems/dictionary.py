n = int(input())
student_marks = {}
sum = 0
for i in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

for key in student_marks:
    if key == query_name:
        for i in range(len(student_marks[key])):
            sum += student_marks[key][i]
        avg = sum / len(student_marks[key])
print("%0.2f"%avg)