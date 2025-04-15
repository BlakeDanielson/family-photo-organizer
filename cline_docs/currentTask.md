## Current Objective

- Define data structure, store photos, and display in GUI.

## Context

- Previous step implemented basic file loading and metadata extraction.
- Need to represent photos consistently and show them to the user.

## Completed Steps

- ~~Define data structure for photo information (e.g., `Photo` class).~~ ✓
- ~~Implement storage for loaded photos (in-memory list initially).~~ ✓
- ~~Display loaded photos/metadata in the GUI.~~ ✓
  - ~~Replaced central widget QLabel with QTableWidget.~~ ✓
  - ~~Added `update_photo_table` method to populate the table.~~ ✓
  - ~~Sorted photos by capture date in the table.~~ ✓

## Next Task

- Implement basic photo quality analysis (placeholder/rule-based initially).
  - Add necessary fields to `Photo` class.
  - Create core analysis module/function.
  - Update GUI to display classification. 