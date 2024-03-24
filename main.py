from PyQt5.QtWidgets import QApplication, QTextEdit, QPushButton, QCalendarWidget
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt
from ui import Ui_MainWindow

class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.notes = {}
        self.ui.textEdit.textChanged.connect(self.save_note)
        self.ui.calendarWidget.clicked.connect(self.show_note)
        self.ui.pushButton_2.clicked.connect(self.del_note)

    def show_note(self):
        selected_date = self.ui.calendarWidget.selectedDate()
        note = self.notes.get(selected_date.toString(Qt.ISODate))
        self.ui.textEdit.setPlainText(note)

    def save_note(self):
        selected_date = self.ui.calendarWidget.selectedDate()
        note_text = self.ui.textEdit.toPlainText()
        self.notes[selected_date.toString(Qt.ISODate)] = note_text

    def del_note(self):
        selected_date = self.ui.calendarWidget.selectedDate()
        del self.notes[selected_date.toString(Qt.ISODate)]

app = QApplication([])
ex = Widget()
ex.show()
app.exec_()
