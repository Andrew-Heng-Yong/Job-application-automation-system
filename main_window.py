from __future__ import annotations

import threading
from pathlib import Path
from typing import Any

from PySide6.QtWidgets import QMainWindow, QMessageBox

from ui_main_window import Ui_MainWindow
from config_manager import load_json, save_json
import backend.core.automation as automation

BASE_DIR = Path(__file__).resolve().parent


class MainWindow(QMainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Internal state
        self._app_config_path = BASE_DIR / "app_config.json"
        self._gemini_config_path = BASE_DIR / "gemini_config.json"
        self._original_resume_catalog: list[dict[str, Any]] | None = None
        self._automation_thread: threading.Thread | None = None

        # Connect buttons
        self.ui.button_load_app_config.clicked.connect(self.load_app_config)
        self.ui.button_save_app_config.clicked.connect(self.save_app_config)
        self.ui.button_load_gemini_config.clicked.connect(self.load_gemini_config)
        self.ui.button_save_gemini_config.clicked.connect(self.save_gemini_config)
        self.ui.button_run.clicked.connect(self.run_automation)
        self.ui.button_stop.clicked.connect(self.stop_automation)

        # Initialize UI with current configs if present
        self.load_app_config()
        self.load_gemini_config()

    # --------------------------
    # App config helpers
    # --------------------------
    def load_app_config(self) -> None:
        cfg = load_json(str(self._app_config_path))
        # set widget values with safe defaults
        self.ui.spin_confidence.setValue(float(cfg.get("confidence", self.ui.spin_confidence.value())))
        self.ui.spin_check_interval.setValue(float(cfg.get("check_interval", self.ui.spin_check_interval.value())))
        self.ui.spin_default_timeout.setValue(int(cfg.get("default_timeout", self.ui.spin_default_timeout.value())))
        self.ui.spin_scroll_step.setValue(int(cfg.get("scroll_step", self.ui.spin_scroll_step.value())))
        self.ui.spin_page_ready_timeout.setValue(int(cfg.get("page_ready_timeout", self.ui.spin_page_ready_timeout.value())))
        self.ui.spin_post_apply_timeout.setValue(int(cfg.get("post_apply_timeout", self.ui.spin_post_apply_timeout.value())))
        self.ui.spin_apply_retry_count.setValue(int(cfg.get("apply_retry_count", self.ui.spin_apply_retry_count.value())))
        self.ui.spin_max_scroll_pages.setValue(int(cfg.get("max_scroll_pages", self.ui.spin_max_scroll_pages.value())))
        self.ui.spin_row_half_height.setValue(int(cfg.get("row_half_height", self.ui.spin_row_half_height.value())))
        self.ui.spin_left_scan_width_ratio.setValue(float(cfg.get("left_scan_width_ratio", self.ui.spin_left_scan_width_ratio.value())))
        self.ui.edit_start_anchor.setText(str(cfg.get("start_anchor", self.ui.edit_start_anchor.text())))
        self.ui.edit_end_anchor.setText(str(cfg.get("end_anchor", self.ui.edit_end_anchor.text())))

        QMessageBox.information(self, "Load App Config", f"Loaded app config from {self._app_config_path}")

    def save_app_config(self) -> None:
        cfg = {
            "confidence": float(self.ui.spin_confidence.value()),
            "check_interval": float(self.ui.spin_check_interval.value()),
            "default_timeout": int(self.ui.spin_default_timeout.value()),
            "scroll_step": int(self.ui.spin_scroll_step.value()),
            "page_ready_timeout": int(self.ui.spin_page_ready_timeout.value()),
            "post_apply_timeout": int(self.ui.spin_post_apply_timeout.value()),
            "apply_retry_count": int(self.ui.spin_apply_retry_count.value()),
            "max_scroll_pages": int(self.ui.spin_max_scroll_pages.value()),
            "row_half_height": int(self.ui.spin_row_half_height.value()),
            "left_scan_width_ratio": float(self.ui.spin_left_scan_width_ratio.value()),
            "start_anchor": str(self.ui.edit_start_anchor.text()),
            "end_anchor": str(self.ui.edit_end_anchor.text()),
        }
        save_json(str(self._app_config_path), cfg)
        QMessageBox.information(self, "Save App Config", f"Saved app config to {self._app_config_path}")

    # --------------------------
    # Gemini config helpers
    # --------------------------
    def load_gemini_config(self) -> None:
        cfg = load_json(str(self._gemini_config_path))
        # preserve original resume catalog for later
        self._original_resume_catalog = cfg.get("RESUME_CATALOG")

        self.ui.edit_api_key.setText(str(cfg.get("API_KEY", self.ui.edit_api_key.text())))
        self.ui.edit_model_name.setText(str(cfg.get("MODEL_NAME", self.ui.edit_model_name.text())))
        self.ui.edit_output_dir.setText(str(cfg.get("OUTPUT_DIR", self.ui.edit_output_dir.text())))
        self.ui.spin_cover_letter_word_limit.setValue(int(cfg.get("COVER_LETTER_WORD_LIMIT", self.ui.spin_cover_letter_word_limit.value())))

        self.ui.text_resume_selection_system_prompt.setPlainText(str(cfg.get("RESUME_SELECTION_SYSTEM_PROMPT", self.ui.text_resume_selection_system_prompt.toPlainText())))
        self.ui.text_resume_selection_user_prompt_template.setPlainText(str(cfg.get("RESUME_SELECTION_USER_PROMPT_TEMPLATE", self.ui.text_resume_selection_user_prompt_template.toPlainText())))

        self.ui.text_cover_letter_system_prompt.setPlainText(str(cfg.get("COVER_LETTER_SYSTEM_PROMPT", self.ui.text_cover_letter_system_prompt.toPlainText())))
        self.ui.text_cover_letter_user_prompt_template.setPlainText(str(cfg.get("COVER_LETTER_USER_PROMPT_TEMPLATE", self.ui.text_cover_letter_user_prompt_template.toPlainText())))

        self.ui.text_minor_change_system_prompt.setPlainText(str(cfg.get("MINOR_CHANGE_SYSTEM_PROMPT", self.ui.text_minor_change_system_prompt.toPlainText())))
        self.ui.text_minor_change_user_prompt_template.setPlainText(str(cfg.get("MINOR_CHANGE_USER_PROMPT_TEMPLATE", self.ui.text_minor_change_user_prompt_template.toPlainText())))

        self.ui.text_additional_personal_information.setPlainText(str(cfg.get("ADDITIONAL_PERSONAL_INFORMATION", self.ui.text_additional_personal_information.toPlainText())))

        # Note: resume catalog table editing not implemented. Preserve original on save.
        QMessageBox.information(self, "Load Gemini Config", f"Loaded gemini config from {self._gemini_config_path}")

    def save_gemini_config(self) -> None:
        # Load existing file to preserve keys not present in UI (e.g., RESUME_CATALOG)
        existing = load_json(str(self._gemini_config_path))
        cfg: dict[str, Any] = existing.copy()

        cfg.update(
            {
                "API_KEY": str(self.ui.edit_api_key.text()),
                "MODEL_NAME": str(self.ui.edit_model_name.text()),
                "OUTPUT_DIR": str(self.ui.edit_output_dir.text()),
                "COVER_LETTER_WORD_LIMIT": int(self.ui.spin_cover_letter_word_limit.value()),

                "RESUME_SELECTION_SYSTEM_PROMPT": str(self.ui.text_resume_selection_system_prompt.toPlainText()),
                "RESUME_SELECTION_USER_PROMPT_TEMPLATE": str(self.ui.text_resume_selection_user_prompt_template.toPlainText()),

                "COVER_LETTER_SYSTEM_PROMPT": str(self.ui.text_cover_letter_system_prompt.toPlainText()),
                "COVER_LETTER_USER_PROMPT_TEMPLATE": str(self.ui.text_cover_letter_user_prompt_template.toPlainText()),

                "MINOR_CHANGE_SYSTEM_PROMPT": str(self.ui.text_minor_change_system_prompt.toPlainText()),
                "MINOR_CHANGE_USER_PROMPT_TEMPLATE": str(self.ui.text_minor_change_user_prompt_template.toPlainText()),

                "ADDITIONAL_PERSONAL_INFORMATION": str(self.ui.text_additional_personal_information.toPlainText()),
            }
        )

        # Ensure RESUME_CATALOG preserved if it existed
        if "RESUME_CATALOG" not in cfg and self._original_resume_catalog is not None:
            cfg["RESUME_CATALOG"] = self._original_resume_catalog

        save_json(str(self._gemini_config_path), cfg)
        QMessageBox.information(self, "Save Gemini Config", f"Saved gemini config to {self._gemini_config_path}")

    # --------------------------
    # Automation control
    # --------------------------
    def _automation_target(self) -> None:
        try:
            automation.main()
        except Exception as exc:
            # show a user-friendly message on failure
            QMessageBox.critical(self, "Automation Error", f"Automation raised an exception: {exc}")
        finally:
            # Re-enable Run button when finished
            self.ui.button_run.setEnabled(True)

    def run_automation(self) -> None:
        if self._automation_thread and self._automation_thread.is_alive():
            QMessageBox.information(self, "Automation", "Automation is already running")
            return

        self.ui.button_run.setEnabled(False)
        self._automation_thread = threading.Thread(target=self._automation_target, daemon=True)
        self._automation_thread.start()
        QMessageBox.information(self, "Automation", "Automation started in background thread")

    def stop_automation(self) -> None:
        # Placeholder: real stop functionality requires a cooperative stop flag in automation
        QMessageBox.information(self, "Stop", "Stop requested — placeholder (no stop flag implemented)")


# If this module is run directly, create and show the window (useful for testing)
if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
