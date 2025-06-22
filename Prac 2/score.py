"""
CP1404/CP5632 - Practical to determine score status
"""

def main():
    """Determine and display the status of a score."""
    score = get_valid_score()
    result = determine_score_status(score)
    print(result)

def get_valid_score():
    """Prompt for and return a valid score."""
    valid = False
    score = None
    while not valid:
        try:
            score = float(input("Enter score: "))
            if 0 <= score <= 100:
                valid = True
            else:
                print("Invalid score (must be 0-100)")
        except ValueError:
            print("Invalid input. Please enter a number.")
    return score

def determine_score_status(score):
    """Return the status (Excellent, Pass, Bad, etc.) based on a score."""
    if score > 90:
        return "Excellent"
    elif score > 50:
        return "Pass"
    else:
        return "Bad"

if __name__ == "__main__":
    main()
