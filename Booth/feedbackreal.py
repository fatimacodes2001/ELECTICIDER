from tkinter import *
from tkinter import Entry
from tkinter.scrolledtext import ScrolledText
from PIL import Image,ImageTk
from tkinter.scrolledtext import ScrolledText
import tkinter.messagebox

var=0
but=0
def submit():
    global result,master
    global feed

    if val=='k':

        feedback=dis2.get('1.0',END)
        file1=open('feedback nathan.txt','a')
        try:
            res='The overall feedback was {}'.format(result)
        except:
            result='None'
            res = 'The overall feedback was {}'.format(result)
        file1.write(res)
        file1.write('\n')
        file1.write(feedback)
        file1.close()
        root.destroy()
        return

    else:

        feedback = dis2.get('1.0',END)

        file2 = open('feedback emma.txt', 'a')
        try:
            res = 'The overall feedback was {}'.format(result)
        except:
            result='None'
            res = 'The overall feedback was {}'.format(result)

        file2.write(res)
        file2.write('\n')
        file2.write(feedback)
        file2.close()
        root.destroy()
        return


def hoveronr1(event):
    while feedback1.get()!="Worst":
        r1.config(fg='#002577',bg='#005AEA')
        rbut1.config(image=radioh,bg='#005AEA')
        return
    while feedback1.get()=="Worst":
        r1.config(fg='#002577',bg='#005AEA')
        rbut1.config(bg='#005AEA')


def clickb1(event):
    feedback1.set("Worst")
    r1.config(bg="#002577",fg='#FFFFFF',activebackground="#002577",activeforeground="#FFFFFF")
    rbut1.config(bg="#002577",image=radioc)
    r2.config(bg='#1745AD', fg='#002577')
    rbut2.config(image=radio1, bg='#1745AD')
    r3.config(bg='#1745AD', fg='#002577')
    rbut3.config(image=radio1, bg='#1745AD')
    r4.config(bg='#1745AD', fg='#002577')
    rbut4.config(image=radio1, bg='#1745AD')
    r5.config(bg='#1745AD', fg='#002577')
    rbut5.config(image=radio1, bg='#1745AD')
    return

def releaseb1(event):
    while feedback1.get()=="Worst":
        r1.config(bg="#1745AD",fg='#FFFFFF',activebackground="#002577",activeforeground="#FFFFFF")
        rbut1.config(bg="#1745AD",image=radiot)
        return

def hoveroffr1(event):
    while feedback1.get()!="Worst":
        r1.config(bg='#1745AD',fg='#002577')
        rbut1.config(image=radio1, bg='#1745AD')
        return
    while feedback1.get()=="Worst":
        r1.config(bg="#002577", fg='#FFFFFF', activebackground="#002577", activeforeground="#FFFFFF")
        rbut1.config(bg="#1745AD", image=radiot)
        return

def hoveronr2(event):
    while feedback1.get()!="Bad":
        r2.config(fg='#002577',bg='#005AEA')
        rbut2.config(image=radioh,bg='#005AEA')
        return
    while feedback1.get()=="Bad":
        r2.config(fg='#002577',bg='#005AEA')
        rbut2.config(bg='#005AEA')
        return

def clickb2(event):
    feedback1.set("Bad")
    r2.config(bg="#002577",fg='#FFFFFF',activebackground="#002577",activeforeground="#FFFFFF")
    rbut2.config(bg="#002577",image=radioc)
    r1.config(bg='#1745AD', fg='#002577')
    rbut1.config(image=radio1, bg='#1745AD')
    r3.config(bg='#1745AD', fg='#002577')
    rbut3.config(image=radio1, bg='#1745AD')
    r4.config(bg='#1745AD', fg='#002577')
    rbut4.config(image=radio1, bg='#1745AD')
    r5.config(bg='#1745AD', fg='#002577')
    rbut5.config(image=radio1, bg='#1745AD')

    return

def releaseb2(event):
    while feedback1.get()=="Bad":
        r2.config(bg="#1745AD",fg='#FFFFFF',activebackground="#002577",activeforeground="#FFFFFF")
        rbut2.config(bg="#1745AD",image=radiot)
        return


def hoveroffr2(event):
    while feedback1.get()!="Bad":
        r2.config(bg='#1745AD',fg='#002577')
        rbut2.config(image=radio1, bg='#1745AD')
        return
    while feedback1.get()=="Bad":
        r2.config(bg="#002577", fg='#FFFFFF', activebackground="#002577", activeforeground="#FFFFFF")
        rbut2.config(bg="#1745AD", image=radiot)
        return

def hoveronr3(event):
    while feedback1.get()!="Average":
        r3.config(fg='#002577',bg='#005AEA')
        rbut3.config(image=radioh,bg='#005AEA')
        return
    while feedback1.get()=="Average":
        r3.config(fg='#002577',bg='#005AEA')
        rbut3.config(bg='#005AEA')
        return

def clickb3(event):
    feedback1.set("Average")
    r3.config(bg="#002577",fg='#FFFFFF',activebackground="#002577",activeforeground="#FFFFFF")
    rbut3.config(bg="#002577",image=radioc)
    r1.config(bg='#1745AD', fg='#002577')
    rbut1.config(image=radio1, bg='#1745AD')
    r2.config(bg='#1745AD', fg='#002577')
    rbut2.config(image=radio1, bg='#1745AD')
    r4.config(bg='#1745AD', fg='#002577')
    rbut4.config(image=radio1, bg='#1745AD')
    r5.config(bg='#1745AD', fg='#002577')
    rbut5.config(image=radio1, bg='#1745AD')

    return

def releaseb3(event):
    while feedback1.get()=="Average":
        r3.config(bg="#1745AD",fg='#FFFFFF',activebackground="#002577",activeforeground="#FFFFFF")
        rbut3.config(bg="#1745AD",image=radiot)
        return


def hoveroffr3(event):
    while feedback1.get()!="Average":
        r3.config(bg='#1745AD',fg='#002577')
        rbut3.config(image=radio1, bg='#1745AD')
        return
    while feedback1.get()=="Average":
        r3.config(bg="#002577", fg='#FFFFFF', activebackground="#002577", activeforeground="#FFFFFF")
        rbut3.config(bg="#1745AD", image=radiot)
        return

def hoveronr4(event):
    while feedback1.get()!="Bad":
        r4.config(fg='#002577',bg='#005AEA')
        rbut4.config(image=radioh,bg='#005AEA')
        return
    while feedback1.get()=="Bad":
        r4.config(fg='#002577',bg='#005AEA')
        rbut4.config(bg='#005AEA')
        return


def clickb4(event):
    feedback1.set("Good")
    r4.config(bg="#002577",fg='#FFFFFF',activebackground="#002577",activeforeground="#FFFFFF")
    rbut4.config(bg="#002577",image=radioc)
    r1.config(bg='#1745AD', fg='#002577')
    rbut1.config(image=radio1, bg='#1745AD')
    r2.config(bg='#1745AD', fg='#002577')
    rbut2.config(image=radio1, bg='#1745AD')
    r3.config(bg='#1745AD', fg='#002577')
    rbut3.config(image=radio1, bg='#1745AD')
    r5.config(bg='#1745AD', fg='#002577')
    rbut5.config(image=radio1, bg='#1745AD')

    return

def releaseb4(event):
    while feedback1.get()=="Good":
        r4.config(bg="#1745AD",fg='#FFFFFF',activebackground="#002577",activeforeground="#FFFFFF")
        rbut4.config(bg="#1745AD",image=radiot)
        return


def hoveroffr4(event):
    while feedback1.get()!="Good":
        r4.config(bg='#1745AD',fg='#002577')
        rbut4.config(image=radio1, bg='#1745AD')
        return
    while feedback1.get()=="Good":
        r4.config(bg="#002577", fg='#FFFFFF', activebackground="#002577", activeforeground="#FFFFFF")
        rbut4.config(bg="#1745AD", image=radiot)
        return

def hoveronr5(event):
    while feedback1.get()!="Best":
        r5.config(fg='#002577',bg='#005AEA')
        rbut5.config(image=radioh,bg='#005AEA')
        return
    while feedback1.get()=="Best":
        r5.config(fg='#002577',bg='#005AEA')
        rbut5.config(bg='#005AEA')
        return


def clickb5(event):
    feedback1.set("Best")
    r5.config(bg="#002577",fg='#FFFFFF',activebackground="#002577",activeforeground="#FFFFFF")
    rbut5.config(bg="#002577",image=radioc)
    r1.config(bg='#1745AD', fg='#002577')
    rbut1.config(image=radio1, bg='#1745AD')
    r2.config(bg='#1745AD', fg='#002577')
    rbut2.config(image=radio1, bg='#1745AD')
    r3.config(bg='#1745AD', fg='#002577')
    rbut3.config(image=radio1, bg='#1745AD')
    r4.config(bg='#1745AD', fg='#002577')
    rbut4.config(image=radio1, bg='#1745AD')
    return

def releaseb5(event):
    while feedback1.get()=="Best":
        r5.config(bg="#1745AD",fg='#FFFFFF',activebackground="#002577",activeforeground="#FFFFFF")
        rbut5.config(bg="#1745AD",image=radiot)
        return


def hoveroffr5(event):
    while feedback1.get()!="Best":
        r5.config(bg='#1745AD',fg='#002577')
        rbut5.config(image=radio1, bg='#1745AD')
        return
    while feedback1.get()=="Best":
        r5.config(bg="#002577", fg='#FFFFFF', activebackground="#002577", activeforeground="#FFFFFF")
        rbut5.config(bg="#1745AD", image=radiot)
        return

##########################################################################################################

def hoveronr6(event):
    while feedback2.get()!="Worst":
        r6.config(fg='#002577',bg='#001F4C')
        rbut6.config(image=radioh,bg='#001F4C')
        return
    while feedback2.get() == "Worst":
        r6.config(fg='#002577', bg='#001F4C')
        rbut6.config(bg='#001F4C')
        return


