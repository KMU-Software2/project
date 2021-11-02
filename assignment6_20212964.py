import pickle
import sys
import copy
from PyQt5.QtWidgets import (QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication, QLabel, QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()
        self.addButton.clicked.connect(self.addScoreDB)
        self.delButton.clicked.connect(self.delScoreDB)
        self.findButton.clicked.connect(self.findScoreDB)
        self.incButton.clicked.connect(self.incScoreDB)
        self.showButton.clicked.connect(self.showScoreDB)

    def initUI(self):
        # Name, Age, Score
        self.name = QLabel('Name:')
        self.age = QLabel('Age:')
        self.score = QLabel('Score:')

        self.nameEdit = QLineEdit()
        self.ageEdit = QLineEdit()
        self.scoreEdit = QLineEdit()

        hbox_1 = QHBoxLayout()
        hbox_1.addWidget(self.name)
        hbox_1.addWidget(self.nameEdit)
        hbox_1.addWidget(self.age)
        hbox_1.addWidget(self.ageEdit)
        hbox_1.addWidget(self.score)
        hbox_1.addWidget(self.scoreEdit)

        # Amount, Key
        self.amount = QLabel('Amount')
        self.amountEdit = QLineEdit()

        self.key = QLabel('Key:')
        self.keyCombo = QComboBox()
        self.keyCombo.addItems(['Name', 'Age', 'Score'])

        hbox_2 = QHBoxLayout()
        hbox_2.addStretch(1)
        hbox_2.addWidget(self.amount)
        hbox_2.addWidget(self.amountEdit)
        hbox_2.addWidget(self.key)
        hbox_2.addWidget(self.keyCombo)

        # Add, Del, Find, Inc, Show
        self.addButton = QPushButton('Add')
        self.delButton = QPushButton('Del')
        self.findButton = QPushButton('Find')
        self.incButton = QPushButton('Inc')
        self.showButton = QPushButton('Show')

        hbox_3 = QHBoxLayout()
        hbox_3.addWidget(self.addButton)
        hbox_3.addWidget(self.delButton)
        hbox_3.addWidget(self.findButton)
        hbox_3.addWidget(self.incButton)
        hbox_3.addWidget(self.showButton)

        # Result
        self.result = QLabel('Result:')
        self.resultEdit = QTextEdit()
        self.resultEdit.setReadOnly(True)

        hbox_4 = QHBoxLayout()
        hbox_4.addWidget(self.result)

        hbox_5 = QHBoxLayout()
        hbox_5.addWidget(self.resultEdit)

        # 최종 설정
        vbox = QVBoxLayout()
        vbox.addLayout(hbox_1)
        vbox.addLayout(hbox_2)
        vbox.addLayout(hbox_3)
        vbox.addLayout(hbox_4)
        vbox.addLayout(hbox_5)

        self.setLayout(vbox)
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')    
        self.show()



    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError:
            self.scoredb = []
            return

        self.scoredb = pickle.load(fH)

        fH.close()

    # write the data into person db
    def addScoreDB(self):
        if self.nameEdit.text() == "" or self.ageEdit.text() == "" or self.scoreEdit.text() == "":
            return
        record = {'Name': self.nameEdit.text(), 'Age': int(self.ageEdit.text()), 'Score': int(self.scoreEdit.text())}
        self.scoredb += [record]
        self.scoredb.sort(key=lambda person: person[self.keyCombo.currentText()])
        self.showScoreDB()
        self.writeScoreDB()

    def delScoreDB(self):
        scoredb_copy = copy.deepcopy(self.scoredb)
        for p in scoredb_copy:
            if p['Name'] == self.nameEdit.text():
                self.scoredb.remove(p)
        self.showScoreDB()
        self.writeScoreDB()

    def findScoreDB(self):
        self.resultEdit.clear()
        for p in self.scoredb:
            if p['Name'] == self.nameEdit.text():
                for attr in sorted(p):
                    self.resultEdit.insertPlainText(attr + '=' + str(p[attr]) + '   \t')
                self.resultEdit.insertPlainText('\n')
        #self.showScoreDB()
        self.writeSCoreDB()

    def incScoreDB(self):
        for p in self.scoredb:
            if p['Name'] == self.nameEdit.text():
                p['Score'] = str(p['Score'] + int(self.amountEdit.text()))
        self.showScoreDB()
        self.writeScoreDB()

    def showScoreDB(self):
        self.resultEdit.clear()
        self.scoredb.sort(key=lambda person: person[self.keyCombo.currentText()])
        for p in self.scoredb:
            for attr in sorted(p):
                self.resultEdit.insertPlainText(attr + '=' + str(p[attr]) + '   \t')
            self.resultEdit.insertPlainText('\n')

    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def closeEvent(self, event):
        self.writeScoreDB()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())

