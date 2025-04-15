## Current Objective

- Implement basic photo quality analysis.

## Context

- Photos are loaded and displayed in the GUI.
- Need to start classifying photos based on quality metrics.

## Completed Steps

- ~~Implement basic photo quality analysis (placeholder/rule-based initially).~~ ✓
  - ~~Add necessary fields to `Photo` class.~~ ✓ (Already present)
  - ~~Create core analysis module/function (`analysis.py`, `analyze_photo_quality`).~~ ✓
  - ~~Update GUI to display classification (added column to table).~~ ✓
  - ~~Integrated analysis call into `process_files`.~~ ✓

## Next Task

- Implement duplicate detection:
  - Choose and implement hashing algorithm (e.g., pHash/dHash from `imagehash`).
  - Add duplicate detection logic to the core module.
  - Update `Photo` class with duplicate information fields.
  - Update GUI to indicate duplicates (e.g., grouping, highlighting). 