def clickb6(event):
    feedback2.set("Worst")
    r6.config(bg="#002577",fg='#FFFFFF',activebackground="#001F4C",activeforeground="#FFFFFF")
    rbut6.config(bg="#002577",image=radioc)
    r7.config(bg='#002577', fg='#002577')
    rbut7.config(image=radio2, bg='#002577')
    r8.config(bg='#002577', fg='#002577')
    rbut8.config(image=radio2, bg='#002577')
    r9.config(bg='#002577', fg='#002577')
    rbut9.config(image=radio2, bg='#002577')
    r10.config(bg='#002577', fg='#002577')
    rbut10.config(image=radio2, bg='#002577')
    return

def releaseb6(event):
    while feedback2.get()=="Worst":
        r6.config(bg="#002577",fg='#FFFFFF',activebackground="#001F4C",activeforeground="#FFFFFF")
        rbut6.config(bg="#002577",image=radiot)
        return

def hoveroffr6(event):
    while feedback2.get()!="Worst":
        r6.config(bg='#002577',fg='#002577')
        rbut6.config(image=radio2, bg='#002577')
        return
    while feedback2.get()=="Worst":
        r6.config(bg="#002577", fg='#FFFFFF', activebackground="#001F4C", activeforeground="#FFFFFF")
        rbut6.config(bg="#002577", image=radiot)
        return

def hoveronr7(event):
    while feedback2.get()!="Bad":
        r7.config(fg='#002577',bg='#001F4C')
        rbut7.config(image=radioh,bg='#001F4C')
        return
    while feedback2.get()=="Bad":
        r7.config(fg='#002577',bg='#001F4C')
        rbut7.config(bg='#001F4C')
        return

def clickb7(event):
    feedback2.set("Bad")
    r7.config(bg="#002577",fg='#FFFFFF',activebackground="#001F4C",activeforeground="#FFFFFF")
    rbut7.config(bg="#002577",image=radioc)
    r6.config(bg='#002577', fg='#002577')
    rbut6.config(image=radio2, bg='#002577')
    r8.config(bg='#002577', fg='#002577')
    rbut8.config(image=radio2, bg='#002577')
    r9.config(bg='#002577', fg='#002577')
    rbut9.config(image=radio2, bg='#002577')
    r10.config(bg='#002577', fg='#002577')
    rbut10.config(image=radio2, bg='#002577')

    return

def releaseb7(event):
    while feedback2.get()=="Bad":
        r7.config(bg="#002577",fg='#FFFFFF',activebackground="#001F4C",activeforeground="#FFFFFF")
        rbut7.config(bg="#002577",image=radiot)
        return


def hoveroffr7(event):
    while feedback2.get()!="Bad":
        r7.config(bg='#002577',fg='#002577')
        rbut7.config(image=radio2, bg='#002577')
        return
    while feedback2.get()=="Bad":
        r7.config(bg="#002577", fg='#FFFFFF', activebackground="#001F4C", activeforeground="#FFFFFF")
        rbut7.config(bg="#002577", image=radiot)
        return

def hoveronr8(event):
    while feedback2.get()!="Average":
        r8.config(fg='#002577',bg='#001F4C')
        rbut8.config(image=radioh,bg='#001F4C')
        return
    while feedback2.get()=="Average":
        r8.config(fg='#002577',bg='#001F4C')
        rbut8.config(bg='#001F4C')
        return

def clickb8(event):
    feedback2.set("Average")
    r8.config(bg="#002577",fg='#FFFFFF',activebackground="#001F4C",activeforeground="#FFFFFF")
    rbut8.config(bg="#002577",image=radioc)
    r6.config(bg='#002577', fg='#002577')
    rbut6.config(image=radio2, bg='#002577')
    r7.config(bg='#002577', fg='#002577')
    rbut7.config(image=radio2, bg='#002577')
    r9.config(bg='#002577', fg='#002577')
    rbut9.config(image=radio2, bg='#002577')
    r10.config(bg='#002577', fg='#002577')
    rbut10.config(image=radio2, bg='#002577')
    return

def releaseb8(event):
    while feedback2.get()=="Average":
        r8.config(bg="#002577",fg='#FFFFFF',activebackground="#001F4C",activeforeground="#FFFFFF")
        rbut8.config(bg="#002577",image=radiot)
        return


def hoveroffr8(event):
    while feedback2.get()!="Average":
        r8.config(bg='#002577',fg='#002577')
        rbut8.config(image=radio2, bg='#002577')
        return
    while feedback2.get()=="Average":
        r8.config(bg="#002577", fg='#FFFFFF', activebackground="#001F4C", activeforeground="#FFFFFF")
        rbut8.config(bg="#002577", image=radiot)
        return

def hoveronr9(event):
    while feedback2.get()!="Bad":
        r9.config(fg='#002577',bg='#001F4C')
        rbut9.config(image=radioh,bg='#001F4C')
        return
    while feedback2.get()=="Bad":
        r9.config(fg='#002577',bg='#001F4C')
        rbut9.config(bg='#001F4C')
        return


def clickb9(event):
    feedback2.set("Good")
    r9.config(bg="#002577",fg='#FFFFFF',activebackground="#001F4C",activeforeground="#FFFFFF")
    rbut9.config(bg="#002577",image=radioc)
    r6.config(bg='#002577', fg='#002577')
    rbut6.config(image=radio2, bg='#002577')
    r7.config(bg='#002577', fg='#002577')
    rbut7.config(image=radio2, bg='#002577')
    r8.config(bg='#002577', fg='#002577')
    rbut8.config(image=radio2, bg='#002577')
    r10.config(bg='#002577', fg='#002577')
    rbut10.config(image=radio2, bg='#002577')

    return

def releaseb9(event):
    while feedback2.get()=="Good":
        r9.config(bg="#002577",fg='#FFFFFF',activebackground="#001F4C",activeforeground="#FFFFFF")
        rbut9.config(bg="#002577",image=radiot)
        return


def hoveroffr9(event):
    while feedback2.get()!="Good":
        r9.config(bg='#002577',fg='#002577')
        rbut9.config(image=radio2, bg='#002577')
        return
    while feedback2.get()=="Good":
        r9.config(bg="#002577", fg='#FFFFFF', activebackground="#001F4C", activeforeground="#FFFFFF")
        rbut9.config(bg="#002577", image=radiot)
        return

def hoveronr10(event):
    while feedback2.get()!="Best":
        r10.config(fg='#002577',bg='#001F4C')
        rbut10.config(image=radioh,bg='#001F4C')
        return
    while feedback2.get()=="Best":
        r10.config(fg='#002577',bg='#001F4C')
        rbut10.config(bg='#001F4C')
        return


def clickb10(event):
    feedback2.set("Best")
    r10.config(bg="#002577",fg='#FFFFFF',activebackground="#001F4C",activeforeground="#FFFFFF")
    rbut10.config(bg="#002577",image=radioc)
    r6.config(bg='#002577', fg='#002577')
    rbut6.config(image=radio2, bg='#002577')
    r7.config(bg='#002577', fg='#002577')
    rbut7.config(image=radio2, bg='#002577')
    r8.config(bg='#002577', fg='#002577')
    rbut8.config(image=radio2, bg='#002577')
    r9.config(bg='#002577', fg='#002577')
    rbut9.config(image=radio2, bg='#002577')
    return

def releaseb10(event):
    while feedback2.get()=="Best":
        r10.config(bg="#002577",fg='#FFFFFF',activebackground="#001F4C",activeforeground="#FFFFFF")
        rbut10.config(bg="#002577",image=radiot)
        return


def hoveroffr10(event):
    while feedback2.get()!="Best":
        r10.config(bg='#002577',fg='#002577')
        rbut10.config(image=radio2, bg='#002577')
        return
    while feedback2.get()=="Best":
        r10.config(bg="#002577", fg='#FFFFFF', activebackground="#001F4C", activeforeground="#FFFFFF")
        rbut10.config(bg="#002577", image=radiot)
        return

##########################################################################################################

def hoveronr11(event):
    while feedback3.get()!="Worst":
        r11.config(fg='#002577',bg='#005AEA')
        rbut11.config(image=radioh,bg='#005AEA')
        return
    while feedback3.get()=="Worst":
        r11.config(fg='#002577',bg='#005AEA')
        rbut11.config(bg='#005AEA')
        return

def clickb11(event):
    feedback3.set("Worst")
    r11.config(bg="#002577",fg='#FFFFFF',activebackground="#002577",activeforeground="#FFFFFF")
    rbut11.config(bg="#002577",image=radioc)
    r12.config(bg='#1745AD', fg='#002577')
    rbut12.config(image=radio1, bg='#1745AD')
    r13.config(bg='#1745AD', fg='#002577')
    rbut13.config(image=radio1, bg='#1745AD')
    r14.config(bg='#1745AD', fg='#002577')
    rbut14.config(image=radio1, bg='#1745AD')
    r15.config(bg='#1745AD', fg='#002577')
    rbut15.config(image=radio1, bg='#1745AD')
    return

def releaseb11(event):
    while feedback3.get()=="Worst":
        r11.config(bg="#1745AD",fg='#FFFFFF',activebackground="#002577",activeforeground="#FFFFFF")
        rbut11.config(bg="#1745AD",image=radiot)
        return

def hoveroffr11(event):
    while feedback3.get()!="Worst":
        r1.config(bg='#1745AD',fg='#002577')
        rbut11.config(image=radio1, bg='#1745AD')
        return
    while feedback3.get()=="Worst":
        r11.config(bg="#002577", fg='#FFFFFF', activebackground="#002577", activeforeground="#FFFFFF")
        rbut11.config(bg="#1745AD", image=radiot)
        return

