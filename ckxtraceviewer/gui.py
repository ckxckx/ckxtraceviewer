#coding:utf-8
######################################################
# Author: Chen KX <ckx1025ckx@gmail.com>             #
# License: BSD 2-Clause                              #
######################################################

from idaapi import PluginForm
from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton
import sip
from .mainlogic import ckxTraceViewPanel


class MyPluginFormClass(PluginForm):
    def OnCreate(self, form):
        """
        Called when the plugin form is created
        """
        # Get parent widget
        # print("......")
        # print(type(form))
        self.parent = self.FormToPyQtWidget(form)
        self.PopulateForm()
        
    # def ckx(self):
        # print("ckx.....")
    def PopulateForm(self):
        # Create layout
        self.tvPannel=ckxTraceViewPanel(self.parent)
        print("....|||")
        self.tvPannel.show()
        # tvPannel = Ui_Form()
        # tvPannel.setupUi(self.parent)

    def OnClose(self, form):
        self.tvPannel.onClose()
        """
        Called when the plugin form is closed
        """
        pass
    def Show(self):
        # 调用顺序是先show，然后再onCreate的，所以我们这里不能瞎重载
        # print("showinng ....")
        return super(MyPluginFormClass,self).Show("ckxTraceView",options = (PluginForm.WOPN_TAB | PluginForm.WCLS_CLOSE_LATER))


