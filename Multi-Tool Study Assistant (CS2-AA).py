# ======================================
#   Unit Converters
# ======================================

def LengthConverter(Value, FromUnit, ToUnit):
    LengthUnitsInMeter = {
        "m": 1,
        "cm": 0.01,
        "mm": 0.001,
        "km": 1000,
        "in": 0.0254,
        "ft": 0.3048,
        "yd": 0.9144,
        "mi": 1609.34
    }

    # Converts the original unit to meters
    ValueInMeters = Value * LengthUnitsInMeter[FromUnit]

    # Converts the converted unit into meters to the desired unit
    ConvertedUnit = ValueInMeters / LengthUnitsInMeter[ToUnit]

    return ConvertedUnit


def WeightConverter(Value, FromUnit, ToUnit):
    WeightUnitsInKilogram = {
        "kg": 1,
        "g": 0.001,
        "mg": 0.000001,
        "lb": 0.453592,
        "oz": 0.0283495,
        "ton": 1000
    }

    # Convert the original unit to kilograms
    ValueInKilograms = Value * WeightUnitsInKilogram[FromUnit]

    # Convert from kilograms to the desired unit
    ConvertedUnit = ValueInKilograms / WeightUnitsInKilogram[ToUnit]

    return ConvertedUnit


def WeightConverter(Value, FromUnit, ToUnit):
    WeightUnitsInKilogram = {
        "kg": 1,
        "g": 0.001,
        "mg": 0.000001,
        "lb": 0.453592,
        "oz": 0.0283495,
        "ton": 1000
    }

    ValueInKilograms = Value * WeightUnitsInKilogram[FromUnit]
    ConvertedUnit = ValueInKilograms / WeightUnitsInKilogram[ToUnit]

    return ConvertedUnit


def CapacityConverter(Value, FromUnit, ToUnit):
    CapacityUnitsInLiter = {
        "ml": 0.001,
        "l": 1,
        "kl": 1000,
        "tsp": 0.00492892,
        "tbsp": 0.0147868,
        "cup": 0.24,
        "pt": 0.473176,
        "qt": 0.946353,
        "gal": 3.78541
    }

    # Convert original unit to liters
    ValueInLiters = Value * CapacityUnitsInLiter[FromUnit]

    # Convert from liters to desired unit
    ConvertedUnit = ValueInLiters / CapacityUnitsInLiter[ToUnit]

    return ConvertedUnit


# ======================================
#   Operations
# ======================================

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "You cannot divide by zero!"
    return a / b

# ======================================
#   Python Error Fixers
# ======================================
def LongFloatingPointErrorFixer(value, decimals=6):
    return float(f"{value:.{decimals}f}")

def UserMenu():
# =======================
#   Main Menu
# =======================

    while True:

        print("\nCreated in PyCharm.")
        print("\n==== MULTI-TOOL STUDY ASSISTANT APP ====\n  -- Tool Categories --")
        print("  1. Unit Converter\n  2. Timer\n  3. To-Do List\n  4. Simple Calculator (Only supports ASMD)\n  5. Exit")
        print("Warning! The To-Do List's contents will be removed unless the app is still running.")
        print("Choose a category (1-4): ")
        CategoryChoice = int(input())

