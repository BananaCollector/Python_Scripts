def normalize_whitespace(text: str) -> str:
    return " ".join(text.split())

def word_count(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for word in normalize_whitespace(text).lower().split(" "):
        counts[word] = counts.get(word, 0) + 1
    return counts

if __name__ == "__main__":
    sample = "Ala ma kota ala"
    print(word_count(sample))