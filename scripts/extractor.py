from argos_bridge.extractor import extract_sql, save_queries


if __name__ == "__main__":
    target = "sample_export.txt"
    found_sql = extract_sql(target)
    saved = save_queries(found_sql)
    print(f"Success: Found {len(found_sql)} SQL queries.")
    for path in saved:
        print(f"Saved: {path}")
