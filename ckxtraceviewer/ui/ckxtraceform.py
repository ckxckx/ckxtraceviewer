# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ckxtraceform.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ckxTraceViewObj(object):
    def setupUi(self, ckxTraceViewObj):
        ckxTraceViewObj.setObjectName("ckxTraceViewObj")
        ckxTraceViewObj.resize(256, 391)
        self.listWidget = QtWidgets.QListWidget(ckxTraceViewObj)
        self.listWidget.setGeometry(QtCore.QRect(30, 20, 201, 221))
        self.listWidget.setObjectName("listWidget")
        self.pushButton_fileexp = QtWidgets.QPushButton(ckxTraceViewObj)
        self.pushButton_fileexp.setGeometry(QtCore.QRect(20, 340, 101, 31))
        self.pushButton_fileexp.setObjectName("pushButton_fileexp")
        self.pushButton_loattrace = QtWidgets.QPushButton(ckxTraceViewObj)
        self.pushButton_loattrace.setGeometry(QtCore.QRect(120, 340, 101, 31))
        self.pushButton_loattrace.setObjectName("pushButton_loattrace")
        self.pushButton_searchnext = QtWidgets.QPushButton(ckxTraceViewObj)
        self.pushButton_searchnext.setEnabled(False)
        self.pushButton_searchnext.setGeometry(QtCore.QRect(210, 270, 31, 31))
        self.pushButton_searchnext.setObjectName("pushButton_searchnext")
        self.widget = QtWidgets.QWidget(ckxTraceViewObj)
        self.widget.setGeometry(QtCore.QRect(29, 249, 208, 20))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_manual = QtWidgets.QRadioButton(self.widget)
        self.radioButton_manual.setChecked(True)
        self.radioButton_manual.setObjectName("radioButton_manual")
        self.horizontalLayout.addWidget(self.radioButton_manual)
        self.radioButton_auto = QtWidgets.QRadioButton(self.widget)
        self.radioButton_auto.setObjectName("radioButton_auto")
        self.horizontalLayout.addWidget(self.radioButton_auto)
        self.widget1 = QtWidgets.QWidget(ckxTraceViewObj)
        self.widget1.setGeometry(QtCore.QRect(30, 280, 171, 21))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit_search = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.horizontalLayout_2.addWidget(self.lineEdit_search)
        self.widget2 = QtWidgets.QWidget(ckxTraceViewObj)
        self.widget2.setGeometry(QtCore.QRect(30, 310, 194, 23))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.widget2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.lineEdit_tracefile = QtWidgets.QLineEdit(self.widget2)
        self.lineEdit_tracefile.setObjectName("lineEdit_tracefile")
        self.horizontalLayout_3.addWidget(self.lineEdit_tracefile)

        self.retranslateUi(ckxTraceViewObj)
        self.pushButton_loattrace.clicked.connect(ckxTraceViewObj.ckx_loadtrace)
        self.pushButton_fileexp.clicked.connect(ckxTraceViewObj.ckx_filechoose)
        self.listWidget.itemSelectionChanged.connect(ckxTraceViewObj.ckx_onSelectionChanged)
        self.listWidget.itemClicked['QListWidgetItem*'].connect(ckxTraceViewObj.ckx_onItemClicked)
        self.lineEdit_search.returnPressed.connect(ckxTraceViewObj.ckx_search_address)
        self.pushButton_searchnext.clicked.connect(ckxTraceViewObj.ckx_next_button_clicked)
        QtCore.QMetaObject.connectSlotsByName(ckxTraceViewObj)

    def retranslateUi(self, ckxTraceViewObj):
        _translate = QtCore.QCoreApplication.translate
        ckxTraceViewObj.setWindowTitle(_translate("ckxTraceViewObj", "Form"))
        self.pushButton_fileexp.setText(_translate("ckxTraceViewObj", "File Explore"))
        self.pushButton_loattrace.setText(_translate("ckxTraceViewObj", "Load Trace"))
        self.pushButton_searchnext.setText(_translate("ckxTraceViewObj", ">"))
        self.radioButton_manual.setText(_translate("ckxTraceViewObj", "Manual Mode"))
        self.radioButton_auto.setText(_translate("ckxTraceViewObj", "Auto Trace"))
        self.label.setText(_translate("ckxTraceViewObj", "Search 0x"))
        self.label_2.setText(_translate("ckxTraceViewObj", "TraceFile:"))
