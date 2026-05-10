def normalize_whitespace(text: str) -> str:
    return " ".join(text.split())

def word_count(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for word in normalize_whitespace(text).lower().split(" "):
        counts[word] = counts.get(word, 0) + 1
    return counts

if __name__ == "__main__":
    ex_1 = input("Enter string (or 'd' for default): ")
    if ex_1=='d':
        print(word_count("Ala have cat named ala"))
    else:
        print(word_count(ex_1))