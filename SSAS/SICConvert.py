
def preProcess(input):
    global RES
    RES = [0]
    '''
        preProcess(): 데이터 로딩 & 스플릿
        리스트에 명령어 형식에 맞추어서 저장
        리스트 저장 형식 : [라벨, 명령어, 오퍼랜드]
    '''
    saveList = []
    for fp in input:
        r = fp.split()
        if len(r) <= 2:
            r = [""] + r

        if r[1] == "RSUB":
            r = r + [""]
        saveList += [r]

    for i in range(len(saveList)):
        if saveList[i][1] == 'RESW':
            RES.append(int(saveList[i][2]) * 3)
        if saveList[i][1] == 'RESB':
            RES.append(int(saveList[i][2]))

    return saveList

def get_Address(inputaddr):
    '''
    :param inputaddr: preProcess()를 거쳐서 나온 리스트에 저장된 명령어들
    :return: 주소처리 된 명령어 셋(주소, 라벨, 명령어, 오퍼랜드)
    '''
    returnList = []
    SymbolTable = []
    startAddress = "0"
    programName="N"
    t = inputaddr[0]
    if t[1] == "START": # Start Case
        programName = t[0]
        startAddress = t[2]
    # 16진수 1000 -> 10진수 ????
    # int(A, 16): 16진수 A를 10진수로. ex) "A" -> 10
    Addr = int(startAddress, 16) # Start Address
    for text in inputaddr:
        q = hex(Addr)[2:] # 16진수 변환 & 슬라이싱
        text = [q] + text
        returnList += [text]
        if text[1] != "":
            temp = []
            temp += [text[1]]
            temp += [q]
            SymbolTable += [temp]

        if text[2] == "START":
            pass
        elif text[2] == "RESB":
            Addr += int(text[3])
            SymbolTable[-1]+=[text[2]]
        elif text[2] == "RESW":
            r = int(text[3])
            Addr += (r * 3)
            SymbolTable[-1]+=[text[2]]

        elif text[2] == "BYTE":
            if text[3].find("C") != -1:  # Character Case
                lens = len(text[3]) - 3
                Addr += lens
            elif text[3].find("B") != -1:  # Byte Case
                lens = len(text[3]) - 3
                lens = lens // 2
                Addr += lens
            else:
                Addr += 1
            SymbolTable[-1]+=[text[2]]
            SymbolTable[-1]+=[text[3]]

        elif text[2] == "WORD":
            Addr += 3
            SymbolTable[-1]+=[text[2]]
            SymbolTable[-1]+=[text[3]]
        elif text[2] == "END":
            pass
        else:
            Addr += 3

    progSize = Addr - int(startAddress, 16)
    endAddress = hex(Addr)[2:]
    return returnList, startAddress, SymbolTable, progSize, endAddress, programName

def find_Operand(Symbol, SymbolTable):
    '''
        Symbol Table에서 특정 Symbol 찾는 Function
    '''

    for items in SymbolTable:
        if items[0] == Symbol:
            return items[1]

    return -1

def get_Ascii(inputStr):
    '''
        inputStr의 문자열을 해당하는 아스키코드로 변경
        EOF -> 454F46 이런식으로 변환할 때 사용하는 함수.
        BYTE에서 C"" 처리시 사용
    '''

    p = ""
    for s in inputStr:
        t = ord(s)
        q = hex(t)[2:]
        p += q

    return p


