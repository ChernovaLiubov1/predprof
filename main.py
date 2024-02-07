class stud:
    id=0
    fio=''
    id_project = ''
    clas = ''
    score = 0
students=[]
f=open('students.csv')
j=0
for i in f:
    s=i.split(',')
    if int(s[3][:-1]) ==10:
        students.append(stud())
        students[j].fio = s[1]
        students[j].id = int(s[0])
        students[j].score = int(s[4])
        j+=1
for i in range(len(students)):
    j=i
    t=students[i]
    st=students[i].score
    while j>0 and students[j-1].score>st:
        students[j]=students[j-1]
        j-=1
    students[j]=t
for k in range(len(students)):
    l=k
    m=students[k]
    sm=students[k].id
    while l>0 and students[l-1].score>sm:
        students[l]=students[l-1]
        l-=1
    students[l]=m

print(students[-1].fio, students[-1].id, students[-1].score)
print(students[-2].fio, students[-2].id, students[-2].score)
print(students[-3].fio, students[-3].id, students[-3].score)