import SSASGui
import SICConvert
import registerExecute

class Table():
    def __init__(self,state,Obcode_list,SymbolTable):
        self.opcode_list= Obcode_list[1:]
        self.SymbolTable=SymbolTable
        self.A = 0
        self.X = 0
        self.L = 0
        self.PC = self.opcode_list[0][0]
        self.SW = 0
        self.count = 0
        self.state=state #현재 주소 저장

    def execute(self):
        #print(self.register.A,self.register.X,self.register.L,self.register.PC,self.register.SW)
        k=0
        while(True):
            print(k)
            if self.PC==self.state:
                break
            for i,x in enumerate(self.opcode_list):
                if self.PC==x[0]: #해당 주소로 가서 명령어 넘겨주기
                    print(x[2], x[3])
                    if "," in x[3]:
                        s=x[3].split(","[0])
                        print(s)
                        self.find(x[2],s[0])
                    else:
                        self.find(x[2],x[3])
                    print("됐다")
                    print(self.A,self.X,self.L,self.PC,self.SW)
                    print()
                    break
            k+=1


    def getAddress(self,symbol):
        for i in self.SymbolTable:
            if symbol==i[0]:
                return i[1]

    def getValue(self,symbol):
        for i in self.SymbolTable:
            if symbol==i[0]:
                return i[-1]


    def getNextAddress(self, currentAddress):  # PC 변경
        for i, x in enumerate(self.opcode_list):
            if currentAddress == x[0]:
                return self.opcode_list[i + 1][0]

    def find(self, ins, m):

        if ins == "ADD":
            self.ADD(m)
        elif ins == "AND":
            self.AND(m)
        elif ins == "COMP":
            self.COMP(m)
        elif ins == "DIV":
            self.DIV(m)
        elif ins == "J":
            self.J(m)
        elif ins == "JEQ":
            self.JEQ(m)
        elif ins == "JGT":
            self.JGT(m)
        elif ins == "JLT":
            self.JLT(m)
        elif ins == "JSUB":
            self.JSUB(m)
        elif ins == "LDA":
            self.LDA(m)
        elif ins == "LDCH":
            self.LDCH(m)
        elif ins == "LDL":
            self.LDL(m)
        elif ins == "LDX":
            self.LDX(m)
        elif ins == "MUL":
            self.MUL(m)
        elif ins == "OR":
            self.OR(m)
        elif ins == "RD":
            self.RD(m)
        elif ins == "RSUB":
            self.RSUB(m)
        elif ins == "STA":
            self.STA(m)
        elif ins == "STCH":
            self.STCH(m)
        elif ins == "STL":
            self.STL(m)
        elif ins == "STSW":
            self.STSW(m)
        elif ins == "STX":
            self.STX(m)
        elif ins == "SUB":
            self.SUB(m)
        elif ins == "TD":
            self.TD(m)
        elif ins == "TIX":
            self.TIX(m)
        elif ins == "WD":
            self.WD(m)

    def ADD(self, m):
        self.A += m
        self.PC = self.getNextAddress(self.PC)

    def AND(self, m): #구현안했음
        print("AND")
        self.PC = self.getNextAddress(self.PC)

    def COMP(self, m):
        self.PC = self.getNextAddress(self.PC)
        if int(self.A) > int(self.getValue(m)):
            print("크다")
            self.SW = ">"
        elif int(self.A) < int(self.getValue(m)):
            print("작다")
            self.SW = "<"
        elif int(self.A)==int(self.getValue(m)):
            self.SW = "="
            print("같다")

    def DIV(self, m):
        self.PC = self.getNextAddress(self.PC)
        if m[0]=="#":
            m=m[1:]
            m=int(m)
            self.A/=m
        else:
            self.A /= self.getValue(m)

    def J(self, m):
        self.PC = self.getAddress(m)

    def JEQ(self, m):
        if self.SW == "=":
            self.PC = self.getAddress(m)
        else:
            self.PC=self.getNextAddress(self.PC)

    def JGT(self, m):
        if self.SW == ">":
            self.PC = self.getAddress(m)
        else:
            self.PC=self.getNextAddress(self.PC)

    def JLT(self, m):
        if self.SW == "<":
            self.PC = self.getAddress(m)
        else:
            self.PC=self.getNextAddress(self.PC)

    def JSUB(self, m):
        self.L = self.getNextAddress(self.PC)
        self.PC = self.getAddress(m)

    def LDA(self, m):
        self.PC = self.getNextAddress(self.PC)
        self.A = self.getValue(m)


    def LDCH(self, m):
        self.PC = self.getNextAddress(self.PC)
        print("LDCH")

    def LDL(self, m):
        self.PC = self.getNextAddress(self.PC)
        self.L = self.getValue(m)

    def LDX(self, m):
        self.PC = self.getNextAddress(self.PC)
        self.X = int(self.getValue(m))

    def MUL(self, m):
        self.PC = self.getNextAddress(self.PC)
        self.A *= self.getValue(m)

    def OR(self, m): #구현안했음
        self.PC = self.getNextAddress(self.PC)
        print("OR")

    def RD(self, m):
        self.PC = self.getNextAddress(self.PC)
        print("RD")

    def RSUB(self, m):
        self.PC = self.L

    def STA(self, m):
        self.PC = self.getNextAddress(self.PC)
        for i, x in enumerate(self.opcode_list):
            if m == x[1]:
                self.opcode_list[i][3] = self.A
                for j, y in enumerate(self.SymbolTable):
                    if m == y[0]:
                        if len(y) == 3:
                            self.SymbolTable[j].append(self.A)
                        else:
                            self.SymbolTable[j][-1] = self.A

    def STCH(self, m):
        self.PC = self.getNextAddress(self.PC)
        print("STCH")

    def STL(self, m):
        self.PC = self.getNextAddress(self.PC)
        for i,x in enumerate(self.opcode_list):
            if m==x[1]:
                self.opcode_list[i][3] = self.L
                for j, y in enumerate(self.SymbolTable):
                    if m == y[0]:
                        if len(y) == 3:
                            self.SymbolTable[j].append(self.L)
                        else:
                            self.SymbolTable[j][-1] = self.L

    def STSW(self, m):
        self.PC = self.getNextAddress(self.PC)
        for i,x in enumerate(self.opcode_list):
            if m==x[1]:
                self.opcode_list[i][3]=self.WE

    def STX(self, m):
        self.PC = self.getNextAddress(self.PC)
        for i,x in enumerate(self.opcode_list):
            if m==x[1]:
                self.opcode_list[i][3]=self.X
                print("opcode:",self.opcode_list[i][3])
                for j,y in enumerate(self.SymbolTable):
                    if m==y[0]:
                        if len(y)==3:
                            self.SymbolTable[j].append(self.X)
                        else:
                            self.SymbolTable[j][-1]=self.X
                    print("symbol:",self.SymbolTable[j])

    def SUB(self, m):
        self.PC = self.getNextAddress(self.PC)
        self.A -= int(self.getValue(m))

    def TD(self, m):
        self.PC = self.getNextAddress(self.PC)
        self.SW="<"
        print("뭔지 모르겠다")

    def TIX(self, m):
        self.PC = self.getNextAddress(self.PC)
        self.X+=1
        if self.X > int(self.getValue(m)):
            self.SW = ">"
        elif self.X < int(self.getValue(m)):
            self.SW = "<"
        else:
            self.SW = "="


    def WD(self, m):
        self.PC = self.getNextAddress(self.PC)
        print("WD")