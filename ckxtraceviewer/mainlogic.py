#coding:utf-8
######################################################
# Author: Chen KX <ckx1025ckx@gmail.com>             #
# License: BSD 2-Clause                              #
######################################################

import sys
from os import path
# from PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import queue
try:
    from .ui.ckxtraceform import Ui_ckxTraceViewObj
    from .ckxrender_in_ida import ckxTR
    import ida_kernwin
except:
    try:
        from ui.ckxtraceform import Ui_ckxTraceViewObj
    except:
        from .ui.ckxtraceform import Ui_ckxTraceViewObj
    pass


default_filepath="/Users/ckx/myproject/qtuis/testpyqt/tmp.trace"

def load_file_to_list(alist,filepath):
    num = 1
    f=open(filepath,"r")
    aline=f.readline()
    while aline:
        aline = aline.split("\n")[0]
        # aline
        QListWidgetItem(aline,alist)
        aline=f.readline()
        if num%1000==0:
            print(num)
        num=num+1

def set_focus_in_ida(address_int):
    print("operations in ida")
    try:
    # if True:
        # if ckxTR.current_viewer == None:
            # ckxTR.get_current_viewer()
        ckxTR.setAddr(address_int)
        # ida_kernwin.activate_widget(ckxTR.current_viewer,True)
        # self.listWidget.setFocus()
    except:
        print("not in real ida")
    pass


class ckxTraceViewPanel(QWidget,Ui_ckxTraceViewObj):
    def __init__(self,parent=None):
        if not parent:
            super(ckxTraceViewPanel,self).__init__(parent)
            self.setupUi(self)
        else:
            super(ckxTraceViewPanel,self).__init__(parent)
            self.setupUi(self)
        self.lineEdit_tracefile.setText(default_filepath)
        self.radioButton_manual.setChecked(True)
        self.is_trace_loaded=False
    def onClose(self):
        try:
            ckxTR.recoverColor()
            ida_graph.refresh_viewer(ckxTR.widget_a)
        except:
            pass
        pass
    def ckx_loadtrace(self):
        if self.is_trace_loaded:
            self.listWidget.clear()
            # print("cleared")
        def check_fileline_valid(fileline):
            if path.exists(fileline):
                return True
            else:
                return False
            
            pass
            return True
        fileline = self.lineEdit_tracefile.text()
        if not check_fileline_valid(fileline):
            self.lineEdit_tracefile.setText("invalid fileline:"+fileline)
            return
        alist=self.listWidget
        load_file_to_list(alist,fileline)
        self.is_trace_loaded=True
        pass
    def ckx_onSelectionChanged(self):
        if self.radioButton_auto.isChecked():
            print("onSelectionChanged do sth....")
            it=self.listWidget.currentItem()
            print(it.text())
            aline = it.text()
            try:
                addr=int(aline,16)
            except ValueError:
                print("not a valid hex address")
                return
            set_focus_in_ida(addr)
            self.listWidget.setFocus()

        else:
            return
        pass
    def ckx_onItemClicked(self,theitem):
        if self.radioButton_manual.isChecked():
            print(theitem.text())
            aline = theitem.text()
            try:
                addr=int(aline,16)
            except ValueError:
                print("not a valid hex address")
                return
            set_focus_in_ida(addr)
            self.listWidget.setFocus()
        else:
            return
    def ckx_search_address(self):
        self.pushButton_searchnext.setEnabled(False)
        self.searchresult = None
        aline = self.lineEdit_search.text()
        try:
            addr= int(aline,16)
        except ValueError:
            print("search : not a valid hex address")
            return
        # print(hex(addr))
        # target = hex(addr)
        target = aline
        resultlist=self.listWidget.findItems(aline,Qt.MatchFlag.MatchExactly)
        if len(resultlist) ==0:
            print("not found matched!")
        else:
            allnum = len(resultlist)
            if allnum>1:
                self.pushButton_searchnext.setEnabled(True)
            self.searchresult= queue.Queue()
            for i in resultlist:
                self.searchresult.put(i)
            # self.searchresult = resultlist
            cur_item = self.searchresult.get()
            self.listWidget.setCurrentItem(cur_item)
            self.searchresult.put(cur_item)

    def ckx_next_button_clicked(self):
        if self.searchresult is not None:
            cur_item = self.searchresult.get()
            self.listWidget.setCurrentItem(cur_item)
            self.searchresult.put(cur_item)
        pass
    def ckx_filechoose(self):
        if False:
            # for debugging usage
            import ipdb
            ipdb.set_trace()
        if True:
            fname = QFileDialog.getOpenFileName(self, 'Open file', '~/','All Files (*)')[0]
            self.lineEdit_tracefile.setText(fname)
        pass
        print("Todo: file choose")
    
    
