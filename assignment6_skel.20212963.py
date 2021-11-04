import pickle
import sys
import copy
from PyQt5.QtWidgets import (QMainWindow, QWidget, QPushButton,
    QHBoxLayout,  QGridLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB('Name')

    def initUI(self): # 전체적인 UI 입력
        Name = QLabel('Name:')
        Age = QLabel('Age:')
        Score = QLabel('Score:')
        Result = QLabel('Result:')
        Amount = QLabel('Amount:')
        Key = QLabel('Key:')

        self.nameEdit = QLineEdit()
        self.ageEdit = QLineEdit()
        self.scoreEdit = QLineEdit()
        self.resultEdit = QTextEdit()
        self.amountEdit = QLineEdit()

        self.cb = QComboBox(self)
        self.cb.addItem('Name')
        self.cb.addItem('Age')
        self.cb.addItem('Score')
        self.cb.setGeometry(370, 40, 110, 21)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(Name, 1, 0)
        grid.addWidget(self.nameEdit, 1, 1)

        grid.addWidget(Age, 1, 2)
        grid.addWidget(self.ageEdit, 1, 3)

        grid.addWidget(Score, 1, 4)
        grid.addWidget(self.scoreEdit, 1, 5)

        grid.addWidget(Amount, 2, 2)
        grid.addWidget(self.amountEdit, 2, 3)

        grid.addWidget(Key, 2, 4)

        grid.addWidget(Result, 4, 0)
        grid.addWidget(self.resultEdit, 5, 0, 6, 7)

        self.setLayout(grid)

        Add = QPushButton("Add", self)
        grid.addWidget(Add, 3, 1)

        Del = QPushButton("Del", self)
        grid.addWidget(Del, 3, 2)

        Find = QPushButton("Find", self)
        grid.addWidget(Find, 3, 3)

        Inc = QPushButton("Inc", self)
        grid.addWidget(Inc, 3, 4)

        Show = QPushButton("Show", self)
        grid.addWidget(Show, 3, 5)

        Add.clicked.connect(self.buttonClicked)
        Del.clicked.connect(self.buttonClicked)
        Find.clicked.connect(self.buttonClicked)
        Inc.clicked.connect(self.buttonClicked)
        Show.clicked.connect(self.buttonClicked)


        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')    
        self.show()

    def combobox_select(self):
        self.combo_label.setText(self.combo.currentText())
        print(self.combo.currentText())
        print(self.combo.currentIndex()) #key 입력을 위한 콤보박스

    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb = pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self, keyname): #result 칸에 현재 정보 입력
        for p in sorted(self.scoredb, key=lambda person: person[keyname]):
            for attr in sorted(p):
                self.resultEdit.insertPlainText(str(attr) + "=" + str(p[attr]) + "\t\t")
            self.resultEdit.insertPlainText("\n")

    def buttonClicked(self):
        button = self.sender()
        key = button.text()
        showdb = self.cb.currentText()
        N = self.nameEdit.text()
        A = self.ageEdit.text()
        S = self.scoreEdit.text()
        if key == 'Add' and N != "" and A != "" and S != "":
            try:
                record = {'Name': N, 'Age': A, 'Score': S}
                self.scoredb += [record]
                self.resultEdit.clear()
                self.showScoreDB(showdb)
            except:
                self.resultEdit.clear()
                self.showScoreDB(showdb)
        elif key == 'Del':
            try:
                scdb1 = copy.deepcopy(self.scoredb)
                for p in scdb1:
                    if p['Name'] == N:
                        self.scoredb.remove(p)
                self.resultEdit.clear()
                self.showScoreDB(showdb)
            except:
                self.resultEdit.clear()
                self.showScoreDB(showdb)
        elif key == 'Find':
            try:
                for p in self.scoredb:
                    if p['Name'] == N:
                        self.resultEdit.clear()
                        for attr in sorted(p):
                            self.resultEdit.insertPlainText(str(attr) + "=" + str(p[attr]) + "\t\t")
                        self.resultEdit.insertPlainText("\n")
            except:
                self.resultEdit.clear()
                self.showScoreDB(showdb)
        elif key == 'Inc':
            try:
                for p in self.scoredb:
                    if p['Name'] == N and S != '':
                        pscore = int(p['Score'])
                        par = int(S)
                        pscore += par
                        p['Score'] = str(pscore)
                    elif S == '':
                        self.resultEdit.clear()
                        self.showScoreDB(showdb)
                        break
            except:
                self.resultEdit.clear()
                self.showScoreDB(showdb)
        elif key == 'Show':
            self.resultEdit.clear()
            self.showScoreDB(showdb)
        else:
            self.resultEdit.clear()
            self.showScoreDB(showdb)


if __name__ == '__main__':    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())

