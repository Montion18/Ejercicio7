class Hora:
    __hora=''
    __min=''
    __seg=''

    def __init__(self,h,m,s):
        self.__hora=h
        self.__min=m
        self.__seg=s

    def Mostrar(self):
        print("Hora: {} Min: {} Seg: {} \n".format(self.__hora,self.__min,self.__seg))
    def geth(self):
        return self.__hora
    def getm(self):
        return self.__min
    def gets(self):
        return self.__seg
    

