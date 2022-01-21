# -*- coding: utf-8 -*-
import sys
from PySide.QtCore import *
from PySide.QtGui import *
import urllib2
import re
#import threading
#from BeautifulSoup import BeautifulSoup

class Dialog(QDialog):
    def __init__(self,parent=None,):
        super(Dialog,self).__init__(parent)
        self.setWindowTitle(u"词典")
        self.browser=QTextBrowser()
        self.edit=QLineEdit(u"输入单词")
        self.browser.setText("QtSharp's Toy")

        quitbutton=QPushButton(u'退出')
        quitbutton.clicked.connect(app.quit)
        searchbutton=QPushButton(u'查询')
        searchbutton.clicked.connect(self.sendword)

        layout=QVBoxLayout()
        layout.addWidget(searchbutton)
        layout.addWidget(self.edit)
        layout.addWidget(quitbutton)
        layout.addWidget(self.browser)
        self.setLayout(layout)

    def sendword(self):
        word=self.edit.text()
        self.sendsignal.emit(word)

    sendsignal=Signal(str)
    @Slot(str)
    def getexp(self,exp):
        self.browser.setText(exp)


class Search(QThread):
        def __init__(self,parent=None,):
            super(Search,self).__init__(parent)

        def run(self):
            wordweb=urllib2.urlopen("http://dict.baidu.com/s?wd=%s"% self.word)
            charset = wordweb.headers['Content-Type'].split(' charset=')[0].lower()
            soup=BeautifulSoup(wordweb,fromEncoding=charset)
            exp=soup.findAll(text=re.compile(u'译典通'))[0].parent.parent.parent.parent
            exp=str(exp).decode('utf8')
            self.exped.emit(exp)

        exped=Signal(str)
        @Slot(str)
        def getword(self,word):
            self.word=word
            self.run()


if __name__=='__main__':

    app=QApplication(sys.argv)
    dialog=Dialog()
    search=Search()
    dialog.sendsignal.connect(search.getword)
    search.exped.connect(dialog.getexp)
    dialog.show()

    sys.exit(app.exec_())