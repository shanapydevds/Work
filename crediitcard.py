def check_credit_card(card_number):
    # Step 1: Ensure the input contains only digits
    if not card_number.isdigit():
        return "Invalid: Card number must contain only digits."

    # Step 2: Check length
    if len(card_number) < 13 or len(card_number) > 19:
        return "Invalid: Card number length must be between 13 and 19 digits."

    # Step 3: Perform Luhn check
    if not luhn_check(card_number):
        return "Invalid: Failed Luhn check."

    # Step 4: Identify card type
    card_type = identify_card_type(card_number)
    return f"Valid: Card is a {card_type}."


def luhn_check(card_number):
    """Validate credit card number using the Luhn algorithm."""
    total = 0
    reverse_digits = card_number[::-1]  # Reverse the card number
    for i, digit in enumerate(reverse_digits):
        n = int(digit)
        # Double every second digit from the right
        if i % 2 == 1:
            n *= 2
            if n > 9:  # If the result is greater than 9, subtract 9
                n -= 9
        total += n
    return total % 10 == 0  # Valid if total is a multiple of 10


def identify_card_type(card_number):
    """Identify the card type based on the starting digits and length."""
    if card_number.startswith("4"):
        return "Visa"
    elif card_number.startswith(("51", "52", "53", "54", "55")):
        return "MasterCard"
    elif card_number.startswith("34") or card_number.startswith("37"):
        return "American Express"
    elif card_number.startswith("6011") or card_number.startswith("65"):
        return "Discover"
    else:
        return "Unknown Card Type"


# Example Usage
card = "6011111111111117"  # Example Visa card
result = check_credit_card(card)
print(result)
