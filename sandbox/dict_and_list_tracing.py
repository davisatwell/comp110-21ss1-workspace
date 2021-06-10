def init(store: dict[str, int], keys: list[str]) -> None:
    """Initialize frequency table."""
    for word in keys:
        store[word] = 0

def main() -> None:
    """Entrypoint."""
    counts: dict[str, int] = {}
    words: list[str] = ["the","and", "but"]
    init(counts, words)
    counts[words[1]] += 2
    counts[words[counts[words[2]]]] += 3
    print(counts)


if __name__ == '__main__':
    main()

