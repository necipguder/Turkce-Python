# -*- coding: cp1254 -*-
from Tkinter import *


line=10
unv={}
import os
import sys

from cStringIO import StringIO
from ModifiedTkinterConsole import *

def Ana(fbuf,pfbuf=""):   # ismi belirlenmiş dosyaya yazılır.
    s=fbuf.split("\n")
    
    tab=0
    for itm in s:
        if (itm=="bit"):
            tab-=1
            itm=""
        m = re.match( r'(\t*)(.*)ise\S*', itm, re.M|re.I)
        ng = re.match( r'(\t*)(.*)girdi(.*)', itm, re.M|re.I)
        n = re.match( r'(\t*)(.*)\S*bir\W*liste\S*', itm, re.M|re.I)
        ns = re.match( r'(\t*)(.*)\S*bir\W*sözlük\S*', itm, re.M|re.I)
        ne = re.match( r'(\t*)(.*)\S*ekle\S*(.*)', itm, re.M|re.I)
        nm = re.match( r'(\t*)\s*\W*(\w+)\s*(\w*)\s*den\s*(\w*)\s*[ea(ye)]', itm, re.M|re.I)
        mm = re.match( r'(\t*)(.*)\s*d[ae]ki\s*her\s*(\w+)\s*için', itm, re.M|re.I)
        l = re.match( r'(\t*)yaz(.*)', itm, re.M|re.I)
        
        da=re.match( r'(\t*)(\w+)=\s*aç\s*\((\w*,*\w*)\)', itm, re.M|re.I)
        frm=re.match( r'(\t*)(\w+)=\s*form\s*\(\)', itm, re.M|re.I)
        btn=re.match( r'(\t*)(\w+)=\s*bas\s*\((\w*),*\)', itm, re.M|re.I)
        km = re.match( r"(\t*)(.*)\s*uzat\s*(.*)", itm, re.M|re.I)
        fm = re.match( r"(\t*)fonks\s*(\w*)\s*\((\w*,*\w*)\)", itm, re.M|re.I)
        rt = re.match( r"(\t*)dönd[üe]r\s*(.*)", itm, re.M|re.I)
        le = re.match( r'(\t*)(\d+[-\*/\+]\d+)', itm, re.M|re.I)
        if m:
            itm=m.group(1)+"if ("+m.group(2)+"):"
            
        
        elif ng:
            itm=ng.group(1)+ng.group(2)+'raw_input'+ng.group(3)
            
        
        elif n:
            itm=n.group(1)+n.group(2)+'=[]'
        elif ns:
            itm=ns.group(1)+ns.group(2)+'={}'
            
        elif km:
            itm = km.group(2)+'.extend(['+km.group(3)+'])'

        elif frm:
            itm = "from Tkinter import *"+'\n'+frm.group(2)+'='+'Tk()'
        elif btn:
            itm = btn.group(1)+btn.group(2)+'='+'Button('+btn.group(3)+')'
            
        
        elif ne:
            itm=ne.group(1)+ne.group(2)+'.append('+ne.group(3)+')'
            
        
        elif nm:
            itm=nm.group(1)+'for '+nm.group(2)+' in range('+ nm.group(3)+','+nm.group(4)+'):'

        
        elif fm:
            itm=fm.group(1)+'def '+ fm.group(2)+'('+ fm.group(3)+')'+':'

        elif rt:
            itm=rt.group(1)+'return '+ rt.group(2)

        elif mm:
            itm=mm.group(1)+'for '+mm.group(3)+' in '+ mm.group(2)+':'

            
        
        elif l:
            if type(l.group(2)) is list:
                itm=l.group(1)+"for iem in "+l.group(2)+":\n"+l.group(1)+"\t"+'print iem'
            else:
                itm=l.group(1)+'print'+l.group(2)
            
            

        elif le:
            itm=le.group(1)+"print ("+"eval('"+le.group(2)+"'))"
            
        
        pfbuf+=itm+"\n"
    return pfbuf
          
           


