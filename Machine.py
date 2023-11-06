import pickle
import sys
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QApplication, QMessageBox
from PyQt5.QtGui import QDoubleValidator, QFont
from PyQt5.QtCore import Qt, QLine
import joblib

with open('modelo_entrenado', 'rb')as f:
    classi_pickle= pickle.load(f) 

classi_pickle= joblib.load('modelo_entrenado')

class Heart(QWidget):

    def __init__(self) -> None :
        super(Heart, self).__init__()
        
        self.sub_head = QLabel("Registro Paciente")
        self.sub_head.setFont(QFont("Times",24, weight=QFont.Bold))
        self.l0 = QLineEdit()
        self.l1 = QLineEdit()
        self.l2 = QLineEdit()
        self.l3 = QLineEdit()
        self.l4 = QLineEdit()
        self.l5 = QLineEdit()
        self.l6 = QLineEdit()
        self.l7 = QLineEdit()
        self.l8 = QLineEdit()
        self.l9 = QLineEdit()
        self.l10 = QLineEdit()
        self.l11 = QLineEdit()
        self.l12 = QLineEdit()
        self.l13 = QLineEdit()
        
        self.t0 = QLabel("Nombre:")
        self.t1 = QLabel("Edad:")
        self.t2 = QLabel("Sexo:")
        self.t3 = QLabel("Dolor pecho:")
        self.t4 = QLabel("Presión sanguínea:")
        self.t5 = QLabel("Colesterol:")
        self.t6 = QLabel("Nivel azúcar:")
        self.t7 = QLabel("EKG:")
        self.t8 = QLabel("Frecuencia cardíaca:")
        self.t9 = QLabel("Angina:")
        self.t10 = QLabel("Depresión ST:")
        self.t11 = QLabel("Pico segmento ST:")
        self.t12 = QLabel("Vasos coloreados:")
        self.t13 = QLabel("thal (0-1-2):")
     
        self.h1 = QHBoxLayout()
        self.h0 = QHBoxLayout()
        self.h2 = QHBoxLayout()
        self.h3 = QHBoxLayout()
        self.h4 = QHBoxLayout()
        self.h5 = QHBoxLayout()
        self.h6 = QHBoxLayout()
        self.h7 = QHBoxLayout()
        self.h8 = QHBoxLayout()
        self.h9 = QHBoxLayout()
        self.h10 = QHBoxLayout()
        self.h11 = QHBoxLayout()
        self.h12 = QHBoxLayout()
        self.h13 = QHBoxLayout()
        self.clbtn = QPushButton("LIMPIAR")
        self.clbtn.setFixedWidth(100)
        self.submit = QPushButton("ENVIAR")
        self.submit.setFixedWidth(100)
        self.v1_box = QVBoxLayout()
        self.v2_box = QVBoxLayout()
        self.final_hbox = QHBoxLayout()
        self.initui()
    

    def initui(self) -> None:
        """ Interfaz gráfica"""
        self.v1_box.addWidget(self.sub_head)
        self.v1_box.addSpacing(10)
        self.v1_box.setSpacing(5)
        self.l1.setValidator(QDoubleValidator())
        self.l2.setValidator(QDoubleValidator())
        self.l3.setValidator(QDoubleValidator())
        self.l4.setValidator(QDoubleValidator())
        self.l5.setValidator(QDoubleValidator())
        self.l6.setValidator(QDoubleValidator())
        self.l7.setValidator(QDoubleValidator())
        self.l8.setValidator(QDoubleValidator())
        self.l9.setValidator(QDoubleValidator())
        self.l10.setValidator(QDoubleValidator())
        self.l11.setValidator(QDoubleValidator())
        self.l12.setValidator(QDoubleValidator())
        self.l13.setValidator(QDoubleValidator())
        self.l0.setToolTip("Ingrese su nombre:")
        self.l1.setToolTip("Ingrese edad:")
        self.l2.setToolTip("Sexo[1-Masculino/ 0-Femenino]")
        self.l3.setToolTip("Dolor en pecho[1-leve/4-extremo]:")
        self.l4.setToolTip("Presión sanguínea:")
        self.l5.setToolTip("Colesterol en sangre:")
        self.l6.setToolTip("Azúcar en sangre(0-1):")
        self.l7.setToolTip("EKG (0,1,2): ")
        self.l8.setToolTip("Frecuencia cardíaca:")
        self.l9.setToolTip("Angina por ejercicio[1-Dolor/ 0-Sin dolor]")
        self.l10.setToolTip("Depresión ST ")
        self.l11.setToolTip("Pico segmento ST")
        self.l12.setToolTip("Vasos coloreados(0-3) ")
        self.l13.setToolTip("Thal (0-1-2)")
        self.l0.setFixedSize(265, 30)
        self.l1.setFixedSize(265,30)
        self.l2.setFixedSize(265,30)
        self.l3.setFixedSize(265,30)
        self.l4.setFixedSize(265,30)
        self.l5.setFixedSize(265,30)
        self.l6.setFixedSize(265,30)
        self.l7.setFixedSize(265,30)
        self.l8.setFixedSize(265,30)
        self.l9.setFixedSize(265,30)
        self.l10.setFixedSize(265,30)
        self.l11.setFixedSize(265,30)
        self.l12.setFixedSize(265,30)
        self.l13.setFixedSize(265,30)
        self.h0.addWidget(self.t0)
        self.h0.addWidget(self.l0)
        self.v1_box.addLayout(self.h0)
        self.h1.addWidget(self.t1)
        self.h1.addWidget(self.l1)
               
        self.v1_box.addLayout(self.h1)
        self.h2.addWidget(self.t2)
        self.h2.addWidget(self.l2)
              
        self.v1_box.addLayout(self.h2)
        self.h3.addWidget(self.t3)
        self.h3.addWidget(self.l3)
              
        self.v1_box.addLayout(self.h3)
        self.h4.addWidget(self.t4)
        self.h4.addWidget(self.l4)
             
        self.v1_box.addLayout(self.h4)
        self.h5.addWidget(self.t5)
        self.h5.addWidget(self.l5)
        self.v1_box.addLayout(self.h5)
        self.h6.addWidget(self.t6)
        self.h6.addWidget(self.l6)
               
        self.v1_box.addLayout(self.h6)
        self.h7.addWidget(self.t7)
        self.h7.addWidget(self.l7)
              
        self.v1_box.addLayout(self.h7)
        self.h8.addWidget(self.t8)
        self.h8.addWidget(self.l8)
              
        self.v1_box.addLayout(self.h8)
        self.h9.addWidget(self.t9)
        self.h9.addWidget(self.l9)
             
        self.v1_box.addLayout(self.h9)
        self.h10.addWidget(self.t10)
        self.h10.addWidget(self.l10)
        self.v1_box.addLayout(self.h10)
        self.h11.addWidget(self.t11)
        self.h11.addWidget(self.l11)
        self.v1_box.addLayout(self.h11)
        self.h12.addWidget(self.t12)
        self.h12.addWidget(self.l12)
        self.v1_box.addLayout(self.h12)
        self.h13.addWidget(self.t13)
        self.h13.addWidget(self.l13)
              
        self.v1_box.addLayout(self.h13)
        self.h14 = QHBoxLayout()
        self.submit.clicked.connect(lambda: self.test_input())
        self.submit.setToolTip("Dale click para ver si tiene probabilidad de sufrir un ataque cardiaco")
        self.clbtn.clicked.connect(lambda: self.clfn())
        self.h14.addWidget(self.submit)
        self.h14.addWidget(self.clbtn)
        self.v1_box.addLayout(self.h14)
        self.report_ui()
        self.final_hbox.addLayout(self.v1_box)
        self.final_hbox.addSpacing(40)
        self.final_hbox.addLayout(self.v2_box)
        self.setLayout(self.final_hbox)

    def report_ui(self):
        self.v2_box.setSpacing(6)
        self.report_subhead = QLabel("Modelo Info.")
        self.report_subhead.setAlignment(Qt.AlignCenter)
        self.report_subhead.setFont(QFont("Times",24, weight=QFont.Bold))
        self.v2_box.addWidget(self.report_subhead)
        self.details = QLabel("Este modelo usa Vector Machine\nAccuracy: 81%.")
        self.details.setFont(QFont("Arial",14, weight=QFont.Bold))
        self.details.setAlignment(Qt.AlignLeft)
        self.details.setWordWrap(True)
        self.model_details = QLabel("Completa las casillas y presiona enviar para ver el resultado.")
        self.model_details.setWordWrap(True)
        self.v2_box.addWidget(self.details)
        self.results = QLabel(" ")
        self.results.setWordWrap(True)
        self.v2_box.addWidget(self.results)
        self.v2_box.addWidget(self.model_details)

    def clfn(self):
        """ Boton clear"""
        self.l0.clear()
        self.l1.clear()
        self.l2.clear()
        self.l3.clear()
        self.l3.clear()
        self.l4.clear()
        self.l5.clear()
        self.l6.clear()
        self.l7.clear()
        self.l8.clear()
        self.l9.clear()
        self.l10.clear()
        self.l11.clear()
        self.l12.clear()
        self.l13.clear()
        self.report_subhead.setText("Registro")
        self.model_details.setText("Completa las casillas y presiona enviar para ver el resultado.")
        self.results.setText(" ")
        self.details.setText("Este modelo usa Vector Machine\nAccuracy: 81%.")
      

    def test_input(self) -> None:
        """ test para enfermedad cardiaca"""
        my_dict = {"edad":float(self.l1.text()), "sexo":float(self.l2.text()),"dolor pecho":float(self.l3.text()), "Presión sanguínea":float(self.l4.text()), "colesterol": float(self.l5.text()),"azucar":float(self.l6.text()), "EKG":float(self.l7.text()),"FC":float(self.l8.text()), "angina":float(self.l9.text()), "ST": float(self.l10.text()),"Pico ST":float(self.l11.text()), "Vasos":float(self.l12.text()),"thal":float(self.l13.text())}


        output = modelo_entrenado.check_input(my_dict)
        
        self.report_subhead.setText("Reporte")
        self.model_details.setText("Este modelo usa Vector Machine\nAccuracy: 81%.")
        self.details.setText("Nombre: {}\n Edad: {}\nSexo: {}\nDolor pecho: {}\nPresión sanguínea: {}\ncolesterol: {}\nazucar:{}\nEKG:{}\nFC:{}\nangina:{}\nST:{}\nPico ST:{}\nVasos:{}\nthal:{}\n".format(self.l0.text(), self.l1.text(), self.l2.text(), self.l3.text(),self.l4.text(),self.l5.text(),self.l6.text(), self.l7.text(), self.l8.text(), self.l9.text(),self.l10.text(),self.l11.text(),self.l12.text(), self.l13.text()))
        
        if output==0:
            self.results.setText("Sugiere probabilidad de ataque cardiaco.")
        else:
            self.results.setText("Sgerente de enfermedad cardiaca, visite a su doctor")
        self.results.setFont(QFont("Arial",14, weight=QFont.Bold))

    def mwindow(self) -> None:
        """ window """
        self.setFixedSize(898, 422)
        self.setWindowTitle("Predicción Ataque Cardiaco")
        self.show()


if __name__=="__main__":
    app = QApplication(sys.argv)
    a_window = Heart()
    a_window.mwindow()
    sys.exit(app.exec_())