# =======================
#   Unit Converter Menu
# =======================

        if CategoryChoice == 1:
            print("\n==========================")  # Divider
            print("  --- Unit Converter ---")
            print("  1. Length\n  2. Weight\n  3. Capacity (Ex. Liters)\n  4. Exit")
            print("Choose a category (1-3): ")
            UnitCategoryChoice = int(input())

            if UnitCategoryChoice == 1:

                # List for the repeat codes if input is not supported or not a unit
                LengthUnits = ["mm", "cm", "in", "ft", "yd", "m", "km", "mi"]
                UnitMenu = "\n|mm (millimeter),\n|cm (centimeter),\n|in (inch),\n|ft (foot),\n|yd (yard),\n|m (meter),\n|km (kilometer),\n|mi (mile)\n"

                # Asks for the value of the unit
                print("Enter the value of your unit:")
                Value = int(input())

                # Corrects the value if value is less than or equal to 0
                if Value <= 0:
                    print("I'm sorry, but the value cannot be 0 or less than 0\n")
                    print("Enter the value of your unit:")
                    Value = int(input())

                # Asks what the unit is
                print(f"Units:\n{UnitMenu}\nFrom unit:")
                FromUnit = input().lower()

                # Repeats the code if the unit is not in the list
                if FromUnit not in LengthUnits:
                    print("\nUnit is not supported, please wait in the future for more updates\n")
                    print(f"Units:\n{UnitMenu}\nFrom unit:")
                    FromUnit = input().lower()

                # Asks what unit to convert into
                print("To unit:")
                ToUnit = input().lower()

                # Same as the code repeater above but replaced with a local variable
                if ToUnit not in LengthUnits:
                    print("\nUnit is not supported, please wait in the future for more updates\n")
                    print("To unit:")
                    ToUnit = input().lower()

                Result = LengthConverter(Value, FromUnit, ToUnit)
                Fixed = LongFloatingPointErrorFixer(Result, 6)

                print(f"\n{Value} {FromUnit} is {Fixed} {ToUnit}")

                # Asks if the user want to use the App again
                print("Do you want to use the app again?\n 1. Yes\n 2. No")
                Reuse = int(input())

                if Reuse == 2:
                    break
                elif Reuse not in [1, 2]:
                    print("Answer is not in the choices")
                else:
                    UserMenu()

            elif UnitCategoryChoice == 2:

                WeightUnits = ["mg", "g", "oz", "lb", "kg", "ton"]
                UnitMenu = "\n|mg (milligram),\n|g (gram),\n|oz (ounce),\n|lb (pound),\n|kg (kilogram),\n|ton (metric ton)\n"

                # Asks for the value of the unit
                print("Enter the value of your unit:")
                Value = float(input())

                # Corrects the value if value is less than or equal to 0
                if Value <= 0:
                    print("I'm sorry, but the value cannot be 0 or less than 0\n")
                    print("Enter the value of your unit:")
                    Value = float(input())

                # Asks what the unit is
                print(f"Units:\n{UnitMenu}\nFrom unit:")
                FromUnit = input().lower()

                # Repeats the code if the unit is not in the list
                if FromUnit not in WeightUnits:
                    print("\nUnit is not supported, please wait in the future for more updates\n")
                    print(f"Units:\n{UnitMenu}\nFrom unit:")
                    FromUnit = input().lower()

                # Asks what unit to convert into
                print("To unit:")
                ToUnit = input().lower()

                # Same as the code repeater above but replaced with a local variable
                if ToUnit not in WeightUnits:
                    print("\nUnit is not supported, please wait in the future for more updates\n")
                    print("To unit:")
                    ToUnit = input().lower()

                # Uses your WeightConverter function
                Result = WeightConverter(Value, FromUnit, ToUnit)
                Fixed = LongFloatingPointErrorFixer(Result, 6)

                print(f"\n{Value}{FromUnit} is {Fixed}{ToUnit}")

                # Asks if the user want to use the App again
                print("Do you want to use the app again?\n 1. Yes\n 2. No")
                Reuse = int(input())

                if Reuse == 2:
                    break
                elif Reuse not in [1, 2]:
                    print("Answer is not in the choices")
                else:
                    UserMenu()

            elif UnitCategoryChoice == 3:

                CapacityUnits = ["ml", "l", "kl", "tsp", "tbsp", "cup", "pt", "qt", "gal"]

                UnitMenu = "\n|ml (milliliter),\n|l (liter),\n|kl (kiloliter),\n|tsp (teaspoon),\n|tbsp (tablespoon),\n|cup (cup),\n|pt (pint),\n|qt (quart),\n|gal (gallon)\n"

                # Asks for the value of the unit
                print("Enter the value of your unit:")
                Value = float(input())

                # Corrects the value if value is less than or equal to 0
                if Value <= 0:
                    print("I'm sorry, but the value cannot be 0 or less than 0\n")
                    print("Enter the value of your unit:")
                    Value = float(input())

                # Asks what the unit is
                print(f"Units:\n{UnitMenu}\nFrom unit:")
                FromUnit = input().lower()

                # Repeats the code if the unit is not in the list
                if FromUnit not in CapacityUnits:
                    print("\nUnit is not supported, please wait in the future for more updates\n")
                    print(f"Units:\n{UnitMenu}\nFrom unit:")
                    FromUnit = input().lower()

                # Asks what unit to convert into
                print("To unit:")
                ToUnit = input().lower()

                # Same as the code repeater above but replaced with a local variable
                if ToUnit not in CapacityUnits:
                    print("\nUnit is not supported, please wait in the future for more updates\n")
                    print("To unit:")
                    ToUnit = input().lower()

                # Uses your CapacityConverter function
                Result = CapacityConverter(Value, FromUnit, ToUnit)
                Fixed = LongFloatingPointErrorFixer(Result, 6)

                print(f"\n{Value}{FromUnit} is {Fixed}{ToUnit}")

                # Asks if the user want to use the App again
                print("Do you want to use the app again?\n 1. Yes\n 2. No")
                Reuse = int(input())

                if Reuse == 2:
                    break
                elif Reuse not in [1, 2]:
                    print("Answer is not in the choices")
                else:
                    UserMenu()


            else:
                UserMenu()
