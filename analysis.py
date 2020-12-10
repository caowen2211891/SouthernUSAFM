# -*- coding: utf-8 -*-
import sys
# import fix_qt_import_error
import math
from scipy.interpolate import UnivariateSpline
from PyQt5.QtWidgets import QApplication, QMessageBox, QFileDialog, QSplashScreen, QMenu, QMainWindow, QAction,QDesktopWidget,QToolTip
from PyQt5.QtGui import QIcon, QDoubleValidator, QIntValidator, QPixmap, QDesktopServices,QFont
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from PyQt5.QtCore import pyqtSignal, QThread, QSettings, Qt, QUrl

import os
import numpy as np
import collections

from sklearn.linear_model import LinearRegression

import qdarkstyle

import ExcelWriter
import FileWriter,calculate_AFM
import DataObtain
import calculate_FD
from Config_Dailog import ConfigDailog
from DataBean import Detail
from Detail_Dailog import DetailDailog
from Loading_Dailog import LoadingDailog
from Result_Dailog import RusultDailog
from SoftConfig import ConfigData
from UI_Main import Ui_MainWindow
from BubbleTips import BubbleLabel

from matplotlib.ticker import ScalarFormatter
import cgitb


class WorkThread(QThread):

    trigger = pyqtSignal(int)

    successSignal = pyqtSignal(list)

    def __int__(self):
        super(WorkThread, self).__init__()

    def addData(self,listitems):
        self.listitems = listitems

    def run(self):
        datas = DataObtain.getData(self.listitems)
        self.successSignal.emit(datas)

class ResultData(object):

    """docstring for SuccessData"""

    def __init__(self,filename,retractindex,sensitivity,springConstant,beforeIndext,afterIndex,E):

        super(ResultData, self).__init__()
        self.filename = filename
        self.retractindex = retractindex
        self.sensitivity = sensitivity
        self.springConstant = springConstant
        self.beforeIndext = beforeIndext
        self.afterIndex = afterIndex
        self.E = E

