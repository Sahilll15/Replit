# take input from user
marks = []
for i in range(5):
    marks.append(int(input("Enter marks for subject {}: ".format(i+1))))

# calculate total marks and percentage
total_marks = sum(marks)
percentage = (total_marks/500)*100

# check if student passed or failed
if percentage >= 60:
    print("Congratulations! You have passed with First division.")
elif percentage >= 50:
    print("Congratulations! You have passed with Second division.")
elif percentage >= 40:
    print("Congratulations! You have passed with Third division.")
else:
    print("Sorry, You have failed the exam.")

# display total marks and percentage
print("Total marks:", total_marks)
print("Percentage:", percentage)
