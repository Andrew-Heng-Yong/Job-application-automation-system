from __future__ import annotations

from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Qt
from ui_popup_editor import Ui_PopupEditer


class PopupEditorDialog(QDialog):
    """Wrapper dialog for the generated PopupEditer UI.

    Exposes a simple modal method `edit_text(initial_text)` which fills the
    editor, runs the dialog, and returns the edited text (or None on cancel).
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_PopupEditer()
        self.ui.setupUi(self)

        # Make this dialog stay on top (similar to overlay behavior) and modal
        try:
            # Keep the existing window flags and add always-on-top/tool hints
            self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint | Qt.Tool)
            # Make the dialog application-modal so it stays above the app
            self.setWindowModality(Qt.ApplicationModal)
        except Exception:
            pass

    def edit_text(self, initial_text: str) -> str | None:
        # Prefill editor and show modal dialog. Returns edited text or None.
        self.ui.editorBox.setPlainText(initial_text)
        # Make title explicit
        try:
            self.setWindowTitle("Edit generated cover letter")
            self.ui.titleLabel.setText("Edit generated cover letter")
        except Exception:
            pass

        # Wire ContinueButton to accept() so exec_() will return QDialog.Accepted
        try:
            self.ui.ContinueButton.clicked.connect(self.accept)
        except Exception:
            pass

        # Bring dialog to front before showing, ensuring it's visible above other windows
        try:
            self.raise_()
            self.activateWindow()
        except Exception:
            pass

        res = self.exec()
        if res == QDialog.Accepted:
            return self.ui.editorBox.toPlainText()
        return None
