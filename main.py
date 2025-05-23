import sys
from PySide6.QtWidgets import QApplication, QFrame
from PySide6.QtCore import QCoreApplication, QMetaObject  # 添加 QMetaObject 导入


class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(400, 300)

        self.retranslateUi(Frame)
        QMetaObject.connectSlotsByName(Frame)  # 确保 QMetaObject 正确导入

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    frame = QFrame()
    ui = Ui_Frame()
    ui.setupUi(frame)
    frame.show()
    sys.exit(app.exec())