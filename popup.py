from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import pyautogui
import time
import os
from datetime import datetime
from threading import Thread
class Popup(QDialog):
    signal = Signal(str)

    def __init__(self, parent:QWidget):
        super().__init__(parent)
        self.mainwindow = parent
        self.is_reserved = False
        self.signal.connect(self.signal_work)
        self.setFixedSize(300,400)
        self.set_ui()

        # 화면 중앙
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):
        # Close the entire application when the dialog is closed
        QApplication.instance().quit()
    
    def signal_work(self, msg):
        if msg == "WorkEnd":
            self.start_button.setEnabled(True)
            self.start_button.setText("Start")

    def set_ui(self):
        self.setWindowTitle('설정')
        # self.layout = QVBoxLayout(self)

        self.lb_time_set = QLabel(self, text="대기시간설정(초) ex) 2시간 = 7200")
        self.tb_time_set = QTextEdit(self, text="7380")
        self.lb_time_set.setGeometry(10, 10, 280, 30)
        self.tb_time_set.setGeometry(10, 40, 280, 30)
        # self.layout.addWidget(self.lb_time_set)
        # self.layout.addWidget(self.tb_time_set)
        

        self.check_poweroff = QCheckBox(self)
        self.check_poweroff.setText("사용 후 PC 종료")
        self.check_poweroff.setChecked(True)
        self.check_poweroff.setGeometry(10, 70, 280, 30)
        # self.layout.addWidget(self.check_poweroff)

        self.check_reservation = QCheckBox(self)
        self.check_reservation.setText("예약사용")
        self.check_reservation.setChecked(False)
        self.check_reservation.checkStateChanged.connect(self.reservation_change)
        self.check_reservation.setGeometry(10, 100, 280, 30)
        # self.layout.addWidget(self.check_reservation)

        self.calendar = QCalendarWidget(self)
        self.calendar.setVisible(False)
        self.calendar.setGridVisible(True)
        self.calendar.setGeometry(10, 140, 280, 150)
        # self.layout.addWidget(self.calendar)


        self.time_edit = QTimeEdit(self)
        self.time_edit.setVisible(False)
        self.time_edit.setTime(QTime.currentTime())  # Set to current time
        self.time_edit.setGeometry(10, 300, 280, 30)
        # self.layout.addWidget(self.time_edit)

        self.label = QLabel(self, text="Selected Time: ")
        self.label.setVisible(False)
        self.label.setGeometry(10, 330, 280, 30)
        # self.layout.addWidget(self.label)

        self.start_button = QPushButton("Start", self)
        self.start_button.clicked.connect(self.simulate_click)
        self.start_button.setGeometry(10, 360, 280, 30)
        # self.layout.addWidget(self.start_button)

        # self.setLayout(self.layout)

    def reservation_change(self):
        if self.is_reserved:
            self.is_reserved = False
            self.calendar.setVisible(False)
            self.time_edit.setVisible(False)
            self.label.setVisible(False)
            # self.calendar.setEnabled(False)
            # self.time_edit.setEnabled(False)
            
        else:
            self.is_reserved = True
            self.calendar.setVisible(True)
            self.time_edit.setVisible(True)
            self.label.setVisible(True)
            # self.calendar.setEnabled(True)
            # self.time_edit.setEnabled(True)

    def update_label(self):
        if self.selected_date and self.selected_time:
            self.label.setText(f"Selected Date and Time: {self.selected_date.toString('yyyy-MM-dd')} {self.selected_time.toString('HH:mm:ss')}")


    def simulate_click(self):
        print("===============================================")
        print("====================START!!===================")
        print("===============================================")

        try:
            self.term = int(self.tb_time_set.toPlainText())
        except:
            self.msgbox = QMessageBox(self)
            self.msgbox.setText("대기시간을 올바르게 설정하세요")
            self.msgbox.show()
            return

        self.start_button.setEnabled(False)
        self.start_button.setText("실행중")

        if self.is_reserved:
            selected_date = self.calendar.selectedDate()
            selected_time = self.time_edit.time()

            selected_datetime = datetime(
                selected_date.year(),
                selected_date.month(),
                selected_date.day(),
                selected_time.hour(),
                selected_time.minute(),
                # selected_time.second()
                0
            )

            now = datetime.now()
            wait_time = (selected_datetime - now).total_seconds()

            if wait_time > 0:
                self.wait_thread = Thread(target=self.wait, args=(selected_datetime, wait_time), daemon=True)
                self.wait_thread.start()
            else:
                print("Selected time is in the past")
                self.label.setText("Selected time is in the past, Work start!")
                self.work_thread = Thread(target=self.work, daemon=True)
                self.work_thread.start()
        else:
            self.work_thread = Thread(target=self.work, daemon=True)
            self.work_thread.start()

    def wait(self, selected_datetime, wait_time):
        print(f"Waiting for {wait_time} seconds until {selected_datetime}")
        time.sleep(wait_time)  # 특정 날짜와 시간까지 대기합니다.
        print(f"Reached {selected_datetime}")
        self.work()

    def work(self):
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

        # 대기시간만큼 기다림
        time.sleep(self.term)

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

        # 대기시간만큼 기다림
        time.sleep(self.term)

        if self.check_poweroff.isChecked():
            # 컴퓨터 종료
            os.system("shutdown /s /t 1")
        else:
            self.signal.emit("WorkEnd")