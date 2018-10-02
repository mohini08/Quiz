# QUIZ

It is a program for creating 35 question papers with 50 questions.Each paper has shuffled questions such that no two paper have same sequencing of questions and their options.

## Requirements

You need to have the following system packages installed:

Python >= 3.4.3

### Working:

* Create a dictionary of states and their capitals.
* Store the dictionary into a json file.
* Now import the json into your main program and load it.
* Run a outer loop till range 35.
* store the states that is keys of dictionary ito other list and shuffle it.
* Create headings for the question paper.
* Now run a inner loop till range 50 as you want to create 50 questions for each paper.
* Fetch the correct answer for the 1st state.
* Create a list of wrong answers which includes all the capitals apart from the correctone.
* Now select any three options from the wrong list.
* Create the options including 3 wrong and 1 right answer.
* Now finally create the question and give options.
* simultaneously save correct answer option into an answer sheet.
* At last 35 question papers with 50 shuffled questions will be created with separate answer sheets.


### Test run

Run following command for executing the project:

$ python Quiz.py

