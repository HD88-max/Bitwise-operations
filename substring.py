def generate_substrings(s):
    """
    Generates and returns all possible substrings of the given string.
    """
    substrings = []
    length = len(s)

    for start in range(length):
        for end in range(start + 1, length + 1):
            substrings.append(s[start:end])
    return substrings


def main():
    s = input("Enter a string: ").strip()

    if not s:
        print("Empty string entered. No substrings to generate.")
        return

    substrings = generate_substrings(s)

    print("\nAll substrings:")
    for sub in substrings:
        print(sub)


if __name__ == "__main__":
    main()
