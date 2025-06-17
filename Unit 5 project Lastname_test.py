#Erik Rivera
#12/9/2024
#Last name_test

# Empty list
testGrades = []

# For loop to gather the 10 scores from the user
for i in range(10):
    # Prompts the user to enter a test score
    value = int(input("Please enter your test score: ")) #prompts the user for test score
   
    # While loop to keep asking user for a number between 0 and 100 if an out of range number is entered
    while value < 0 or  value > 100:
        value = int(input("Please try again. The test score must be between 0 and 100: "))
   
    # Adds score to the empty list
    testGrades.append(value)

# Sorts list from lowest to highest
testGrades.sort()

# Removes the first two scores from the list
testGrades.pop(0)
testGrades.pop(0)

# Calculates the average of the test scores
average = sum(testGrades) / len(testGrades)

# Outputs the average
print("The average test score is: " + str(average) + ".")
      