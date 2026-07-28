def calculate_love_score(name1, name2):
    # Combine both names and convert to lowercase
    combined_names = (name1 + name2).lower()

    # Count letters in TRUE
    true_score = (
        combined_names.count("t") +
        combined_names.count("r") +
        combined_names.count("u") +
        combined_names.count("e")
    )

    # Count letters in LOVE
    love_score = (
        combined_names.count("l") +
        combined_names.count("o") +
        combined_names.count("v") +
        combined_names.count("e")
    )

    # Combine the scores
    print(f"{true_score}{love_score}")


# Test the function
calculate_love_score("Jack Reacher", "Roscoe Clinton")