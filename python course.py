#assignment
"""x=3
y=5
x+=y
print(x)
x=10
y=6
x-=y
print("x") """
"""a=int(input("enter the number:"))
a=int(a)
if(a%2)==0:
  print("it is an even number")
else:
  print("it is an odd number")"""
"""length=int(input("enter length of the rectangle:"))
wide=int(input("enter the wide of the rectangle"))
area=length*wide
print("the area of the rectangle is:",area)"""
"""score=int(input("enter score:"))
presence_percentage=int(input("enter presence_percentage:"))
if(score>=33 and presence_percentage>=75):
    print("passed!")
else:
    print("failed!")"""
#4.3.1
"""a=int(input("enter the number:"))
a=int(a)
if(a%2)==0:
  print("it is an even number")
else:
  print("it is an odd number")"""
student_name=[]
marks=[]
has_passed=[]

#adding student names and marks
for _ in range(2):#assuming 2 students for demonsdtraction
    name=input("enter students name:")
    student_names.append(name)
    mark=int(input("enter students mark: "))
    marks.append(mark)
    has_passed.append(mark>=40)#cheaking if the student has passed

    #creating results list
    resuls=[]
    for i in range(len(student_names)):
        results.append(mark>=40)#cheaking if the students has passed
    #creating results list
    results=[]
    for i in range(len(student_names)):
        results.append([student_names[i],marks[i],has_passed[i]]) 

        print("results:",results)