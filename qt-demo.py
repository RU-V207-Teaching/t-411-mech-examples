#!/usr/bin/env python3
## Python Helper with GUI example
## By Joseph T. Foley <foley AT ru.is>
## Created onb 2024-09-23
# Ubuntu:  apt install python3-pyqt5
## Intial code from https://www.pythonguis.com/tutorials/creating-your-first-pyqt-window/
#### Reference documents
## https://doc.qt.io/qt-6/qplaintextedit.html
## https://doc.qt.io/qt-6/qlineedit.html
import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLineEdit, QPlainTextEdit
from random import choice, randint

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Peerwise Helper")
        layout = QVBoxLayout()
        
        query = QLineEdit("IA?")
        layout.addWidget(query)
        self.query = query#access in method
        # TODO:  Add dropdown

        btn = QPushButton("Pick")
        btn.pressed.connect(self.the_button_was_clicked)
        layout.addWidget(btn)
        
        output = QPlainTextEdit("Selection here")
        layout.addWidget(output)
        self.output = output#access in method

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def the_button_was_clicked(self):
        topic = self.query.text()
        print(f"Topic: {topic}")
        #self.output.setPlainText(topic)#testing

        ## STUB:  not right for selecting
        selections = []
        for i in range(3):
            book = choice(["Git Book", "Exploring Raspberry Pi"])
            page = randint(1, 100)
            selections.append(f"{book} page {page}")
            
        self.output.setPlainText("\n".join(selections))

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
