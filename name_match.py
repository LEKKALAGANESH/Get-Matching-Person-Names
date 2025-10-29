import rapidfuzz.fuzz
import rapidfuzz.process

names = [
    "Geetha", "Gita", "Gitu", "Geetanjali", "Geeta", "Githa", "Gitaa", "Geetha Kumari",
    "Gita Sharma", "Geetika", "Geetha Priya", "Gita Devi", "Geetanjali Rao", "Githa Nair",
    "Gita Patel", "Geetha Singh", "Gitu Verma", "Geetika Jain", "Geetha Reddy", "Gita Kumar",
    "Geetanjali Gupta", "Githa Iyer", "Gita Choudhury", "Geetha Menon", "Gitu Das",
    "Geetika Banerjee", "Geetha Chatterjee", "Gita Mukherjee", "Geetanjali Sen", "Githa Roy",
    "Gita Das", "Geetu", "Gheetal", "Githika", "Geethika", "Geetanjali Mishra", "Geetali", 
    "Gitanjali", "Geetanshi", "Geethanjali", "Githanjali", "Gethika", "Geetashree",
    "Geetha Lakshmi", "Gita Raj", "Githika Ramesh", "Geetha Das", "Gita Mehra",
    "Geethika Rao", "Gita Rani", "Geetha Latha", "Geetanjali Das", "Gita Joshi",
    "Githu", "Getha", "Gitu Kumari", "Githika Menon", "Geetanjali Nair", "Getha Priya",
    "Gita Laxmi", "Geetha Rajesh", "Gitu Patel"
]


def get_best_match(input_name, threshold=60):
    """
    Returns the best matching name from the list based on similarity score.
    If no match above threshold, returns None.
    """
    input_lower = input_name.lower().strip()
    input_clean = ''.join(c for c in input_lower if c.isalnum())

    result = rapidfuzz.process.extractOne(input_clean, [''.join(c for c in n.lower() if c.isalnum()) for n in names], scorer=rapidfuzz.fuzz.ratio)

    if result and result[1] >= threshold:
        return names[result[2]]
    return None

def get_list_of_matches(input_name, limit=5, threshold=60):
    """
    Returns a list of top matching names with their similarity scores.
    """
    input_lower = input_name.lower().strip()
    input_clean = ''.join(c for c in input_lower if c.isalnum())

    results = rapidfuzz.process.extract(input_clean, [''.join(c for c in n.lower() if c.isalnum()) for n in names], scorer=rapidfuzz.fuzz.ratio, limit=limit)

    matches = [(names[result[2]], result[1]) for result in results if result[1] >= threshold]
    return matches

if __name__ == "__main__":
    input_name = input("Enter a name to search: ")
    best_match = get_best_match(input_name)
    list_matches = get_list_of_matches(input_name)

    print(f"Input: {input_name}")
    print(f"Best Match: {best_match}")
    print("List of Matches:")
    for name, score in list_matches:
        print(f"  {name}: {score:.2f}%")