def create_ObjCode(mList, SymbolTable):
    '''
    create_ObjCode : 오브젝트 코드를 생성하는 함수
    (주소, 라벨, 명령어, 오퍼랜드, 오브젝트코드)

    :param mList: 위 get_Address까지 거쳐서 나온 주소처리 된 명령어들
    :param SymbolTable: 위 get_Address를 통해 나온 SymbolTable
    :return: Object Code를 포함한 List
    '''

    Opcode = {"ADD":"18", "ADDF":"58", "ADDR":"90", "AND":"40", "CLEAR":"B4",
              "COMP":"28", "COMPF":"88","COMPR":"A0","DIV":"24","DIVF":"64","DIVR":"9C",
              "J":"3C", "JEQ":"30", "JGT":"34", "JLT":"38","LDF":"70","LDS":"6C","LDT":"74",
              "FIX":"C4","FLOAT":"C0","HIO":"F4","JSUB":"48", "LDA":"00", "LDB":"68","LDCH":"50", "LDL":"08",
              "LDX":"04", "MUL":"20", "OR":"44", "RD":"D8","LPS":"D0","MULF":"60","MULR":"98",
              "RSUB":"4C", "STA":"0C", "STB":"78","STCH":"54", "STL":"14","NORM":"C8","RMO":"AC","SIO":"F0","SSK":"EC",
              "STSW":"E8", "STF":"80","STI":"D4","STX":"10", "SUB":"1C", "TD":"E0","SHIFTL":"A4","SHIFTR":"A8","STS":"7C","STT":"84",
              "TIX":"2C", "TIO":"F8","TIXR":"B8","WD": "DC","SUBF":"5C","SUBR":"94","SVC":"B0"}

    returnList = []
    i=0
    for item in mList:
        if item[2] == "START" or item[2] == "END" or item[2] == "RESB" or item[2] == "RESW":
            returnList += [item + [""]]

        elif item[2] == "BYTE":
            if item[3].find("X") != -1:
                returnList += [item + [item[3][2:-1]]] # X와 " 사이의 값만
            elif item[3].find("C") != -1:
                operand_Chr = item[3][2:-1] # C와 " 사이의 값 + 아스키코드 변환
                q = get_Ascii(operand_Chr)
                returnList += [item + [q]]

        elif item[2] == "WORD":
            p = hex(int(item[3]))[2:].zfill(6)
            returnList += [item + [p]]
        elif item[2] == "RSUB":
            returnList += [item + ["4C0000"]]
        else:
            idx_mode = 0
            Op_code = Opcode[item[2]]
            opr = ""

            if item[3].find(",") != -1: # index Addressing 처리
                opr = item[3][:-2]
                idx_mode = 1
            else:
                opr = item[3]
            if opr[0]=="#":
                Op_Addr=format(int(''.join(opr[1:])),'x')
            else:
                Op_Addr = find_Operand(opr, SymbolTable) # 이부분 상수부분도 처리하도록 수정해야함.
                Op_Addr = chr(ord(Op_Addr[0]) + 8) + Op_Addr[1:] if idx_mode == 1 else Op_Addr
            try:
                Op_Sumation = Op_code + Op_Addr
            except:
                print(item)

            returnList += [item + [Op_Sumation]]
            i+=1

    return returnList

def create_ObjFile(oplist, startAddr, ProgName, progSize):
    '''
    :param oplist: Object code가 있는 list
    :return: Object Program Array
    '''
    Address = None
    item_index = 0
    count = 0
    ObjectCode = []
    H_record = "H^"+ProgName+"^"+startAddr.zfill(6)+"^"+hex(progSize)[2:].zfill(6)
    T_rcdarr = []
    for i in range(1, len(oplist)-1, 10):
        if i + 10 > len(oplist)-1:
            temp = oplist[i:len(oplist)-1]
            start = oplist[i][0]
            end = oplist[len(oplist)-1][0]
        else:
            temp = oplist[i:i+10]
            start = oplist[i][0]
            end = oplist[i+10][0]

        Object_Code = list(map(lambda x:x[4], temp))
        Obcode = '^'.join(Object_Code)
        size = hex(int(end, 16) - int(start, 16))[2:]
        if i <= len(oplist)-len(oplist)%10:
            for j in range(0, 10):
                if oplist[(i + j)][2] == 'RESB' or oplist[(i + j)][2] == 'RESW':
                    count += 1
                    size = hex(int(size, 16) - int(RES[count]))[2:]
        else:
            for j in range(0, len(oplist) % 10 - 1):
                if oplist[(i + j)][2] == 'RESB' or oplist[(i + j)][2] == 'RESW':
                    count += 1
                    size = hex(int(size, 16) - int(RES[count]))[2:]



        H_temp = "T^"+start.zfill(6)+"^"+size.zfill(2)+"^"+Obcode
        T_rcdarr += [H_temp]

    E_record = "E^"+startAddr.zfill(6)

    ObjectCode += [H_record]
    ObjectCode += T_rcdarr
    ObjectCode += [E_record]

    return ObjectCode