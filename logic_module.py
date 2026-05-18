def validate_score(score):
    """Checks if the score falls within the standard 0 to 100 range."""
    return 0 <= score <= 100

def calculate_grade(score):
    """Maps numerical scores to their corresponding alphabetic grades."""
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 45:
        return "D"
    elif score >= 40:
        return "E"
    else:
        return "F"
