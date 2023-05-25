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
def a_f():
    py.press('a')
    t.sleep(pausa)

def b_f():
    py.press('b')
    t.sleep(pausa)

def c_f():
    py.press('c')
    t.sleep(pausa)

def d_f():
    py.press('d')
    t.sleep(pausa)

def e_f():
    py.press('e')
    t.sleep(pausa)

def f_f():
    py.press('f')
    t.sleep(pausa)

def g_f():
    py.press('g')
    t.sleep(pausa)

def h_f():
    py.press('h')
    t.sleep(pausa)

def i_f():
    py.press('i')
    t.sleep(pausa)

def j_f():
    py.press('j')
    t.sleep(pausa)

def k_f():
    py.press('k')
    t.sleep(pausa)

def l_f():
    py.press('l')
    t.sleep(pausa)

def m_f():
    py.press('m')
    t.sleep(pausa)

def n_f():
    py.press('n')
    t.sleep(pausa)

def o_f():
    py.press('o')
    t.sleep(pausa)

def p_f():
    py.press('p')
    t.sleep(pausa)

def q_f():
    py.press('q')
    t.sleep(pausa)

def r_f():
    py.press('r')
    t.sleep(pausa)

def s_f():
    py.press('s')
    t.sleep(pausa)

def t_f():
    py.press('t')
    t.sleep(pausa)

def u_f():
    py.press('u')
    t.sleep(pausa)

def v_f():
    py.press('v')
    t.sleep(pausa)

def w_f():
    py.press('w')
    t.sleep(pausa)

def x_f():
    py.press('x')
    t.sleep(pausa)

def y_f():
    py.press('y')
    t.sleep(pausa)

def z_f():
    py.press('z')
    t.sleep(pausa)

#Não sei o nome desses botões
def up_f():
    py.press('up')
    #t.sleep(pausa)    

def right_f():
    py.press('right')
    #t.sleep(pausa)

def down_f(i):
    count = 0
    while count < i:        
        py.press('down')
        #t.sleep(pausa)
        count += 1

def left_f():
    py.press('left')
    #t.sleep(pausa)

#Também não sei como nomear estes
def enter_f():
    py.press('enter')
    t.sleep(pausa)

def pgdown_f(i):    
    count = 0
    while count < i:        
        py.press('pagedown')
        #t.sleep(pausa)
        count += 1

def pgup_f():
    py.press('pageup')
    t.sleep(pausa)

def home_f():
    py.press('home')
    t.sleep(pausa)

def end_f():
    py.press('end')
    t.sleep(pausa)

def delete_f(i):
    count = 0
    while count < i:        
        py.press('delete')
        #t.sleep(pausa)
        count += 1    


#Muito menos estes
def tab_f():
    py.press('tab')
    t.sleep(pausa)

def esc_f():
    py.press('esc')
    t.sleep(pausa)

def f9_f():
    py.press('f9')
    t.sleep(pausa)

#Comandos
def copy_f():
    py.keyDown('ctrl')
    py.press('c')
    py.keyUp('ctrl')
    t.sleep(pausa)

def past_f():
    py.keyDown('ctrl')
    py.press('v')
    py.keyUp('ctrl')
    t.sleep(pausa)

def altern_f():
    py.keyDown('alt')
    py.press('tab')
    py.keyUp('alt')
    t.sleep(pausa)


#Funções
def saveContract():
    for i in range(1):        
        d_f()
        #enter_f()
        t.sleep(10)
        r_f()
        down_f(1)
        enter_f()
        t.sleep(3)
        down_f(1)
        down_f(1)
        enter_f()
        down_f(1)
        t_f()
        pgdown_f(4)        
        down_f(7)        
        delete_f(19)
        t.sleep(1)        
        past_f()
        t.sleep(1)
        py.click(x= 322, y= 103)#Arquivo
        py.click(x= 299, y= 127)#Salvar
        py.click(x= 834, y= 456)#ASPEC
        t.sleep(1)
        esc_f()
        t.sleep(1)
        l_f()
        enter_f()
        enter_f()
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
        esc_f()
    return i

t.sleep(3)
py.click(x= 1488, y= 321)#ASPEC0

saveContract()
down_f(5)
saveContract()
down_f(5)
saveContract()
down_f(5)
saveContract()
down_f(7)
saveContract()
down_f(4)
saveContract()
down_f(4)
saveContract()
down_f(4)
saveContract()
down_f(4)
saveContract()
down_f(5)
saveContract()
down_f(4)