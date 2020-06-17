from PyQt5.QtCore import QLine
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import pyqrcode
import png
import win32ctypes
from pyzbar.pyzbar import decode
from PIL import Image
#from pyqrcode import QRCode
#py abdelmajid el-boussidi

app=QApplication(sys.argv)
windo=QTabWidget()
windo.setWindowIcon(QIcon('home.ico'))
windo.setFixedSize(300,400)
windo.setWindowTitle('QRCode')

tab1=QWidget()
tab2=QWidget()
tab3=QWidget()

windo.addTab(tab1,'Créer')
windo.addTab(tab2,'Décoder QR')
windo.addTab(tab3,'À propos ')

txt=QLineEdit(tab1)
txt.move(20,60)
txt.resize(240,30)
txt.setPlaceholderText('veuillez saisir un texte')

name=QLineEdit(tab1)
name.resize(240,30)
name.move(20,110)
name.setPlaceholderText("Nommez l'image")

save=QLineEdit(tab1)
save.resize(182,30)
save.move(20,160)
save.setPlaceholderText('Choisissez un emplacement ')

brs=QPushButton('Choisir',tab1)
brs.resize(55,30)
brs.move(205,160)
brs.setIcon(QIcon('rech.ico'))

creat=QPushButton('Créer',tab1)
creat.move(40,240)
creat.resize(200,30)
creat.setIcon(QIcon('accept.png'))


show=QPushButton('Regarder',tab1)
show.move(40,290)
show.setIcon(QIcon('rega.ico'))
show.resize(200,30)
show.hide()

lbl=QLabel(tab1)
lbl.move(50,0)
lbl.hide()

masar=QLineEdit(tab1)
masar.resize(240,30)
masar.move(30,210)
masar.hide()

ret1=QPushButton('Créer un nouveau',tab1)
ret1.resize(130,30)
ret1.hide()
ret1.setIcon(QIcon('add2.ico'))
ret1.move(80,260)

#codage
def location():
    save.setText(QFileDialog.getExistingDirectory(tab1,"l'emplacement de l'image"))

def creatqr():
    data = txt.text()
    na=name.text()
    local=save.text()
    ex='.png'
    full=local+'/'+na+ex
    qr=pyqrcode.create(data)
    qr.png(full,scale=6)
    msg=QMessageBox.information(tab1,'Succès','Votre code a été créé avec succès')
    show.show()

def show1():
    data = txt.text()
    na = name.text()
    local = save.text()
    ex = '.png'
    full = local + '/' +na+ex
    img = QPixmap(full).scaled(160,160)
    txt.hide()
    name.hide()
    save.hide()
    brs.hide()
    creat.hide()
    lbl.setPixmap(img)
    lbl.show()
    masar.setText(full)
    masar.show()
    lbl.resize(250,250)
    show.hide()
    ret1.show()
def ret():
    txt.show()
    name.show()
    save.show()
    brs.show()
    creat.show()
    lbl.hide()
    masar.hide()
    txt.setText("")
    name.setText("")
    save.setText("")
    ret1.hide()

brs.clicked.connect(location)
creat.clicked.connect(creatqr)
show.clicked.connect(show1)
ret1.clicked.connect(ret)

#tab2


lien=QLineEdit(tab2)
lien.resize(190,30)
lien.move(20,100)
lien.setPlaceholderText("Entrez l'emplacement de l'image")

bread=QPushButton('Choisir',tab2)
bread.resize(55,30)
bread.move(215,100)


red=QPushButton('Décoder',tab2)
red.move(40,180)
red.resize(200,30)
red.setIcon(QIcon('rech.ico'))

lbimg=QLabel(tab2)
lbimg.hide()
lbimg.resize(160,140)
lbimg.move(60,10)

lbl1=QLabel('Contenu :',tab2)
lbl1.hide()
lbl1.move(90,180)
lbl1.setStyleSheet('font-size:13pt;color:blue;')

lbl2=QLineEdit(tab2)
lbl2.hide()
lbl2.resize(260,30)
lbl2.move(20,210)
lbl2.setStyleSheet('font-size:12pt;color:black;')


new=QPushButton('Lisez un autre',tab2)
new.move(40,290)
new.resize(200,30)
new.hide()
new.setIcon(QIcon('add2.ico'))
def gitnam():
    url=QFileDialog.getOpenFileName()
    #print(url[0])
    lien.setText(url[0])

def read():
    lie=lien.text()
    lien.hide()
    red.hide()
    bread.hide()
    rimag=QPixmap(lie).scaled(160,160)
    lbimg.setPixmap(rimag)
    result=decode(Image.open(lie))
    resultfin=result[0].data.decode('ascii')
    lbl2.setText(resultfin)
    lbl1.show()
    lbimg.show()
    lbl2.show()
    new.show()
def rered():
    lbl1.hide()
    lbimg.hide()
    lbl2.hide()
    new.hide()
    lien.show()
    red.show()
    bread.show()
    lien.setText('')

red.clicked.connect(read)
new.clicked.connect(rered)
bread.clicked.connect(gitnam)

#tab3
by=QLabel('by :',tab3)
by.move(50,100)
lblname=QLabel('ABDELMAJID EL BOUSSIDI',tab3)
lblname.move(20,120)
lblname.setStyleSheet('color:blue;font-size:16pt;')

f=QLabel('08/06/2020 | V1,0',tab3)
f.move(100,335)
f.setStyleSheet('font-size:9pt;')

windo.show()
app.exec_()