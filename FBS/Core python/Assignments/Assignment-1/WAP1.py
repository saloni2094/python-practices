##Take input 5 subject 
math = int(input('Enter math marks:'))
english = int(input('Enter english marks:'))
reasoning = int(input('Enter reasoning marks:'))
python = int(input('Enter python marks:'))
hindi = int(input('Enter hindi marks:'))

##Total marks of subject
total = math + english + reasoning + python + hindi

##find percentage of 5 subject marks
percentage = (total/500)*100

##Display result
print('total marks =', total)
print('percentage =', percentage,'%')