def hoveronr12(event):
    while feedback3.get()!="Bad":
        r12.config(fg='#002577',bg='#005AEA')
        rbut12.config(image=radioh,bg='#005AEA')
        return
    while feedback3.get()=="Bad":
        r12.config(fg='#002577',bg='#005AEA')
        rbut12.config(bg='#005AEA')
        return

def clickb12(event):
    feedback3.set("Bad")
    r12.config(bg="#002577",fg='#FFFFFF',activebackground="#002577",activeforeground="#FFFFFF")
    rbut12.config(bg="#002577",image=radioc)
    r11.config(bg='#1745AD', fg='#002577')
    rbut11.config(image=radio1, bg='#1745AD')
    r13.config(bg='#1745AD', fg='#002577')
    rbut13.config(image=radio1, bg='#1745AD')
    r14.config(bg='#1745AD', fg='#002577')
    rbut14.config(image=radio1, bg='#1745AD')
    r15.config(bg='#1745AD', fg='#002577')
    rbut15.config(image=radio1, bg='#1745AD')

    return

def releaseb12(event):
    while feedback3.get()=="Bad":
        r12.config(bg="#1745AD",fg='#FFFFFF',activebackground="#002577",activeforeground="#FFFFFF")
        rbut12.config(bg="#1745AD",image=radiot)
        return


def hoveroffr12(event):
    while feedback3.get()!="Bad":
        r12.config(bg='#1745AD',fg='#002577')
        rbut12.config(image=radio1, bg='#1745AD')
        return
    while feedback3.get()=="Bad":
        r12.config(bg="#002577", fg='#FFFFFF', activebackground="#002577", activeforeground="#FFFFFF")
        rbut12.config(bg="#1745AD", image=radiot)
        return

def hoveronr13(event):
    while feedback3.get()!="Average":
        r13.config(fg='#002577',bg='#005AEA')
        rbut13.config(image=radioh,bg='#005AEA')
        return
    while feedback3.get()=="Average":
        r13.config(fg='#002577',bg='#005AEA')
        rbut13.config(bg='#005AEA')
        return

def clickb13(event):
    feedback3.set("Average")
    r13.config(bg="#002577",fg='#FFFFFF',activebackground="#002577",activeforeground="#FFFFFF")
    rbut13.config(bg="#002577",image=radioc)
    r11.config(bg='#1745AD', fg='#002577')
    rbut11.config(image=radio1, bg='#1745AD')
    r12.config(bg='#1745AD', fg='#002577')
    rbut12.config(image=radio1, bg='#1745AD')
    r14.config(bg='#1745AD', fg='#002577')
    rbut14.config(image=radio1, bg='#1745AD')
    r15.config(bg='#1745AD', fg='#002577')
    rbut15.config(image=radio1, bg='#1745AD')

    return

def releaseb13(event):
    while feedback3.get()=="Average":
        r13.config(bg="#1745AD",fg='#FFFFFF',activebackground="#002577",activeforeground="#FFFFFF")
        rbut13.config(bg="#1745AD",image=radiot)
        return


def hoveroffr13(event):
    while feedback3.get()!="Average":
        r13.config(bg='#1745AD',fg='#002577')
        rbut13.config(image=radio1, bg='#1745AD')
        return
    while feedback3.get()=="Average":
        r13.config(bg="#002577", fg='#FFFFFF', activebackground="#002577", activeforeground="#FFFFFF")
        rbut13.config(bg="#1745AD", image=radiot)
        return

def hoveronr14(event):
    while feedback3.get()!="Bad":
        r14.config(fg='#002577',bg='#005AEA')
        rbut14.config(image=radioh,bg='#005AEA')
        return
    while feedback3.get()=="Bad":
        r14.config(fg='#002577',bg='#005AEA')
        rbut14.config(bg='#005AEA')
        return


def clickb14(event):
    feedback3.set("Good")
    r14.config(bg="#002577",fg='#FFFFFF',activebackground="#002577",activeforeground="#FFFFFF")
    rbut14.config(bg="#002577",image=radioc)
    r11.config(bg='#1745AD', fg='#002577')
    rbut11.config(image=radio1, bg='#1745AD')
    r12.config(bg='#1745AD', fg='#002577')
    rbut12.config(image=radio1, bg='#1745AD')
    r13.config(bg='#1745AD', fg='#002577')
    rbut13.config(image=radio1, bg='#1745AD')
    r15.config(bg='#1745AD', fg='#002577')
    rbut15.config(image=radio1, bg='#1745AD')

    return

def releaseb14(event):
    while feedback3.get()=="Good":
        r14.config(bg="#1745AD",fg='#FFFFFF',activebackground="#002577",activeforeground="#FFFFFF")
        rbut14.config(bg="#1745AD",image=radiot)
        return


def hoveroffr14(event):
    while feedback3.get()!="Good":
        r14.config(bg='#1745AD',fg='#002577')
        rbut14.config(image=radio1, bg='#1745AD')
        return
    while feedback3.get()=="Good":
        r14.config(bg="#002577", fg='#FFFFFF', activebackground="#002577", activeforeground="#FFFFFF")
        rbut14.config(bg="#1745AD", image=radiot)
        return

def hoveronr15(event):
    while feedback3.get()!="Best":
        r15.config(fg='#002577',bg='#005AEA')
        rbut15.config(image=radioh,bg='#005AEA')
        return
    while feedback3.get()=="Best":
        r15.config(fg='#002577',bg='#005AEA')
        rbut15.config(bg='#005AEA')
        return


def clickb15(event):
    feedback3.set("Best")
    r15.config(bg="#002577",fg='#FFFFFF',activebackground="#002577",activeforeground="#FFFFFF")
    rbut15.config(bg="#002577",image=radioc)
    r11.config(bg='#1745AD', fg='#002577')
    rbut11.config(image=radio1, bg='#1745AD')
    r12.config(bg='#1745AD', fg='#002577')
    rbut12.config(image=radio1, bg='#1745AD')
    r13.config(bg='#1745AD', fg='#002577')
    rbut13.config(image=radio1, bg='#1745AD')
    r14.config(bg='#1745AD', fg='#002577')
    rbut14.config(image=radio1, bg='#1745AD')
    return

def releaseb15(event):
    while feedback3.get()=="Best":
        r15.config(bg="#1745AD",fg='#FFFFFF',activebackground="#002577",activeforeground="#FFFFFF")
        rbut15.config(bg="#1745AD",image=radiot)
        return


def hoveroffr15(event):
    while feedback3.get()!="Best":
        r15.config(bg='#1745AD',fg='#002577')
        rbut15.config(image=radio1, bg='#1745AD')
        return
    while feedback3.get()=="Best":
        r15.config(bg="#002577", fg='#FFFFFF', activebackground="#002577", activeforeground="#FFFFFF")
        rbut15.config(bg="#1745AD", image=radiot)
        return

##########################################################################################################

def hoveronr16(event):
    while feedback4.get()!="Worst":
        r16.config(fg='#002577',bg='#001F4C')
        rbut16.config(image=radioh,bg='#001F4C')
        return
    while feedback4.get() == "Worst":
        r16.config(fg='#002577', bg='#001F4C')
        rbut16.config(bg='#001F4C')
        return


def clickb16(event):
    feedback4.set("Worst")
    r16.config(bg="#002577",fg='#FFFFFF',activebackground="#001F4C",activeforeground="#FFFFFF")
    rbut16.config(bg="#002577",image=radioc)
    r17.config(bg='#002577', fg='#002577')
    rbut17.config(image=radio2, bg='#002577')
    r18.config(bg='#002577', fg='#002577')
    rbut18.config(image=radio2, bg='#002577')
    r19.config(bg='#002577', fg='#002577')
    rbut19.config(image=radio2, bg='#002577')
    r20.config(bg='#002577', fg='#002577')
    rbut20.config(image=radio2, bg='#002577')
    return

def releaseb16(event):
    while feedback4.get()=="Worst":
        r16.config(bg="#002577",fg='#FFFFFF',activebackground="#001F4C",activeforeground="#FFFFFF")
        rbut16.config(bg="#002577",image=radiot)
        return

def hoveroffr16(event):
    while feedback4.get()!="Worst":
        r16.config(bg='#002577',fg='#002577')
        rbut16.config(image=radio2, bg='#002577')
        return
    while feedback4.get()=="Worst":
        r16.config(bg="#002577", fg='#FFFFFF', activebackground="#001F4C", activeforeground="#FFFFFF")
        rbut16.config(bg="#002577", image=radiot)
        return

def hoveronr17(event):
    while feedback4.get()!="Bad":
        r17.config(fg='#002577',bg='#001F4C')
        rbut17.config(image=radioh,bg='#001F4C')
        return
    while feedback4.get()=="Bad":
        r17.config(fg='#002577',bg='#001F4C')
        rbut17.config(bg='#001F4C')
        return

def clickb17(event):
    feedback4.set("Bad")
    r17.config(bg="#002577",fg='#FFFFFF',activebackground="#001F4C",activeforeground="#FFFFFF")
    rbut17.config(bg="#002577",image=radioc)
    r16.config(bg='#002577', fg='#002577')
    rbut16.config(image=radio2, bg='#002577')
    r18.config(bg='#002577', fg='#002577')
    rbut18.config(image=radio2, bg='#002577')
    r19.config(bg='#002577', fg='#002577')
    rbut19.config(image=radio2, bg='#002577')
    r20.config(bg='#002577', fg='#002577')
    rbut20.config(image=radio2, bg='#002577')

    return

def releaseb17(event):
    while feedback4.get()=="Bad":
        r17.config(bg="#002577",fg='#FFFFFF',activebackground="#001F4C",activeforeground="#FFFFFF")
        rbut17.config(bg="#002577",image=radiot)
        return


