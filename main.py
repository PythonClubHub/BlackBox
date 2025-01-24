import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu Bar Test")
        self.setGeometry(100, 100, 600, 400)

        # Create Menu Bar
        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)  # Force menu bar to render in window

        # Add Menus
        file_menu = menu_bar.addMenu("File")
        help_menu = menu_bar.addMenu("Help")

        # Add Actions
        file_menu.addAction("Exit").triggered.connect(self.close)
        help_menu.addAction("About")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Menu Bar Test")  # Required for macOS menu rendering
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
