from IPython.display import display
import pyautogui as py
import time as t
import pandas as pd


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

def left_f(i):    
    count = 0
    while count < i:        
        py.press('left')
        #t.sleep(pausa)
        count += 1

#Também não sei como nomear estes
def enter_f(i):    
    count = 0
    while count < i:        
        py.press('enter')
        t.sleep(pausa)
        count += 1

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
def tab_f(i):
    count = 0
    while count < i:        
        py.press('tab')
        #t.sleep(pausa)
        count += 1

def esc_f():
    py.press('esc')
    t.sleep(pausa)

def f9_f():
    py.press('f9')
    t.sleep(pausa)

insertType = str(input('C p/aquisição ou S p/servico: '))

tabela = pd.read_excel("REGISTERED.xlsx", sheet_name=f"{insertType}")

t.sleep(5)

for i, cod_item in enumerate(tabela["COD"]):
    #subgroup = tabela.loc[i, "SUBGROUP"]
    #unit = tabela.loc[i, "UNIDADE"]
    quantitative = tabela.loc[i, "QUANTITATIVO"]
    
    p_f()
    t.sleep(1)
    c_f()
    t.sleep(1)
    py.write(str(cod_item))
    enter_f(2)
    py.write(str(quantitative))
    t.sleep(1)
    enter_f(3)
    t.sleep(1)