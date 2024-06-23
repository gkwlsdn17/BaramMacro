from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from popup import Popup

'''
실행방법
- 관리자 권한으로 cmd 실행
python main.py 로 실행
start 버튼 클릭
'''

class FullScreenTransparentWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Transparent Fullscreen with Rectangles")
        self.showFullScreen()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setGeometry(0, 0, self.screen().size().width(), self.screen().size().height())
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.popup = Popup(self)
        self.popup.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen(Qt.red, 3)
        painter.setPen(pen)
        
        # Define two rectangles
        rect1 = QRect(0, 0, 1024, 800)
        rect2 = QRect(896, 0, 1024, 800)
        
        painter.drawRect(rect1)
        painter.drawRect(rect2)


if __name__ == "__main__":
    
    app = QApplication([])
    window = FullScreenTransparentWidget()
    window.show()
    app.exec()