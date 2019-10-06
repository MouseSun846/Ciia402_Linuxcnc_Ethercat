import hal
import glib
import time
import os,sys
from gladevcp.persistence import IniFile,widget_defaults,set_debug,select_widgets
import hal_glib
import gtk

class AxisPos:
	xpos=0
	ypos=0
	zpos=0
	apos=0
	bpos=0
	cpos=0
	xinc=11111
	yinc=11111
	zinc=11111
	ainc=11111
	binc=11111
	cinc=11111
	xen=0
	yen=0
	zen=0
	aen=0
	ben=0
	cen=0
class HandlerClass:
    def on_XPlusButton_pressed(self,widget,data=None):
        self.axis.xpos +=  self.axis.xinc
        self.builder.get_object('XTPos').set_label("%d" % (self.axis.xpos))
	self.builder.get_object('XTPos').hal_pin.set(self.axis.xpos)
    def on_XMinusButton_pressed(self,widget,data=None):
        self.axis.xpos  -= self.axis.xinc
        self.builder.get_object('XTPos').set_label("%d" % (self.axis.xpos))
	self.builder.get_object('XTPos').hal_pin.set(self.axis.xpos)
    def on_YPlusButton_pressed(self,widget,data=None):
        self.axis.ypos +=  self.axis.yinc
        self.builder.get_object('YTPos').set_label("%d" % (self.axis.ypos))
	self.builder.get_object('YTPos').hal_pin.set(self.axis.ypos)
    def on_YMinusButton_pressed(self,widget,data=None):
        self.axis.ypos  -= self.axis.yinc
        self.builder.get_object('YTPos').set_label("%d" % (self.axis.ypos))
	self.builder.get_object('YTPos').hal_pin.set(self.axis.ypos)
    def on_ZPlusButton_pressed(self,widget,data=None):
        self.axis.zpos +=  self.axis.zinc
        self.builder.get_object('ZTPos').set_label("%d" % (self.axis.zpos))
	self.builder.get_object('ZTPos').hal_pin.set(self.axis.zpos)
    def on_ZMinusButton_pressed(self,widget,data=None):
        self.axis.zpos  -= self.axis.zinc
        self.builder.get_object('ZTPos').set_label("%d" % (self.axis.zpos))
	self.builder.get_object('ZTPos').hal_pin.set(self.axis.zpos)
    def on_APlusButton_pressed(self,widget,data=None):
        self.axis.apos +=  self.axis.ainc
        self.builder.get_object('ATPos').set_label("%d" % (self.axis.apos))
	self.builder.get_object('ATPos').hal_pin.set(self.axis.apos)
    def on_AMinusButton_pressed(self,widget,data=None):
        self.axis.apos  -= self.axis.ainc
        self.builder.get_object('ATPos').set_label("%d" % (self.axis.apos))
	self.builder.get_object('ATPos').hal_pin.set(self.axis.apos)
    def on_BPlusButton_pressed(self,widget,data=None):
        self.axis.bpos +=  self.axis.binc
        self.builder.get_object('BTPos').set_label("%d" % (self.axis.bpos))
	self.builder.get_object('BTPos').hal_pin.set(self.axis.bpos)
    def on_BMinusButton_pressed(self,widget,data=None):
        self.axis.bpos  -= self.axis.binc
        self.builder.get_object('BTPos').set_label("%d" % (self.axis.bpos))
	self.builder.get_object('BTPos').hal_pin.set(self.axis.bpos)
    def on_CPlusButton_pressed(self,widget,data=None):
        self.axis.cpos +=  self.axis.cinc
        self.builder.get_object('CTPos').set_label("%d" % (self.axis.cpos))
	self.builder.get_object('CTPos').hal_pin.set(self.axis.cpos)
    def on_CMinusButton_pressed(self,widget,data=None):
        self.axis.cpos  -= self.axis.cinc
        self.builder.get_object('CTPos').set_label("%d" % (self.axis.cpos))
	self.builder.get_object('CTPos').hal_pin.set(self.axis.cpos)
    def on_XEnable_toggled(self,widget,data=None):
	self.axis.xen=not self.axis.xen
	if self.axis.xen == 1:
		hal.set_p("lcec.0.0.onedrivecontrol","31")
	else:
		hal.set_p("lcec.0.0.onedrivecontrol","6")
    def on_YEnable_toggled(self,widget,data=None):
	self.axis.yen=not self.axis.yen
	if self.axis.yen == 1:
		hal.set_p("lcec.0.0.twodrivecontrol","31")
	else:
		hal.set_p("lcec.0.0.twodrivecontrol","6")
    def on_ZEnable_toggled(self,widget,data=None):
	self.axis.zen=not self.axis.zen
	if self.axis.zen == 1:
		hal.set_p("lcec.0.0.threedrivecontrol","31")
	else:
		hal.set_p("lcec.0.0.threedrivecontrol","6")
    def on_AEnable_toggled(self,widget,data=None):
	self.axis.aen=not self.axis.aen
	if self.axis.aen == 1:
		hal.set_p("lcec.0.0.fourdrivecontrol","31")
	else:
		hal.set_p("lcec.0.0.fourdrivecontrol","6")
    def on_BEnable_toggled(self,widget,data=None):
	self.axis.ben=not self.axis.ben
	if self.axis.ben == 1:
		hal.set_p("lcec.0.0.fivedrivecontrol","31")
	else:
		hal.set_p("lcec.0.0.fivedrivecontrol","6")
    def on_CEnable_toggled(self,widget,data=None):
	self.axis.cen=not self.axis.cen
	if self.axis.cen == 1:
		hal.set_p("lcec.0.0.sixdrivecontrol","31")
	else:
		hal.set_p("lcec.0.0.sixdrivecontrol","6")
    def __init__(self, halcomp,builder,useropts):
    	self.halcomp = halcomp
        self.builder = builder
        self.axis =AxisPos()
	hal.set_p("lcec.0.0.onedrivecontrol","6")
	hal.set_p("lcec.0.0.twodrivecontrol","6")
	hal.set_p("lcec.0.0.threedrivecontrol","6")
	hal.set_p("lcec.0.0.fourdrivecontrol","6")
	hal.set_p("lcec.0.0.fivedrivecontrol","6")
hal.set_p("lcec.0.0.sixdrivecontrol","6")
def get_handlers(halcomp,builder,useropts):
    return [HandlerClass(halcomp,builder,useropts)]