def hoveroffr17(event):
    while feedback4.get()!="Bad":
        r17.config(bg='#002577',fg='#002577')
        rbut17.config(image=radio2, bg='#002577')
        return
    while feedback4.get()=="Bad":
        r17.config(bg="#002577", fg='#FFFFFF', activebackground="#001F4C", activeforeground="#FFFFFF")
        rbut17.config(bg="#002577", image=radiot)
        return

def hoveronr18(event):
    while feedback4.get()!="Average":
        r18.config(fg='#002577',bg='#001F4C')
        rbut18.config(image=radioh,bg='#001F4C')
        return
    while feedback4.get()=="Average":
        r18.config(fg='#002577',bg='#001F4C')
        rbut18.config(bg='#001F4C')
        return

def clickb18(event):
    feedback4.set("Average")
    r18.config(bg="#002577",fg='#FFFFFF',activebackground="#001F4C",activeforeground="#FFFFFF")
    rbut18.config(bg="#002577",image=radioc)
    r16.config(bg='#002577', fg='#002577')
    rbut16.config(image=radio2, bg='#002577')
    r17.config(bg='#002577', fg='#002577')
    rbut17.config(image=radio2, bg='#002577')
    r19.config(bg='#002577', fg='#002577')
    rbut19.config(image=radio2, bg='#002577')
    r20.config(bg='#002577', fg='#002577')
    rbut20.config(image=radio2, bg='#002577')
    return

def releaseb18(event):
    while feedback4.get()=="Average":
        r18.config(bg="#002577",fg='#FFFFFF',activebackground="#001F4C",activeforeground="#FFFFFF")
        rbut18.config(bg="#002577",image=radiot)
        return


def hoveroffr18(event):
    while feedback4.get()!="Average":
        r18.config(bg='#002577',fg='#002577')
        rbut18.config(image=radio2, bg='#002577')
        return
    while feedback4.get()=="Average":
        r18.config(bg="#002577", fg='#FFFFFF', activebackground="#001F4C", activeforeground="#FFFFFF")
        rbut18.config(bg="#002577", image=radiot)
        return

def hoveronr19(event):
    while feedback4.get()!="Bad":
        r19.config(fg='#002577',bg='#001F4C')
        rbut19.config(image=radioh,bg='#001F4C')
        return
    while feedback4.get()=="Bad":
        r19.config(fg='#002577',bg='#001F4C')
        rbut19.config(bg='#001F4C')
        return


def clickb19(event):
    feedback4.set("Good")
    r19.config(bg="#002577",fg='#FFFFFF',activebackground="#001F4C",activeforeground="#FFFFFF")
    rbut19.config(bg="#002577",image=radioc)
    r16.config(bg='#002577', fg='#002577')
    rbut16.config(image=radio2, bg='#002577')
    r17.config(bg='#002577', fg='#002577')
    rbut17.config(image=radio2, bg='#002577')
    r18.config(bg='#002577', fg='#002577')
    rbut18.config(image=radio2, bg='#002577')
    r20.config(bg='#002577', fg='#002577')
    rbut20.config(image=radio2, bg='#002577')

    return

def releaseb19(event):
    while feedback4.get()=="Good":
        r19.config(bg="#002577",fg='#FFFFFF',activebackground="#001F4C",activeforeground="#FFFFFF")
        rbut19.config(bg="#002577",image=radiot)
        return


def hoveroffr19(event):
    while feedback4.get()!="Good":
        r19.config(bg='#002577',fg='#002577')
        rbut19.config(image=radio2, bg='#002577')
        return
    while feedback4.get()=="Good":
        r19.config(bg="#002577", fg='#FFFFFF', activebackground="#001F4C", activeforeground="#FFFFFF")
        rbut19.config(bg="#002577", image=radiot)
        return

def hoveronr20(event):
    while feedback4.get()!="Best":
        r20.config(fg='#002577',bg='#001F4C')
        rbut20.config(image=radioh,bg='#001F4C')
        return
    while feedback4.get()=="Best":
        r20.config(fg='#002577',bg='#001F4C')
        rbut20.config(bg='#001F4C')
        return


def clickb20(event):
    feedback4.set("Best")
    r20.config(bg="#002577",fg='#FFFFFF',activebackground="#001F4C",activeforeground="#FFFFFF")
    rbut20.config(bg="#002577",image=radioc)
    r16.config(bg='#002577', fg='#002577')
    rbut16.config(image=radio2, bg='#002577')
    r17.config(bg='#002577', fg='#002577')
    rbut17.config(image=radio2, bg='#002577')
    r18.config(bg='#002577', fg='#002577')
    rbut18.config(image=radio2, bg='#002577')
    r19.config(bg='#002577', fg='#002577')
    rbut19.config(image=radio2, bg='#002577')
    return

def releaseb20(event):
    while feedback4.get()=="Best":
        r20.config(bg="#002577",fg='#FFFFFF',activebackground="#001F4C",activeforeground="#FFFFFF")
        rbut20.config(bg="#002577",image=radiot)
        return


def hoveroffr20(event):
    while feedback4.get()!="Best":
        r20.config(bg='#002577',fg='#002577')
        rbut20.config(image=radio2, bg='#002577')
        return
    while feedback4.get()=="Best":
        r20.config(bg="#002577", fg='#FFFFFF', activebackground="#001F4C", activeforeground="#FFFFFF")
        rbut20.config(bg="#002577", image=radiot)
        return

##########################################################################################################

def hoveronr21(event):
    while feedback5.get()!="Worst":
        r21.config(fg='#002577',bg='#005AEA')
        rbut21.config(image=radioh,bg='#005AEA')
        return
    while feedback5.get()=="Worst":
        r21.config(fg='#002577',bg='#005AEA')
        rbut21.config(bg='#005AEA')
        return

def clickb21(event):
    feedback5.set("Worst")
    r21.config(bg="#002577",fg='#FFFFFF',activebackground="#002577",activeforeground="#FFFFFF")
    rbut21.config(bg="#002577",image=radioc)
    r22.config(bg='#1745AD', fg='#002577')
    rbut22.config(image=radio1, bg='#1745AD')
    r23.config(bg='#1745AD', fg='#002577')
    rbut23.config(image=radio1, bg='#1745AD')
    r24.config(bg='#1745AD', fg='#002577')
    rbut24.config(image=radio1, bg='#1745AD')
    r25.config(bg='#1745AD', fg='#002577')
    rbut25.config(image=radio1, bg='#1745AD')
    return

def releaseb21(event):
    while feedback5.get()=="Worst":
        r21.config(bg="#1745AD",fg='#FFFFFF',activebackground="#002577",activeforeground="#FFFFFF")
        rbut21.config(bg="#1745AD",image=radiot)
        return

def hoveroffr21(event):
    while feedback5.get()!="Worst":
        r21.config(bg='#1745AD',fg='#002577')
        rbut21.config(image=radio1, bg='#1745AD')
        return
    while feedback5.get()=="Worst":
        r21.config(bg="#002577", fg='#FFFFFF', activebackground="#002577", activeforeground="#FFFFFF")
        rbut21.config(bg="#1745AD", image=radiot)
        return

def hoveronr22(event):
    while feedback5.get()!="Bad":
        r22.config(fg='#002577',bg='#005AEA')
        rbut22.config(image=radioh,bg='#005AEA')
        return
    while feedback5.get()=="Bad":
        r22.config(fg='#002577',bg='#005AEA')
        rbut22.config(bg='#005AEA')
        return

def clickb22(event):
    feedback5.set("Bad")
    r22.config(bg="#002577",fg='#FFFFFF',activebackground="#002577",activeforeground="#FFFFFF")
    rbut22.config(bg="#002577",image=radioc)
    r21.config(bg='#1745AD', fg='#002577')
    rbut21.config(image=radio1, bg='#1745AD')
    r23.config(bg='#1745AD', fg='#002577')
    rbut23.config(image=radio1, bg='#1745AD')
    r24.config(bg='#1745AD', fg='#002577')
    rbut24.config(image=radio1, bg='#1745AD')
    r25.config(bg='#1745AD', fg='#002577')
    rbut25.config(image=radio1, bg='#1745AD')

    return

def releaseb22(event):
    while feedback5.get()=="Bad":
        r22.config(bg="#1745AD",fg='#FFFFFF',activebackground="#002577",activeforeground="#FFFFFF")
        rbut22.config(bg="#1745AD",image=radiot)
        return


def hoveroffr22(event):
    while feedback5.get()!="Bad":
        r22.config(bg='#1745AD',fg='#002577')
        rbut22.config(image=radio1, bg='#1745AD')
        return
    while feedback5.get()=="Bad":
        r22.config(bg="#002577", fg='#FFFFFF', activebackground="#002577", activeforeground="#FFFFFF")
        rbut22.config(bg="#1745AD", image=radiot)
        return

def hoveronr23(event):
    while feedback5.get()!="Average":
        r23.config(fg='#002577',bg='#005AEA')
        rbut23.config(image=radioh,bg='#005AEA')
        return
    while feedback5.get()=="Average":
        r23.config(fg='#002577',bg='#005AEA')
        rbut23.config(bg='#005AEA')
        return

def clickb23(event):
    feedback5.set("Average")
    r23.config(bg="#002577",fg='#FFFFFF',activebackground="#002577",activeforeground="#FFFFFF")
    rbut23.config(bg="#002577",image=radioc)
    r21.config(bg='#1745AD', fg='#002577')
    rbut21.config(image=radio1, bg='#1745AD')
    r22.config(bg='#1745AD', fg='#002577')
    rbut22.config(image=radio1, bg='#1745AD')
    r24.config(bg='#1745AD', fg='#002577')
    rbut24.config(image=radio1, bg='#1745AD')
    r25.config(bg='#1745AD', fg='#002577')
    rbut25.config(image=radio1, bg='#1745AD')

    return

