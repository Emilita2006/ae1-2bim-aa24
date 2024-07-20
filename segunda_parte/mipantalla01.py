from PyQt5 import QtCore, QtGui, QtWidgets
from base_datos import conn


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
       
        self.nombre = QtWidgets.QLineEdit(self.centralwidget)
        self.nombre.setGeometry(QtCore.QRect(140, 30, 113, 23))
        self.nombre.setObjectName("nombre")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 30, 54, 15))
        self.label.setObjectName("label")
       
        self.siglas = QtWidgets.QLineEdit(self.centralwidget)
        self.siglas.setGeometry(QtCore.QRect(140, 60, 113, 23))
        self.siglas.setObjectName("siglas")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(70, 60, 54, 15))
        self.label_1.setObjectName("label_1")

        self.estadio = QtWidgets.QLineEdit(self.centralwidget)
        self.estadio.setGeometry(QtCore.QRect(140, 90, 113, 23))
        self.estadio.setObjectName("estadio")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 90, 54, 15))
        self.label_2.setObjectName("label_2")

        self.seguidores = QtWidgets.QLineEdit(self.centralwidget)
        self.seguidores.setGeometry(QtCore.QRect(140, 120, 113, 23))
        self.seguidores.setObjectName("seguidores")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 120, 54, 15))
        self.label_3.setObjectName("label_3")

        self.campeonato = QtWidgets.QLineEdit(self.centralwidget)
        self.campeonato.setGeometry(QtCore.QRect(140, 150, 113, 23))
        self.campeonato.setObjectName("campeonato")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 150, 54, 15))
        self.label_4.setObjectName("label_4")

        self.guardar = QtWidgets.QPushButton(self.centralwidget)
        self.guardar.setGeometry(QtCore.QRect(70, 200, 211, 21))
        self.guardar.setObjectName("guardar")

        self.actualizar = QtWidgets.QPushButton(self.centralwidget)
        self.actualizar.setGeometry(QtCore.QRect(70, 230, 211, 21))
        self.actualizar.setObjectName("actualizar")

        self.listaEquipos = QtWidgets.QTableWidget(self.centralwidget)
        self.listaEquipos.setGeometry(QtCore.QRect(300, 30, 450, 400))
        self.listaEquipos.setObjectName("listaEquipos")
        self.listaEquipos.setColumnCount(5)
        self.listaEquipos.setRowCount(0)
        self.listaEquipos.setHorizontalHeaderLabels(["Nombre", "Siglas", "Estadio", "Seguidores", "Campeonato"])

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.crear_base()
        self.obtener_informacion()
        self.guardar.clicked.connect(self.guardar_informacion)
        self.actualizar.clicked.connect(self.obtener_informacion)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gestión de Equipos"))
        self.label.setText(_translate("MainWindow", "Nombre"))
        self.label_1.setText(_translate("MainWindow", "Siglas"))
        self.label_2.setText(_translate("MainWindow", "Estadio"))
        self.label_3.setText(_translate("MainWindow", "Seguidores"))
        self.label_4.setText(_translate("MainWindow", "Campeonato"))
        self.guardar.setText(_translate("MainWindow", "Guardar"))
        self.actualizar.setText(_translate("MainWindow", "Actualizar"))

    def crear_base(self):
        cursor = conn.cursor()
        cadena_sql = '''CREATE TABLE IF NOT EXISTS Equipo (
                        nombre TEXT,
                        siglas TEXT,
                        estadio TEXT,
                        seguidores INTEGER,
                        campeonato TEXT)'''
        cursor.execute(cadena_sql)
        conn.commit()
        cursor.close()

    def guardar_informacion(self):
        cursor = conn.cursor()
        nombre = str(self.nombre.text())
        siglas = str(self.siglas.text())
        estadio = str(self.estadio.text())
        seguidores = int(self.seguidores.text())
        campeonato = str(self.campeonato.text())
        cadena_sql = '''INSERT INTO Equipo (nombre, siglas, estadio, seguidores, campeonato)
                        VALUES (?, ?, ?, ?, ?)'''
        cursor.execute(cadena_sql, (nombre, siglas, estadio, seguidores, campeonato))
        conn.commit()
        cursor.close()
        self.obtener_informacion()

    def obtener_informacion(self):
        cursor = conn.cursor()
        cadena_consulta_sql = "SELECT * FROM Equipo"
        cursor.execute(cadena_consulta_sql)
        informacion = cursor.fetchall()
        self.listaEquipos.setRowCount(len(informacion))
        for i, row in enumerate(informacion):
            for j, val in enumerate(row):
                self.listaEquipos.setItem(i, j, QtWidgets.QTableWidgetItem(str(val)))
        cursor.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())