######################################################
# Author: Chen KX <ckx1025ckx@gmail.com>             #
# License: BSD 2-Clause                              #
######################################################

import idaapi

class ckxtraceviewerplugin(idaapi.plugin_t):
    flags = idaapi.PLUGIN_KEEP
    comment = ""
    help = ""
    wanted_name = "ckxtraceviewer"
    wanted_hotkey = "Ctrl-Alt-I"
    
    def init(self):
        idaapi.msg("\n########### ckxtraceviewer plugin ###########\n")
        return idaapi.PLUGIN_KEEP

    def run(self, arg):
        self.openPanel()

    def term(self):
        idaapi.msg("ckxtraceviewer plugin: terminated\n")

    def openPanel(self):
        from ckxtraceviewer.gui import MyPluginFormClass
        plg = MyPluginFormClass()
        plg.Show()
        idaapi.msg("ckxtraceviewer: open the pannel.\n")

def PLUGIN_ENTRY():
    return ckxtraceviewerplugin()