def releaseb23(event):
    while feedback5.get()=="Average":
        r23.config(bg="#1745AD",fg='#FFFFFF',activebackground="#002577",activeforeground="#FFFFFF")
        rbut23.config(bg="#1745AD",image=radiot)
        return


def hoveroffr23(event):
    while feedback5.get()!="Average":
        r23.config(bg='#1745AD',fg='#002577')
        rbut23.config(image=radio1, bg='#1745AD')
        return
    while feedback5.get()=="Average":
        r23.config(bg="#002577", fg='#FFFFFF', activebackground="#002577", activeforeground="#FFFFFF")
        rbut23.config(bg="#1745AD", image=radiot)
        return

def hoveronr24(event):
    while feedback5.get()!="Bad":
        r24.config(fg='#002577',bg='#005AEA')
        rbut24.config(image=radioh,bg='#005AEA')
        return
    while feedback5.get()=="Bad":
        r24.config(fg='#002577',bg='#005AEA')
        rbut24.config(bg='#005AEA')
        return


def clickb24(event):
    feedback5.set("Good")
    r24.config(bg="#002577",fg='#FFFFFF',activebackground="#002577",activeforeground="#FFFFFF")
    rbut24.config(bg="#002577",image=radioc)
    r21.config(bg='#1745AD', fg='#002577')
    rbut21.config(image=radio1, bg='#1745AD')
    r22.config(bg='#1745AD', fg='#002577')
    rbut22.config(image=radio1, bg='#1745AD')
    r23.config(bg='#1745AD', fg='#002577')
    rbut23.config(image=radio1, bg='#1745AD')
    r25.config(bg='#1745AD', fg='#002577')
    rbut25.config(image=radio1, bg='#1745AD')

    return

def releaseb24(event):
    while feedback5.get()=="Good":
        r24.config(bg="#1745AD",fg='#FFFFFF',activebackground="#002577",activeforeground="#FFFFFF")
        rbut24.config(bg="#1745AD",image=radiot)
        return


def hoveroffr24(event):
    while feedback5.get()!="Good":
        r24.config(bg='#1745AD',fg='#002577')
        rbut24.config(image=radio1, bg='#1745AD')
        return
    while feedback5.get()=="Good":
        r24.config(bg="#002577", fg='#FFFFFF', activebackground="#002577", activeforeground="#FFFFFF")
        rbut24.config(bg="#1745AD", image=radiot)
        return

def hoveronr25(event):
    while feedback5.get()!="Best":
        r25.config(fg='#002577',bg='#005AEA')
        rbut25.config(image=radioh,bg='#005AEA')
        return
    while feedback5.get()=="Best":
        r25.config(fg='#002577',bg='#005AEA')
        rbut25.config(bg='#005AEA')
        return


def clickb25(event):
    feedback5.set("Best")
    r25.config(bg="#002577",fg='#FFFFFF',activebackground="#002577",activeforeground="#FFFFFF")
    rbut25.config(bg="#002577",image=radioc)
    r21.config(bg='#1745AD', fg='#002577')
    rbut21.config(image=radio1, bg='#1745AD')
    r22.config(bg='#1745AD', fg='#002577')
    rbut22.config(image=radio1, bg='#1745AD')
    r23.config(bg='#1745AD', fg='#002577')
    rbut23.config(image=radio1, bg='#1745AD')
    r24.config(bg='#1745AD', fg='#002577')
    rbut24.config(image=radio1, bg='#1745AD')
    return

def releaseb25(event):
    while feedback5.get()=="Best":
        r25.config(bg="#1745AD",fg='#FFFFFF',activebackground="#002577",activeforeground="#FFFFFF")
        rbut25.config(bg="#1745AD",image=radiot)
        return


def hoveroffr25(event):
    while feedback5.get()!="Best":
        r25.config(bg='#1745AD',fg='#002577')
        rbut25.config(image=radio1, bg='#1745AD')
        return
    while feedback5.get()=="Best":
        r25.config(bg="#002577", fg='#FFFFFF', activebackground="#002577", activeforeground="#FFFFFF")
        rbut25.config(bg="#1745AD", image=radiot)
        return


def output(var1,var2,var3,var4,var5):

    outputs=[var1,var2,var3,var4,var5]

    global statement

    worst=[]
    bad=[]
    average=[]
    good=[]
    best=[]

    for n in outputs:
        if n=="Worst":
            worst.append(n)
        if n=="Bad":
            bad.append(n)
        if n=="Average":
            average.append(n)
        if n=="Good":
            good.append(n)
        if n=="Best":
            best.append(n)

    len1=len(worst)
    len2=len(bad)
    len3=len(average)
    len4=len(good)
    len5=len(best)
    lens=[len1,len2,len3,len4,len5]
    length=max(lens)

    global result
    result=''

    if length==len(worst):
        result='worst'
    if length==len(bad):
        result='bad'
    if length==len(average):
        result='average'
    if length==len(good):
        result='good'
    if length==len(best):
        result='best'
    statement=""
    statement=("your overall opinion was: "+result)

    global label
    global var
    global but
    if var==0:
        label = Label(frame8,text=statement,bg="#C2C2FF",fg="#002577",font="Helvetica 11")
        label.pack(fill="both",expand="true",side="left")
        var+=1

    def click():
        global var
        var-=1

    def stop():
        global but
        but-=1

    if but==0:
        reset= Button(frame8,text='Reset',command=lambda: [label.pack_forget(),reset.pack_forget(),click(),stop()],relief="flat",bg="#B5B5E8",fg="#002577",activebackground="#B5B5E8",activeforeground="white",borderwidth=0,font="Helvetica 10 bold",padx=10)
        reset.pack(fill="both",side="right")

        def hoveron(event):
            reset.config(bg='#F74343', fg='white')
            return

        def hoveroff(event):
            reset.config(fg='#002577', bg='#B5B5E8')
            return

        reset.bind('<Enter>', hoveron)
        reset.bind('<Leave>', hoveroff)

        but+=1


def hoveron2(event):
    myButton.config(image=btfh1)
    return
def hoveroff2(event):
    myButton.config(image=btf1)
    return
def click2(event):
    myButton.config(image=btfc1)
    return
def release2(event):
    myButton.config(image=btfh1)
    return

def hoveron1(event):
    buttondis.config(image=btfh2)
    return
def click1(event):
    buttondis.config(image=btfc2)
    return
def release1(event):
    buttondis.config(image=btfh2)
    return
def hoveroff1(event):
    buttondis.config(image=btf2)
    return

