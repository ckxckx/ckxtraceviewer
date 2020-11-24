
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from ckxtraceviewer.mainlogic import ckxTraceViewPanel


app = QApplication(sys.argv)
tv = ckxTraceViewPanel()
tv.show()
app.exec_()
import sys
sys.exit()
