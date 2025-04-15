"""
Main window for the Family Photo Organizer application.
"""

import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QVBoxLayout,
    QWidget,
    QFileDialog,
)
from PySide6.QtGui import QAction

# Import the metadata extractor
from family_photo_organizer.core.metadata_extractor import extract_basic_metadata
import os # Needed for folder scanning


class MainWindow(QMainWindow):
    """Main application window."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Family Photo Organizer")
        self.setGeometry(100, 100, 800, 600)  # x, y, width, height

        self._create_menus()
        self._create_central_widget()

    def _create_menus(self):
        """Create the menu bar."""
        menu_bar = self.menuBar()

        # File Menu
        file_menu = menu_bar.addMenu("&File")

        open_action = QAction("&Open Files...", self)
        open_action.triggered.connect(self.open_files)
        file_menu.addAction(open_action)

        open_folder_action = QAction("Open &Folder...", self)
        open_folder_action.triggered.connect(self.open_folder)
        file_menu.addAction(open_folder_action)

        file_menu.addSeparator()

        exit_action = QAction("&Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

    def _create_central_widget(self):
        """Create the central widget placeholder."""
        central_widget = QWidget()
        layout = QVBoxLayout()
        self.status_label = QLabel("Welcome! Select File > Open to load photos.")
        layout.addWidget(self.status_label)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def open_files(self):
        """Open a file dialog to select multiple image files."""
        # TODO: Add more specific file filters based on supported types
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        file_dialog.setNameFilter("Images (*.png *.jpg *.jpeg *.heic *.raw)") # Add more as needed
        file_dialog.setViewMode(QFileDialog.ViewMode.List)

        if file_dialog.exec():
            filenames = file_dialog.selectedFiles()
            if filenames:
                print(f"Selected files: {filenames}")
                self.status_label.setText(f"Processing {len(filenames)} file(s)...")
                # Pass filenames to the core processing module
                self.process_files(filenames)
                self.status_label.setText(f"Finished processing {len(filenames)} file(s).")

    def open_folder(self):
        """Open a file dialog to select a folder."""
        folder_dialog = QFileDialog(self)
        folder_path = folder_dialog.getExistingDirectory(self, "Select Folder")

        if folder_path:
            print(f"Selected folder: {folder_path}")
            self.status_label.setText(f"Scanning folder: {folder_path}...")
            # Process all supported files in the folder
            supported_extensions = (".png", ".jpg", ".jpeg", ".heic", ".raw") # Case-insensitive
            files_to_process = []
            for item in os.listdir(folder_path):
                if item.lower().endswith(supported_extensions):
                    files_to_process.append(os.path.join(folder_path, item))
            
            if files_to_process:
                print(f"Found {len(files_to_process)} supported files in folder.")
                self.process_files(files_to_process)
                self.status_label.setText(f"Finished processing {len(files_to_process)} file(s) from folder.")
            else:
                self.status_label.setText(f"No supported image files found in folder: {folder_path}")

    def process_files(self, file_paths):
        """
        Processes a list of image files, extracting metadata.

        Args:
            file_paths (list): A list of absolute paths to image files.
        """
        all_metadata = []
        for file_path in file_paths:
            print(f"--- Processing: {os.path.basename(file_path)} ---")
            metadata = extract_basic_metadata(file_path)
            if metadata:
                print(f"  Capture Date: {metadata.get('capture_date')}")
                all_metadata.append(metadata)
            else:
                print("  Could not extract metadata.")
            print("-------------------------------")
        
        # TODO: Store or display the extracted metadata
        print(f"\nSuccessfully extracted metadata for {len(all_metadata)} out of {len(file_paths)} files.")


# Example usage for testing the window directly
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec()) 