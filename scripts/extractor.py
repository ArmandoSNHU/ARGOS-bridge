import re
import os
from datetime import datetime

def extract_sql(input_file):
    """
    Extracts SQL blocks from a text-based report export.
    Useful for version controlling Argos logic in GitHub.
    """
    try:
        with open(input_file, 'r') as f:
            data = f.read()
        
        # Regex to find standard SQL patterns (SELECT/UPDATE/INSERT)
        # It looks for keywords and captures everything until a semicolon
        sql_pattern = r"(SELECT[\s\S]*?;|INSERT[\s\S]*?;|UPDATE[\s\S]*?;)"
        matches = re.findall(sql_pattern, data, re.IGNORECASE)
        
        if not matches:
            print(f"No SQL patterns found in {input_file}")
            return []
            
        print(f"Success: Found {len(matches)} SQL queries.")
        return matches

    except Exception as e:
        print(f"Error reading file: {e}")
        return []

def save_queries(queries):
    """Saves extracted queries into the sql_queries folder with timestamps."""
    for i, query in enumerate(queries):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        filename = f"sql_queries/extracted_query_{timestamp}_{i}.sql"
        
        with open(filename, 'w') as f:
            f.write("-- Extracted via ARGOS-bridge\n")
            f.write(query.strip())
        print(f"Saved: {filename}")

if __name__ == "__main__":
    # For now, we point to a dummy file we are about to create
    target = "sample_export.txt"
    found_sql = extract_sql(target)
    save_queries(found_sql)