# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Wed Jun  5 22:41:43 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 440)
        MainWindow.setMinimumSize(QtCore.QSize(700, 440))
        MainWindow.setMaximumSize(QtCore.QSize(700, 440))
        MainWindow.setCursor(QtCore.Qt.ArrowCursor)
        MainWindow.setMouseTracking(False)
        self.horizontalLayoutWidget = QtGui.QWidget(MainWindow)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(390, 10, 304, 31))
        self.horizontalLayoutWidget.setMinimumSize(QtCore.QSize(120, 0))
        self.horizontalLayoutWidget.setMaximumSize(QtCore.QSize(350, 16777215))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_new = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btn_new.setMinimumSize(QtCore.QSize(120, 25))
        self.btn_new.setMaximumSize(QtCore.QSize(120, 25))
        self.btn_new.setObjectName("btn_new")
        self.horizontalLayout.addWidget(self.btn_new)
        self.btn_edit = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btn_edit.setMinimumSize(QtCore.QSize(80, 25))
        self.btn_edit.setMaximumSize(QtCore.QSize(80, 25))
        self.btn_edit.setObjectName("btn_edit")
        self.horizontalLayout.addWidget(self.btn_edit)
        self.btn_delete = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btn_delete.setMinimumSize(QtCore.QSize(90, 25))
        self.btn_delete.setMaximumSize(QtCore.QSize(90, 25))
        self.btn_delete.setObjectName("btn_delete")
        self.horizontalLayout.addWidget(self.btn_delete)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(MainWindow)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 70, 681, 34))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.search_box = QtGui.QLineEdit(self.horizontalLayoutWidget_2)
        self.search_box.setMinimumSize(QtCore.QSize(350, 25))
        self.search_box.setMaximumSize(QtCore.QSize(350, 25))
        self.search_box.setText("")
        self.search_box.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.search_box.setObjectName("search_box")
        self.horizontalLayout_2.addWidget(self.search_box)
        self.label = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label.setMinimumSize(QtCore.QSize(130, 25))
        self.label.setMaximumSize(QtCore.QSize(140, 25))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.selectBrand = QtGui.QComboBox(self.horizontalLayoutWidget_2)
        self.selectBrand.setMinimumSize(QtCore.QSize(180, 25))
        self.selectBrand.setMaximumSize(QtCore.QSize(180, 25))
        self.selectBrand.setMouseTracking(False)
        self.selectBrand.setEditable(False)
        self.selectBrand.setMaxVisibleItems(30)
        self.selectBrand.setInsertPolicy(QtGui.QComboBox.InsertAlphabetically)
        self.selectBrand.setObjectName("selectBrand")
        self.horizontalLayout_2.addWidget(self.selectBrand)
        self.table = QtGui.QTableView(MainWindow)
        self.table.setGeometry(QtCore.QRect(10, 110, 680, 310))
        self.table.setMinimumSize(QtCore.QSize(680, 310))
        self.table.setMaximumSize(QtCore.QSize(680, 310))
        self.table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.table.setObjectName("table")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Lista de productos", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_new.setText(QtGui.QApplication.translate("MainWindow", "Nuevo Producto", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_edit.setText(QtGui.QApplication.translate("MainWindow", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_delete.setText(QtGui.QApplication.translate("MainWindow", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))
        self.search_box.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "Qué producto está buscando", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Buscar por marca:", None, QtGui.QApplication.UnicodeUTF8))

