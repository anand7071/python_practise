n = int(input("enter n"))
student_marks = {}
l=0
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
print(student_marks)
query_name = input()
m=student_marks.get(query_name)
for i in range(len(m)):
    l =l + m[i]
n=n/3    
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
m=student_marks.get(query_name)
for i in range(len(m)):
    l =l + m[i]
l=l/3    
print("%.2f" % l)

