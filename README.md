# Task 1: Name Similarity Matching

This Python script implements fuzzy string matching to identify similar names from a predefined dataset. It utilizes the RapidFuzz library for efficient similarity calculations and provides ranked results based on string similarity scores.

## Features

- **Fuzzy Matching**: Uses token-based similarity algorithms for accurate name matching
- **Case-Insensitive**: Handles variations in capitalization
- **Data Cleaning**: Automatically removes spaces and punctuation for better matching
- **Configurable Threshold**: Filters results based on a minimum similarity score (default 60%)
- **Ranked Results**: Returns the best match and a sorted list of similar names with scores

## Prerequisites

- Python 3.8 or higher
- Required Python packages (see requirements.txt)

## Installation

1. Navigate to the task1_name_match directory:
   ```bash
   cd task1_name_match
   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # source venv/bin/activate  # On macOS/Linux
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Execute the script from the command line:
```bash
python name_match.py
```

When prompted, enter a name to search for similar matches in the dataset.

## Sample Input/Output

**Input:**
```
Enter a name to match: Gita
```

**Output:**
```
Input: Gita
Best Match: Gita (100.00%)
Top Matches:
  Gita: 100.00%
  Gitaa: 80.00%
  Gitu: 75.00%
  Geetha: 66.67%
  Geeta: 66.67%
```

## Implementation Details

The script processes a hardcoded list of names and uses RapidFuzz's token_set_ratio for similarity calculation. This approach provides robust matching even with partial name variations or common misspellings.

## Notes

- The dataset is currently hardcoded within the script
- Similarity threshold can be adjusted by modifying the THRESHOLD constant
- Results are sorted by similarity score in descending order
