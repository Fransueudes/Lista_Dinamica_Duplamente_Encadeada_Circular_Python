

class No():
    def __init__(self, valor, proximo):
        self.info = valor
        self.prox = proximo

class Ldsec():
    def __init__(self):
        self.prim = None
        self.ult = None
        self.quant = 0

    def inserirInicio(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor, self.prim)
        else:
            self.prim = No(valor, self.prim)
            self.ult.prox = self.prim
        self.quant += 1

    def inserirFim(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor, self.prim)
        else:
            self.ult.prox = self.ult = No(valor, self.prim)
            self.ult.prox = self.prim
        self.quant += 1

    '''def removerFim(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            pos = 0
            aux = self.prim
            while self.quant-1 != pos:
                cos = aux
                aux = aux.prox
                pos += 1
            self.ult = cos
            self.ult.prox = self.prim
        self.quant -= 1'''

    def removerFim(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            aux =  self.prim
            while aux.prox != self.ult:
                aux = aux.prox
           
            self.ult = aux
            self.ult.prox = self.prim
        self.quant -= 1
            

    def removerInicio(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.prim = self.prim.prox
            self.ult = self.prim
        self.quant -= 1

    def show(self):
        pos = 0
        aux = self.prim
        while self.quant != pos:
            print(aux.info)
            aux = aux.prox
            pos += 1
     
            
    def inserirAposDet(self, valor1, valor2):
        aux = self.prim
        while aux.info != valor2:
            aux = aux.prox
        aux.prox = No(valor1, aux.prox)
        self.quant += 1
        



