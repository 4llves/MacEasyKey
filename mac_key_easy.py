import pyautogui as py
import time as t


print('\n**************MacEasyKey**************'
      '\n*****Software em Teste Versão 0.5*****'
      '\n*******Desenvolvido por: 4llves*******'
      '\n**************MacEasyKey**************'
      )
print('')

pausa = float(1)

#Letras
def aF():
    py.press('a')
    t.sleep(pausa)

def bF():
    py.press('b')
    t.sleep(pausa)

def cF():
    py.press('c')
    t.sleep(pausa)

def dF():
    py.press('d')
    t.sleep(pausa)

def eF():
    py.press('e')
    t.sleep(pausa)

def fF():
    py.press('f')
    t.sleep(pausa)

def gF():
    py.press('g')
    t.sleep(pausa)

def hF():
    py.press('h')
    t.sleep(pausa)

def iF():
    py.press('i')
    t.sleep(pausa)

def jF():
    py.press('j')
    t.sleep(pausa)

def kF():
    py.press('k')
    t.sleep(pausa)

def lF():
    py.press('l')
    t.sleep(pausa)

def mF():
    py.press('m')
    t.sleep(pausa)

def nF():
    py.press('n')
    t.sleep(pausa)

def oF():
    py.press('o')
    t.sleep(pausa)

def pF():
    py.press('p')
    t.sleep(pausa)

def qF():
    py.press('q')
    t.sleep(pausa)

def rF():
    py.press('r')
    t.sleep(pausa)

def sF():
    py.press('s')
    t.sleep(pausa)

def tF():
    py.press('t')
    t.sleep(pausa)

def uF():
    py.press('u')
    t.sleep(pausa)

def vF():
    py.press('v')
    t.sleep(pausa)

def wF():
    py.press('w')
    t.sleep(pausa)

def xF():
    py.press('x')
    t.sleep(pausa)

def yF():
    py.press('y')
    t.sleep(pausa)

def zF():
    py.press('z')
    t.sleep(pausa)

#Não sei o nome desses botões
def upF():
    py.press('up')
    #t.sleep(pausa)    

def rightF():
    py.press('right')
    #t.sleep(pausa)

def downF(i):
    count = 0
    while count < i:        
        py.press('down')
        #t.sleep(pausa)
        count += 1

def leftF():
    py.press('left')
    #t.sleep(pausa)

#Também não sei como nomear estes
def enterF():
    py.press('enter')
    t.sleep(pausa)

def pgdownF(i):    
    count = 0
    while count < i:        
        py.press('pagedown')
        #t.sleep(pausa)
        count += 1

def pgupF():
    py.press('pageup')
    t.sleep(pausa)

def homeF():
    py.press('home')
    t.sleep(pausa)

def endF():
    py.press('end')
    t.sleep(pausa)

def deleteF(i):
    count = 0
    while count < i:        
        py.press('delete')
        #t.sleep(pausa)
        count += 1    


#Muito menos estes
def tabF():
    py.press('tab')
    t.sleep(pausa)

def escF():
    py.press('esc')
    t.sleep(pausa)

def f9F():
    py.press('f9')
    t.sleep(pausa)

#Comandos
def copyF():
    py.keyDown('ctrl')
    py.press('c')
    py.keyUp('ctrl')
    t.sleep(pausa)

def pastF():
    py.keyDown('ctrl')
    py.press('v')
    py.keyUp('ctrl')
    t.sleep(pausa)

def alternF():
    py.keyDown('alt')
    py.press('tab')
    py.keyUp('alt')
    t.sleep(pausa)


#Funções
def saveContract():
    for i in range(1):        
        dF()
        #enterF()
        t.sleep(10)
        rF()
        downF(1)
        enterF()
        t.sleep(3)
        downF(1)
        downF(1)
        enterF()
        downF(1)
        tF()
        pgdownF(4)        
        downF(7)        
        deleteF(19)
        t.sleep(1)        
        pastF()
        t.sleep(1)
        py.click(x= 322, y= 103)#Arquivo
        py.click(x= 299, y= 127)#Salvar
        py.click(x= 834, y= 456)#ASPEC
        t.sleep(1)
        escF()
        t.sleep(1)
        lF()
        enterF()
        enterF()
        t.sleep(5)
        py.click(x= 396, y= 54)#PDF
        t.sleep(5)
        py.click(x= 1095, y= 560)#Confirmar
        t.sleep(1)
        py.click(x= 790, y= 430)#Sobrescrever
        t.sleep(2)
        py.click(x= 1579, y= 64)#Sair
        t.sleep(3)
        py.click(x= 839, y= 363)#ASPEC2
        t.sleep(1)
        escF()
    return i


#quant = int(input('insira quantidade de itens: '))
#cod = int(input('insira codigo subgrupo: '))
t.sleep(3)

py.click(x= 1488, y= 321)#ASPEC0

saveContract()
downF(5)
saveContract()
downF(5)
saveContract()
downF(5)
saveContract()
downF(7)
saveContract()
downF(4)
saveContract()
downF(4)
saveContract()
downF(4)
saveContract()
downF(4)
saveContract()
downF(5)
saveContract()
downF(4)