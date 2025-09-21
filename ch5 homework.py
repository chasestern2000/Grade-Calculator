# Chase Stern Chapter 5 homework
# Title for program
print(f'Grade Calculator')
print()
print(f'====================')
print()

# Making a main function
def main():
    print()
    
    # Number of students
    total_students = int(input(f'Please Type the Number of Students in your class: '))
    print()
    
    # Loops for amount of students enterned
    for students in range(total_students):
        print(f'Student #{students + 1}')
        
        # Collects name of student
        name = input(f'Enter the Name of your Student: ')
        
        # Collects 4 test scores
        score1 = int(input(f'Test Score 1: '))
        score2 = int(input(f'Test Score 2: '))
        score3 = int(input(f'Test Score 3: '))
        score4 = int(input(f'Test Score 4: '))
        
        #dont use same name for variables as the function. create new variable calling the function
        total_score = score1 + score2 + score3 + score4
        score_average = average(total_score)
        letter = letter_grade(score_average)
        display_grade_info(name, score_average, letter)
    
# Collecting scores to make an average
    
def average(total_score):
    avg = total_score / 4
    return avg

# Determining your letter grade
def letter_grade(score_average):
    if score_average >= 90 and score_average <= 100:
        letter_grade = 'A'
        return letter_grade
        
    elif score_average >= 80 and score_average <= 89:
        letter_grade = 'B'
        return letter_grade

    elif score_average >= 70 and score_average <= 79:
        letter_grade = 'C'
        return letter_grade

    elif score_average >= 60 and score_average <= 69:
        letter_grade = 'D'
        return letter_grade

    elif score_average < 60:
        letter_grade = 'F'
        return letter_grade

# Displaying the information
#when printing out concatenated strings and the variable isnt a char or string, need to convert to string 
def display_grade_info(name, average, letter):
    print()
    print("Student Name: " + name)
    print("Average: " + str(average))
    print("Letter Grade: " + letter)
    print("________________________")
    print()
    return display_grade_info
    

# Calling main function
main()
