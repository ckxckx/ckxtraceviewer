#coding:utf-8
######################################################
# Author: Chen KX <ckx1025ckx@gmail.com>             #
# License: BSD 2-Clause                              #
######################################################

import ida_graph
import idc
import ida_kernwin
import idaapi

def get_bb_id(graph, ea):
    for block in graph:
        if block.start_ea <= ea and block.end_ea > ea:
            return block.id

def reset_all_block_color_to_white(addr):
    white = 0xffffff
    f = idaapi.get_func(addr)
    g = idaapi.FlowChart(f, flags=idaapi.FC_PREDS) 
    p = idaapi.node_info_t()
    p.bg_color = white
    base_block_ea = f.start_ea
    for block in g:
        idaapi.set_node_info(
            base_block_ea,
            block.id, 
            p,
            idaapi.NIF_BG_COLOR | idaapi.NIF_FRAME_COLOR)


class ckxTraceRender(object):
    def __init__(self):
        self.widget_a = ida_kernwin.find_widget("IDA View-A")
        if not self.widget_a:
            raise Exception("IDA View-A not opened!")
        self.current_block_start_ea=None
        self.current_focused_addr = None
        self.current_bb_id = None
        self.current_viewer = None
    def get_current_viewer(self):
        self.current_viewer=ida_kernwin.get_current_viewer()
        print("get current_viewer")
    def setAddr(self,address):
        	
        if self.current_focused_addr == address:
            return
        else:
            idc.jumpto(address)
        f = idaapi.get_func(address)
        # print(f)
        if f == None:
            print("not found function address...")
            return
        g = idaapi.FlowChart(f, flags=idaapi.FC_PREDS) 
        target_bb_id = get_bb_id(g, address)
        # print(target_bb_id)
        
        if self.current_block_start_ea==f.start_ea and self.current_bb_id == target_bb_id:
            return
        else:

            self.recoverColor()
            self.current_block_start_ea = f.start_ea
            self.current_focused_addr = address
            self.current_bb_id = target_bb_id
            self.changeColor()
            ida_graph.refresh_viewer(self.widget_a)

    def changeColor(self):
        p = idaapi.node_info_t()
        color =0xffff00
        p.bg_color = color
        idaapi.set_node_info(
            self.current_block_start_ea,
            self.current_bb_id, 
            p,
            idaapi.NIF_BG_COLOR | idaapi.NIF_FRAME_COLOR)
        

    def recoverColor(self):
        if not self.current_focused_addr:
            # print("1")
            return
        if self.current_bb_id ==None:
            # print("2")
            return
        p = idaapi.node_info_t()
        color =0xffffff
        p.bg_color = color
        idaapi.set_node_info(
            self.current_block_start_ea, 
            self.current_bb_id, 
            p,
            idaapi.NIF_BG_COLOR | idaapi.NIF_FRAME_COLOR)
        # print("3")
        # ida_graph.refresh_viewer(self.widget_a)


ckxTR = ckxTraceRender()
# ckxTR.setAddr(0x40C9A0)
# ckxTR.setAddr(0x40C9E2)

# ckxTR.setAddr(0x60)
# ckxTR.setAddr(0x69)
# ckxTR.setAddr(0x4a)
# reset_all_block_color_to_white(0x4a)

