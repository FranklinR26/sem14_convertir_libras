import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

class Dialogo(QMainWindow):
    # Definir los tipos de cambio
    USDtoPEN = 3.84
    USDtoEUR = 0.93
    USDtoGBP = 0.84  # Tipo de cambio USD a GBP

    def __init__(self):
        super().__init__()
        ruta = os.path.dirname(os.path.abspath(__file__)) + r"\..\vista\currencyConvert.ui"
        uic.loadUi(ruta, self)

        self.pbTipoCambio.clicked.connect(self.calcularConversion)

    def calcularConversion(self):
        convertido = 0.0
        inicial = 0.0

        inicial = float(self.leImporte.text())
        convertido = inicial

        # Conversión desde USD
        if self.rbDeUSD.isChecked():
            if self.rbAUSD.isChecked():
                convertido = inicial  # De USD a USD (mismo valor)
            elif self.rbAEUR.isChecked():
                convertido = inicial * self.USDtoEUR  # De USD a EUR
            elif self.rbAPEN.isChecked():
                convertido = inicial * self.USDtoPEN  # De USD a PEN
            elif self.rbAGBP.isChecked():
                convertido = inicial * self.USDtoGBP  # De USD a GBP

        # Conversión desde EUR
        elif self.rbDeEUR.isChecked():
            if self.rbAUSD.isChecked():
                convertido = inicial / self.USDtoEUR  # De EUR a USD
            elif self.rbAEUR.isChecked():
                convertido = inicial  # De EUR a EUR (mismo valor)
            elif self.rbAPEN.isChecked():
                convertido = (inicial / self.USDtoEUR) * self.USDtoPEN  # De EUR a PEN
            elif self.rbAGBP.isChecked():
                convertido = (inicial / self.USDtoEUR) * self.USDtoGBP  # De EUR a GBP

        # Conversión desde PEN
        elif self.rbDePEN.isChecked():
            if self.rbAUSD.isChecked():
                convertido = inicial / self.USDtoPEN  # De PEN a USD
            elif self.rbAEUR.isChecked():
                convertido = (inicial / self.USDtoPEN) * self.USDtoEUR  # De PEN a EUR
            elif self.rbAPEN.isChecked():
                convertido = inicial  # De PEN a PEN (mismo valor)
            elif self.rbAGBP.isChecked():
                convertido = (inicial / self.USDtoPEN) * self.USDtoGBP  # De PEN a GBP

        # Conversión desde GBP
        elif self.rbDeGBP.isChecked():
            if self.rbAUSD.isChecked():
                convertido = inicial / self.USDtoGBP  # De GBP a USD
            elif self.rbAEUR.isChecked():
                convertido = (inicial / self.USDtoGBP) * self.USDtoEUR  # De GBP a EUR
            elif self.rbAPEN.isChecked():
                convertido = (inicial / self.USDtoGBP) * self.USDtoPEN  # De GBP a PEN
            elif self.rbAGBP.isChecked():
                convertido = inicial  # De GBP a GBP (mismo valor)

        self.lblCambio.setText(f"{convertido:.2f}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialogo = Dialogo()
    dialogo.show()
    app.exec_()
