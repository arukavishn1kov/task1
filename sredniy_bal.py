grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3],[5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

a= grades[0]
b= grades[1]
c= grades[2]
d= grades[3]
e= grades[4]

a1= (sum(a)/len(a))
b1= (sum(b)/len(b))
c1= (sum(c)/len(c))
d1= (sum(d)/len(d))
e1= (sum(e)/len(e))

sort_= list(students)
sort_.sort()
a2=sort_[0]
b2=sort_[1]
c2=sort_[2]
d2=sort_[3]
e2=sort_[4]

sb= {str(a2):a1, str(b2):b1, str(c2):c1, str(d2):d1, str(e2):e1}
print(sb)

grades= input('оценки студентов, пиши в []: ')
students= input("имена студентов, пиши в '': ")