class MainTool(QMainWindow,Ui_MainWindow):

    workThread = WorkThread()
    settings = QSettings("amf","amf")
    cf = ''
    detail = None

    listitems = []
    filelist = []
    resultlist = collections.OrderedDict()
    fileindex = 0

    curfilename = ''
    curE = ''

    init_x_min = None

    data = None
    ax_tm_mainline = None
    annot_tm = None
    retract_index = 0
    latest_before_index = 0
    latest_after_index = 0
    smooth_level = 0

    sensitivity = -1
    springConstant = -1
    radius = -1
    poissonvalue = 1
    radioselect = 0
    hh = None
    pu = None
    hu = None
    pk = None
    s = None
    er = None
    es = None
    hc = None
    ac = None
    c1 = None
    c2 = None
    c3 = None
    c4 = None

    zooming = False
    inaxes = False
    mode = 0

    def __init__(self,name):
        super(MainTool,self).__init__()
        self.fileName = name
        self.cf = ConfigData()
        self.listitems.append(name)
        self.setupUi(self)
        self.initUI()

    def initUI(self):

        openFileAction = QAction(QIcon('res/pic/single.png'), '&Open', self)
        openFileAction.triggered.connect(self.open)

        openFolderAction = QAction(QIcon('res/pic/open.png'), '&Folder', self)
        openFolderAction.triggered.connect(self.openbatch)

        exportAction = QAction(QIcon('res/pic/txt.png'), '&Export TXT', self)
        exportAction.triggered.connect(self.save)

        exportexcelAction = QAction(QIcon('res/pic/Excel.png'), '&Export Excel', self)
        exportexcelAction.triggered.connect(self.exportExcel)

        savepicAction = QAction(QIcon('res/pic/photo.png'), '&Save Image', self)
        savepicAction.triggered.connect(self.saveimage)

        settingsAction = QAction(QIcon('res/pic/setting.png'), '&Settings', self)
        settingsAction.triggered.connect(self.show_config)

        helpAction = QAction(QIcon('res/pic/help.png'), '&Help', self)
        helpAction.triggered.connect(self.help)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        toolsMenu = menubar.addMenu('&Tools')
        helpMenu = menubar.addMenu('&Help')

        fileMenu.addAction(openFileAction)
        fileMenu.addAction(openFolderAction)
        fileMenu.addAction(exportAction)
        fileMenu.addAction(exportexcelAction)
        fileMenu.addAction(settingsAction)

        toolsMenu.addAction(savepicAction)

        helpMenu.addAction(helpAction)

        self.ls = ['Time', 'Froce', 'Height']
        self.refresh_combo(self.ls)
        self.x_combo.currentTextChanged.connect(self.on_x_select)
        self.y_combo.currentTextChanged.connect(self.on_y_select)
        self.smooth_spinBox.valueChanged.connect(self.on_smooth_change)
        self.radius = np.array(self.radius_et.text(), dtype=np.float64) * 1e-6

        self.build_tm()

        self.pushButton_2.clicked.connect(self.openResult)
        self.calculateButton.clicked.connect(self.calculateResult)

        self.radius_et.setValidator(QDoubleValidator())
        self.prtip_et.setValidator(QDoubleValidator())
        self.prsample_et.setValidator(QDoubleValidator())
        self.etip_et.setValidator(QDoubleValidator())
        self.et_c1.setValidator(QDoubleValidator())
        self.et_c2.setValidator(QDoubleValidator())
        self.et_c3.setValidator(QDoubleValidator())
        self.et_c4.setValidator(QDoubleValidator())
        self.bc_et.setValidator(QIntValidator())
        self.ac_et.setValidator(QIntValidator())

        self.c1 = np.array(self.settings.value('et_c1', '0'), dtype=np.float64)
        self.c2 = np.array(self.settings.value('et_c2', '0'), dtype=np.float64)
        self.c3 = np.array(self.settings.value('et_c3', '0'), dtype=np.float64)
        self.c4 = np.array(self.settings.value('et_c4', '0'), dtype=np.float64)

        self.et_c1.setText(str(self.c1))
        self.et_c2.setText(str(self.c2))
        self.et_c3.setText(str(self.c3))
        self.et_c4.setText(str(self.c4))
        self.prtip_et.setText(self.settings.value('prtip_et', '0'))
        self.prsample_et.setText(self.settings.value('prsample_et', '0'))
        self.etip_et.setText(self.settings.value('etip_et', '1'))

        self.et_c1.editingFinished.connect(self.onc1edit)
        self.et_c2.editingFinished.connect(self.onc2edit)
        self.et_c3.editingFinished.connect(self.onc3edit)
        self.et_c4.editingFinished.connect(self.onc4edit)
        self.prtip_et.editingFinished.connect(self.prtip_etedit)
        self.prsample_et.editingFinished.connect(self.prsample_etedit)
        self.etip_et.editingFinished.connect(self.etip_etedit)

        self.radius_et.editingFinished.connect(self.onradiusedit)
        self.bc_et.editingFinished.connect(self.on_bf_edit_finish)
        self.ac_et.editingFinished.connect(self.on_af_edit_finish)
        self.bc_et.textChanged.connect(self.onbcedit)
        self.ac_et.textChanged.connect(self.onacedit)

        self.radioselect = self.settings.value('radioselect', 0)
        if self.radioselect == 0:
            self.radio_cone.setChecked(True)
            self.stackedWidget.setCurrentIndex(0)
        elif self.radioselect == 1:
            self.radio_spher.setChecked(True)
            self.stackedWidget.setCurrentIndex(1)
        else:
            self.radio_punch.setChecked(True)
            self.stackedWidget.setCurrentIndex(1)
        self.radio_cone.toggled.connect(self.radiotoggle)
        self.radio_spher.toggled.connect(self.radiotoggle)
        self.radio_punch.toggled.connect(self.radiotoggle)

        self.igonre.clicked.connect(self.next)
        self.lastButton.clicked.connect(self.last)
        self.add.clicked.connect(self.add_result)
        self.pushButton.clicked.connect(self.show_detail)
        self.label_32.setToolTip('Ac=C1*hc^2+C2*hc+C3*hc^0.5+C4*hc^0.25')
        self.checkBoxApplyToAllTips.setToolTip('If checked,the next file will also be used the same point of time,\notherwise, use the first point')

        self.workThread.successSignal.connect(self.setResult)

        self.setWindowTitle(self.fileName)
        self.setWindowIcon(QIcon('res/pic/test.png'))

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        self.setAcceptDrops(True)

        self.show()
        if self.cf.isAsDefault():
            if str(self.settings.value('isOpenFile', True)).lower() == 'true':
                self.open()
            else:
                self.openbatch()
        else:
            self.show_config()

    def compute_h(self):
        if self.radioselect == 0:
            # H=Pu/Ac
            if math.isclose(self.ac,0e-9,rel_tol=1e-9):
                return
            self.hh = self.pu/self.ac
        elif self.radioselect == 1:
            # H=Pu/(3.14159*R*hu)
            if math.isclose(self.radius,0e-9,rel_tol=1e-9):
                return
            self.hh = self.pu/(3.14159*self.radius*self.hu)
        else:
            # H=Pu/(3.14159*R^2)
            if math.isclose(self.radius,0e-9,rel_tol=1e-9):
                return
            self.hh = self.pu/(3.14159 * (self.radius**2))
        self.label_h.setText(str('%.3e' % self.hh))


       # compute ROF
    def compute_s_data(self):
        index = self.retract_index
        if index is None or index < 0:
            return
        before = self.getbeforeindex()
        after = self.getafterindex()
        if before == 0 or after == 0 or before == index or after == index:
            return
        self.s = calculate_FD.computeS(
            self.data.T_list[before:index], self.data.T_list[index:after],
            self.data.m_list[before:index], self.data.m_list[index:after],
            self.data.V_list[before:index], self.data.V_list[index:after])
        self.label_s.setText(str('%.3e' % self.s))


    def compute_es(self,pr):
        # Es = (1 - PRsample ^ 2) / (1 / Er - PK）
        # compute pk
        # PK = (1 - PRtip ^ 2) / Etip
        PRtip = np.array(self.prtip_et.text(), dtype=np.float64)
        Etip = np.array(self.etip_et.text(), dtype=np.float64)
        if Etip == 0:
            self.showErrorDialog('Param Etip Is 0 ')
            return
        self.pk = (1-PRtip**2)/Etip
        self.label_pk.setText(str('%.3e' % self.pk))
        # compute er
        if self.radioselect == 0:
            # Er = 3.14159 ^ 0.5 * 0.5 * S / (Ac ^ 0.5)
            temp = 3.14159**0.5
            if self.s is None:
                self.showErrorDialog('Param Goodness of Fit Is 0')
                return

            # Hc = Hu - 0.72 * Pu / S
            # Ac = C1hc ^ 2 + C2hc + C3hc ^ 0.5 + C4hc ^ 0.25
            self.hc = self.hu-0.72*self.pu/self.s
            if self.hc < 0:
                self.showErrorDialog('Param Hc < 0')
                return
            self.label_hc.setText(str('%.3e' % self.hc))
            self.ac = self.c1*(self.hc**2)+self.c2*self.hc+self.c3*(self.hc**0.5)+self.c4*(self.hc**0.25)
            self.label_ac.setText(str('%.3e' % self.ac))

            tempac = self.ac**0.5
            if tempac == 0:
                self.showErrorDialog('Param Ac Is 0')
                return
            self.er = temp*0.5*self.s/tempac
        elif self.radioselect == 1:
            # Er = S / (2 *（R * Hu） ^ 0.5)
            temp = (self.radius*self.hu)**0.5
            if temp == 0:
                self.showErrorDialog('Param radius or hu Is 0')
                return
            self.er = self.s/(2*temp)
        else:
            # Er = S / (2R)
            if self.radius == 0:
                self.showErrorDialog('Param radius Is 0')
                return
            self.er = self.s/(2 * self.radius)
        self.label_er.setText(str('%.3e' % self.er))
        # compute es
        if 1/self.er-self.pk == 0:
            self.showErrorDialog('Param er == pk')
            return
        self.es = (1 - pr**2)/(1/self.er-self.pk)
        self.lable_esdata.setText(str('%.3e' % self.es))
        return self.es


    def radiotoggle(self):
        if self.radio_cone.isChecked():
            self.radioselect = 0
            self.stackedWidget.setCurrentIndex(0)
        elif self.radio_spher.isChecked():
            self.radioselect = 1
            self.stackedWidget.setCurrentIndex(1)
        else:
            self.radioselect = 2
            self.stackedWidget.setCurrentIndex(1)
        self.settings.setValue('radioselect', self.radioselect)
        # self.calculateResult()

    def onradiusedit(self):
        temp = np.array(self.radius_et.text(), dtype=np.float64) * 1e-6
        if temp != self.radius:
            self.radius = temp
            if self.data is None:
                return
            # self.calculateResult()
    
    def prtip_etedit(self):
        self.settings.setValue('prtip_et', str(np.array(self.prtip_et.text(), dtype=np.float64)))

    def prsample_etedit(self):
        self.settings.setValue('prsample_et', str(np.array(self.prsample_et.text(), dtype=np.float64)))

    def etip_etedit(self):
        self.settings.setValue('etip_et', str(np.array(self.etip_et.text(), dtype=np.float64)))


    def onc1edit(self):
        self.c1 = np.array(self.et_c1.text(), dtype=np.float64)
        self.settings.setValue('et_c1', str(self.c1))
        # self.calculateResult()

    def onc2edit(self):
        self.c2 = np.array(self.et_c2.text(), dtype=np.float64)
        self.settings.setValue('et_c2', str(self.c2))
        # self.calculateResult()

    def onc3edit(self):
        self.c3 = np.array(self.et_c3.text(), dtype=np.float64)
        self.settings.setValue('et_c3', str(self.c3))
        # self.calculateResult()

    def onc4edit(self):
        self.c4 = np.array(self.et_c4.text(), dtype=np.float64)
        self.settings.setValue('et_c4', str(self.c4))
        # self.calculateResult()

    def onprsample_etediting(self,arg1):
        if arg1 == '':
            self.prsample_et.setText(str(0))

    def onprtip_etediting(self,arg1):
        if arg1 == '':
            self.prtip_et.setText(str(0))

    def onetip_etediting(self,arg1):
        if arg1 == '' or math.isclose(float(arg1), 0e-9, rel_tol=1e-9):
            self.etip_et.setText(str(0.01))


    def onbcedit(self,arg1):
        try:
            self.bc_et.setText(str(int(arg1)))
        except Exception as identifier:
            self.bc_et.setText(str(0))


    def onacedit(self,arg1):
        try:
            self.ac_et.setText(str(int(arg1)))
        except Exception as identifier:
            self.ac_et.setText(str(0))

    def on_bf_edit_finish(self):
        if self.data is None:
            return
        index = self.getbeforeindex()
        if self.latest_before_index != index:
            self.draw_before(index)
            self.latest_before_index = index
            self.compute_s_data()

    def on_af_edit_finish(self):
        if self.data is None:
            return
        index = self.getafterindex()
        if self.latest_after_index != index:
            self.draw_after(index)
            self.latest_after_index = index
            self.compute_s_data()

    def saveimage(self):
        self.toolbar.save_figure()

    def saveimg(self,path):
        plt.savefig('D:\est.png')

    def build_tm(self):
        self.fig_tm, self.ax_tm = plt.subplots()
        self.fig_tm.subplots_adjust(left=0.15,right=0.95)
        self.canvas_tm = FigureCanvas(self.fig_tm)
        layout = self.main_view
        layout.addWidget(self.canvas_tm)
        self.toolbar = NavigationToolbar(self.canvas_tm, self)
        self.toolbar.setVisible(False)
        layout.addWidget(self.toolbar)

        self.canvas_tm.mpl_connect('motion_notify_event', self.on_move)
        self.canvas_tm.mpl_connect('button_press_event', self.on_click)
        self.canvas_tm.mpl_connect('button_release_event', self.button_release_callback)
        self.canvas_tm.mpl_connect('axes_enter_event', self.tm_axes_enter_event)
        self.canvas_tm.mpl_connect('axes_leave_event', self.tm_axes_leave_event)
        # self.canvas_tm.mpl_connect('scroll_event', self.on_scroll)



    def button_release_callback(self,event):
        self.is_panmode = False

    def tm_axes_enter_event(self,event):
        self.inaxes = True

    def tm_axes_leave_event(self,event):
        self.inaxes = False
        if self.annot_tm is not None:
            self.annot_tm.set_visible(False)

