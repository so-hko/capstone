import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from SICConvert import *
from PyQt5.QtGui import *###
from registerManage import *
import registerManage
import registerExecute


form_class = uic.loadUiType("SIC_UI.ui")[0]
form_class_logo = uic.loadUiType("Logo_UI.ui")[0]

# Input받는 TEXT : InputText
# Modify 버튼 : Btn_modify
# Execute 버튼 : Btn_Execute
# Register : Reg_A, Reg_X, Reg_L, Reg_PC, Reg_SW
# 테이블 : HexaTable, BinaryTable, AsciiTable
# Reset Register : Btn_resetR
# Reset Memory : Btn_ResetM
# output : textEdit
# Logo : LogoPicture
# Memory: MemoryTable



output=""
input=""
Obcode_list=[]
SymbolTable=[]


class LogoWindow(QMainWindow, form_class_logo):
    def __init__(self, parent=None):
        super(LogoWindow,self).__init__(parent)
        self.setupUi(self)

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.qPixmapVar = QPixmap()### QPixmap사진 객체 생성
        self.qPixmapVar.load("Logosample.png")###
        self.LogoPicture.setPixmap(self.qPixmapVar)###

        self.Btn_Execute.clicked.connect(self.ExecuteProcess)
        clickable(self.LogoPicture).connect(self.LogoProcess)

        #Memory 클릭했을때
        self.MemoryTable.cellDoubleClicked.connect(self.memorySave)

    def memorySave(self): #memory의 상태를 저장하고, 변경
        clickedInstruction = self.MemoryTable.currentItem().text()
        #print(clickedInstruction)
        clickedInstruction = clickedInstruction.split()
        #print(clickedInstruction)

        for i,x in enumerate(Obcode_list):
            if clickedInstruction[-1]==x[0]:
                state=Obcode_list[i+1][0]
                register=registerManage.Table(state,Obcode_list,SymbolTable)
                #print(register.state)

        register.execute()





    def addInstructionToMemory(self,t):
        k=0
        for i in range(len(t)//8+1):
            for j in range(8):
                if k==len(t):
                    break
                s=QTableWidgetItem(t[k]+" "+Obcode_list[k][0])
                self.MemoryTable.setItem(i,j,s)
                k+=1



    def LogoProcess(self):
        print("새창띄우기")
        self.logoWindow=LogoWindow(self)
        self.logoWindow.show()

    def addTableMember(self, t, oblist):
        self.HexaTable.setRowCount(t.index(t[-1]) + 1)  # HexaTable 최대 Row
        self.HexaTable.setColumnCount(2)

        for i, x in enumerate(oblist):
            P = QTableWidgetItem(t[i])
            Q = QTableWidgetItem(x)
            self.HexaTable.setItem(i, 0, P)
            self.HexaTable.setItem(i, 1, Q)

        self.BinaryTable.setRowCount(t.index(t[-1]) + 1)
        self.BinaryTable.setColumnCount(2)
        for i, x in enumerate(oblist):
            Binary = ""
            if x != '':
                Binary = bin(int(x, 16))[2:].zfill(24)
            P = QTableWidgetItem(t[i])
            Q = QTableWidgetItem(Binary)
            self.BinaryTable.setItem(i, 0, P)
            self.BinaryTable.setItem(i, 1, Q)

        self.AsciiTable.setRowCount(t.index(t[-1]) + 1)
        self.AsciiTable.setColumnCount(2)
        for i, x in enumerate(oblist):
            Ascii = ""
            for k in range(0, len(x), 2):
                Ascii = Ascii + (str(HexaToDec(x[k]) * 16 + HexaToDec(x[k + 1]))).zfill(2)
            P = QTableWidgetItem(t[i])
            Q = QTableWidgetItem(Ascii)
            self.AsciiTable.setItem(i, 0, P)
            print(x)
            self.AsciiTable.setItem(i, 1, Q)


    def ExecuteProcess(self):
        global input
        global output
        global HexaList
        global AsciiList
        global binaryList
        global Obcode_list
        global SymbolTable


        input = self.InputText.toPlainText()  # InputText내용 저장
        if input=="":
            return
        t = input.split("\n")
        t = list(map(lambda x: x.strip(), t))

        myList = preProcess(t)  # 파일 불러오기 / 스플릿
        mList, startAddr, SymbolTable, progSize, endAddress, programName = get_Address(
            myList)  # 불러온 파일에서 시작주소, 주소가 담긴 명령어, 심볼테이블 로딩
        Obcode_list = create_ObjCode(mList, SymbolTable)  # Obcode_list에 Obcode 저장
        Oblist = list(map(lambda x: x[4], Obcode_list))
        print(Oblist)
        #self.addTableMember(t, Oblist)
        ObProg_list = create_ObjFile(Obcode_list, startAddr, programName, progSize)  # Object_Program이 ObProg_list에 저장
        print("SymbolTable:",SymbolTable)
        print("Obcode_list:",Obcode_list)
        output=""
        for i in ObProg_list:
            output += i + "\n"
        self.textEdit.setPlainText(output)

        #memory에 명령어 저장
        self.addInstructionToMemory(t)

def HexaToDec(Hexa):
    if Hexa >= '0' and Hexa <= '9':
        return ord(Hexa) - ord('0')
    if Hexa >= 'A' and Hexa <= 'F':
        return ord(Hexa) - ord('A') + 10
    if Hexa >= 'a' and Hexa <= 'f':
        return ord(Hexa) - ord('a') + 10
    return 0


def clickable(widget):###클릭 불가능한 QObject객체를 클릭가능하게하는 함수
    class Filter(QObject):
        clicked = pyqtSignal()  # pyside2 사용자는 pyqtSignal() -> Signal()로 변경
        def eventFilter(self, obj, event):
            if obj == widget:
                if event.type() == QEvent.MouseButtonRelease:
                    if obj.rect().contains(event.pos()):
                        self.clicked.emit()
                        # The developer can opt for .emit(obj) to get the object within the slot.
                        return True
            return False
    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.clicked



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()