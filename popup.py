from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import pyautogui
import time
import os
class Popup(QDialog):
    def __init__(self, parent:QWidget):
        super().__init__(parent)
        self.mainwindow = parent
        self.setFixedSize(200,200)
        self.set_ui()

    def closeEvent(self, event):
        # Close the entire application when the dialog is closed
        QApplication.instance().quit()

    def set_ui(self):
        self.setWindowTitle('설정')
        self.layout = QVBoxLayout(self)
        self.time_edit = QTimeEdit(self)
        self.time_edit.setTime(QTime.currentTime())  # Set to current time

        self.layout.addWidget(self.time_edit)
        self.label = QLabel("Selected Time: ")
        self.layout.addWidget(self.label)

        self.button = QPushButton("Set Time", self)
        self.button.clicked.connect(self.show_time)
        self.layout.addWidget(self.button)


        self.start_button = QPushButton("Start", self)
        self.start_button.clicked.connect(self.simulate_click)
        self.layout.addWidget(self.start_button)

        self.setLayout(self.layout)

    def show_time(self):
        # Get the selected time from QTimeEdit
        selected_time = self.time_edit.time()
        # Display the selected time in the QLabel
        self.label.setText(f"Selected Time: {selected_time.toString('HH:mm:ss')}")

    def simulate_click(self):
        # Simulate a mouse click at position (410, 530)
        print("===============================================")
        print("====================START!!===================")
        print("===============================================")

        # 자동사냥 버튼
        pyautogui.click(568, 772)
        pyautogui.click(568, 772)

        time.sleep(1)
        # 사망시 자동부활 버튼
        pyautogui.click(413, 486)
        
        # 시작 버튼
        time.sleep(1)
        pyautogui.click(410, 530)

        time.sleep(1)
        # 확인 버튼
        pyautogui.click(345, 507)

        # 두시간 5분 기다림
        time.sleep(7500)

        # 2번째 창 자동사냥 버튼
        pyautogui.click(1460, 772)
        pyautogui.click(1460, 772)

        time.sleep(1)
        # 사망시 자동부활 버튼
        pyautogui.click(1279, 486)

        # 시작 버튼
        time.sleep(1)
        pyautogui.click(1303, 530)

        # 확인 버튼
        time.sleep(1)
        pyautogui.click(1246, 507)

        # 두시간 5분 기다림
        time.sleep(7500)

        # 컴퓨터 종료
        os.system("shutdown /s /t 1")