# 获取force
    def getForce(self,v0,vt):
        return (vt-v0)*self.data.sensitivity*self.data.springConstant
# 获取force
    def getForceData(self,vt):
        return self.getForce(self.v0, vt)

    ingcalculateResult = False
    def calculateResult(self):
        if self.ingcalculateResult:
            return
        self.ingcalculateResult = True
        if self.data is None:
            self.show_no_data_warning()
            self.ingcalculateResult = False
            return
        index = self.retract_index
        if index is None or index < 0:
            self.showErrorDialog('Should Set Retract Index')
            self.ingcalculateResult = False
            return
        if self.radius is None or self.radius <= 0:
            self.showErrorDialog('Should Set Tip Geometry')
            self.ingcalculateResult = False
            return
        try:
            pr = np.array(self.prsample_et.text(), dtype=np.float64)
        except Exception as e:
            self.showErrorDialog('Illegal Params:PRsample')
            self.ingcalculateResult = False
            return
        
        before = self.getbeforeindex()
        after = self.getafterindex()
        if before == 0 or after == 0 or before == index or after == index:
            self.ingcalculateResult = False
            return
        
        if self.mode == 1:
            afm = calculate_AFM.compute(self.sensitivity, self.data.springConstant, self.radius,self.data.T_list[before:index],self.data.T_list[index:after],self.data.m_list[before:index],self.data.m_list[index:after], self.data.V_list[before:index],self.data.V_list[index:after])
            E = 2 * self.poissonvalue * afm
            self.es = E

        else:
            # self.compute_s_data()
            
            self.es = self.compute_es(pr)
            if self.es is None:
                self.ingcalculateResult = False
                return
            
            self.compute_h()
            self.detail = self.create_detail()
        ## auto add result()
        
        self.add_result()
        self.ingcalculateResult = False


    def showToast(self,text):
        if hasattr(self, "_blabel"):
            self._blabel.stop()
            self._blabel.deleteLater()
            del self._blabel
        self._blabel = BubbleLabel()
        self._blabel.setText(text)
        self._blabel.show()
        # self.toast = QMessageBox(self) ##Message Box that doesn't run
        # self.toast.setIcon(QMessageBox.Information)
        # self.toast.setText(text)
        # self.toast.setWindowTitle("Information")
        # self.toast.setStandardButtons(QMessageBox.Ok)
        # self.toast.button(QMessageBox.Ok).animateClick(1500)       #1.5秒自动关闭
        # self.toast.exec_()

    def on_move(self,event):
        if self.zooming:
            return
        if event.inaxes == self.ax_tm:
            if self.ax_tm_mainline is None or self.annot_tm is None:
                return
            if self.is_panmode:
                axtemp=event.inaxes
                x_min, x_max = axtemp.get_xlim()
                y_min, y_max = axtemp.get_ylim()
                x, y = event.xdata, event.ydata
                axtemp.set(xlim=(x_min + self.startx - x, x_max+ self.startx - x),ylim=(y_min + self.starty - y, y_max + self.starty - y))
            else:
                self.visible_tm = self.annot_tm.get_visible()
                contain, i = self.ax_tm_mainline.contains(event)
                if contain:
                    index = i['ind'][0]
                    x = self.xdata[index]
                    y = self.ydata[index]
                    self.annot_tm.xy = (x,y)
                    self.annot_tm.set_text(str(x) + ',' + str(y))
                    self.annot_tm.set_visible(True)
                else:
                    if self.visible_tm:
                        self.annot_tm.set_visible(False)
            event.canvas.draw_idle()

    # 坐标系移动模式
    is_panmode = False
    # 坐标系移动前的x,y初始值
    startx = None
    starty = None

    def on_click(self,event):
        if self.data is None:
            return
        # if self.zooming:
        #     return
        if event.button == 1:
            if event.inaxes is not None:
                self.is_panmode = True
                x, y = event.xdata, event.ydata
                self.startx = x
                self.starty = y
        elif event.button == 3:
            if event.inaxes == self.ax_tm:
                contain, x = self.ax_tm_mainline.contains(event)
                if contain:
                    self.clickIndex = x['ind'][0]
                    self.show = 0
                else:
                    self.show = 1
            else:
                self.show = -1

    def show_detail(self):
        if self.detail is None:
            return
        self.detailDailog = DetailDailog(self, self.detail)
        self.detailDailog.exec()

    def openResult(self):
        self.resultDailog = RusultDailog(self,self.resultlist)
        self.resultDailog.resultSignal.connect(self.changeHistory)
        self.resultDailog.exec()

    def changeHistory(self,items):
        self.resultlist = items

    v0 = None
    FDFrocelist = []

    def dragEnterEvent(self, a0):
        if a0.mimeData().hasUrls():
            a0.accept()
        else:
            a0.ignore()

    def dropEvent(self, event):
        try:
            if event.mimeData().hasUrls:
                event.setDropAction(Qt.CopyAction)
                event.accept()
                links = []
                for url in event.mimeData().urls():
                    links.append(str(url.toLocalFile()))
                if len(links) > 0:
                    filepath = links[0]
                    if os.path.isfile(filepath) and (os.path.splitext(filepath)[1] == '.txt' or os.path.splitext(filepath)[1] == '.xlsx'):
                        self.open_file(filepath)
                    elif os.path.isdir(filepath):
                        self.open_dir(filepath)
            else:
                event.ignore()
        except Exception as e:
            print(e)

    def contextMenuEvent(self, e):
        if self.inaxes is False:
            return
        if self.data is None:
            return
        if self.show == -1:
            return
        else :
            # 创建菜单
            cmenu = QMenu(self)
            selectAc = None
            selectReset = None
            selectFD = None
            resetV0 = None
            zoomAction = None
            if self.show == 0:
                selectAc = cmenu.addAction("Set Retract Point")
                # if self.v0 is None and self.xlabel == 'Time (s)':
                #     selectFD = cmenu.addAction("Set Applied Load Start Point")
            # if self.v0 is not None and self.xlabel == 'Time (s)':
            #     resetV0 = cmenu.addAction("Reset Applied Load Start Point")
            if self.init_x_min is not None:
                x_min, x_max = self.ax_tm.get_xlim()
                y_min, y_max = self.ax_tm.get_ylim()
                if self.init_x_min != x_min or self.init_x_max != x_max or self.init_y_min != y_min or self.init_y_max != y_max:
                    selectReset = cmenu.addAction("Reset graphics")
            if self.zooming:
                zoomAction = cmenu.addAction("Out Zoom Mode")
            else:
                zoomAction = cmenu.addAction("Zoom Mode")
            action = cmenu.exec_(self.mapToGlobal(e.pos()))
            # 菜单动作
            if selectAc is not None and action == selectAc:
                self.retract_index = self.clickIndex
                self.setindexdata()
                self.draw_tm_retract(self.xdata[self.retract_index],self.ydata[self.retract_index])
                self.canvas_tm.draw_idle()
                self.compute_s_data()
                self.calculateResult()
            elif selectReset is not None and action == selectReset:
                if self.zooming:
                    self.toolbar.zoom()
                    self.zooming = not self.zooming
                self.ax_tm.set(xlim=(self.init_x_min, self.init_x_max),ylim=(self.init_y_min, self.init_y_max))
            elif selectFD is not None and action == selectFD:
                if self.sensitivity is None or self.sensitivity <= 0:
                    self.showErrorDialog('Should Set Sensitivity')
                    return
                if self.data.springConstant is None or self.data.springConstant <= 0:
                    self.showErrorDialog('Should Set SpringConstant')
                    return
                self.FDFrocelist = []
                self.v0 = self.data.V_list[self.clickIndex]
                for index in range(len(self.data.V_list)):
                    self.FDFrocelist.append(self.getForceData(self.data.V_list[index]))
                self.initDataXY()
                self.draw_t_m(False)
            elif resetV0 is not None and action == resetV0:
                self.FDFrocelist = []
                self.v0 = None
                self.initDataXY()
                self.draw_t_m(False)
            elif zoomAction is not None and action == zoomAction:
                self.toolbar.zoom()
                self.zooming = not self.zooming

    def setindexdata(self):
        self.pu = self.data.V_list[self.retract_index]
        self.hu = self.data.m_list[self.retract_index]
        self.label_pu.setText(str('%.3e' % self.pu))
        self.label_hu.setText(str('%.3e' % self.hu))
        self.rt_et.setText(str(self.data.T_list[self.retract_index]))

    def setResult(self,datas):
        self.loading.close()
        data_len = len(datas)
        if data_len>0:
            lenth = len(datas[0].T_list)
            if lenth == 0:
                self.show_no_data_warning()
            else:
                self.data = datas[0]
                if self.retract_index+1 > lenth:
                    self.retract_index = 0
                if not self.checkBoxApplyToAll.isChecked():
                    self.retract_index = 0
                if self.cf.isForceMode():
                    self.finalSetResult()
                else:
                    self.data.springConstant = np.array(self.data.springConstant, dtype=np.float64)
                    self.data.sensitivity = np.array(self.data.sensitivity, dtype=np.float64)
                    if str(self.data.springConstant) == self.cf.getSpringConstant() and str(self.data.sensitivity) == self.cf.getSensitivity():
                        self.updateForceModeData()
                        self.finalSetResult()
                    else:
                        self.show_spring_contant_confirm()
        else:
            self.show_no_data_warning()

    def updateForceModeData(self):
        self.v0 = 0
        for index in range(len(self.data.V_list)):
            self.data.V_list[index] = self.getForceData(self.data.V_list[index])

    def show_spring_contant_confirm(self):
        title = 'Notice'
        content = 'The detected \n springConstant=' + str(self.data.springConstant) + ' sensitivity=' + str(self.data.sensitivity) +' Use or not?'
        button = QMessageBox.warning(self,title,content,QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        if button == QMessageBox.Yes:
            self.cf.setSpringConstant(str(self.data.springConstant))
            self.cf.setSensitivity(str(self.data.sensitivity))
        else:
            self.data.springConstant = np.array(self.cf.getSpringConstant(), dtype=np.float64)
            self.data.sensitivity = np.array(self.cf.getSensitivity(), dtype=np.float64)
        self.updateForceModeData()
        self.finalSetResult()

    def finalSetResult(self):
        self.initDataXY()
        self.draw_t_m(True)
        if self.retract_index>0:
            self.setindexdata()
            self.compute_s_data()
            self.calculateResult()


    def showErrorDialog(self,msg):
        QMessageBox.information(self,'Information', str(msg)) 

    def show_no_data_warning(self):
        title = 'No Data'
        content = 'Current data is empty,Do you want to open the settings?'
        button = QMessageBox.warning(self,title,content,QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        if button == QMessageBox.Yes:
            self.show_config()

    def draw_ax_tm_smoothline(self):
        if self.smooth_level == 0:
            if self.ax_tm_smoothline is not None:
                self.ax_tm_smoothline.set_data([], [])
                self.canvas_tm.draw()
            return
        x = self.xdata
        y = self.get_smooth_y()
        if self.ax_tm_smoothline is None:
            self.ax_tm_smoothline, = self.ax_tm.plot(x, y, 'o', markersize=2,
                                                     color=self.cf.getSmoothLineColor())
        else:
            self.ax_tm_smoothline.set_data(x, y)
        self.canvas_tm.draw()

    def draw_tm_retract(self,x,y):
        if self.retract_index < 0:
            return
        if self.ax_tm_retractpoint is None:
            self.ax_tm_retractpoint, = self.ax_tm.plot(x, y, 'o', markersize=5, color=self.cf.getRetractPointColor(),
                                                       label='RetractTimePoint')
        else:
            self.ax_tm_retractpoint.set_data(x, y)
        self.draw_before(self.getbeforeindex())
        self.draw_after(self.getafterindex())

    def initDataXY(self):
        self.smooth_level = 0
        self.xlabel =self.get_lab(self.ls[0])
        self.ylabel =self.get_lab(self.ls[1])
        self.xdata = self.get_data(self.ls[0])
        self.ydata = self.get_data(self.ls[1])


    def refresh_combo(self,ls):
        self.x_combo.clear()
        self.y_combo.clear()
        for x in ls:
            self.x_combo.addItem(x)
            self.y_combo.addItem(x)
        self.y_combo.setCurrentIndex(1)


    def get_lab(self,name):
        if name == 'Time':
            return 'Time (s)'
        elif name == 'Froce':
            return 'Applied Load (N)'
        elif name == 'Height':
            return 'Height (m)'


    def get_data(self,arg):
        if arg == 'Time':
            return self.data.T_list
        elif arg == 'Froce':
            return self.data.V_list
        elif arg == 'Height':
            return self.data.m_list


    def on_x_select(self,arg):
        if self.data is None:
            return
        self.xdata = self.get_data(arg)
        self.xlabel =self.get_lab(arg)
        self.smooth_spinBox.setValue(0)
        self.draw_t_m(False)

    def on_y_select(self,arg):
        if self.data is None:
            return
        self.ydata = self.get_data(arg)
        self.ylabel =self.get_lab(arg)
        self.smooth_spinBox.setValue(0)
        self.draw_t_m(False)

    def on_smooth_change(self,arg):
        if self.data is None:
            return
        if arg == -1:
            return
        if self.xlabel != 'Time (s)':
            return
        self.smooth_level = arg
        self.draw_ax_tm_smoothline()

    def get_smooth_y(self):
        f = UnivariateSpline(self.xdata,self.ydata, s=self.smooth_spinBox.value())
        return f(self.xdata)

    ax_tm_kAfterLine = None
    ax_tm_kBeforeLine = None
    ax_tm_kAfterText = None
    ax_tm_kBeforeText = None
    ax_tm_smoothline = None
    ax_tm_retractpoint = None
    ax_tm_beforeline = None
    ax_tm_afterline = None
    ax_tm_beforepoint = None
    ax_tm_afterpoint = None

    def clear_ax_lines(self):
        self.ax_tm_kAfterLine = None
        self.ax_tm_kBeforeLine = None
        self.ax_tm_kAfterText = None
        self.ax_tm_kBeforeText = None
        self.ax_tm_mainline = None
        self.ax_tm_smoothline = None
        self.ax_tm_retractpoint = None
        self.ax_tm_beforeline = None
        self.ax_tm_afterline = None
        self.ax_tm_beforepoint = None
        self.ax_tm_afterpoint = None

    def draw_r2_before(self,before):
        if self.data is None:
            return
        if self.ax_tm is None:
            return
        if self.retract_index < 0 or self.retract_index-before<1:
            if self.ax_tm_kBeforeLine is not None:
                self.ax_tm_kBeforeLine.set_data([], [])
            if self.ax_tm_kBeforeText is not None:
                self.ax_tm_kBeforeText.set_text('')
            self.r2_before.setText(str(1))
            self.slope_before.setText(str(0))
            return
        if self.xlabel != 'Time (s)':
            return
        x1 = self.xdata[before:self.retract_index]
        y1 = self.ydata[before:self.retract_index]
        temx1 = np.array(x1).astype(np.float64).reshape(len(x1), 1)
        temy1 = np.array(y1).astype(np.float64).reshape(len(y1), 1)
        reg1 = LinearRegression().fit(temx1, temy1)
        k = reg1.coef_[0][0]
        b = reg1.intercept_[0]
        if self.ax_tm_kBeforeLine is None:
            self.ax_tm_kBeforeLine, = self.ax_tm.plot(temx1, reg1.predict(temx1), color='red', linewidth=1)
        else:
            self.ax_tm_kBeforeLine.set_data(temx1, reg1.predict(temx1))
        r2 = reg1.score(temx1, temy1)
        self.r2_before.setText(str(round(r2,2)))
        self.slope_before.setText(str('%.3e' % k))
        text = "R2 = %.5f" % (r2)
        if self.ax_tm_kBeforeText is None:
            self.ax_tm_kBeforeText = self.ax_tm.text(temx1[0], reg1.predict(temx1)[0], text, fontsize=8,
                                                     rotation_mode='anchor')
        else:
            self.ax_tm_kBeforeText.set_text(text)
            self.ax_tm_kBeforeText.set_x(temx1[0])
            self.ax_tm_kBeforeText.set_y(reg1.predict(temx1)[0])

    def draw_r2_after(self, after):
        if self.data is None:
            return
        if self.ax_tm is None:
            return
        if self.retract_index < 0 or after-self.retract_index<1:
            if self.ax_tm_kAfterLine is not None:
                self.ax_tm_kAfterLine.set_data([], [])
            if self.ax_tm_kAfterText is not None:
                self.ax_tm_kAfterText.set_text('')
            self.r2_after.setText(str(1))
            self.slope_after.setText(str(0))
            return
        if self.xlabel != 'Time (s)':
            return
        x2 = self.xdata[self.retract_index:after]
        y2 = self.ydata[self.retract_index:after]

        temx1 = np.array(x2).astype(np.float64).reshape(len(x2), 1)
        temy1 = np.array(y2).astype(np.float64).reshape(len(y2), 1)

        reg1 = LinearRegression().fit(temx1, temy1)
        k = reg1.coef_[0][0]
        b = reg1.intercept_[0]

        if self.ax_tm_kAfterLine is None:
            self.ax_tm_kAfterLine, = self.ax_tm.plot(temx1, reg1.predict(temx1), color='red', linewidth=1)
        else:
            self.ax_tm_kAfterLine.set_data(temx1, reg1.predict(temx1))
        r2 = reg1.score(temx1, temy1)
        self.r2_after.setText(str(round(r2,2)))
        self.slope_after.setText(str('%.3e' % k))
        text = "R2 = %.5f" % ( r2)
        if self.ax_tm_kAfterText is None:
            self.ax_tm_kAfterText = self.ax_tm.text(temx1[0], reg1.predict(temx1)[0], text, fontsize=8,
                                                     rotation_mode='anchor')
        else:
            self.ax_tm_kAfterText.set_text(text)
            self.ax_tm_kAfterText.set_x(temx1[0])
            self.ax_tm_kAfterText.set_y(reg1.predict(temx1)[0])

    def draw_t_m(self,calculate):
        if self.data is None:
            return
        if len(self.data.T_list) == 0:
             self.show_no_data_warning()
        else:
            self.ax_tm.cla()
            self.ax_tm.grid()
            self.clear_ax_lines()
            self.ax_tm.set(xlabel=self.xlabel, ylabel=self.ylabel, title=self.xlabel + '-' + self.ylabel)
            y_formatter = ScalarFormatter(useOffset=True)
            y_formatter.set_powerlimits((-2,2))
            self.ax_tm.yaxis.set_major_formatter(y_formatter)
            self.ax_tm.xaxis.set_major_formatter(y_formatter)
            self.ax_tm_mainline, = self.ax_tm.plot(self.xdata, self.ydata, 'o', markersize=2, color=self.cf.getDataLineColor())
            x_min, x_max = self.ax_tm.get_xlim()
            y_min, y_max = self.ax_tm.get_ylim()
            self.init_x_min = x_min
            self.init_x_max = x_max
            self.init_y_min = y_min
            self.init_y_max = y_max
            self.draw_tm_retract(self.xdata[self.retract_index], self.ydata[self.retract_index])

            # annotate
            self.annot_tm = self.ax_tm.annotate("",xy=(0,0), xytext=(-50, 50),
                                textcoords='offset pixels',
                                bbox=dict(boxstyle="round",fc="#7eff14"),
                                arrowprops=dict(arrowstyle="->")
                                )
            self.annot_tm.set_visible(False)
            self.canvas_tm.draw()
            if calculate:
                self.calculateResult()

    def getbeforeindex(self):
        before_count=0
        try:
            before_count = int(self.bc_et.text())
        except Exception as e:
            pass
        before = self.retract_index - before_count
        if(before < 0):
            before = 0
        return before

    def getafterindex(self):
        after_count=0
        try:
            after_count = int(self.ac_et.text())
        except Exception as e:
            pass
        after = self.retract_index + after_count
        if(after >= len(self.data.T_list)):
            after = len(self.data.T_list)-1
        if after <= 0:
            after = 0
        return after

    def draw_before(self,before):
        self.before_time.setText(str(self.data.T_list[before]))
        if self.xlabel == 'Time (s)':
            if self.ax_tm_beforeline is None:
                self.ax_tm_beforeline = self.ax_tm.axvline(x=self.xdata[before], linestyle='--', color=self.cf.getCountPointColor())
            else:
                self.ax_tm_beforeline.set_xdata(self.xdata[before])
        else:
            if self.ax_tm_beforepoint is None:
                self.ax_tm_beforepoint, = self.ax_tm.plot(self.xdata[before], self.ydata[before], 'o', markersize=5,
                                                          color=self.cf.getCountPointColor())
            else:
                self.ax_tm_beforepoint.set_xdata(self.xdata[before])
                self.ax_tm_beforepoint.set_ydata(self.ydata[before])
        self.draw_r2_before(before)
        self.canvas_tm.draw()

    def draw_after(self, after):
        self.after_time.setText(str(self.data.T_list[after]))
        if self.xlabel == 'Time (s)':
            self.draw_r2_after(after)
            if self.ax_tm_afterline is None:
                self.ax_tm_afterline = self.ax_tm.axvline(x=self.xdata[after], linestyle='--', color=self.cf.getCountPointColor())
            else:
                self.ax_tm_afterline.set_xdata(self.xdata[after])
        else:
            if self.ax_tm_afterpoint is None:
                self.ax_tm_afterpoint, = self.ax_tm.plot(self.xdata[after], self.ydata[after], 'o', markersize=5,
                                                         color=self.cf.getCountPointColor())
            else:
                self.ax_tm_afterpoint.set_xdata(self.xdata[after])
                self.ax_tm_afterpoint.set_ydata(self.ydata[after])
        self.canvas_tm.draw()

    def show_config(self):
        self.configD = ConfigDailog(self)
        self.configD.exec()

    def openbatch(self):
        dir=QFileDialog.getExistingDirectory(self,"Select Directory",self.settings.value('selectdir',"/"))
        if dir == '':
            return
        self.settings.setValue('selectdir', os.path.abspath(dir))
        self.open_dir(dir)

    def open_dir(self,dir):
        self.resultlist.clear()
        self.filelist.clear()
        for i in os.listdir(dir):
            if os.path.splitext(i)[1] == '.txt' or os.path.splitext(i)[1] == '.xlsx' or os.path.splitext(i)[1] == '.xls':
                self.filelist.append(os.path.join(dir, i))
        if len(self.filelist) <= 0:
            self.showErrorDialog('Not Found .txt .xlsx .xls File')
            return
        self.inputdata(self.filelist[0])
        self.fileindex = 0
        self.setfileIndexAandCount()
        self.settings.setValue('isOpenFile', False)

    def next(self):
        if self.data is None:
            return
        if len(self.filelist) <= self.fileindex +1:
            self.showToast("It's the last one")
            return
        self.fileindex = self.fileindex + 1
        self.setfileIndexAandCount()
        self.inputdata(self.filelist[self.fileindex])

    def last(self):
        if self.data is None:
            return
        if self.fileindex == 0:
            self.showToast("It's the first one")
            return
        self.fileindex = self.fileindex - 1
        self.setfileIndexAandCount()
        self.inputdata(self.filelist[self.fileindex])

    def setfileIndexAandCount(self):
        i = self.fileindex+1
        count = len(self.filelist)
        text = str(i) + '/'+str(count)
        self.countindex.setText(text)

    def add_result(self):
        if self.detail is None:
            return
        if self.curfilename == '':
            return
        key = str(self.curfilename).replace('/','\\')
        detail = self.create_detail()
        self.resultlist.update({key: detail})
        self.showToast('Add Result:' + key)

    def create_detail(self):
        if self.radioselect == 0:
            detail = Detail(self.hh, self.s, self.es, self.pu, self.hu, self.hc, self.ac, None)
        else:
            detail = Detail(self.hh, self.s, self.es, self.pu, self.hu, None, None, self.radius)
        return detail

    def open(self):
        files,ok1=QFileDialog.getOpenFileNames(self,"Select File",self.settings.value('select',"/"),"Text Files (*.txt *.xlsx *.xls)")
        if(len(files) > 0):
            self.settings.setValue('select', os.path.abspath(os.path.dirname(files[0])+os.path.sep+"."))
            if len(files) <= 0:
                self.showErrorDialog('Not Found .txt .xlsx .xls File')
                return
            self.open_file(files[0])

    def open_file(self,filepath):
        self.resultlist.clear()
        crashDir = FileWriter.mkcrashfile(filepath)
        cgitb.enable(display=1,logdir=crashDir,format='text')
        self.inputdata(filepath)
        self.filelist.clear()
        self.filelist.append(filepath)
        self.fileindex = 0
        self.setfileIndexAandCount()
        self.settings.setValue('isOpenFile', True)



    def inputdata(self,file):
        file = file.replace('/','\\')
        self.setWindowTitle(file)
        self.detail = None
        self.curfilename = file
        self.workThread.addData([file])
        self.workThread.start()
        self.loading = LoadingDailog(self)
        self.loading.exec()

    def exportExcel(self):
        if self.resultlist is None or len(self.resultlist) == 0:
            self.showToast('No Result')
            return
        filename,filetype=QFileDialog.getSaveFileName(self,'save file','/E.xlsx',"Text Files (*.xlsx)")
        if filename == "":
            return
        try:
            ExcelWriter.write(filename, self.resultlist)
            self.showToast('Save Success:' + filename)
        except Exception as i:
            print(repr(i))
            self.showErrorDialog('Excel Writer Error,maybe the file has been opened')


    def save(self):
        if self.resultlist is None or len(self.resultlist) == 0:
            self.showToast('No Result')
            return
        filename,filetype=QFileDialog.getSaveFileName(self,'save file','/E.txt',"Text Files (*.txt)")
        if filename == "":
            return
        FileWriter.write(filename, self.resultlist)
        self.showToast('Save Success:' + filename)

    def help(self):
        QDesktopServices.openUrl(QUrl.fromLocalFile('res/text/help.pdf'))

    def closeEvent(self, event):
        plt.close()


if __name__ == '__main__':
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    pixmap = QPixmap("res/luncher.png")
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    splash = QSplashScreen(pixmap)
    splash.show()
    app.processEvents()
    ex = MainTool(' ')
    splash.finish(ex)
    sys.exit(app.exec_())