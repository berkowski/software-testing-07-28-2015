from PyQt4 import (QtGui, QtCore)

from ui import ui_whoiDialog

class WhoiDialog(QtGui.QDialog, ui_whoiDialog.Ui_Dialog):
    """

    """
    textChanged = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):

        QtGui.QDialog.__init__(self, parent=parent)

        self.setupUi(self)

        self.pushButton.clicked.connect(self.handleClick)

    @QtCore.pyqtSlot()
    def handleClick(self):

        lineText = self.lineEdit.text()
        self.textChanged.emit(lineText)
        self.label.setText(lineText)



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)

    gui = WhoiDialog()
    gui.show()
    app.exec_()