# =======================
#   Timer
# =======================

        elif CategoryChoice == 2:
            print("""\n --- Timer ---""")
            import time

            print("How long in hours?")
            Hours = int(input())
            print("\nHow long in minutes?")
            Minutes = int(input())
            print("\nHow long in seconds?")
            Seconds = int(input())

            # Combines them into seconds
            TotalSeconds = Hours * 3600 + Minutes * 60 + Seconds

            print(f"Timer ends in {Hours:02d}:{Minutes:02d}:{Seconds:02d} (HH:MM:SS)")

            while TotalSeconds > 0:
                # Calculates hours, minutes, and seconds from total_seconds

                Hrs = TotalSeconds // 3600
                Mins = (TotalSeconds % 3600) // 60
                Secs = TotalSeconds % 60

                print(f"{Hrs:02d}:{Mins:02d}:{Secs:02d}\n", end='\r')
                time.sleep(1)
                TotalSeconds -= 1

            print("\nTime's up!")

            # Same as the one used above
            print("Do you want to use the app again?\n 1. Yes\n 2. No")
            Reuse = int(input())

            if Reuse == 2:
                break
            elif Reuse not in [1, 2]:
                print("Answer is not in the choices")
            else:
                UserMenu()
# ======================================
#   To-Do List Menu
# ======================================

        elif CategoryChoice == 3:
            ToDoList = []
            while True:
                print("\n======================")  # Divider
                print("  --- To-Do List ---")
                print("  1. Add Task\n  2. View Tasks\n  3. Remove Task\n  4. Exit")
                print("Choose a category (1-4): ")
                ToDoListCategoryChoice = int(input())

                if ToDoListCategoryChoice == 1:
                    print("\n=================")
                    Task = input("Enter a new task: ")
                    ToDoList.append(Task)
                    print(f"Task '{Task}' added!")

                elif ToDoListCategoryChoice == 2:
                    if len(ToDoList) == 0:
                        print("Your To-Do List is empty.")
                    else:
                        print("\n======================")
                        print("  --- YOUR TASKS ---")
                        for i, Task in enumerate(ToDoList):
                            print(f"  {i + 1}. {Task}")

                elif ToDoListCategoryChoice == 3:
                    if len(ToDoList) == 0:
                        print("\nNo tasks to remove.")
                    else:
                        print("\n=======================")
                        print("\n=== REMOVE TASK ===")
                        for i, Task in enumerate(ToDoList):
                            print(f"{i + 1}. {Task}")

                            Index = int(
                                input("\n===============================\nEnter the task number to remove: ")) - 1

                            if 0 <= Index < len(ToDoList):
                                Removed = ToDoList.pop(Index)
                                print(f"Removed task: {Removed}")
                            else:
                                print("Invalid task number!")

                elif ToDoListCategoryChoice == 4:
                    print("Goodbye!")
                    UserMenu()

                else:
                    print("Invalid option. Please try again.")

# ======================================
#   Simple Calculator (Currently supports ASMD)
# ======================================

        elif CategoryChoice == 4:
            while True:
                print("\n============================")
                print("\n--- SIMPLE CALCULATOR ---")
                print("1. Addition")
                print("2. Subtraction")
                print("3. Multiplication")
                print("4. Division")
                print("5. Exit")
                print("Choose an operation (1-4):")
                Operation = int(input())

                if Operation in [1, 2, 3, 4]:
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))
                    if Operation == 1:
                        print(f"= {add(num1, num2)}")
                    elif Operation == 2:
                        print(f"= {subtract(num1, num2)}")
                    elif Operation == 3:
                        print(f"= {multiply(num1, num2)}")
                    elif Operation == 4:
                        print(f"= {divide(num1, num2)}")
                    else:
                        print("Operation not supported. Please try again and wait for the next update.")


        else:
            break

UserMenu()
