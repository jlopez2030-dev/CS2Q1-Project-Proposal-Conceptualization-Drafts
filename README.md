# Project Title: Multi-tool Study Assistant App
A multi-tool study app designed to help or assist scholars as effeciently as possible.

## Project Description
  The Multi-Tool Study Assistant App is a command-line Python application designed to help students with everyday academic tasks.
  It integrates four major tools into one system:
 - Unit Converter
 - Timer
 - To-Do List
 - Simple Calculator

## Features

1. Unit Converter
Supports three categories(Units of Measurement):
-Length Converter
-Units supported:
-mm (millimeter)
-cm (centimeter)
-in (inch)
-ft (foot)
-yd (yard)
-m (meter)
-km (kilometer)
-mi (mile)
-Weight Converter
-Units supported:
-mg (milligram)
-g (gram)
-oz (ounce)
-lb (pound)
-kg (kilogram)
-ton (metric ton)
-Capacity Converter
-Units supported:
-ml (milliliter)
-l (liter)
-kl (kiloliter)
-tsp (teaspoon)
-tbsp (tablespoon)
-cup
-pt (pint)
-qt (quart)
-gal (gallon)

2. Timer
-Accepts hours, minutes, and seconds
-Converts time into total seconds
-Displays real-time countdown (HH:MM:SS format)
-Notifies when time is up
-Converts units into desired units

3.To-Do List
-Add tasks
-View tasks
-Remove tasks
-Dynamic indexing using enumerate()
-⚠ Note: Tasks are session-based and will reset when the program closes.

4.Simple Calculator
-Supports:
-Addition
-Subtraction
-Multiplication
-Division
-Includes protection against division by zero.

## Project Structure
  Multi-Tool Study Assistant App/
    CHANGELOG.md
    Multi-Tool Study Assistant (CS2-AA).py
    README.md

## Technologies Used
- Python
- PyCharm
- Github

## How to Run the Program

1. Make sure you have Python installed.
2. Download the file `Multi-Tool Study Assistant App.py`.
3. Open the Python (IDLE) you installed.
4. Click 'File' on the upper left corner of the Python (IDLE). Then click 'open' and select the `Multi-Tool Study Assistant App.py` file
6. Run the program by pressing F5 or clicking 'Run' 
7. Follow the instructions seen after running the Multi-tool Study Assistant App.

## Example Output
Created in PyCharm.

==== MULTI-TOOL STUDY ASSISTANT APP ====
  -- Tool Categories --
  1. Unit Converter
  2. Timer
  3. To-Do List
  4. Simple Calculator (Only supports ASMD)
  5. Exit
Warning! The To-Do List's contents will be removed unless the app is still running.
Choose a category (1-4): 
1

==========================
  --- Unit Converter ---
  1. Length
  2. Weight
  3. Capacity (Ex. Liters)
  4. Exit
Choose a category (1-3): 
1
Enter the value of your unit:
2
Units:

|mm,
|cm,
|in,
|ft,
|yd,
|m,
|km,
|mi

From unit:
cm
To unit:
in

2.0 cm is 0.787402 in

Created in PyCharm.

==== MULTI-TOOL STUDY ASSISTANT APP ====
  -- Tool Categories --
  1. Unit Converter
  2. Timer
  3. To-Do List
  4. Simple Calculator (Only supports ASMD)
  5. Exit
Warning! The To-Do List's contents will be removed unless the app is still running.
Choose a category (1-4): 
2
How long in hours?
0
How long in minutes?
0
How long in seconds?
10
Timer ends in 00:00:10

Time's up!

Created in PyCharm.

==== MULTI-TOOL STUDY ASSISTANT APP ====
  -- Tool Categories --
  1. Unit Converter
  2. Timer
  3. To-Do List
  4. Simple Calculator (Only supports ASMD)
  5. Exit
Warning! The To-Do List's contents will be removed unless the app is still running.
Choose a category (1-4): 
3

======================
  --- To-Do List ---
  1. Add Task
  2. View Tasks
  3. Remove Task
  4. Exit
Choose a category (1-4): 
1
Enter a new task: Math HW
Task 'Math HW' added!

======================
  --- To-Do List ---
  1. Add Task
  2. View Tasks
  3. Remove Task
  4. Exit
Choose a category (1-4): 
2
1. Math HW

======================
  --- To-Do List ---
  1. Add Task
  2. View Tasks
  3. Remove Task
  4. Exit
Choose a category (1-4): 
3
1. Math HW
Enter the task number to remove: 1
Removed task: Math HW

======================
  --- To-Do List ---
  1. Add Task
  2. View Tasks
  3. Remove Task
  4. Exit
Choose a category (1-4): 
4

Created in PyCharm.

==== MULTI-TOOL STUDY ASSISTANT APP ====
  -- Tool Categories --
  1. Unit Converter
  2. Timer
  3. To-Do List
  4. Simple Calculator (Only supports ASMD)
  5. Exit
Warning! The To-Do List's contents will be removed unless the app is still running.
Choose a category (1-4): 
4

--- SIMPLE CALCULATOR ---
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
Choose an operation (1-5): 1
Enter first number: 1
Enter second number: 1
= 2.0

--- SIMPLE CALCULATOR ---
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
Choose an operation (1-5): 2
Enter first number: 1
Enter second number: 1
= 0.0

--- SIMPLE CALCULATOR ---
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
Choose an operation (1-5): 3
Enter first number: 2
Enter second number: 2
= 4.0

--- SIMPLE CALCULATOR ---
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
Choose an operation (1-5): 4
Enter first number: 2
Enter second number: 2
= 1.0

## References


## Contributors
- Student 1: Isabeau Mithi Salibad (Debugger and Tester)
- Student 2: Mary Hera Carmona (Readme and Changelogs Manager)
- Student 3: Jake Lopez (Python Maker and Updater)