def mains3(v):
    global master
    global val,feed
    val=v
    global root
    global r1;global r2;global r3;global r4;global r5
    global r6;global r7;global r8;global r9;global r10
    global r11;global r12;global r13;global r14;global r15
    global r16;global r17;global r18;global r19;global r20
    global r21;global r22;global r23;global r24;global r25
    global rbut1; global rbut2; global rbut3; global rbut4; global rbut5
    global rbut6;global rbut7; global rbut8; global rbut9; global rbut10
    global rbut11;global rbut12; global rbut13; global rbut14; global rbut15
    global rbut16;global rbut17; global rbut18; global rbut19; global rbut20
    global rbut21;global rbut22; global rbut23; global rbut24; global rbut25
    global radio1; global radio2; global radioh; global radioc; global radiot
    global myButton; global buttondis
    global frame8
    global feedback1; global feedback2; global feedback3; global feedback4; global feedback5
    global btf1; global btfc1; global btfh1
    global btf2; global btfc2; global btfh2
    global hf1; global hf2
    global dis2

    root = Tk()
    root.title('Electicider Feedback Form')
    root.attributes("-fullscreen", True)
    root.minsize(870,710)
    feed=StringVar()
    imgn=Image.open("backtemp.png")
    imgn=imgn.resize((1600,900),Image.ANTIALIAS)
    temp=ImageTk.PhotoImage(imgn)

    imgn = Image.open("headf1.png")
    imgn = imgn.resize((533, 45), Image.ANTIALIAS)
    hf1 = ImageTk.PhotoImage(imgn)

    imgn = Image.open("headf2.png")
    imgn = imgn.resize((803, 60), Image.ANTIALIAS)
    hf2 = ImageTk.PhotoImage(imgn)

    imgn = Image.open("buttf1.png")
    imgn = imgn.resize((803, 60), Image.ANTIALIAS)
    btf1 = ImageTk.PhotoImage(imgn)

    imgn = Image.open("buttf1h.png")
    imgn = imgn.resize((803, 60), Image.ANTIALIAS)
    btfh1 = ImageTk.PhotoImage(imgn)

    imgn = Image.open("buttf1c.png")
    imgn = imgn.resize((803, 60), Image.ANTIALIAS)
    btfc1 = ImageTk.PhotoImage(imgn)

    imgn = Image.open("buttf2.png")
    imgn = imgn.resize((1340, 100), Image.ANTIALIAS)
    btf2 = ImageTk.PhotoImage(imgn)

    imgn = Image.open("buttf2h.png")
    imgn = imgn.resize((1340, 110), Image.ANTIALIAS)
    btfh2 = ImageTk.PhotoImage(imgn)

    imgn = Image.open("buttf2c.png")
    imgn = imgn.resize((1340, 110), Image.ANTIALIAS)
    btfc2 = ImageTk.PhotoImage(imgn)


    imgn=Image.open("radio1.png")
    imgn=imgn.resize((20,20),Image.ANTIALIAS)
    radio1=ImageTk.PhotoImage(imgn)

    imgn=Image.open("radio2.png")
    imgn=imgn.resize((20,20),Image.ANTIALIAS)
    radio2=ImageTk.PhotoImage(imgn)

    imgn=Image.open("radioh.png")
    imgn=imgn.resize((20,20),Image.ANTIALIAS)
    radioh=ImageTk.PhotoImage(imgn)

    imgn=Image.open("radioc.png")
    imgn=imgn.resize((20,20),Image.ANTIALIAS)
    radioc=ImageTk.PhotoImage(imgn)

    imgn=Image.open("radiot.png")
    imgn=imgn.resize((20,20),Image.ANTIALIAS)
    radiot=ImageTk.PhotoImage(imgn)

    img1=Image.open("nust.png")
    img1=img1.resize((75,65),Image.ANTIALIAS)
    pic=ImageTk.PhotoImage(img1)

    main=Frame(root,bg="white")
    main.place(relx=0,rely=0,relheight=1,relwidth=1)

    backs=Frame(main,bg="white") #side-line for text
    backs.place(relx=0,rely=0,relwidth=1,relheight=0.25)

    labtemp1 = Label(backs, image=temp)
    labtemp1.place(relx=0, rely=0, relheight=1, relwidth=1)

    headings=Frame(backs,bg="#1745AD") #side-line for text
    headings.place(relx=0,rely=0,width=800,relheight=0.975)

    line1=Frame(backs,bg="white") #separator line
    line1.place(relx=0,rely=0,relwidth=1,relheight=0.2)

    head1=Frame(line1,bg="white")
    head1.place(relx=0,rely=0,relwidth=1,relheight=0.92)

    head2=Frame(headings,bg="#DDDDDD") #text background
    head2.place(relx=0.009,rely=0.2,width=800,relheight=0.12)
    head3=Frame(headings,bg="#DDDDDD") #text background
    head3.place(relx=0.009,rely=0.32,width=800,relheight=0.56)
    head4=Frame(headings,bg="#DDDDDD") #text background
    head4.place(relx=0.009,rely=0.88,width=800,relheight=0.12)

    box=Frame(main,bg="white")
    box.place(relx=0,rely=0.25,relwidth=1,relheight=0.45)

    bottom=Frame(main,bg="white")
    bottom.place(relx=0,rely=0.7,relwidth=1,relheight=0.3)

    lowerbox=Frame(bottom,bg="#1745AD") #side line for text 2
    lowerbox.place(relx=0,rely=0,relwidth=1,relheight=1)

    desc1=Frame(lowerbox,bg="white") #text background
    desc1.place(relx=0.009,rely=0,relwidth=1,relheight=0.1)

    de2=Frame(lowerbox,bg="white") #upper border for entry
    de2.place(relx=0,rely=0.1,relwidth=1,relheight=0.6)
    des2=Frame(de2,bg="#DDDDDD") #border of entry box
    des2.place(relx=0,rely=0.035,relwidth=1,relheight=1)

    labtemp3 = Label(desc1, image=temp)
    labtemp3.place(relx=0, rely=0, relheight=1, relwidth=1)


    desc2=Frame(des2,bg="white")
    desc2.place(relx=0.004,rely=0.02,relwidth=0.992,relheight=0.92)

    but3=Frame(lowerbox,bg="white")
    but3.place(relx=0,rely=0.7,relwidth=1,relheight=0.2)

    labtemp4 = Label(but3, image=temp)
    labtemp4.place(relx=0, rely=0, relheight=1, relwidth=1)

    desc3=Frame(but3,bg="white")
    desc3.place(relx=0.005,rely=0.1,relwidth=0.99,relheight=0.8)

    desc4=Frame(lowerbox,bg="white")
    desc4.place(relx=0,rely=0.9,relwidth=1,relheight=0.1)

    box1=Frame(box,bg="white")
    box1.place(relx=0.4,rely=0,relwidth=0.6,relheight=1)

    box2=Frame(box,bg="white") #questions background
    box2.place(relx=0,rely=0,relwidth=0.4,relheight=1)

    texts=Frame(box2,bg="white")
    texts.place(relx=0,rely=0,relwidth=1,relheight=0.76)

    vertical=Frame(texts,bg="white")
    vertical.place(relx=0,rely=0.18,relwidth=1,relheight=0.8)

    vertical1=Frame(vertical,bg="white")
    vertical1.place(relx=0,rely=0,relwidth=1,relheight=0.19)
    vertical2=Frame(vertical,bg="white")
    vertical2.place(relx=0,rely=0.19,relwidth=1,relheight=0.2)
    vertical3=Frame(vertical,bg="white")
    vertical3.place(relx=0,rely=0.39,relwidth=1,relheight=0.21)
    vertical4=Frame(vertical,bg="white")
    vertical4.place(relx=0,rely=0.6,relwidth=1,relheight=0.2)
    vertical5=Frame(vertical,bg="white")
    vertical5.place(relx=0,rely=0.8,relwidth=1,relheight=0.2)

    divisor1=Frame(box2,bg="white") #borderline
    divisor1.place(relx=0,rely=0.76,relwidth=1,relheight=0.24)

    divisor=Frame(divisor1,bg="#8796CB") #space below questions
    divisor.place(relx=0,rely=0,relwidth=1,relheight=0.95)
    divlab=Label(divisor,image=pic)
    divlab.place(relx=0,rely=0,relwidth=1,relheight=1)

    hea1=Frame(texts,bg="white") #qestion heading border
    hea1.place(relx=0,rely=0,relwidth=1,relheight=0.185)

    heading1=Frame(hea1,bg="white")
    heading1.place(relx=0.015,rely=0.03,relwidth=0.97,relheight=0.9)
    heframe1=Label(heading1,bg="white",image=hf1)
    heframe1.place(relx=0,rely=0.15,relwidth=1,relheight=1)

    fra1=Frame(box1,bg="#1745AD") #option heading border
    fra1.place(relx=0,rely=0,relwidth=1,relheight=0.125)

    frame1=Frame(fra1,bg="#1745AD")
    frame1.place(relx=0.01,rely=0.1,relwidth=0.98,relheight=0.9)
    frabel1=Label(frame1,bg="#1745AD",image=hf2)
    frabel1.place(relx=0,rely=0.09,relwidth=1,relheight=1)




    frame2=Frame(box1,bg="white")
    frame2.place(relx=0,rely=0.125,relwidth=1,relheight=0.125)
    frameb2 = Frame(box1, bg="black")
    frameb2.place(relx=0, rely=0.125, relwidth=1, relheight=0.125)
    frame3=Frame(box1,bg="white")
    frame3.place(relx=0,rely=0.25,relwidth=1,relheight=0.125)
    frameb3=Frame(box1,bg="white")
    frameb3.place(relx=0,rely=0.25,relwidth=1,relheight=0.125)
    frame4=Frame(box1,bg="white")
    frame4.place(relx=0,rely=0.375,relwidth=1,relheight=0.125)
    frameb4=Frame(box1,bg="white")
    frameb4.place(relx=0,rely=0.375,relwidth=1,relheight=0.125)
    frame5=Frame(box1,bg="white")
    frame5.place(relx=0,rely=0.5,relwidth=1,relheight=0.125)
    frameb5=Frame(box1,bg="white")
    frameb5.place(relx=0,rely=0.5,relwidth=1,relheight=0.125)
    frame6=Frame(box1,bg="white")
    frame6.place(relx=0,rely=0.625,relwidth=1,relheight=0.125)
    frameb6=Frame(box1,bg="white")
    frameb6.place(relx=0,rely=0.625,relwidth=1,relheight=0.125)

    fra7=Frame(box1,bg="#1745AD") #button background
    fra7.place(relx=0,rely=0.75,relwidth=1,relheight=0.125)

    frame7=Frame(fra7,bg="white")
    frame7.place(relx=0.01,rely=0.1,relwidth=0.98,relheight=0.8)

    fra8=Frame(box1,bg="white") #bottom border line 2
    fra8.place(relx=0,rely=0.875,relwidth=1,relheight=0.125)

    frame8=Frame(fra8,bg="#C2C2FF") #space for label
    frame8.place(relx=0,rely=0,relwidth=1,relheight=0.9)


    h1=Label(head1,text="Feedback form",bg="#002577",fg="white",font="BigJohn 13 bold")
    h1.pack(expand="True",fill="both",side="top")
    h2=Label(head2,text="KINDLY CO-OPERATE!",bg="#DDDDDD",fg="#002577",font="Cambria 15 bold")
    h2.pack(fill="both",side="left")
    h3=Label(head3,text="""Everyone  must  excercise the  right  to vote and your  vote will be of paramount value.Now that you have casted 
your vote, Kindly  provide  your  feedback  regarding  the  candidate  you  have  voted  for  and  give  your review
about the election process.You are required to rate the candidate on the basis of their election campaign and give 
your suggestions to your chosen candidate and express your expectations from them.""",bg="#DDDDDD",fg="#002577",justify="left",font="Cambria 11")
    h3.pack(side="left",fill="both")
    h4=Label(head4,text="Kindly provide your feedback about the chosen candidate by answering the questions given below:",bg="#DDDDDD",fg="#002577",font="Cambria 12 bold")
    h4.pack(fill="both",side="left")

    feedback1 = StringVar()
    feedback1.set("Average")
    feedback2 = StringVar()
    feedback2.set("Average")
    feedback3 = StringVar()
    feedback3.set("Average")
    feedback4 = StringVar()
    feedback4.set("Average")
    feedback5 = StringVar()
    feedback5.set("Average")

    text1=Label(heading1, text="QUESTIONS",bg="#1745AD",fg="white",font="BigJohn 12").pack(side="top",expand="True")

    label1=Label(frame1,text="Worst",bg="white",fg="#002577",font="BigJohn 12").pack(side="left",expand="true")
    label2=Label(frame1,text="Bad",bg="white",fg="#002577",font="BigJohn 12").pack(side="left",expand="true")
    label3=Label(frame1,text="Average",bg="white",fg="#002577",font="BigJohn 12").pack(side="left",expand="true")
    label4=Label(frame1,text="Good",bg="white",fg="#002577",font="BigJohn 12").pack(side="left",expand="true")
    label5=Label(frame1,text="Best",bg="white",fg="#002577",font="BigJohn 12").pack(side="left",expand="true")

    text2=Label(vertical1, text="How was the election campaign of your chosen candidate?",bg="white",fg="#002577",font="Cambria 11").pack(side="top",fill="both",expand="true")

    r1=Radiobutton(frame2, text="", variable=feedback1, value="Worst",selectcolor="white",bg="#1745AD",fg="#002577",borderwidth=0)
    r1.pack(side="left",fill="both",expand="true")
    r2=Radiobutton(frame2, text="", variable=feedback1, value="Bad",selectcolor="white",bg="#1745AD",fg="#002577",borderwidth=0)
    r2.pack(side="left",fill="both",expand="true")
    r3=Radiobutton(frame2, text="", variable=feedback1, value="Average",selectcolor="white",bg="#1745AD",fg="#002577",borderwidth=0)
    r3.pack(side="left",fill="both",expand="true")
    r4=Radiobutton(frame2, text="", variable=feedback1, value="Good",selectcolor="white",bg="#1745AD",fg="#002577",borderwidth=0)
    r4.pack(side="left",fill="both",expand="true")
    r5=Radiobutton(frame2, text="", variable=feedback1, value="Best",selectcolor="white",bg="#1745AD",fg="#002577",borderwidth=0)
    r5.pack(side="left",fill="both",expand="true")

    rbut1=Button(frameb2,bg="#1745AD",image=radio1,relief="flat",bd=0,activebackground='#002577')
    rbut1.pack(side="left",fill="both",expand="true")
    rbut2=Button(frameb2,bg="#1745AD",image=radio1,relief="flat",bd=0,activebackground='#002577')
    rbut2.pack(side="left",fill="both",expand="true")
    rbut3=Button(frameb2,bg="#1745AD",image=radiot,relief="flat",bd=0,activebackground='#002577')
    rbut3.pack(side="left",fill="both",expand="true")
    rbut4=Button(frameb2,bg="#1745AD",image=radio1,relief="flat",bd=0,activebackground='#002577')
    rbut4.pack(side="left",fill="both",expand="true")
    rbut5=Button(frameb2,bg="#1745AD",image=radio1,relief="flat",bd=0,activebackground='#002577')
    rbut5.pack(side="left",fill="both",expand="true")


    rbut1.bind('<Enter>',hoveronr1)
    rbut1.bind('<Leave>',hoveroffr1)
    rbut1.bind('<Button>', clickb1)
    rbut1.bind('<ButtonRelease>', releaseb1)
    rbut2.bind('<Enter>',hoveronr2)
    rbut2.bind('<Leave>',hoveroffr2)
    rbut2.bind('<Button>', clickb2)
    rbut2.bind('<ButtonRelease>', releaseb2)
    rbut3.bind('<Enter>',hoveronr3)
    rbut3.bind('<Leave>',hoveroffr3)
    rbut3.bind('<Button>', clickb3)
    rbut3.bind('<ButtonRelease>', releaseb3)
    rbut4.bind('<Enter>',hoveronr4)
    rbut4.bind('<Leave>',hoveroffr4)
    rbut4.bind('<Button>', clickb4)
    rbut4.bind('<ButtonRelease>', releaseb4)
    rbut5.bind('<Enter>',hoveronr5)
    rbut5.bind('<Leave>',hoveroffr5)
    rbut5.bind('<Button>', clickb5)
    rbut5.bind('<ButtonRelease>', releaseb5)

    text3=Label(vertical2, text="Your chosen candidate's conduct is:",bg="#DDDDDD",fg="#002577",font="Cambria 11").pack(side="top",fill="both",expand="true")

    r6=Radiobutton(frame3, text="", variable=feedback2, value="Worst",selectcolor="white",bg="#002577",fg="#1745AD",borderwidth=0,activebackground="#1745AD",activeforeground="#FFFFFF")
    r6.pack(side="left",fill="both",expand="true")
    r7=Radiobutton(frame3, text="", variable=feedback2, value="Bad",selectcolor="white",bg="#002577",fg="#1745AD",borderwidth=0,activebackground="#1745AD",activeforeground="#FFFFFF")
    r7.pack(side="left",fill="both",expand="true")
    r8=Radiobutton(frame3, text="", variable=feedback2, value="Average",selectcolor="white",bg="#002577",fg="#1745AD",borderwidth=0,activebackground="#1745AD",activeforeground="#FFFFFF")
    r8.pack(side="left",fill="both",expand="true")
    r9=Radiobutton(frame3, text="", variable=feedback2, value="Good",selectcolor="white",bg="#002577",fg="#1745AD",borderwidth=0,activebackground="#1745AD",activeforeground="#FFFFFF")
    r9.pack(side="left",fill="both",expand="true")
    r10=Radiobutton(frame3, text="", variable=feedback2, value="Best",selectcolor="white",bg="#002577",fg="#1745AD",borderwidth=0,activebackground="#1745AD",activeforeground="#FFFFFF")
    r10.pack(side="left",fill="both",expand="true")

    rbut6=Button(frameb3,bg="#002577",image=radio2,relief="flat",bd=0,activebackground='#1745AD')
    rbut6.pack(side="left",fill="both",expand="true")
    rbut7=Button(frameb3,bg="#002577",image=radio2,relief="flat",bd=0,activebackground='#1745AD')
    rbut7.pack(side="left",fill="both",expand="true")
    rbut8=Button(frameb3,bg="#002577",image=radiot,relief="flat",bd=0,activebackground='#1745AD')
    rbut8.pack(side="left",fill="both",expand="true")
    rbut9=Button(frameb3,bg="#002577",image=radio2,relief="flat",bd=0,activebackground='#1745AD')
    rbut9.pack(side="left",fill="both",expand="true")
    rbut10=Button(frameb3,bg="#002577",image=radio2,relief="flat",bd=0,activebackground='#1745AD')
    rbut10.pack(side="left",fill="both",expand="true")


    rbut6.bind('<Enter>',hoveronr6)
    rbut6.bind('<Leave>',hoveroffr6)
    rbut6.bind('<Button>', clickb6)
    rbut6.bind('<ButtonRelease>', releaseb6)
    rbut7.bind('<Enter>',hoveronr7)
    rbut7.bind('<Leave>',hoveroffr7)
    rbut7.bind('<Button>', clickb7)
    rbut7.bind('<ButtonRelease>', releaseb7)
    rbut8.bind('<Enter>',hoveronr8)
    rbut8.bind('<Leave>',hoveroffr8)
    rbut8.bind('<Button>', clickb8)
    rbut8.bind('<ButtonRelease>', releaseb8)
    rbut9.bind('<Enter>',hoveronr9)
    rbut9.bind('<Leave>',hoveroffr9)
    rbut9.bind('<Button>', clickb9)
    rbut9.bind('<ButtonRelease>', releaseb9)
    rbut10.bind('<Enter>',hoveronr10)
    rbut10.bind('<Leave>',hoveroffr10)
    rbut10.bind('<Button>', clickb10)
    rbut10.bind('<ButtonRelease>', releaseb10)


    text4=Label(vertical3, text="What was the level of co-operation of the candidate with you?",bg="white",fg="#002577",font="Cambria 11").pack(side="top",fill="both",expand="true")

    r11=Radiobutton(frame4, text="", variable=feedback3, value="Worst",selectcolor="white",bg="#1745AD",fg="#002577",borderwidth=0,activebackground="#002577",activeforeground="#FFFFFF")
    r11.pack(side="left",fill="both",expand="true")
    r12=Radiobutton(frame4, text="", variable=feedback3, value="Bad",selectcolor="white",bg="#1745AD",fg="#002577",borderwidth=0,activebackground="#002577",activeforeground="#FFFFFF")
    r12.pack(side="left",fill="both",expand="true")
    r13=Radiobutton(frame4, text="", variable=feedback3, value="Average",selectcolor="white",bg="#1745AD",fg="#002577",borderwidth=0,activebackground="#002577",activeforeground="#FFFFFF")
    r13.pack(side="left",fill="both",expand="true")
    r14=Radiobutton(frame4, text="", variable=feedback3, value="Good",selectcolor="white",bg="#1745AD",fg="#002577",borderwidth=0,activebackground="#002577",activeforeground="#FFFFFF")
    r14.pack(side="left",fill="both",expand="true")
    r15=Radiobutton(frame4, text="", variable=feedback3, value="Best",selectcolor="white",bg="#1745AD",fg="#002577",borderwidth=0,activebackground="#002577",activeforeground="#FFFFFF")
    r15.pack(side="left",fill="both",expand="true")

    rbut11=Button(frameb4,bg="#1745AD",image=radio1,relief="flat",bd=0,activebackground='#002577')
    rbut11.pack(side="left",fill="both",expand="true")
    rbut12=Button(frameb4,bg="#1745AD",image=radio1,relief="flat",bd=0,activebackground='#002577')
    rbut12.pack(side="left",fill="both",expand="true")
    rbut13=Button(frameb4,bg="#1745AD",image=radiot,relief="flat",bd=0,activebackground='#002577')
    rbut13.pack(side="left",fill="both",expand="true")
    rbut14=Button(frameb4,bg="#1745AD",image=radio1,relief="flat",bd=0,activebackground='#002577')
    rbut14.pack(side="left",fill="both",expand="true")
    rbut15=Button(frameb4,bg="#1745AD",image=radio1,relief="flat",bd=0,activebackground='#002577')
    rbut15.pack(side="left",fill="both",expand="true")


    rbut11.bind('<Enter>',hoveronr11)
    rbut11.bind('<Leave>',hoveroffr11)
    rbut11.bind('<Button>', clickb11)
    rbut11.bind('<ButtonRelease>', releaseb11)
    rbut12.bind('<Enter>',hoveronr12)
    rbut12.bind('<Leave>',hoveroffr12)
    rbut12.bind('<Button>', clickb12)
    rbut12.bind('<ButtonRelease>', releaseb12)
    rbut13.bind('<Enter>',hoveronr13)
    rbut13.bind('<Leave>',hoveroffr13)
    rbut13.bind('<Button>', clickb13)
    rbut13.bind('<ButtonRelease>', releaseb13)
    rbut14.bind('<Enter>',hoveronr14)
    rbut14.bind('<Leave>',hoveroffr14)
    rbut14.bind('<Button>', clickb14)
    rbut14.bind('<ButtonRelease>', releaseb14)
    rbut15.bind('<Enter>',hoveronr15)
    rbut15.bind('<Leave>',hoveroffr15)
    rbut15.bind('<Button>', clickb15)
    rbut15.bind('<ButtonRelease>', releaseb15)


    text5=Label(vertical4, text="How smooth was the election process?",bg="#DDDDDD",fg="#002577",font="Cambria 11").pack(side="top",fill="both",expand="true")

    r16=Radiobutton(frame5, text="", variable=feedback4, value="Worst",selectcolor="white",bg="#002577",fg="#1745AD",borderwidth=0,activebackground="#1745AD",activeforeground="#FFFFFF")
    r16.pack(side="left",fill="both",expand="true")
    r17=Radiobutton(frame5, text="", variable=feedback4, value="Bad",selectcolor="white",bg="#002577",fg="#1745AD",borderwidth=0,activebackground="#1745AD",activeforeground="#FFFFFF")
    r17.pack(side="left",fill="both",expand="true")
    r18=Radiobutton(frame5, text="", variable=feedback4, value="Average",selectcolor="white",bg="#002577",fg="#1745AD",borderwidth=0,activebackground="#1745AD",activeforeground="#FFFFFF")
    r18.pack(side="left",fill="both",expand="true")
    r19=Radiobutton(frame5, text="", variable=feedback4, value="Good",selectcolor="white",bg="#002577",fg="#1745AD",borderwidth=0,activebackground="#1745AD",activeforeground="#FFFFFF")
    r19.pack(side="left",fill="both",expand="true")
    r20=Radiobutton(frame5, text="", variable=feedback4, value="Best",selectcolor="white",bg="#002577",fg="#1745AD",borderwidth=0,activebackground="#1745AD",activeforeground="#FFFFFF")
    r20.pack(side="left",fill="both",expand="true")

    rbut16 = Button(frameb5, bg="#002577", image=radio2, relief="flat", bd=0, activebackground='#1745AD')
    rbut16.pack(side="left", fill="both", expand="true")
    rbut17 = Button(frameb5, bg="#002577", image=radio2, relief="flat", bd=0, activebackground='#1745AD')
    rbut17.pack(side="left", fill="both", expand="true")
    rbut18 = Button(frameb5, bg="#002577", image=radiot, relief="flat", bd=0, activebackground='#1745AD')
    rbut18.pack(side="left", fill="both", expand="true")
    rbut19 = Button(frameb5, bg="#002577", image=radio2, relief="flat", bd=0, activebackground='#1745AD')
    rbut19.pack(side="left", fill="both", expand="true")
    rbut20 = Button(frameb5, bg="#002577", image=radio2, relief="flat", bd=0, activebackground='#1745AD')
    rbut20.pack(side="left", fill="both", expand="true")

    rbut16.bind('<Enter>', hoveronr16)
    rbut16.bind('<Leave>', hoveroffr16)
    rbut16.bind('<Button>', clickb16)
    rbut16.bind('<ButtonRelease>', releaseb16)
    rbut17.bind('<Enter>', hoveronr17)
    rbut17.bind('<Leave>', hoveroffr17)
    rbut17.bind('<Button>', clickb17)
    rbut17.bind('<ButtonRelease>', releaseb17)
    rbut18.bind('<Enter>', hoveronr18)
    rbut18.bind('<Leave>', hoveroffr18)
    rbut18.bind('<Button>', clickb18)
    rbut18.bind('<ButtonRelease>', releaseb18)
    rbut19.bind('<Enter>', hoveronr19)
    rbut19.bind('<Leave>', hoveroffr19)
    rbut19.bind('<Button>', clickb19)
    rbut19.bind('<ButtonRelease>', releaseb19)
    rbut20.bind('<Enter>', hoveronr20)
    rbut20.bind('<Leave>', hoveroffr20)
    rbut20.bind('<Button>', clickb20)
    rbut20.bind('<ButtonRelease>', releaseb20)


    text6=Label(vertical5, text="Your expectation from the chosen candidate are:",bg="white",fg="#002577",font="Cambria 11").pack(side="top",fill="both",expand="true")

    r21=Radiobutton(frame6, text="", variable=feedback5, value="Worst",selectcolor="white",bg="#1745AD",fg="#002577",borderwidth=0,activebackground="#002577",activeforeground="#FFFFFF")
    r21.pack(side="left",fill="both",expand="true")
    r22=Radiobutton(frame6, text="", variable=feedback5, value="Bad",selectcolor="white",bg="#1745AD",fg="#002577",borderwidth=0,activebackground="#002577",activeforeground="#FFFFFF")
    r22.pack(side="left",fill="both",expand="true")
    r23=Radiobutton(frame6, text="", variable=feedback5, value="Average",selectcolor="white",bg="#1745AD",fg="#002577",borderwidth=0,activebackground="#002577",activeforeground="#FFFFFF")
    r23.pack(side="left",fill="both",expand="true")
    r24=Radiobutton(frame6, text="", variable=feedback5, value="Good",selectcolor="white",bg="#1745AD",fg="#002577",borderwidth=0,activebackground="#002577",activeforeground="#FFFFFF")
    r24.pack(side="left",fill="both",expand="true")
    r25=Radiobutton(frame6, text="", variable=feedback5, value="Best",selectcolor="white",bg="#1745AD",fg="#002577",borderwidth=0,activebackground="#002577",activeforeground="#FFFFFF")
    r25.pack(side="left",fill="both",expand="true")

    rbut21=Button(frameb6,bg="#1745AD",image=radio1,relief="flat",bd=0,activebackground='#002577')
    rbut21.pack(side="left",fill="both",expand="true")
    rbut22=Button(frameb6,bg="#1745AD",image=radio1,relief="flat",bd=0,activebackground='#002577')
    rbut22.pack(side="left",fill="both",expand="true")
    rbut23=Button(frameb6,bg="#1745AD",image=radiot,relief="flat",bd=0,activebackground='#002577')
    rbut23.pack(side="left",fill="both",expand="true")
    rbut24=Button(frameb6,bg="#1745AD",image=radio1,relief="flat",bd=0,activebackground='#002577')
    rbut24.pack(side="left",fill="both",expand="true")
    rbut25=Button(frameb6,bg="#1745AD",image=radio1,relief="flat",bd=0,activebackground='#002577')
    rbut25.pack(side="left",fill="both",expand="true")


    rbut21.bind('<Enter>',hoveronr21)
    rbut21.bind('<Leave>',hoveroffr21)
    rbut21.bind('<Button>', clickb21)
    rbut21.bind('<ButtonRelease>', releaseb21)
    rbut22.bind('<Enter>',hoveronr22)
    rbut22.bind('<Leave>',hoveroffr22)
    rbut22.bind('<Button>', clickb22)
    rbut22.bind('<ButtonRelease>', releaseb22)
    rbut23.bind('<Enter>',hoveronr23)
    rbut23.bind('<Leave>',hoveroffr23)
    rbut23.bind('<Button>', clickb23)
    rbut23.bind('<ButtonRelease>', releaseb23)
    rbut24.bind('<Enter>',hoveronr24)
    rbut24.bind('<Leave>',hoveroffr24)
    rbut24.bind('<Button>', clickb24)
    rbut24.bind('<ButtonRelease>', releaseb24)
    rbut25.bind('<Enter>',hoveronr25)
    rbut25.bind('<Leave>',hoveroffr25)
    rbut25.bind('<Button>', clickb25)
    rbut25.bind('<ButtonRelease>', releaseb25)


    myButton = Button(frame7,text="Select option",command=lambda:[output(feedback1.get(),feedback2.get(),feedback3.get(),feedback4.get(),feedback5.get())],relief="flat",borderwidth=0,bg="#1745AD",activebackground="#1745AD",image=btf1,font="Cambria 15 bold")
    myButton.pack(side="left",fill="both",expand="true")
    myButton.bind('<Enter>',hoveron2)
    myButton.bind('<Leave>',hoveroff2)
    myButton.bind('<Button>', click2)
    myButton.bind('<ButtonRelease>', release2)

    dis1=Label(desc1,text="If you have any suggestions for the candidate, feel free to tell us: ",bg="#DDDDDD",fg="#002577",font="Cambria 10 bold")
    dis1.pack(side="left",fill="both")

    feed=StringVar()
    dis2=ScrolledText(desc2,bg="white",fg="#002577",relief="flat",borderwidth=0,selectbackground="#8796CB",selectforeground="white")
    dis2.pack(side="left",expand="True",fill="both")
    dis4=Label(desc4,text="Thankyou for your valuable feedback ",bg="#002577",fg="white",font="Helvetica 10 bold")
    dis4.pack(side="left",expand="True",fill="both")

    buttondis = Button(desc3,text="Submit",relief="flat",borderwidth=0,bg="white",activebackground="white",font="Cambria 16 bold",image=btf2,command=submit)
    buttondis.pack(side="left",fill="both",expand="true")

    buttondis.bind('<Enter>',hoveron1)
    buttondis.bind('<Leave>',hoveroff1)
    buttondis.bind('<Button>', click1)
    buttondis.bind('<ButtonRelease>', release1)


    root.mainloop()
    return

