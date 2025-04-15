## Current Objective

- Implement basic photo loading and metadata extraction.

## Context

- Building upon the initial project structure.
- Need to allow users to select photos and extract initial data (capture date).

## Completed Steps

- ~~Create basic GUI main window (`MainWindow`)~~ ✓
- ~~Add File > Open Files and File > Open Folder menu actions~~ ✓
- ~~Implement `QFileDialog` for file/folder selection~~ ✓
- ~~Create core `metadata_extractor` module~~ ✓
- ~~Implement `extract_basic_metadata` function using `exifread`~~ ✓
- ~~Connect GUI actions to call the metadata extractor~~ ✓
- ~~Update `main.py` to launch the GUI~~ ✓

## Next Task

- Define data structure for photo information (e.g., `Photo` class).
- Implement storage for loaded photos (in-memory list initially).
- Display loaded photos/metadata in the GUI. 