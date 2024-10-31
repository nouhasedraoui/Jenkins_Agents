from Calculator import Calculator

def main():
    calculator = Calculator()
    # Predefined options for testing
    operations = [1, 2, 3, 4]  # Add, Subtract, Multiply, Divide
    results = []
    
    for choice in operations:
        if choice == 1:
            result = calculator.add(5, 3)  # Example addition
            results.append(f"Add: 5 + 3 = {result}")
        elif choice == 2:
            result = calculator.subtract(5, 3)  # Example subtraction
            results.append(f"Subtract: 5 - 3 = {result}")
        elif choice == 3:
            result = calculator.multiply(5, 3)  # Example multiplication
            results.append(f"Multiply: 5 * 3 = {result}")
        elif choice == 4:
            result = calculator.divide(5, 3)  # Example division
            results.append(f"Divide: 5 / 3 = {result}")
    
    # Print all results
    for output in results:
        print(output)

if __name__ == "__main__":
    main()
