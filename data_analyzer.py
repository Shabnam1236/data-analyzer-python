# Data Analyzer and Transformer Program
# prsented by Shabnam Panara

def display_menu():
    print("\nWelcome to the Data Analyzer and Transformer Program")
    print("Main Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program")

# Step 1: Input Data
def input_data():
    global data
    user_input = input("Enter data for a 1D array (separated by spaces): ")
    data = list(map(int, user_input.split()))
    print("Data has been stored successfully!")

# Step 2: Display Data Summary
def display_summary():
    if not data:
        print("No data available!")
        return
    print("\nData Summary:")
    print(f"Total elements: {len(data)}")
    print(f"Minimum value: {min(data)}")
    print(f"Maximum value: {max(data)}")
    print(f"Sum of all values: {sum(data)}")
    avg=sum(data)/len(data)
    print(f"Average value:{avg:.2f}")
 
# Step 3: Factorial using Recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def calculate_factorial():
    num = int(input("Enter a number to calculate its factorial: "))
    print(f"Factorial of {num} is: {factorial(num)}")

# Step 4: Filter Data using Lambda
def filter_data():
    if not data:
        print("No data available!")
        return
    threshold = int(input("Enter a threshold value to filter out data above this value: "))
    filtered = list(filter(lambda x: x >= threshold, data))
    print(f"Filtered Data (values >= {threshold}):")
    print(", ".join(map(str, filtered)))

# Step 5: Sort Data
def sort_data():
    if not data:
        print("No data available!")
        return
    print("Choose sorting option:")
    print("1. Ascending")
    print("2. Descending")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        sorted_data = sorted(data)
        print("Sorted Data in Ascending Order:")
    elif choice == 2:
        sorted_data = sorted(data, reverse=True)
        print("Sorted Data in Descending Order:")
    else:
        print("Invalid choice!")
        return
    print(", ".join(map(str, sorted_data)))

# Step 6: Dataset Statistics (Return Multiple Values)
def dataset_statistics():
    if not data:
        print("No data available!")
        return
    min_val = min(data)
    max_val = max(data)
    total = sum(data)
    avg = total / len(data)
    return min_val, max_val, total, avg

def display_statistics():
    stats = dataset_statistics()
    if stats:
        min_val, max_val, total, avg = stats
        print("\nDataset Statistics:")
        print(f"- Minimum value: {min_val}")
        print(f"- Maximum value: {max_val}")
        print(f"- Sum of all values: {total}")
        print(f"- Average value: {avg:.2f}")

# Main Program
data = []

while True:
    display_menu()
    choice = int(input("Please enter your choice: "))

    if choice == 1:
        input_data()
    elif choice == 2:
        display_summary()
    elif choice == 3:
        calculate_factorial()
    elif choice == 4:
        filter_data()
    elif choice == 5:
        sort_data()
    elif choice == 6:
        display_statistics()
    elif choice == 7:
        print("Thank you for using the Data Analyzer and Transformer Program. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
