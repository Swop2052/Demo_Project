def compare_quotes(quotes, user_profile):
    scores = {}

    for q in quotes:
        score = 0

        if user_profile["family_size"] >= 4:
            score += q["sum_insured"] / 100000

        score += max(0, (20000 - q["deductible"]) / 1000)
        score += max(0, (30000 - q["annual_premium"]) / 1000)

        scores[q["quote_id"]] = round(score, 2)

    best_quote = max(scores, key=scores.get)

    return {
        "best_quote": best_quote,
        "scores": scores
    }
