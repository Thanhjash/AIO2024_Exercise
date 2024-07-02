def get_valid_input(prompt):
    """Gets a valid integer input greater than zero from the user."""
    while True:
        value = input(prompt)
        if not value.isdigit():
            print(f"{prompt.split('(')[0]} must be an integer")
            continue

        value = int(value)
        if value <= 0:
            print(f"{prompt.split('(')[0]} must be greater than zero")
            continue
        
        return value

def get_input():
    """Gets input from the user for True Positives (tp), False Positives (fp), and False Negatives (fn), ensuring they are integers."""
    print("Start input:")
    tp = get_valid_input("Enter True Positives (tp): ")
    fp = get_valid_input("Enter False Positives (fp): ")
    fn = get_valid_input("Enter False Negatives (fn): ")
    
    return tp, fp, fn

def calculate_metrics(tp, fp, fn):
    """Calculates precision, recall, and F1-score."""
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * (precision * recall) / (precision + recall)
    print(f"Precision is {precision:.4f}")
    print(f"Recall is {recall:.4f}")
    print(f"F1-score is {f1_score:.4f}")

# Main program loop
while True:
    tp, fp, fn = get_input()  # Get valid integer inputs
    calculate_metrics(tp, fp, fn)  # Calculate and print metrics

    continue_input = input("Do you want to continue? (y/n): ")
    if continue_input.lower() != 'y':
        break  # Exit the loop if the user doesn't want to continue
