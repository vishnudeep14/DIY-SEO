from PyQt5.QtWidgets import *
import sys
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow (QMainWindow):
    def __init__(self):

        super(MainWindow, self).__init__ ()
        self.showMaximized ()
        self.browser = QWebEngineView ()
        self.browser.setUrl (QUrl ("http://google.com"))
        self.setCentralWidget (self.browser)
        self.showMaximized ()
        navibar = QToolBar()
        self.addToolBar(navibar)

        back_btn=QAction('<--',self)
        back_btn.triggered.connect(self.browser.back)
        navibar.addAction(back_btn)

        forw_btn = QAction ('-->', self)
        forw_btn.triggered.connect (self.browser.forward)
        navibar.addAction (forw_btn)

        refbtn=QAction('Refresh',self)
        refbtn.triggered.connect(self.browser.reload)
        navibar.addAction(refbtn)

        hombtn = QAction ('Home', self)
        hombtn.triggered.connect (self.navigate_home)
        navibar.addAction (hombtn)

        self.url_bar=QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_url)
        navibar.addWidget(self.url_bar)





    def navigate_home(self):
        self.browser.setUrl (QUrl("http://google.com"))



    def navigate_url(self):
        url=self.url_bar.text()
        self.browser.setUrl(QUrl(url))



app = QApplication(sys.argv)
QApplication.setApplicationName('ANTARJALA')
window=MainWindow()
app.exec_()
