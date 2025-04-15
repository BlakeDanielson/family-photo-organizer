## Current Objective

- Implement duplicate detection using perceptual hashing.

## Context

- Basic photo analysis (blur) is implemented.
- Need to identify visually similar photos.

## Completed Steps

- ~~Implement duplicate detection:~~ ✓
  - ~~Choose and implement hashing algorithm (pHash from `imagehash`).~~ ✓
  - ~~Add duplicate detection logic to the core module (`analysis.py` calculates hash).~~ ✓
  - ~~Update `Photo` class with duplicate information fields (`phash`, `is_duplicate_of`, `duplicate_group_id`).~~ ✓
  - ~~Updated `process_files` in GUI to compare hashes and mark duplicates.~~ ✓
  - ~~Update GUI to indicate duplicates (added "Duplicate Info" column).~~ ✓

## Next Task

- Implement Manual Classification Override:
  - Add mechanism in GUI (e.g., right-click context menu on table row) to change classification.
  - Update `Photo` object to store the override.
  - Visually indicate override in the table (e.g., different color, icon). 