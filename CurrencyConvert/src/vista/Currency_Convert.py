from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TipoDeCambio(object):
    def setupUi(self, TipoDeCambio):
        TipoDeCambio.setObjectName("TipoDeCambio")
        TipoDeCambio.resize(517, 248)

        self.centralwidget = QtWidgets.QWidget(TipoDeCambio)
        self.centralwidget.setObjectName("centralwidget")

        self.lblConvertir = QtWidgets.QLabel(self.centralwidget)
        self.lblConvertir.setGeometry(QtCore.QRect(20, 20, 61, 16))
        self.lblConvertir.setObjectName("lblConvertir")

        self.leImporte = QtWidgets.QLineEdit(self.centralwidget)
        self.leImporte.setGeometry(QtCore.QRect(90, 20, 113, 20))
        self.leImporte.setObjectName("leImporte")

        self.gbDe = QtWidgets.QGroupBox(self.centralwidget)
        self.gbDe.setGeometry(QtCore.QRect(20, 80, 151, 141))
        self.gbDe.setObjectName("gbDe")

        self.rbDeUSD = QtWidgets.QRadioButton(self.gbDe)
        self.rbDeUSD.setGeometry(QtCore.QRect(10, 30, 82, 17))
        self.rbDeUSD.setChecked(True)
        self.rbDeUSD.setObjectName("rbDeUSD")

        self.rbDeEUR = QtWidgets.QRadioButton(self.gbDe)
        self.rbDeEUR.setGeometry(QtCore.QRect(10, 60, 82, 17))
        self.rbDeEUR.setObjectName("rbDeEUR")

        self.rbDePEN = QtWidgets.QRadioButton(self.gbDe)
        self.rbDePEN.setGeometry(QtCore.QRect(10, 90, 82, 17))
        self.rbDePEN.setObjectName("rbDePEN")

        self.rbDeGBP = QtWidgets.QRadioButton(self.gbDe)
        self.rbDeGBP.setGeometry(QtCore.QRect(10, 120, 82, 17))
        self.rbDeGBP.setObjectName("rbDeGBP")

        self.gbA = QtWidgets.QGroupBox(self.centralwidget)
        self.gbA.setGeometry(QtCore.QRect(210, 80, 151, 141))
        self.gbA.setObjectName("gbA")

        self.rbAUSD = QtWidgets.QRadioButton(self.gbA)
        self.rbAUSD.setGeometry(QtCore.QRect(20, 20, 82, 17))
        self.rbAUSD.setChecked(True)
        self.rbAUSD.setObjectName("rbAUSD")

        self.rbAEUR = QtWidgets.QRadioButton(self.gbA)
        self.rbAEUR.setGeometry(QtCore.QRect(20, 50, 82, 17))
        self.rbAEUR.setObjectName("rbAEUR")

        self.rbAPEN = QtWidgets.QRadioButton(self.gbA)
        self.rbAPEN.setGeometry(QtCore.QRect(20, 80, 82, 17))
        self.rbAPEN.setObjectName("rbAPEN")

        self.rbAGBP = QtWidgets.QRadioButton(self.gbA)
        self.rbAGBP.setGeometry(QtCore.QRect(20, 110, 82, 17))
        self.rbAGBP.setObjectName("rbAGBP")

        self.lblResultado = QtWidgets.QLabel(self.centralwidget)
        self.lblResultado.setGeometry(QtCore.QRect(370, 110, 61, 16))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.lblResultado.setFont(font)
        self.lblResultado.setObjectName("lblResultado")

        self.lblCambio = QtWidgets.QLabel(self.centralwidget)
        self.lblCambio.setGeometry(QtCore.QRect(370, 140, 47, 13))
        self.lblCambio.setObjectName("lblCambio")

        self.pbTipoCambio = QtWidgets.QPushButton(self.centralwidget)
        self.pbTipoCambio.setGeometry(QtCore.QRect(410, 170, 75, 23))
        self.pbTipoCambio.setObjectName("pbTipoCambio")

        TipoDeCambio.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(TipoDeCambio)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 517, 26))
        self.menubar.setObjectName("menubar")
        TipoDeCambio.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(TipoDeCambio)
        self.statusbar.setObjectName("statusbar")
        TipoDeCambio.setStatusBar(self.statusbar)

        self.retranslateUi(TipoDeCambio)
        QtCore.QMetaObject.connectSlotsByName(TipoDeCambio)

    def retranslateUi(self, TipoDeCambio):
        _translate = QtCore.QCoreApplication.translate
        TipoDeCambio.setWindowTitle(_translate("TipoDeCambio", "Tipo de cambio"))
        self.lblConvertir.setText(_translate("TipoDeCambio", "Convertir"))
        self.leImporte.setText(_translate("TipoDeCambio", "0"))
        self.gbDe.setTitle(_translate("TipoDeCambio", "De:"))
        self.rbDeUSD.setText(_translate("TipoDeCambio", "USD"))
        self.rbDeEUR.setText(_translate("TipoDeCambio", "EUR"))
        self.rbDePEN.setText(_translate("TipoDeCambio", "PEN"))
        self.rbDeGBP.setText(_translate("TipoDeCambio", "GBP"))
        self.gbA.setTitle(_translate("TipoDeCambio", "A:"))
        self.rbAUSD.setText(_translate("TipoDeCambio", "USD"))
        self.rbAEUR.setText(_translate("TipoDeCambio", "EUR"))
        self.rbAPEN.setText(_translate("TipoDeCambio", "PEN"))
        self.rbAGBP.setText(_translate("TipoDeCambio", "GBP"))
        self.lblResultado.setText(_translate("TipoDeCambio", "Resultado:"))
        self.lblCambio.setText(_translate("TipoDeCambio", "0.0"))
        self.pbTipoCambio.setText(_translate("TipoDeCambio", "Convertir"))
