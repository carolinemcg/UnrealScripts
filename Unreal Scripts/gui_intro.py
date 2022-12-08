import unreal

from PySide2 import QtCore, QtGui, QtUiTools

class SimpleGUI(QtGui.QtWidget):
    def __init__(self, parent=None):
        super(SimpleGUI, self).__init__(parent)

        # load the created ui widget
        self.widget = QtUiTools.QuiLoader().load("C:\\Qt Projects\\UntitledProject\\content\\Screen01.ui.qml")

# only create an instance of the GUI when it's not alerady running
app = None
if not QtGui.QApplication.instaqnce():
    app =QtGui.QApplication(sys.argv)

# start the GUI
main_window = SimpleGUI()
main_window.show()