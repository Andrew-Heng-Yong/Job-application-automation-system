from __future__ import annotations

import sys
from PySide6.QtWidgets import QApplication

from ui_main_window import Ui_MainWindow


def main() -> None:
    app = QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()