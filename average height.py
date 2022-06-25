student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

                  ######## Using "sum" and "len" #########
# total_height = sum(student_heights)
# number_of_students = len(student_heights)
# avarage_height = round(total_height / number_of_students)
# print(avarage_height)

  
                  ######## Using a for loop #########
number_of_students = 0
total_height = 0
  
print(student_heights)
for height in student_heights:
  total_height += height
  number_of_students += 1

avarage_height = total_height / number_of_students

print(int(avarage_height))



