######################################################
# Author: Chen KX <ckx1025ckx@gmail.com>             #
# License: BSD 2-Clause                              #
######################################################

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from mainlogic import ckxTraceViewPanel


app = QApplication(sys.argv)
tv = ckxTraceViewPanel()
tv.show()
app.exec_()
import sys
sys.exit()
