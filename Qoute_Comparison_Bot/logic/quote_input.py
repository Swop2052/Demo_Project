def get_quotes_from_user():
    quotes = []
    print("\nEnter details for 3 insurance quotes:\n")

    for i in range(1, 4):
        print(f"--- Quote {i} ---")
        quote = {
            "quote_id": f"Q{i}",
            "annual_premium": int(input("Annual Premium (INR): ")),
            "sum_insured": int(input("Sum Insured (INR): ")),
            "deductible": int(input("Deductible (INR): "))
        }
        quotes.append(quote)
        print()

    return quotes


def get_user_profile():
    return {
        "family_size": int(input("Enter family size: "))
    }