def eski(prg="",s=''):
    if (s!=''):
        sx=s.split("\n")
        Ana(prg,sx)
        fl=open(prg,"r")
        flbuf=fl.read()
        T2.delete('1.0','end')
        T2.insert('end',flbuf)
        fl.close()
        

    else:
        try:
            fl=open(prg,"r")
            if fl:
                print "file opened"
                flbuf=fl.read()
                print flbuf
            T2.insert('end',flbuf)
            #Ana(prg,s)
        except:
            sx=s.split("\n")
            print sx
            Ana(prg,sx)
            fl=open(prg,"r")
            T2.delete('1.0','end')
            T2.insert('end',flbuf)
                
                

def konv():
    prg=ent1.get()
    fbuf = T1.get('1.0','end')
    pfbuf=Ana(fbuf)
    T2.delete('1.0','end')
    T2.insert('end',pfbuf)
    kos()
    
def kanv(event):
    prg=ent1.get()
    fbuf = T1.get('1.0','end')
    pfbuf=Ana(fbuf)
    T2.delete('1.0','end')
    T2.insert('end',pfbuf)
    if cvar.get()==1:
        kos()
def e1change(event):
    try:
        btnKyd["text"]="Kaydet"
    except:
        print "no change"    

def kaydet():
    pfbuf = T2.get('1.0','end')
    ptbuf = T1.get('1.0','end')
    
    try:
        fl=open(ent1.get()+".py","w")
        fl.write(pfbuf)
        
        fl.close()
        if flt:
            btnKyd["text"]="Kaydedildi"
    except:
        pass
    try:
        flt=open(ent1.get()+".py.tr","w")
        #print ptbuf
        flt.write(ptbuf.encode('utf8'))
        flt.close()
        if flt:
            btnKyd["text"]="Kaydedildi"
    except:
        print "no kayit"
        
def ykle():
    try:
        fl=open(ent1.get()+".py.tr","r")
        ptbuf=fl.read().decode('utf8')
        T1.insert('end',ptbuf)
        if fl:
            konv()
        fl.close()
        btnYkl["text"]="Yüklendi"
    except:
        btnYkl["text"]="Olmadi"       

def kos():
    c.delete()
    pfbuf = T2.get('1.0','end')
    kaydet()
    c.run(pfbuf)
    
root = Tk()

cvar=IntVar()


BLbl=Label(root,text='T1ürkçe Basic Programlama')
BLbl.grid(row=0,column=1,columnspan=2)
Rchk=Checkbutton(root,text="run",variable=cvar)
cvar.set(1)
T1 = Text(root, height=10, width=40,font=("Helvetica",12))
T2 = Text(root, height=10, width=40,font=("Helvetica",12))
T3= Text(root, height=4, width=80,font=("Helvetica",12))

c = Console(T3,dict={})
c.dict["console"] = c
c.pack(fill=BOTH, expand=1)
#c.master.title("Python Console v%s" % VERSION)





btn=Button(text='Konv',command=konv)
btn2=Button(text='Run',command=kos)
btnKyd=Button(text='Kaydet',command=kaydet)
btnYkl=Button(text='Yükle',command=ykle)
ent1=Entry(root,width=20)
ent1.bind("<Key>",e1change)
T1.bind("<Return>", kanv)

ent1.grid(row=1,column=1)

T1.grid(row=2,column=1)
T2.grid(row=2,column=2)
T3.grid(row=4,column=1,columnspan=2)
btn.grid(row=3,column=1)
btn2.grid(row=3,column=2)
btnKyd.grid(row=1,column=1,sticky=E)
btnYkl.grid(row=1,column=1,sticky=W)
Rchk.grid(row=1,column=2,sticky=E)
stbuf="yaz 'merhaba,'\nyaz 'bu Türkce python '\nyaz 5*8\
\na 1 den 8 e\n\tb 4 den 30 a\n\t\tyaz a,'*',b,'=',a*b"




T1.insert('end',stbuf)

T1.focus_set()



mainloop()
