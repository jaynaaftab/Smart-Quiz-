# Smart-Quiz
The purpose of this project is to provide a quiz on concepts concerning Technology, such as IOT (Internet of Things), managing data,
environmental considerations in technology, etc. 

It uses try/except, while and for loops, input statements, and various other built-in functions in Python.

This project begins by using a for loop to go through every question present in a list 'questions' (see code.). For every question,
an input statement would be prompted to ask the user that question. It then takes in the input the user gives and ensures that the 
data given is valid (corresponding to what the program needs). Through try/except and while loops, it will continually force the user 
to reenter their data if it is not of a valid answer. These are called through functions used in the code. 

It then uses another function, 'answer_check' to test if the answer given by the user (validated) is correct in terms of answer. If it is, the program will append a 1 to a list of all the questions the user has gotten correct, 'user_correct". Otherwise, it will not do this. 

Once all of the questions have been answered by the user, the quiz finishes with a total score, and it recieves this score by taking the user_correct list, which is now full with a series of 1's, and finds the sum of this list and assigns it to the variable 'score'. 
