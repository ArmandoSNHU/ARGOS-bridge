from argos_bridge.validator import format_validation_report, validate_sql_standards


if __name__ == "__main__":
    print("Running ARGOS-bridge SQL validation...")
    result = validate_sql_standards("sql_queries")
    print(format_validation_report(result))
