import os

def validate_sql_standards(directory):
    """
    Checks SQL files in a directory for Sample College coding standards.
    """
    passed = True
    for filename in os.listdir(directory):
        if filename.endswith(".sql"):
            with open(os.path.join(directory, filename), 'r') as f:
                content = f.read().upper()
                
                # Rule 1: No Dangerous Commands (Security Check)
                if "DROP TABLE" in content or "TRUNCATE" in content:
                    print(f"SECURITY ALERT: Dangerous command found in {filename}")
                    passed = False
                
                # Rule 2: Must have a semi-colon
                if ";" not in content:
                    print(f"LINTING ERROR: Missing semicolon in {filename}")
                    passed = False
                    
    return passed

if __name__ == "__main__":
    print("Running SQL Validation for Sample College...")
    if validate_sql_standards("sql_queries"):
        print("All SQL files pass the institutional standards.")
    else:
        print("Validation failed. Please review errors.")