def read_site_metadata():
    """Retrieve and return structured site information."""
    return {
        "name": "ZhaiYouXi",
        "url": "https://zhaiyouxi.com.cn",
        "tags": ["games", "entertainment", "reviews", "indie"],
        "keywords": ["爱游戏", "game recommendations", "playable web games"],
        "description": "A curated platform for discovering and reviewing indie and casual online games."
    }


def format_keywords(keywords):
    """Convert keyword list into a readable string."""
    return ", ".join(keywords)


def format_tags(tags):
    """Convert tag list into a hashtag-style string."""
    return " ".join(f"#{tag}" for tag in tags)


def generate_summary(metadata):
    """Compose a structured text summary from provided metadata."""
    lines = []
    lines.append("=" * 50)
    lines.append(f"Site Name: {metadata['name']}")
    lines.append(f"URL: {metadata['url']}")
    lines.append(f"Keywords: {format_keywords(metadata['keywords'])}")
    lines.append(f"Tags: {format_tags(metadata['tags'])}")
    lines.append("-" * 50)
    lines.append(f"Description: {metadata['description']}")
    lines.append("=" * 50)
    return "\n".join(lines)


def write_summary_to_file(summary_text, filename="site_summary_output.txt"):
    """Write the generated summary to a text file for reference."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(summary_text + "\n")
    print(f"Summary written to {filename}")


def display_summary_from_file(filename="site_summary_output.txt"):
    """Read and print the summary from file if it exists."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        print("Reading from file:")
        print(content)
    except FileNotFoundError:
        print(f"File {filename} not found. Generate it first.")


def main():
    metadata = read_site_metadata()
    summary = generate_summary(metadata)
    print(summary)
    write_summary_to_file(summary)
    display_summary_from_file()


if __name__ == "__main__":
    main()