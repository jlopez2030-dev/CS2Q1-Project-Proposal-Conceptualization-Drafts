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

    ValueInMeters = Value * LengthUnitsInMeter[FromUnit]
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

    ValueInLiters = Value * CapacityUnitsInLiter[FromUnit]
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


def LongFloatingPointErrorFixer(value, decimals=6):
    return float(f"{value:.{decimals}f}")


def UserMenu():
    while True:
        print("\nCreated in PyCharm.")
        print("\n==== MULTI-TOOL STUDY ASSISTANT APP ====\n  -- Tool Categories --")
        print("  1. Unit Converter\n  2. Timer\n  3. To-Do List\n  4. Simple Calculator (Only supports ASMD)\n  5. Exit")
        print("Warning! The To-Do List's contents will be removed unless the app is still running.")
        print("Choose a category (1-5): ")

        try:
            CategoryChoice = int(input())
        except:
            print("Invalid input.")
            continue

        if CategoryChoice == 1:
            print("\n==========================")
            print("  --- Unit Converter ---")
            print("  1. Length\n  2. Weight\n  3. Capacity (Ex. Liters)\n  4. Exit")
            print("Choose a category (1-4): ")

            try:
                UnitCategoryChoice = int(input())
            except:
                print("Invalid input.")
                continue

            if UnitCategoryChoice == 1:
                LengthUnits = ["mm", "cm", "in", "ft", "yd", "m", "km", "mi"]
                UnitMenu = "\n|mm,\n|cm,\n|in,\n|ft,\n|yd,\n|m,\n|km,\n|mi\n"

                print("Enter the value of your unit:")
                try:
                    Value = float(input())
                except:
                    print("Invalid input.")
                    continue

                print(f"Units:\n{UnitMenu}\nFrom unit:")
                FromUnit = input().lower()
                if FromUnit not in LengthUnits:
                    print("Unit not supported.")
                    continue

                print("To unit:")
                ToUnit = input().lower()
                if ToUnit not in LengthUnits:
                    print("Unit not supported.")
                    continue

                Result = LengthConverter(Value, FromUnit, ToUnit)
                Fixed = LongFloatingPointErrorFixer(Result, 6)
                print(f"\n{Value} {FromUnit} is {Fixed} {ToUnit}")

            elif UnitCategoryChoice == 2:
                WeightUnits = ["mg", "g", "oz", "lb", "kg", "ton"]
                UnitMenu = "\n|mg,\n|g,\n|oz,\n|lb,\n|kg,\n|ton\n"

                print("Enter the value of your unit:")
                try:
                    Value = float(input())
                except:
                    print("Invalid input.")
                    continue

                print(f"Units:\n{UnitMenu}\nFrom unit:")
                FromUnit = input().lower()
                if FromUnit not in WeightUnits:
                    print("Unit not supported.")
                    continue

                print("To unit:")
                ToUnit = input().lower()
                if ToUnit not in WeightUnits:
                    print("Unit not supported.")
                    continue

                Result = WeightConverter(Value, FromUnit, ToUnit)
                Fixed = LongFloatingPointErrorFixer(Result, 6)
                print(f"\n{Value}{FromUnit} is {Fixed}{ToUnit}")

            elif UnitCategoryChoice == 3:
                CapacityUnits = ["ml", "l", "kl", "tsp", "tbsp", "cup", "pt", "qt", "gal"]
                UnitMenu = "\n|ml,\n|l,\n|kl,\n|tsp,\n|tbsp,\n|cup,\n|pt,\n|qt,\n|gal\n"

                print("Enter the value of your unit:")
                try:
                    Value = float(input())
                except:
                    print("Invalid input.")
                    continue

                print(f"Units:\n{UnitMenu}\nFrom unit:")
                FromUnit = input().lower()
                if FromUnit not in CapacityUnits:
                    print("Unit not supported.")
                    continue

                print("To unit:")
                ToUnit = input().lower()
                if ToUnit not in CapacityUnits:
                    print("Unit not supported.")
                    continue

                Result = CapacityConverter(Value, FromUnit, ToUnit)
                Fixed = LongFloatingPointErrorFixer(Result, 6)
                print(f"\n{Value}{FromUnit} is {Fixed}{ToUnit}")

        elif CategoryChoice == 2:
            import time

            try:
                Hours = int(input("How long in hours?\n"))
                Minutes = int(input("How long in minutes?\n"))
                Seconds = int(input("How long in seconds?\n"))
            except:
                print("Invalid input.")
                continue

            TotalSeconds = Hours * 3600 + Minutes * 60 + Seconds
            print(f"Timer ends in {Hours:02d}:{Minutes:02d}:{Seconds:02d}")

            while TotalSeconds > 0:
                Hrs = TotalSeconds // 3600
                Mins = (TotalSeconds % 3600) // 60
                Secs = TotalSeconds % 60
                print(f"{Hrs:02d}:{Mins:02d}:{Secs:02d}", end='\r')
                time.sleep(1)
                TotalSeconds -= 1

            print("\nTime's up!")

        elif CategoryChoice == 3:
            ToDoList = []
            while True:
                print("\n======================")
                print("  --- To-Do List ---")
                print("  1. Add Task\n  2. View Tasks\n  3. Remove Task\n  4. Exit")
                print("Choose a category (1-4): ")

                try:
                    ToDoListCategoryChoice = int(input())
                except:
                    print("Invalid input.")
                    continue

                if ToDoListCategoryChoice == 1:
                    Task = input("Enter a new task: ")
                    ToDoList.append(Task)
                    print(f"Task '{Task}' added!")

                elif ToDoListCategoryChoice == 2:
                    if len(ToDoList) == 0:
                        print("Your To-Do List is empty.")
                    else:
                        for i, Task in enumerate(ToDoList):
                            print(f"{i + 1}. {Task}")

                elif ToDoListCategoryChoice == 3:
                    if len(ToDoList) == 0:
                        print("No tasks to remove.")
                    else:
                        for i, Task in enumerate(ToDoList):
                            print(f"{i + 1}. {Task}")
                        try:
                            Index = int(input("Enter the task number to remove: ")) - 1
                            if 0 <= Index < len(ToDoList):
                                Removed = ToDoList.pop(Index)
                                print(f"Removed task: {Removed}")
                            else:
                                print("Invalid task number!")
                        except:
                            print("Invalid input.")

                elif ToDoListCategoryChoice == 4:
                    break

        elif CategoryChoice == 4:
            while True:
                print("\n--- SIMPLE CALCULATOR ---")
                print("1. Addition")
                print("2. Subtraction")
                print("3. Multiplication")
                print("4. Division")
                print("5. Exit")

                try:
                    Operation = int(input("Choose an operation (1-5): "))
                except:
                    print("Invalid input.")
                    continue

                if Operation == 5:
                    break

                if Operation in [1, 2, 3, 4]:
                    try:
                        num1 = float(input("Enter first number: "))
                        num2 = float(input("Enter second number: "))
                    except:
                        print("Invalid input.")
                        continue

                    if Operation == 1:
                        print(f"= {add(num1, num2)}")
                    elif Operation == 2:
                        print(f"= {subtract(num1, num2)}")
                    elif Operation == 3:
                        print(f"= {multiply(num1, num2)}")
                    elif Operation == 4:
                        print(f"= {divide(num1, num2)}")

        elif CategoryChoice == 5:
            break


UserMenu()
