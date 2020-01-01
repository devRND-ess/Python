'''
from PyQt4 import QtGui, QtCore, uic
import sys

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    app.setStyle("cleanLooks")

    #DATA
    data = QtCore.QStringList()
    data << "one" << "two" << "three" << "four" << "five"

    listView = QtGui.QListView()
    listView.show()

    #MODEL
    model = QtGui.QStringListModel(data)

    listView.setModel(model)

    listView2 = QtGui.QListView()
    listView2.show()
    listView2.setModel(model)

    sys.exit(app.exec_())
'''
def mult():
    listi = []
    listu = []
    for x in range(5):
        listi.append(str(x))
    for z in range(3):
        listu.append(str(z))
    return listi, listu

y = mult()
print(y)
