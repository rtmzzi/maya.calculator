import maya.cmds as cmds
import maya.mel as mel
from functools import partial

### MAYA CALCULATER PYTHON
### SCPIPT BY RAFAEL TOMAZZI 2024
    
def click(value, *args):
    current_text = cmds.textField('resultField', query=True, text=True)
    cmds.textField('resultField', edit=True, text=current_text + str(value))

def limpar(*args):
        cmds.textField('resultField', edit=True, text="")
    
def igual(*args):
    expression = cmds.textField('resultField', query=True, text=True)
    resultado = eval(expression)
    cmds.textField('resultField', edit=True, text=resultado)


    
window = cmds.window(title="Calculator",sizeable=False, widthHeight=(185,295))

form = cmds.formLayout(numberOfDivisions=100)
btnDisplay = cmds.textField('resultField', en=False, height=60, width=175)
btnAC = cmds.button(label="A/C", height=40, width=40, command=partial(limpar))
btnPorcent = cmds.button(label="%", height=40, width=40, command=partial(click, "%"))
btnMultiply = cmds.button(label="x", height=40, width=40, command=partial(click, "*"))
btnDivide = cmds.button(label="/", height=40, width=40, command=partial(click, "/"))
btnMais = cmds.button(label="+", height=40, width=40, command=partial(click, "+"))
btnMenos = cmds.button(label="-", height=40, width=40, command=partial(click, "-"))
btnIgual = cmds.button(label="=", height=85, width=40, command=partial(igual))
btn1 = cmds.button(label="1", command=partial(click, "1"), height=40, width=40)
btn2 = cmds.button(label="2", command=partial(click, "2"), height=40, width=40)
btn3 = cmds.button(label="3", command=partial(click, "3"), height=40, width=40)
btn4 = cmds.button(label="4", command=partial(click, "4"), height=40, width=40)
btn5 = cmds.button(label="5", command=partial(click, "5"), height=40, width=40)
btn6 = cmds.button(label="6", command=partial(click, "6"), height=40, width=40)
btn7 = cmds.button(label="7", command=partial(click, "7"), height=40, width=40)
btn8 = cmds.button(label="8", command=partial(click, "8"), height=40, width=40)
btn9 = cmds.button(label="9", command=partial(click, "9"), height=40, width=40)
btn0 = cmds.button(label="0", command=partial(click, "0"), height=40, width=130)


cmds.formLayout(form, edit=True, attachForm = [
(btnDisplay,"top",5), 
(btnDisplay,"left",5),
(btnAC,"left",5),
(btn1,"left",5),
(btn4,"left",5),
(btn7,"left",5),
(btn0,"left",5)],


attachControl=[
(btnAC,"top",5,btnDisplay),
(btnPorcent,"top",5,btnDisplay),
(btnPorcent,"left",5,btnAC),

(btnMultiply, "left",5, btnPorcent),
(btnMultiply, "top", 5, btnDisplay),
(btnDivide, "left", 5, btnMultiply),
(btnDivide, "top", 5, btnDisplay),

(btnMenos, "left", 5, btn3),
(btnMenos, "top", 5, btnDivide),

(btnMais, "left", 5, btn6),
(btnMais, "top", 5, btnMenos),

(btn1,"top",5,btnAC),
(btn2,"left",5,btn1),
(btn2,"top",5,btnPorcent),
(btn3,"left",5,btn2),
(btn3,"top",5,btnPorcent),
(btn4,"top",5,btn1),
(btn5,"top",5,btn2),
(btn5,"left",5,btn1),
(btn6,"top",5,btn3),
(btn6,"left",5,btn2),
(btn7,"top",5,btn5),
(btn8,"top",5,btn6),
(btn8,"left",5,btn7),

(btn9,"left",5,btn8),
(btn9,"top",5,btn6),
(btn0,"top",5,btn7),
(btnIgual,"left",5,btn0),
(btnIgual,"top",5,btn6)]


)

cmds.showWindow(window)


