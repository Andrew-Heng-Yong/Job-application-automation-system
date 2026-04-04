# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QCheckBox,
    QDoubleSpinBox, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPlainTextEdit, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QSpinBox, QStatusBar,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1100, 820)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_main = QVBoxLayout(self.centralwidget)
        self.verticalLayout_main.setSpacing(10)
        self.verticalLayout_main.setObjectName(u"verticalLayout_main")
        self.verticalLayout_main.setContentsMargins(12, 12, 12, 12)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_app_config = QWidget()
        self.tab_app_config.setObjectName(u"tab_app_config")
        self.verticalLayout_app_tab = QVBoxLayout(self.tab_app_config)
        self.verticalLayout_app_tab.setSpacing(10)
        self.verticalLayout_app_tab.setObjectName(u"verticalLayout_app_tab")
        self.groupBox_app_config = QGroupBox(self.tab_app_config)
        self.groupBox_app_config.setObjectName(u"groupBox_app_config")
        self.gridLayout_app_config = QGridLayout(self.groupBox_app_config)
        self.gridLayout_app_config.setObjectName(u"gridLayout_app_config")
        self.gridLayout_app_config.setHorizontalSpacing(16)
        self.gridLayout_app_config.setVerticalSpacing(10)
        self.label_end_anchor = QLabel(self.groupBox_app_config)
        self.label_end_anchor.setObjectName(u"label_end_anchor")

        self.gridLayout_app_config.addWidget(self.label_end_anchor, 6, 0, 1, 1)

        self.spin_max_scroll_pages = QSpinBox(self.groupBox_app_config)
        self.spin_max_scroll_pages.setObjectName(u"spin_max_scroll_pages")
        self.spin_max_scroll_pages.setMaximum(99999)
        self.spin_max_scroll_pages.setValue(20)

        self.gridLayout_app_config.addWidget(self.spin_max_scroll_pages, 3, 3, 1, 1)

        self.label_post_apply_timeout = QLabel(self.groupBox_app_config)
        self.label_post_apply_timeout.setObjectName(u"label_post_apply_timeout")

        self.gridLayout_app_config.addWidget(self.label_post_apply_timeout, 2, 2, 1, 1)

        self.label_row_half_height = QLabel(self.groupBox_app_config)
        self.label_row_half_height.setObjectName(u"label_row_half_height")

        self.gridLayout_app_config.addWidget(self.label_row_half_height, 4, 0, 1, 1)

        self.label_check_interval = QLabel(self.groupBox_app_config)
        self.label_check_interval.setObjectName(u"label_check_interval")

        self.gridLayout_app_config.addWidget(self.label_check_interval, 0, 2, 1, 1)

        self.spin_scroll_step = QSpinBox(self.groupBox_app_config)
        self.spin_scroll_step.setObjectName(u"spin_scroll_step")
        self.spin_scroll_step.setMinimum(-999999)
        self.spin_scroll_step.setMaximum(999999)
        self.spin_scroll_step.setValue(-700)

        self.gridLayout_app_config.addWidget(self.spin_scroll_step, 1, 3, 1, 1)

        self.label_confidence = QLabel(self.groupBox_app_config)
        self.label_confidence.setObjectName(u"label_confidence")

        self.gridLayout_app_config.addWidget(self.label_confidence, 0, 0, 1, 1)

        self.edit_end_anchor = QLineEdit(self.groupBox_app_config)
        self.edit_end_anchor.setObjectName(u"edit_end_anchor")

        self.gridLayout_app_config.addWidget(self.edit_end_anchor, 6, 1, 1, 3)

        self.spin_page_ready_timeout = QSpinBox(self.groupBox_app_config)
        self.spin_page_ready_timeout.setObjectName(u"spin_page_ready_timeout")
        self.spin_page_ready_timeout.setMaximum(99999)
        self.spin_page_ready_timeout.setValue(30)

        self.gridLayout_app_config.addWidget(self.spin_page_ready_timeout, 2, 1, 1, 1)

        self.spin_confidence = QDoubleSpinBox(self.groupBox_app_config)
        self.spin_confidence.setObjectName(u"spin_confidence")
        self.spin_confidence.setDecimals(2)
        self.spin_confidence.setMinimum(0.000000000000000)
        self.spin_confidence.setMaximum(1.000000000000000)
        self.spin_confidence.setSingleStep(0.010000000000000)
        self.spin_confidence.setValue(0.850000000000000)

        self.gridLayout_app_config.addWidget(self.spin_confidence, 0, 1, 1, 1)

        self.spin_check_interval = QDoubleSpinBox(self.groupBox_app_config)
        self.spin_check_interval.setObjectName(u"spin_check_interval")
        self.spin_check_interval.setDecimals(2)
        self.spin_check_interval.setMinimum(0.000000000000000)
        self.spin_check_interval.setMaximum(9999.000000000000000)
        self.spin_check_interval.setSingleStep(0.050000000000000)
        self.spin_check_interval.setValue(0.350000000000000)

        self.gridLayout_app_config.addWidget(self.spin_check_interval, 0, 3, 1, 1)

        self.edit_start_anchor = QLineEdit(self.groupBox_app_config)
        self.edit_start_anchor.setObjectName(u"edit_start_anchor")

        self.gridLayout_app_config.addWidget(self.edit_start_anchor, 5, 1, 1, 3)

        self.spin_apply_retry_count = QSpinBox(self.groupBox_app_config)
        self.spin_apply_retry_count.setObjectName(u"spin_apply_retry_count")
        self.spin_apply_retry_count.setMaximum(99999)
        self.spin_apply_retry_count.setValue(3)

        self.gridLayout_app_config.addWidget(self.spin_apply_retry_count, 3, 1, 1, 1)

        self.spin_row_half_height = QSpinBox(self.groupBox_app_config)
        self.spin_row_half_height.setObjectName(u"spin_row_half_height")
        self.spin_row_half_height.setMaximum(99999)
        self.spin_row_half_height.setValue(60)

        self.gridLayout_app_config.addWidget(self.spin_row_half_height, 4, 1, 1, 1)

        self.label_page_ready_timeout = QLabel(self.groupBox_app_config)
        self.label_page_ready_timeout.setObjectName(u"label_page_ready_timeout")

        self.gridLayout_app_config.addWidget(self.label_page_ready_timeout, 2, 0, 1, 1)

        self.label_max_scroll_pages = QLabel(self.groupBox_app_config)
        self.label_max_scroll_pages.setObjectName(u"label_max_scroll_pages")

        self.gridLayout_app_config.addWidget(self.label_max_scroll_pages, 3, 2, 1, 1)

        self.spin_default_timeout = QSpinBox(self.groupBox_app_config)
        self.spin_default_timeout.setObjectName(u"spin_default_timeout")
        self.spin_default_timeout.setMaximum(99999)
        self.spin_default_timeout.setValue(10)

        self.gridLayout_app_config.addWidget(self.spin_default_timeout, 1, 1, 1, 1)

        self.label_default_timeout = QLabel(self.groupBox_app_config)
        self.label_default_timeout.setObjectName(u"label_default_timeout")

        self.gridLayout_app_config.addWidget(self.label_default_timeout, 1, 0, 1, 1)

        self.spin_left_scan_width_ratio = QDoubleSpinBox(self.groupBox_app_config)
        self.spin_left_scan_width_ratio.setObjectName(u"spin_left_scan_width_ratio")
        self.spin_left_scan_width_ratio.setDecimals(2)
        self.spin_left_scan_width_ratio.setMinimum(0.000000000000000)
        self.spin_left_scan_width_ratio.setMaximum(1.000000000000000)
        self.spin_left_scan_width_ratio.setSingleStep(0.010000000000000)
        self.spin_left_scan_width_ratio.setValue(0.820000000000000)

        self.gridLayout_app_config.addWidget(self.spin_left_scan_width_ratio, 4, 3, 1, 1)

        self.spin_post_apply_timeout = QSpinBox(self.groupBox_app_config)
        self.spin_post_apply_timeout.setObjectName(u"spin_post_apply_timeout")
        self.spin_post_apply_timeout.setMaximum(100)
        self.spin_post_apply_timeout.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spin_post_apply_timeout.setValue(1)

        self.gridLayout_app_config.addWidget(self.spin_post_apply_timeout, 2, 3, 1, 1)

        self.label_start_anchor = QLabel(self.groupBox_app_config)
        self.label_start_anchor.setObjectName(u"label_start_anchor")

        self.gridLayout_app_config.addWidget(self.label_start_anchor, 5, 0, 1, 1)

        self.label_scroll_step = QLabel(self.groupBox_app_config)
        self.label_scroll_step.setObjectName(u"label_scroll_step")

        self.gridLayout_app_config.addWidget(self.label_scroll_step, 1, 2, 1, 1)

        self.label_apply_retry_count = QLabel(self.groupBox_app_config)
        self.label_apply_retry_count.setObjectName(u"label_apply_retry_count")

        self.gridLayout_app_config.addWidget(self.label_apply_retry_count, 3, 0, 1, 1)

        self.label_left_scan_width_ratio = QLabel(self.groupBox_app_config)
        self.label_left_scan_width_ratio.setObjectName(u"label_left_scan_width_ratio")

        self.gridLayout_app_config.addWidget(self.label_left_scan_width_ratio, 4, 2, 1, 1)

        self.use_text_editer = QCheckBox(self.groupBox_app_config)
        self.use_text_editer.setObjectName(u"use_text_editer")

        self.gridLayout_app_config.addWidget(self.use_text_editer, 7, 0, 1, 1)

        self.generater_deployment_override = QCheckBox(self.groupBox_app_config)
        self.generater_deployment_override.setObjectName(u"generater_deployment_override")

        self.gridLayout_app_config.addWidget(self.generater_deployment_override, 7, 1, 1, 1)


        self.verticalLayout_app_tab.addWidget(self.groupBox_app_config)

        self.verticalSpacer_app = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_app_tab.addItem(self.verticalSpacer_app)

        self.horizontalLayout_app_buttons = QHBoxLayout()
        self.horizontalLayout_app_buttons.setObjectName(u"horizontalLayout_app_buttons")
        self.horizontalSpacer_app_left = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_app_buttons.addItem(self.horizontalSpacer_app_left)

        self.button_load_app_config = QPushButton(self.tab_app_config)
        self.button_load_app_config.setObjectName(u"button_load_app_config")

        self.horizontalLayout_app_buttons.addWidget(self.button_load_app_config)

        self.button_save_app_config = QPushButton(self.tab_app_config)
        self.button_save_app_config.setObjectName(u"button_save_app_config")

        self.horizontalLayout_app_buttons.addWidget(self.button_save_app_config)


        self.verticalLayout_app_tab.addLayout(self.horizontalLayout_app_buttons)

        self.tabWidget.addTab(self.tab_app_config, "")
        self.tab_gemini_config = QWidget()
        self.tab_gemini_config.setObjectName(u"tab_gemini_config")
        self.verticalLayout_gemini_tab = QVBoxLayout(self.tab_gemini_config)
        self.verticalLayout_gemini_tab.setSpacing(10)
        self.verticalLayout_gemini_tab.setObjectName(u"verticalLayout_gemini_tab")
        self.scrollArea_gemini = QScrollArea(self.tab_gemini_config)
        self.scrollArea_gemini.setObjectName(u"scrollArea_gemini")
        self.scrollArea_gemini.setWidgetResizable(True)
        self.scrollAreaWidgetContents_gemini = QWidget()
        self.scrollAreaWidgetContents_gemini.setObjectName(u"scrollAreaWidgetContents_gemini")
        self.scrollAreaWidgetContents_gemini.setGeometry(QRect(0, 0, 1031, 1339))
        self.verticalLayout_gemini_content = QVBoxLayout(self.scrollAreaWidgetContents_gemini)
        self.verticalLayout_gemini_content.setSpacing(12)
        self.verticalLayout_gemini_content.setObjectName(u"verticalLayout_gemini_content")
        self.groupBox_gemini_basic = QGroupBox(self.scrollAreaWidgetContents_gemini)
        self.groupBox_gemini_basic.setObjectName(u"groupBox_gemini_basic")
        self.gridLayout_gemini_basic = QGridLayout(self.groupBox_gemini_basic)
        self.gridLayout_gemini_basic.setObjectName(u"gridLayout_gemini_basic")
        self.gridLayout_gemini_basic.setHorizontalSpacing(16)
        self.gridLayout_gemini_basic.setVerticalSpacing(10)
        self.label_model_name = QLabel(self.groupBox_gemini_basic)
        self.label_model_name.setObjectName(u"label_model_name")

        self.gridLayout_gemini_basic.addWidget(self.label_model_name, 1, 0, 1, 1)

        self.edit_api_key = QLineEdit(self.groupBox_gemini_basic)
        self.edit_api_key.setObjectName(u"edit_api_key")
        self.edit_api_key.setEchoMode(QLineEdit.EchoMode.Normal)

        self.gridLayout_gemini_basic.addWidget(self.edit_api_key, 0, 1, 1, 1)

        self.label_api_key = QLabel(self.groupBox_gemini_basic)
        self.label_api_key.setObjectName(u"label_api_key")

        self.gridLayout_gemini_basic.addWidget(self.label_api_key, 0, 0, 1, 1)

        self.edit_model_name = QLineEdit(self.groupBox_gemini_basic)
        self.edit_model_name.setObjectName(u"edit_model_name")

        self.gridLayout_gemini_basic.addWidget(self.edit_model_name, 1, 1, 1, 1)

        self.spin_cover_letter_word_limit = QSpinBox(self.groupBox_gemini_basic)
        self.spin_cover_letter_word_limit.setObjectName(u"spin_cover_letter_word_limit")
        self.spin_cover_letter_word_limit.setMaximum(10000)
        self.spin_cover_letter_word_limit.setValue(150)

        self.gridLayout_gemini_basic.addWidget(self.spin_cover_letter_word_limit, 2, 1, 1, 1)

        self.label_cover_letter_word_limit = QLabel(self.groupBox_gemini_basic)
        self.label_cover_letter_word_limit.setObjectName(u"label_cover_letter_word_limit")

        self.gridLayout_gemini_basic.addWidget(self.label_cover_letter_word_limit, 2, 0, 1, 1)


        self.verticalLayout_gemini_content.addWidget(self.groupBox_gemini_basic)

        self.groupBox_resume_selection_prompts = QGroupBox(self.scrollAreaWidgetContents_gemini)
        self.groupBox_resume_selection_prompts.setObjectName(u"groupBox_resume_selection_prompts")
        self.verticalLayout_resume_selection_prompts = QVBoxLayout(self.groupBox_resume_selection_prompts)
        self.verticalLayout_resume_selection_prompts.setObjectName(u"verticalLayout_resume_selection_prompts")
        self.label_resume_selection_system_prompt = QLabel(self.groupBox_resume_selection_prompts)
        self.label_resume_selection_system_prompt.setObjectName(u"label_resume_selection_system_prompt")

        self.verticalLayout_resume_selection_prompts.addWidget(self.label_resume_selection_system_prompt)

        self.text_resume_selection_system_prompt = QPlainTextEdit(self.groupBox_resume_selection_prompts)
        self.text_resume_selection_system_prompt.setObjectName(u"text_resume_selection_system_prompt")

        self.verticalLayout_resume_selection_prompts.addWidget(self.text_resume_selection_system_prompt)

        self.label_resume_selection_user_prompt_template = QLabel(self.groupBox_resume_selection_prompts)
        self.label_resume_selection_user_prompt_template.setObjectName(u"label_resume_selection_user_prompt_template")

        self.verticalLayout_resume_selection_prompts.addWidget(self.label_resume_selection_user_prompt_template)

        self.text_resume_selection_user_prompt_template = QPlainTextEdit(self.groupBox_resume_selection_prompts)
        self.text_resume_selection_user_prompt_template.setObjectName(u"text_resume_selection_user_prompt_template")

        self.verticalLayout_resume_selection_prompts.addWidget(self.text_resume_selection_user_prompt_template)


        self.verticalLayout_gemini_content.addWidget(self.groupBox_resume_selection_prompts)

        self.groupBox_cover_letter_prompts = QGroupBox(self.scrollAreaWidgetContents_gemini)
        self.groupBox_cover_letter_prompts.setObjectName(u"groupBox_cover_letter_prompts")
        self.verticalLayout_cover_letter_prompts = QVBoxLayout(self.groupBox_cover_letter_prompts)
        self.verticalLayout_cover_letter_prompts.setObjectName(u"verticalLayout_cover_letter_prompts")
        self.label_cover_letter_system_prompt = QLabel(self.groupBox_cover_letter_prompts)
        self.label_cover_letter_system_prompt.setObjectName(u"label_cover_letter_system_prompt")

        self.verticalLayout_cover_letter_prompts.addWidget(self.label_cover_letter_system_prompt)

        self.text_cover_letter_system_prompt = QPlainTextEdit(self.groupBox_cover_letter_prompts)
        self.text_cover_letter_system_prompt.setObjectName(u"text_cover_letter_system_prompt")

        self.verticalLayout_cover_letter_prompts.addWidget(self.text_cover_letter_system_prompt)

        self.label_cover_letter_user_prompt_template = QLabel(self.groupBox_cover_letter_prompts)
        self.label_cover_letter_user_prompt_template.setObjectName(u"label_cover_letter_user_prompt_template")

        self.verticalLayout_cover_letter_prompts.addWidget(self.label_cover_letter_user_prompt_template)

        self.text_cover_letter_user_prompt_template = QPlainTextEdit(self.groupBox_cover_letter_prompts)
        self.text_cover_letter_user_prompt_template.setObjectName(u"text_cover_letter_user_prompt_template")

        self.verticalLayout_cover_letter_prompts.addWidget(self.text_cover_letter_user_prompt_template)


        self.verticalLayout_gemini_content.addWidget(self.groupBox_cover_letter_prompts)

        self.groupBox_minor_change_prompts = QGroupBox(self.scrollAreaWidgetContents_gemini)
        self.groupBox_minor_change_prompts.setObjectName(u"groupBox_minor_change_prompts")
        self.verticalLayout_minor_change_prompts = QVBoxLayout(self.groupBox_minor_change_prompts)
        self.verticalLayout_minor_change_prompts.setObjectName(u"verticalLayout_minor_change_prompts")
        self.label_minor_change_system_prompt = QLabel(self.groupBox_minor_change_prompts)
        self.label_minor_change_system_prompt.setObjectName(u"label_minor_change_system_prompt")

        self.verticalLayout_minor_change_prompts.addWidget(self.label_minor_change_system_prompt)

        self.text_minor_change_system_prompt = QPlainTextEdit(self.groupBox_minor_change_prompts)
        self.text_minor_change_system_prompt.setObjectName(u"text_minor_change_system_prompt")

        self.verticalLayout_minor_change_prompts.addWidget(self.text_minor_change_system_prompt)

        self.label_minor_change_user_prompt_template = QLabel(self.groupBox_minor_change_prompts)
        self.label_minor_change_user_prompt_template.setObjectName(u"label_minor_change_user_prompt_template")

        self.verticalLayout_minor_change_prompts.addWidget(self.label_minor_change_user_prompt_template)

        self.text_minor_change_user_prompt_template = QPlainTextEdit(self.groupBox_minor_change_prompts)
        self.text_minor_change_user_prompt_template.setObjectName(u"text_minor_change_user_prompt_template")

        self.verticalLayout_minor_change_prompts.addWidget(self.text_minor_change_user_prompt_template)


        self.verticalLayout_gemini_content.addWidget(self.groupBox_minor_change_prompts)

        self.groupBox_additional_info = QGroupBox(self.scrollAreaWidgetContents_gemini)
        self.groupBox_additional_info.setObjectName(u"groupBox_additional_info")
        self.verticalLayout_additional_info = QVBoxLayout(self.groupBox_additional_info)
        self.verticalLayout_additional_info.setObjectName(u"verticalLayout_additional_info")
        self.text_additional_personal_information = QPlainTextEdit(self.groupBox_additional_info)
        self.text_additional_personal_information.setObjectName(u"text_additional_personal_information")

        self.verticalLayout_additional_info.addWidget(self.text_additional_personal_information)


        self.verticalLayout_gemini_content.addWidget(self.groupBox_additional_info)

        self.groupBox_resume_catalog = QGroupBox(self.scrollAreaWidgetContents_gemini)
        self.groupBox_resume_catalog.setObjectName(u"groupBox_resume_catalog")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_resume_catalog.sizePolicy().hasHeightForWidth())
        self.groupBox_resume_catalog.setSizePolicy(sizePolicy)
        self.verticalLayout_resume_catalog = QVBoxLayout(self.groupBox_resume_catalog)
        self.verticalLayout_resume_catalog.setObjectName(u"verticalLayout_resume_catalog")
        self.table_resume_catalog = QTableWidget(self.groupBox_resume_catalog)
        if (self.table_resume_catalog.columnCount() < 2):
            self.table_resume_catalog.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_resume_catalog.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_resume_catalog.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.table_resume_catalog.rowCount() < 3):
            self.table_resume_catalog.setRowCount(3)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_resume_catalog.setItem(0, 0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_resume_catalog.setItem(0, 1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_resume_catalog.setItem(1, 0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_resume_catalog.setItem(1, 1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_resume_catalog.setItem(2, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_resume_catalog.setItem(2, 1, __qtablewidgetitem7)
        self.table_resume_catalog.setObjectName(u"table_resume_catalog")
        self.table_resume_catalog.setEditTriggers(QAbstractItemView.EditTrigger.AnyKeyPressed|QAbstractItemView.EditTrigger.DoubleClicked|QAbstractItemView.EditTrigger.EditKeyPressed)
        self.table_resume_catalog.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.table_resume_catalog.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_resume_catalog.setRowCount(3)
        self.table_resume_catalog.setColumnCount(2)
        self.table_resume_catalog.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_resume_catalog.addWidget(self.table_resume_catalog)

        self.horizontalLayout_resume_catalog_buttons = QHBoxLayout()
        self.horizontalLayout_resume_catalog_buttons.setObjectName(u"horizontalLayout_resume_catalog_buttons")
        self.button_add_resume_row = QPushButton(self.groupBox_resume_catalog)
        self.button_add_resume_row.setObjectName(u"button_add_resume_row")

        self.horizontalLayout_resume_catalog_buttons.addWidget(self.button_add_resume_row)

        self.button_remove_resume_row = QPushButton(self.groupBox_resume_catalog)
        self.button_remove_resume_row.setObjectName(u"button_remove_resume_row")

        self.horizontalLayout_resume_catalog_buttons.addWidget(self.button_remove_resume_row)

        self.horizontalSpacer_resume_catalog_buttons = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_resume_catalog_buttons.addItem(self.horizontalSpacer_resume_catalog_buttons)


        self.verticalLayout_resume_catalog.addLayout(self.horizontalLayout_resume_catalog_buttons)


        self.verticalLayout_gemini_content.addWidget(self.groupBox_resume_catalog)

        self.verticalSpacer_gemini_bottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_gemini_content.addItem(self.verticalSpacer_gemini_bottom)

        self.scrollArea_gemini.setWidget(self.scrollAreaWidgetContents_gemini)

        self.verticalLayout_gemini_tab.addWidget(self.scrollArea_gemini)

        self.horizontalLayout_gemini_buttons = QHBoxLayout()
        self.horizontalLayout_gemini_buttons.setObjectName(u"horizontalLayout_gemini_buttons")
        self.horizontalSpacer_gemini_left = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_gemini_buttons.addItem(self.horizontalSpacer_gemini_left)

        self.button_load_gemini_config = QPushButton(self.tab_gemini_config)
        self.button_load_gemini_config.setObjectName(u"button_load_gemini_config")

        self.horizontalLayout_gemini_buttons.addWidget(self.button_load_gemini_config)

        self.button_save_gemini_config = QPushButton(self.tab_gemini_config)
        self.button_save_gemini_config.setObjectName(u"button_save_gemini_config")

        self.horizontalLayout_gemini_buttons.addWidget(self.button_save_gemini_config)


        self.verticalLayout_gemini_tab.addLayout(self.horizontalLayout_gemini_buttons)

        self.tabWidget.addTab(self.tab_gemini_config, "")
        self.tab_logs = QWidget()
        self.tab_logs.setObjectName(u"tab_logs")
        self.verticalLayout_logs_tab = QVBoxLayout(self.tab_logs)
        self.verticalLayout_logs_tab.setSpacing(10)
        self.verticalLayout_logs_tab.setObjectName(u"verticalLayout_logs_tab")
        self.groupBox_logs = QGroupBox(self.tab_logs)
        self.groupBox_logs.setObjectName(u"groupBox_logs")
        self.verticalLayout_logs_group = QVBoxLayout(self.groupBox_logs)
        self.verticalLayout_logs_group.setObjectName(u"verticalLayout_logs_group")
        self.text_logs = QPlainTextEdit(self.groupBox_logs)
        self.text_logs.setObjectName(u"text_logs")
        self.text_logs.setReadOnly(True)

        self.verticalLayout_logs_group.addWidget(self.text_logs)

        self.horizontalLayout_logs_buttons = QHBoxLayout()
        self.horizontalLayout_logs_buttons.setObjectName(u"horizontalLayout_logs_buttons")
        self.button_clear_logs = QPushButton(self.groupBox_logs)
        self.button_clear_logs.setObjectName(u"button_clear_logs")

        self.horizontalLayout_logs_buttons.addWidget(self.button_clear_logs)

        self.horizontalSpacer_logs_buttons = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_logs_buttons.addItem(self.horizontalSpacer_logs_buttons)


        self.verticalLayout_logs_group.addLayout(self.horizontalLayout_logs_buttons)


        self.verticalLayout_logs_tab.addWidget(self.groupBox_logs)

        self.tabWidget.addTab(self.tab_logs, "")

        self.verticalLayout_main.addWidget(self.tabWidget)

        self.horizontalLayout_run_stop = QHBoxLayout()
        self.horizontalLayout_run_stop.setObjectName(u"horizontalLayout_run_stop")
        self.horizontalSpacer_run_left = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_run_stop.addItem(self.horizontalSpacer_run_left)

        self.run = QPushButton(self.centralwidget)
        self.run.setObjectName(u"run")
        self.run.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_run_stop.addWidget(self.run)

        self.pause = QPushButton(self.centralwidget)
        self.pause.setObjectName(u"pause")
        self.pause.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_run_stop.addWidget(self.pause)

        self.resume = QPushButton(self.centralwidget)
        self.resume.setObjectName(u"resume")
        self.resume.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_run_stop.addWidget(self.resume)

        self.stop = QPushButton(self.centralwidget)
        self.stop.setObjectName(u"stop")
        self.stop.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_run_stop.addWidget(self.stop)


        self.verticalLayout_main.addLayout(self.horizontalLayout_run_stop)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1100, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Application Automation Config", None))
        self.groupBox_app_config.setTitle(QCoreApplication.translate("MainWindow", u"Application Settings", None))
        self.label_end_anchor.setText(QCoreApplication.translate("MainWindow", u"end_anchor", None))
        self.label_post_apply_timeout.setText(QCoreApplication.translate("MainWindow", u"post_apply_timeout", None))
        self.label_row_half_height.setText(QCoreApplication.translate("MainWindow", u"row_half_height", None))
        self.label_check_interval.setText(QCoreApplication.translate("MainWindow", u"check_interval", None))
        self.label_confidence.setText(QCoreApplication.translate("MainWindow", u"confidence", None))
        self.edit_end_anchor.setText(QCoreApplication.translate("MainWindow", u"Targeted Degrees and Disciplines:", None))
        self.edit_start_anchor.setText(QCoreApplication.translate("MainWindow", u"Job - Country:", None))
        self.label_page_ready_timeout.setText(QCoreApplication.translate("MainWindow", u"page_ready_timeout", None))
        self.label_max_scroll_pages.setText(QCoreApplication.translate("MainWindow", u"max_scroll_pages", None))
        self.label_default_timeout.setText(QCoreApplication.translate("MainWindow", u"default_timeout", None))
        self.label_start_anchor.setText(QCoreApplication.translate("MainWindow", u"start_anchor", None))
        self.label_scroll_step.setText(QCoreApplication.translate("MainWindow", u"scroll_step", None))
        self.label_apply_retry_count.setText(QCoreApplication.translate("MainWindow", u"apply_retry_count", None))
        self.label_left_scan_width_ratio.setText(QCoreApplication.translate("MainWindow", u"left_scan_width_ratio", None))
        self.use_text_editer.setText(QCoreApplication.translate("MainWindow", u"use text editor", None))
        self.generater_deployment_override.setText(QCoreApplication.translate("MainWindow", u"generater deployment override", None))
        self.button_load_app_config.setText(QCoreApplication.translate("MainWindow", u"Load Config", None))
        self.button_save_app_config.setText(QCoreApplication.translate("MainWindow", u"Save Config", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_app_config), QCoreApplication.translate("MainWindow", u"App Config", None))
        self.groupBox_gemini_basic.setTitle(QCoreApplication.translate("MainWindow", u"Basic Gemini Settings", None))
        self.label_model_name.setText(QCoreApplication.translate("MainWindow", u"MODEL_NAME", None))
        self.edit_api_key.setText("")
        self.label_api_key.setText(QCoreApplication.translate("MainWindow", u"API_KEY", None))
        self.edit_model_name.setText(QCoreApplication.translate("MainWindow", u"gemini-2.5-flash", None))
        self.label_cover_letter_word_limit.setText(QCoreApplication.translate("MainWindow", u"COVER_LETTER_WORD_LIMIT", None))
        self.groupBox_resume_selection_prompts.setTitle(QCoreApplication.translate("MainWindow", u"Resume Selection Prompts", None))
        self.label_resume_selection_system_prompt.setText(QCoreApplication.translate("MainWindow", u"RESUME_SELECTION_SYSTEM_PROMPT", None))
        self.text_resume_selection_system_prompt.setPlainText(QCoreApplication.translate("MainWindow", u"You are helping choose the best resume version for a job application.\n"
"Pick exactly one resume from the provided catalog.\n"
"Prefer conservative extraction over guessing.\n"
"Return JSON only.", None))
        self.label_resume_selection_user_prompt_template.setText(QCoreApplication.translate("MainWindow", u"RESUME_SELECTION_USER_PROMPT_TEMPLATE", None))
        self.text_resume_selection_user_prompt_template.setPlainText(QCoreApplication.translate("MainWindow", u"Job description:\n"
"{job_description}\n"
"\n"
"Resume catalog:\n"
"{resume_catalog}\n"
"\n"
"Tasks:\n"
"1. Select the single best resume for this job.\n"
"2. Extract the company name from the job description if it is explicitly stated.\n"
"3. Provide 3 to 6 emphasis points to use in the cover letter.\n"
"\n"
"Return JSON with keys:\n"
"- company_name\n"
"- selected_resume_name\n"
"- rationale\n"
"- emphasis_points", None))
        self.groupBox_cover_letter_prompts.setTitle(QCoreApplication.translate("MainWindow", u"Cover Letter Prompts", None))
        self.label_cover_letter_system_prompt.setText(QCoreApplication.translate("MainWindow", u"COVER_LETTER_SYSTEM_PROMPT", None))
        self.text_cover_letter_system_prompt.setPlainText(QCoreApplication.translate("MainWindow", u"You write concise, specific, professional cover letters.\n"
"Use only the provided materials.\n"
"Do not invent experience.\n"
"Do not mention missing information.\n"
"Output only the final cover letter text.", None))
        self.label_cover_letter_user_prompt_template.setText(QCoreApplication.translate("MainWindow", u"COVER_LETTER_USER_PROMPT_TEMPLATE", None))
        self.text_cover_letter_user_prompt_template.setPlainText(QCoreApplication.translate("MainWindow", u"Write a tailored cover letter.\n"
"\n"
"Company: {company_name}\n"
"\n"
"Job description:\n"
"{job_description}\n"
"\n"
"Selected resume name: {resume_name}\n"
"Selected resume text:\n"
"{resume_text}\n"
"\n"
"Emphasis points:\n"
"{emphasis_points}", None))
        self.groupBox_minor_change_prompts.setTitle(QCoreApplication.translate("MainWindow", u"Minor Change Prompts", None))
        self.label_minor_change_system_prompt.setText(QCoreApplication.translate("MainWindow", u"MINOR_CHANGE_SYSTEM_PROMPT", None))
        self.text_minor_change_system_prompt.setPlainText(QCoreApplication.translate("MainWindow", u"You write concise, specific, professional cover letters.\n"
"You are revising for a new role at the same company.\n"
"Keep continuity with the previous cover letter, but introduce only minor changes to fit the new job.\n"
"Avoid copying long phrases verbatim.\n"
"Use only the provided materials.\n"
"Output only the final cover letter text.", None))
        self.label_minor_change_user_prompt_template.setText(QCoreApplication.translate("MainWindow", u"MINOR_CHANGE_USER_PROMPT_TEMPLATE", None))
        self.text_minor_change_user_prompt_template.setPlainText(QCoreApplication.translate("MainWindow", u"Write a tailored cover letter for a new role at the same company.\n"
"\n"
"Company: {company_name}\n"
"\n"
"Job description:\n"
"{job_description}\n"
"\n"
"Selected resume name: {resume_name}\n"
"Selected resume text:\n"
"{resume_text}\n"
"\n"
"Emphasis points:\n"
"{emphasis_points}\n"
"\n"
"Use the uploaded previous cover letter PDF as context.\n"
"Preserve general tone and motivation, but make minor changes for the new role.", None))
        self.groupBox_additional_info.setTitle(QCoreApplication.translate("MainWindow", u"Additional Personal Information", None))
        self.text_additional_personal_information.setPlainText(QCoreApplication.translate("MainWindow", u"use them selectively based on the job description: \n"
"", None))
        self.groupBox_resume_catalog.setTitle(QCoreApplication.translate("MainWindow", u"Resume Catalog", None))
        ___qtablewidgetitem = self.table_resume_catalog.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        ___qtablewidgetitem1 = self.table_resume_catalog.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Summary", None))

        __sortingEnabled = self.table_resume_catalog.isSortingEnabled()
        self.table_resume_catalog.setSortingEnabled(False)
        ___qtablewidgetitem2 = self.table_resume_catalog.item(0, 0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"general", None))
        ___qtablewidgetitem3 = self.table_resume_catalog.item(0, 1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"General software, programming, analytics, and broad technical experience.", None))
        ___qtablewidgetitem4 = self.table_resume_catalog.item(1, 0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"software_dev", None))
        ___qtablewidgetitem5 = self.table_resume_catalog.item(1, 1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Software development, coding, implementation, debugging, and developer workflows.", None))
        ___qtablewidgetitem6 = self.table_resume_catalog.item(2, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"complete", None))
        ___qtablewidgetitem7 = self.table_resume_catalog.item(2, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"complete resume with all experience, including detailed description, but this is too long for most postings", None))
        self.table_resume_catalog.setSortingEnabled(__sortingEnabled)

        self.button_add_resume_row.setText(QCoreApplication.translate("MainWindow", u"Add Row", None))
        self.button_remove_resume_row.setText(QCoreApplication.translate("MainWindow", u"Remove Selected Row", None))
        self.button_load_gemini_config.setText(QCoreApplication.translate("MainWindow", u"Load Config", None))
        self.button_save_gemini_config.setText(QCoreApplication.translate("MainWindow", u"Save Config", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_gemini_config), QCoreApplication.translate("MainWindow", u"Gemini Config", None))
        self.groupBox_logs.setTitle(QCoreApplication.translate("MainWindow", u"Application Logs", None))
        self.text_logs.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Logs will appear here...", None))
        self.button_clear_logs.setText(QCoreApplication.translate("MainWindow", u"Clear Logs", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_logs), QCoreApplication.translate("MainWindow", u"Logs", None))
        self.run.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.pause.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
        self.resume.setText(QCoreApplication.translate("MainWindow", u"Resume", None))
        self.stop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
    # retranslateUi

