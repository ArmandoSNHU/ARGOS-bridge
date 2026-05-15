# ARGOS-bridge

ARGOS-bridge is a Python project for Banner-style institutional reporting and Argos-style report governance. It shows how teams can extract SQL from report exports, organize report assets, validate SQL safety, and document report purpose.

This repository uses fictional `SC_ERP` sample objects. It does not connect to a real Banner, Argos, or ERP environment.

## What It Demonstrates

- SQL report extraction from text exports.
- Governed SQL examples for Student, Finance, Human Resources, and Financial Aid.
- Argos-style report metadata: audience, parameters, output type, sensitivity, and business question.
- Validation for risky report patterns such as destructive SQL, missing semicolons, and `SELECT *`.
- A clean command-line workflow for repeatable report checks.

## Quick Start

Run from the repository root:

```powershell
python -m argos_bridge demo
```

Useful commands:

```powershell
python -m argos_bridge inventory
python -m argos_bridge validate sql_queries
python -m argos_bridge extract sample_export.txt
python -m unittest discover
```

`extract` creates timestamped SQL files in `sql_queries/`, so inspect generated files before committing.

## Why This Matters

In a college MIS environment, Banner-style systems are the source of administrative data. Reporting tools such as Argos-style platforms package SQL, parameters, security, and output delivery so Finance, HR, Student Services, and Financial Aid users can make decisions without writing SQL themselves.

ARGOS-bridge demonstrates the bridge role:

- Translate functional questions into report requirements.
- Write readable SQL against institutional data.
- Track reports as version-controlled assets.
- Validate risky patterns before release.
- Document purpose, audience, parameters, and data sensitivity.

## Project Layout

- `argos_bridge/` - CLI package for extraction, validation, and report inventory.
- `reports/` - Argos-style metadata for report assets.
- `sql_queries/` - sample Banner-style SQL reports and extracted SQL.
- `tests/` - standard-library unit tests.
- `scripts/` - compatibility wrappers for the original proof-of-concept scripts.

## Project Summary

The SQL files represent governed report logic, the metadata files represent Argos-style DataBlock/report documentation, and the validator catches patterns that could cause security, data quality, or maintainability problems.

## Current Limits

- SQL parsing is intentionally lightweight and regex-based.
- Metadata simulates Argos-style report governance; it is not a proprietary Argos export parser.
- The ERP API push step is still future work.
- All sample data is fictional and FERPA-safe.
