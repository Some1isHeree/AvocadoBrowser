from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
import os
import sys


class MyWebBrowser(QMainWindow):

    def __init__(self):
        self.window = QWidget()
        self.window.setWindowTitle("Avocado Browser (v1.0)")

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.back_btn = QPushButton("<")
        self.back_btn.setMaximumHeight(25)
        self.url_bar = QTextEdit()
        self.url_bar.setMaximumHeight(25)
        self.go_btn = QPushButton("Search")
        self.go_btn.setMaximumHeight(25)
        self.forward_btn = QPushButton(">")
        self.forward_btn.setMaximumHeight(25)
        self.home_btn = QPushButton("Home")
        self.home_btn.setMaximumHeight(25)
        self.new_btn = QPushButton("New Window")
        self.new_btn.setMaximumHeight(25)

        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_btn)
        self.horizontal.addWidget(self.back_btn)   
        self.horizontal.addWidget(self.forward_btn)
        self.horizontal.addWidget(self.home_btn)
        self.horizontal.addWidget(self.new_btn)

        self.browser = QWebEngineView()

        self.go_btn.clicked.connect(lambda: self.navigate(self.url_bar.toPlainText()))
        self.back_btn.clicked.connect(self.browser.back)
        self.forward_btn.clicked.connect(self.browser.forward)
        self.home_btn.clicked.connect(self.navhome)
        self.new_btn.clicked.connect(self.newein)

        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)
        self.browser.setUrl(QUrl("http://bing.com"))
        self.window.setLayout(self.layout)
        self.window.show()

    def navigate(self, url):
        if not url.startswith("http://"):
            url = "http://" + url
            self.url_bar.setText(url)
        self.browser.setUrl(QUrl(url))

    def navhome(self):
        self.browser.setUrl(QUrl("http://bing.com"))
        url = "http://"

    def newein(self):
        cwd = os.getcwd()
        print(cwd)
        os.startfile("main.py") 


app = QApplication([])
window = MyWebBrowser()
app.exec_()

