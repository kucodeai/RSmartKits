# -*- coding: utf-8 -*-

# Form
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import qtawesome

class SwitchBtn(QWidget):
    # 信号
    checkedChanged = pyqtSignal(bool)

    def __init__(self, parent=None, checked=False):
        super(QWidget, self).__init__(parent)
        self.checked = checked
        self.bgColorOff = QColor(169, 169, 169)
        self.bgColorOn = QColor(124, 252, 0)

        self.sliderColorOff = QColor(245,245,245)
        self.sliderColorOn = QColor(245, 245, 245)

        self.textColorOff = QColor(143, 143, 143)
        self.textColorOn = QColor(255, 255, 255)

        self.textOff = "OFF"
        self.textOn = "ON"

        self.space = 2
        self.rectRadius = 5

        self.step = self.width() / 50
        if checked:
            self.startX = self.height()
        else:
            self.startX = 0
        self.endX = 0

        self.timer = QTimer(self)  # 初始化一个定时器
        self.timer.timeout.connect(self.updateValue)  # 计时结束调用operate()方法

        #self.timer.start(5)  # 设置计时间隔并启动

        self.setFont(QFont("Microsoft Yahei", 10))

        #self.resize(55,22)

    def updateValue(self):
        if self.checked:
            if self.startX < self.endX:
                self.startX = self.startX + self.step
            else:
                self.startX = self.endX
                self.timer.stop()
        else:
            if self.startX  > self.endX:
                self.startX = self.startX - self.step
            else:
                self.startX = self.endX
                self.timer.stop()

        self.update()

    def mousePressEvent(self, event):
        self.checked = not self.checked
        #发射信号
        self.checkedChanged.emit(self.checked)

        # 每次移动的步长为宽度的50分之一
        self.step = self.width() / 50
        #状态切换改变后自动计算终点坐标
        if self.checked:
            self.endX = self.width() - self.height()
            # print("11111 ")
        else:
            self.endX = 0
        self.timer.start(5)

    def paintEvent(self, evt):
        #绘制准备工作, 启用反锯齿
            painter = QPainter()
            painter.begin(self)
            painter.setRenderHint(QPainter.Antialiasing)

            #绘制背景
            self.drawBg(evt, painter)
            #绘制滑块
            self.drawSlider(evt, painter)
            #绘制文字
            self.drawText(evt, painter)

            painter.end()

    def drawText(self, event, painter):
        painter.save()

        if self.checked:
            painter.setPen(self.textColorOn)
            painter.drawText(0, 0, self.width() / 2 + self.space * 2, self.height(), Qt.AlignCenter, self.textOn)
        else:
            painter.setPen(self.textColorOff)
            painter.drawText(self.width() / 2, 0, self.width() / 2 - self.space, self.height(), Qt.AlignCenter, self.textOff)

        painter.restore()

    def drawBg(self, event, painter):
        painter.save()
        painter.setPen(Qt.NoPen)

        if self.checked:
            painter.setBrush(self.bgColorOn)
        else:
            painter.setBrush(self.bgColorOff)

        rect = QRect(0, 0, self.width(), self.height())
        #半径为高度的一半
        radius = rect.height() / 2
        #圆的宽度为高度
        circleWidth = rect.height()

        path = QPainterPath()
        path.moveTo(radius, rect.left())
        path.arcTo(QRectF(rect.left(), rect.top(), circleWidth, circleWidth), 90, 180)
        path.lineTo(rect.width() - radius, rect.height())
        path.arcTo(QRectF(rect.width() - rect.height(), rect.top(), circleWidth, circleWidth), 270, 180)
        path.lineTo(radius, rect.top())

        painter.drawPath(path)
        painter.restore()

    def drawSlider(self, event, painter):
        painter.save()

        if self.checked:
            painter.setBrush(self.sliderColorOn)
        else:
            painter.setBrush(self.sliderColorOff)

        rect = QRect(0, 0, self.width(), self.height())
        sliderWidth = rect.height() - self.space * 2
        sliderRect = QRect(self.startX + self.space, self.space, sliderWidth, sliderWidth)
        painter.drawEllipse(sliderRect)

        painter.restore()
        
class MainUi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
            self.setFixedSize(980, 610)
            self.main_widget = QWidget()  # 创建窗口主部件
            self.setWindowIcon(QIcon("/etc/kucodeai/images/logo.ico"))
            self.main_layout = QGridLayout()  # 创建主部件的网格布局
            self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局

            self.left_widget = QWidget()  # 创建左侧部件
            self.left_widget.setObjectName('left_widget')
            self.left_layout = QGridLayout()  # 创建左侧部件的网格布局层
            self.left_widget.setLayout(self.left_layout)  # 设置左侧部件布局为网格
            self.right_widget = QWidget()  # 创建右上侧部件
            self.right_widget.setObjectName('right_widget')
            self.right_layout = QGridLayout()
            self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为网格

            self.right_down_widget = QWidget()  # 创建右下侧部件
            self.right_down_widget.setObjectName('right_down_widget')
            self.right_down_layout = QGridLayout()
            self.right_down_widget.setLayout(self.right_down_layout)  # 设置右侧部件布局为网格

            self.right_up_widget = QWidget()  # 创建右上侧部件
            self.right_up_widget.setObjectName('right_up_widget')
            self.right_up_layout = QGridLayout()
            self.right_up_widget.setLayout(self.right_up_layout)  # 设置右侧部件布局为网格

            self.right_down_widget = QWidget()  # 创建右下侧部件
            self.right_down_widget.setObjectName('right_down_widget')
            self.right_down_layout = QGridLayout()
            self.right_down_widget.setLayout(self.right_down_layout)  # 设置右侧部件布局为网格

            self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2)  # 左侧部件在第0行第0列，占8行3列
            # self.main_layout.addWidget(self.right_up_widget, 0, 2, 2, 10)  # 左侧部件在第0行第0列，占8行3列
            self.main_layout.addWidget(self.right_widget, 0, 2, 12, 10)  # 右侧部件在第0行第3列，占8行9列
            self.setCentralWidget(self.main_widget)  # 设置窗口主部件

            self.right_layout.addWidget(self.right_up_widget, 0, 0, 1, 9)
            self.right_layout.addWidget(self.right_down_widget, 1, 0, 8, 9)
            self.left_close = QPushButton("")  # 关闭按钮
            self.left_mini = QPushButton("")  # 最小化按钮

            self.left_connect_label = QPushButton("锐智导航")
            self.left_connect_label.setObjectName('left_label')
            self.left_settings_label = QPushButton("AI模型库")
            self.left_settings_label.setObjectName('left_label')
            self.left_help__label = QPushButton("帮助中心")
            self.left_help__label.setObjectName('left_label')

            self.left_button_1 = QPushButton(qtawesome.icon('fa.book', color='#5F6366'), "课程列表")
            self.left_button_1.setObjectName('left_button')
            self.left_button_3 = QPushButton(qtawesome.icon('fa.camera', color='#5F6366'), "环境测试")
            self.left_button_3.setObjectName('left_button')
            self.left_button_4 = QPushButton(qtawesome.icon('fa.object-group', color='#5F6366'), "对象识别")
            self.left_button_4.setObjectName('left_button')
            self.left_button_5 = QPushButton(qtawesome.icon('fa.cog', color='#5F6366'), "系统设置")
            self.left_button_5.setObjectName('left_button')
            self.left_btn_info=QPushButton(qtawesome.icon('fa.info-circle', color='#5F6366'), "版本信息")
            self.left_btn_info.setObjectName('left_button')


            self.left_layout.addWidget(self.left_mini, 0, 1, 1, 3)
            self.left_layout.addWidget(self.left_close, 0, 2, 1, 2)
            self.left_layout.addWidget(self.left_connect_label, 2, 0, 1, 3)
            self.left_layout.addWidget(self.left_button_1, 3, 0, 1, 3)
            self.left_layout.addWidget(self.left_settings_label, 5, 0, 1, 3)
            # self.left_layout.addWidget(self.left_button_2, 6, 0, 1, 3)
            self.left_layout.addWidget(self.left_button_3, 6, 0, 1, 3)
            self.left_layout.addWidget(self.left_button_4, 7, 0, 1, 3)
            self.left_layout.addWidget(self.left_help__label, 9, 0, 1, 3)
            self.left_layout.addWidget(self.left_button_5, 10, 0, 1, 3)
            self.left_layout.addWidget(self.left_btn_info, 11, 0, 1, 3)
            
            self.right_bar_widget = QWidget()  # 右侧顶部logo部件
            self.right_bar_layout = QGridLayout()  # 右侧顶部logo网格布局
            self.right_bar_widget.setLayout(self.right_bar_layout)
            self.kucodeAI_icon = QLabel()
            self.kucodeAI_icon.setPixmap(QPixmap("/etc/kucodeai/images/logo.ico"))
            self.kucodeAI_label = QLabel('KucodeAI-锐智')
            self.kucodeAI_label.setFont(qtawesome.font('fa', 24))

            self.right_bar_layout.addWidget(self.kucodeAI_icon, 0, 0, 1, 4, Qt.AlignRight)
            self.right_bar_layout.addWidget(self.kucodeAI_label, 0, 4, 1, 5, Qt.AlignLeft)

            self.right_up_layout.addWidget(self.right_bar_widget, 0, 0, 1, 9)
            # self.right_layout.addWidget(self.right_one_widget, 1, 0, 8, 9)
            

            # 顶部三个按钮Qss
            self.left_close.setFixedSize(15, 15)  # 设置关闭按钮的大小
            self.left_mini.setFixedSize(15, 15)  # 设置最小化按钮大小
            self.left_close.setStyleSheet(
                '''QPushButton{background:#F76677;border-radius:7px;}
                QPushButton:hover{background:red;}''')
            self.left_mini.setStyleSheet(
                '''QPushButton{background:#6DDF6D;border-radius:7px;}
                QPushButton:hover{background:green;}''')

            # 左部Qss
            self.left_widget.setStyleSheet('''
                QPushButton{border:none;color:#303030;}
                QPushButton#left_label{
                    border:none;
                    border-bottom:1px solid #303030;
                    font-size:18px;
                    font-weight:700;
                }
                QPushButton#left_button:hover{border-left:6px solid #06D66E;font-weight:700;}
                QWidget#left_widget{
                    background:#ECEFF4;
                    border-top:1px solid white;
                    border-bottom:1px solid white;
                    border-left:1px solid white;
                    border-top-left-radius:10px;
                    border-bottom-left-radius:10px;
                    }
            ''')

            # 右部Qss
            self.right_widget.setStyleSheet('''
                QWidget#right_widget{
                    color:#232C51;
                    background:white;
                    border-top:1px solid darkGray;
                    border-bottom:1px solid darkGray;
                    border-right:1px solid darkGray;
                    border-top-right-radius:10px;
                    border-bottom-right-radius:10px;
                }
                QLabel#right_lable{
                    border:none;
                    font-size:16px;
                    font-weight:700;
                }
            ''')

            self.right_up_widget.setStyleSheet('''
                QWidget#right_up_widget{
                    border-bottom: 2px solid darkGray;
                }
            ''')
            
            # self.setWindowOpacity(0.95)  # 设置窗口透明度
            self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口背景透明
            self.setWindowFlag(Qt.FramelessWindowHint)  # 隐藏边框
            self.main_layout.setSpacing(0)

            self.config_setting_widget = QWidget()
            self.system_setting_widget = QWidget()
            self.help_widget = QWidget()
            self.first_widget = QWidget()
            
            # 配置页面
            self.config_setting_ui = Ui_Setting1_Form()
            self.config_setting_ui.setupUi(self.config_setting_widget)
            self.right_down_layout.addWidget(self.config_setting_widget)

            # 系统设置页面
            self.system_setting_ui = Ui_SystemSettings()
            self.system_setting_ui.setupUi(self.system_setting_widget)
            self.right_down_layout.addWidget(self.system_setting_widget)

            # 版本说明页面
            self.help_ui = Ui_HelpUi()
            self.help_ui.setupUi(self.help_widget)
            self.right_down_layout.addWidget(self.help_widget)

            # 主页连接页面
            self.first_ui = Ui_FirstPage()
            self.first_ui.setupUi(self.first_widget)
            self.right_down_layout.addWidget(self.first_widget)

            # 分享配置窗口
            self.share_ui = QDialog()
            self.share_child_ui = Ui_Share_Dialog()
            self.share_child_ui.setupUi(self.share_ui)

            # # 二维码分享配置窗口
            # self.qr_ui = QDialog()
            # self.qr_child_ui = Ui_Qr_Dialog()
            # self.qr_child_ui.setupUi(self.qr_ui)

            # 添加ss窗口
            self.ss_add_ui = QDialog()
            self.ss_add_child_ui = Ui_Add_Ss_Dialog()
            self.ss_add_child_ui.setupUi(self.ss_add_ui)

            # 添加vmess窗口
            self.vmess_add_ui = QDialog()
            self.vmess_add_child_ui = Ui_Add_Vmess_Dialog()
            self.vmess_add_child_ui.setupUi(self.vmess_add_ui)

            # 订阅设置窗口
            self.subs_ui = QDialog()
            self.subs_child_ui = Ui_Subs_Dialog()
            self.subs_child_ui.setupUi(self.subs_ui)

            # 订阅设置窗口
            self.add_subs_ui = QDialog()
            self.subs_add_child_ui = Ui_Add_Subs_Form()
            self.subs_add_child_ui.setupUi(self.add_subs_ui)

            # 托盘菜单
            self.a1 = QAction('恢复')
            self.a2 = QAction('退出')
            self.logMenu = QMenu("日志")
            self.a3 = QAction('启用', checkable=True)
            self.a4 = QAction('禁用', checkable=True)
            self.proxyMenu = QMenu("全局代理")
            self.a5 = QAction('白名单模式', checkable=True)
            self.a6 = QAction('黑名单模式', checkable=True)
            self.a7 = QAction('关闭全局代理', checkable=True)
            self.logMenu.addAction(self.a3)
            self.logMenu.addAction(self.a4)
            self.proxyMenu.addAction(self.a5)
            self.proxyMenu.addAction(self.a6)
            self.proxyMenu.addAction(self.a7)
            self.tpMenu = QMenu()
            self.tpMenu.addAction(self.a1)
            self.tpMenu.addSeparator()
            self.tpMenu.addMenu(self.logMenu)
            self.tpMenu.addSeparator()
            self.tpMenu.addMenu(self.proxyMenu)
            self.tpMenu.addSeparator()
            self.tpMenu.addAction(self.a2)

            self.current_page = self.first_widget
            self.config_setting_widget.hide()
            self.system_setting_widget.hide()
            self.help_widget.hide()
                
            self.left_mini.clicked.connect(self.on_left_mini_clicked)
            self.left_close.clicked.connect(self.on_left_close_clicked)
            self.left_button_1.clicked.connect(self.change_to_firstPage)
            self.left_button_3.clicked.connect(self.change_to_configSetting)
            self.left_button_4.clicked.connect(self.change_to_Help)
            self.left_button_5.clicked.connect(self.change_to_systemSetting)
            self.left_btn_info.clicked.connect(self.change_to_Help)
        
        
    def change_to_firstPage(self):
            self.current_page.hide()
            self.first_widget.show()
            self.current_page = self.first_widget

    def change_to_systemSetting(self):
            self.current_page.hide()
            self.system_setting_widget.show()
            self.current_page = self.system_setting_widget

    def change_to_configSetting(self):
            self.current_page.hide()
            self.config_setting_widget.show()
            self.current_page = self.config_setting_widget

    def change_to_Help(self):
            self.current_page.hide()
            self.help_widget.show()
            self.current_page = self.help_widget

    def mousePressEvent(self, event):
            if event.button() == Qt.LeftButton:
                self.m_flag = True
                self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
                event.accept()
                self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
            if Qt.LeftButton and self.m_flag:
                self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
                QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
            self.m_flag = False
            self.setCursor(QCursor(Qt.ArrowCursor))

    def on_left_close_clicked(self):
            """
            关闭窗口
            """
            self.close()

    def on_left_mini_clicked(self):
            """
            最小化窗口
            """
            self.showMinimized()


class Ui_Setting1_Form(object):
    def setupUi(self, Form):
            Form.setObjectName("Form")
            Form.resize(796, 489)
            self.label = QLabel(Form)

            self.retranslateUi(Form)
            QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
            _translate = QCoreApplication.translate
            Form.setWindowTitle(_translate("Form", "Form"))
           


class Ui_SystemSettings(object):
    def setupUi(self, SystemSettings):
            SystemSettings.setObjectName("SystemSettings")
            SystemSettings.resize(796, 489)
            
            self.label = QLabel(SystemSettings)
            self.label.setGeometry(QRect(310, 40, 101, 31))
            self.label.setStyleSheet("font-size: 24px;\n"
                                     "color:rgb(136, 138, 133);")
            self.label.setObjectName("label")
            

            self.retranslateUi(SystemSettings)
            QMetaObject.connectSlotsByName(SystemSettings)

    def retranslateUi(self, SystemSettings):
            _translate = QCoreApplication.translate
            SystemSettings.setWindowTitle(_translate("SystemSettings", "Form"))


class Ui_HelpUi(object):
    def setupUi(self, HelpUi):
            HelpUi.setObjectName("HelpUi")
            HelpUi.resize(796, 489)
            self.label_3 = QLabel(HelpUi)
            self.label_3.setGeometry(QRect(40, 40, 611, 231))
            self.label_3.setObjectName("label_3")
            self.label = QLabel(HelpUi)
            self.label.setGeometry(QRect(130, 260, 481, 171))
            self.label.setObjectName("label")

            self.retranslateUi(HelpUi)
            QMetaObject.connectSlotsByName(HelpUi)

    def retranslateUi(self, HelpUi):
            _translate = QCoreApplication.translate
            HelpUi.setWindowTitle(_translate("HelpUi", "Form"))
            self.label_3.setWhatsThis(_translate("HelpUi", "<html><head/><body><p><br/></p></body></html>"))
            self.label_3.setText(_translate("HelpUi", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\"; font-size:11pt; font-weight:400; font-style:normal;\">\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">当前版本</span></p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">——————————————————————</span></p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">v0.1</span></p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">说明</span></p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">——————————————————————</span></p></body></html>"))
            self.label.setText(_translate("HelpUi",
            "1. 讨论区地址:https://disscus.kucodeai.com \n"
            "2. 目前此版本仅支持锐智AI第一期课程\n"
            "3. 程序可能存在未测试到的Bug，使用过程中发现Bug请在讨论区提交"))


class CenterDelegate(QItemDelegate):
    def __init__(self, parent=None):
        QItemDelegate.__init__(self, parent)

    def paint(self, painter, option, index):
        painter.save()
        painter.drawText(option.rect, Qt.AlignCenter, str(index.data(Qt.DisplayRole)))
        painter.restore()


class Ui_FirstPage(object):
    def setupUi(self, Form):
        self.label = QLabel(Form)
        
        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def add_item(self, args):
        item = QTableWidgetItem(str(args[0]))
        self.tableWidget.setItem(args[0]-1, 0, item)
        item = QTableWidgetItem(args[1])
        self.tableWidget.setItem(args[0]-1, 1, item)
        item = QTableWidgetItem(args[2])
        self.tableWidget.setItem(args[0]-1, 2, item)
        item = QTableWidgetItem(args[3])
        self.tableWidget.setItem(args[0]-1, 3, item)
        item = QTableWidgetItem("")
        self.tableWidget.setItem(args[0] - 1, 4, item)
        label_1 = QLabel()
        if args[4]:
            switchBtn = SwitchBtn(label_1, True)
        else:
            switchBtn = SwitchBtn(label_1, False)
        switchBtn.setGeometry(20, 5, 60, 30)
        switchBtn.checkedChanged.connect(lambda: args[5](args[0]-1, not switchBtn.checked))
        self.tableWidget.setCellWidget(args[0]-1, 4, label_1)
        item = QTableWidgetItem("")
        self.tableWidget.setItem(args[0] - 1, 5, item)
        button1 = QPushButton("删除")
        button1.setObjectName("delbt")
        button1.setStyleSheet('''
            #delbt{border-width: 0px; 
            border-radius: 15px; 
            background: red; 
            outline: none; 
            color: white; 
            font-size: 13px; 
            margin:5px;
            }
            #delbt:hover{ background: #FF6347;}
        ''')
        button1.clicked.connect(lambda: args[6](args[0]-1))
        self.tableWidget.setCellWidget(args[0]-1, 5, button1)
        item = QTableWidgetItem("")
        self.tableWidget.setItem(args[0] - 1, 6, item)
        button2 = QPushButton("分享")
        button2.setObjectName("delbt")
        button2.setStyleSheet('''
            #delbt{border-width: 0px; 
            border-radius: 15px; 
            background: #1E90FF; 
            outline: none; 
            color: white; 
            font-size: 13px; 
            margin:5px;
            }
            #delbt:hover{ background: #5599FF;}
        ''')
        button2.clicked.connect(lambda: args[7](args[1]))
        self.tableWidget.setCellWidget(args[0]-1, 6, button2)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        
        self.label.setText(_translate("Form", "名称"))
      


class Ui_Share_Dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(565, 480)
        dialog.setStyleSheet("#dialog{color:#232C51;  background:white; }")
        # dialog.setWindowOpacity(0.95)  # 设置窗口透明度
        self.label = QLabel(dialog)
        self.label.setGeometry(QRect(170, 20, 200, 200))
        self.label.setText("")
        self.label.setObjectName("label")
        self.textBrowser = QTextBrowser(dialog)
        self.textBrowser.setGeometry(QRect(20, 250, 501, 171))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(dialog)
        QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "配置分享"))


class Ui_Add_Ss_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(314, 329)
        Dialog.setStyleSheet("""
                   #Dialog{
                color:#232C51;
                background:white;
            }
            """)
       # Dialog.setWindowOpacity(0.95)  # 设置窗口透明度
       # Dialog.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.label = QLabel(Dialog)
        self.label.setGeometry(QRect(20, 30, 111, 20))
        self.label.setObjectName("label")
        self.label_2 = QLabel(Dialog)
        self.label_2.setGeometry(QRect(20, 80, 121, 17))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QRect(70, 30, 221, 25))
        self.lineEdit_2.setStyleSheet("border-style:none none solid none;background-color:transparent;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QLabel(Dialog)
        self.label_3.setGeometry(QRect(20, 130, 121, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QLabel(Dialog)
        self.label_4.setGeometry(QRect(20, 180, 131, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QLabel(Dialog)
        self.label_5.setGeometry(QRect(20, 230, 121, 17))
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QRect(70, 80, 221, 25))
        self.lineEdit_3.setStyleSheet("border-style:none none solid none;background-color:transparent;")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QRect(70, 130, 221, 25))
        self.lineEdit_4.setStyleSheet("border-style:none none solid none;background-color:transparent;")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QRect(70, 180, 221, 25))
        self.lineEdit_5.setStyleSheet("border-style:none none solid none;background-color:transparent;")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setEchoMode(QLineEdit.Password)
        self.comboBox = QComboBox(Dialog)
        self.comboBox.setGeometry(QRect(100, 230, 191, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setGeometry(QRect(80, 280, 151, 31))
        self.pushButton.setStyleSheet("#pushButton{border-width: 0px; border-radius: 15px; background: #1E90FF; outline: none; color: white; font-size: 13px; } \n"
"#pushButton:hover{ background: #5599FF;}")
        self.pushButton.setObjectName("pushButton")
        self.line = QFrame(Dialog)
        self.line.setGeometry(QRect(70, 50, 231, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QFrame(Dialog)
        self.line_2.setGeometry(QRect(70, 100, 231, 16))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QFrame(Dialog)
        self.line_3.setGeometry(QRect(70, 150, 231, 16))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QFrame(Dialog)
        self.line_4.setGeometry(QRect(70, 200, 231, 16))
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.line_4.setObjectName("line_4")

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "手动添加ShadowSocks配置"))
        self.label.setText(_translate("Dialog", "别名:"))
        self.label_2.setText(_translate("Dialog", "地址:"))
        self.label_3.setText(_translate("Dialog", "端口:"))
        self.label_4.setText(_translate("Dialog", "密码:"))
        self.label_5.setText(_translate("Dialog", "加密方式:"))
        self.comboBox.setItemText(0, _translate("Dialog", "aes-256-cfb"))
        self.comboBox.setItemText(1, _translate("Dialog", "aes-128-cfb"))
        self.comboBox.setItemText(2, _translate("Dialog", "chacha20"))
        self.comboBox.setItemText(3, _translate("Dialog", "chacha20-ietf"))
        self.comboBox.setItemText(4, _translate("Dialog", "aes-256-gcm"))
        self.comboBox.setItemText(5, _translate("Dialog", "aes-128-gcm"))
        self.comboBox.setItemText(6, _translate("Dialog", "chacha20-poly1305"))
        self.comboBox.setItemText(7, _translate("Dialog", "chacha20-ietf-poly1305"))
        self.pushButton.setText(_translate("Dialog", "确认添加"))


class Ui_Add_Vmess_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(465, 527)
        Dialog.setStyleSheet("#Dialog{color:#232C51;  background:white; }")
        # Dialog.setWindowOpacity(0.95)  # 设置窗口透明度
        self.label = QLabel(Dialog)
        self.label.setGeometry(QRect(30, 35, 111, 17))
        self.label.setObjectName("label")
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setGeometry(QRect(140, 30, 301, 25))
        self.lineEdit.setStyleSheet("border-style:none none solid none;background-color:transparent;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QLabel(Dialog)
        self.label_2.setGeometry(QRect(30, 75, 121, 17))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QRect(120, 70, 321, 25))
        self.lineEdit_2.setStyleSheet("border-style:none none solid none;background-color:transparent;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QLabel(Dialog)
        self.label_3.setGeometry(QRect(30, 115, 101, 17))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QRect(120, 110, 321, 25))
        self.lineEdit_3.setStyleSheet("border-style:none none solid none;background-color:transparent;")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QLabel(Dialog)
        self.label_4.setGeometry(QRect(30, 155, 91, 17))
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QRect(120, 150, 321, 25))
        self.lineEdit_4.setStyleSheet("border-style:none none solid none;background-color:transparent;")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QRect(150, 190, 291, 25))
        self.lineEdit_5.setStyleSheet("border-style:none none solid none;background-color:transparent;")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_5 = QLabel(Dialog)
        self.label_5.setGeometry(QRect(30, 195, 111, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QLabel(Dialog)
        self.label_6.setGeometry(QRect(30, 240, 121, 17))
        self.label_6.setObjectName("label_6")
        self.label_7 = QLabel(Dialog)
        self.label_7.setGeometry(QRect(30, 330, 111, 17))
        self.label_7.setObjectName("label_7")
        self.comboBox = QComboBox(Dialog)
        self.comboBox.setGeometry(QRect(150, 235, 86, 25))
        #self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_8 = QLabel(Dialog)
        self.label_8.setGeometry(QRect(30, 286, 221, 21))
        self.label_8.setObjectName("label_8")
        self.comboBox_2 = QComboBox(Dialog)
        self.comboBox_2.setGeometry(QRect(150, 325, 86, 25))
        #self.comboBox_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")

        self.comboBox_3 = QComboBox(Dialog)
        self.comboBox_3.setGeometry(QRect(150, 437, 86, 25))
        # self.comboBox_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_3.setObjectName("comboBox_2")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label_9 = QLabel(Dialog)
        self.label_9.setGeometry(QRect(30, 365, 121, 17))
        self.label_9.setObjectName("label_9")
        self.lineEdit_6 = QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QRect(150, 360, 291, 25))
        self.lineEdit_6.setStyleSheet("border-style:none none solid none;background-color:transparent;")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_10 = QLabel(Dialog)
        self.label_10.setGeometry(QRect(30, 405, 67, 19))
        self.label_10.setObjectName("label_10")
        self.label_11 = QLabel(Dialog)
        self.label_11.setGeometry(QRect(30, 437, 125, 20))
        self.label_11.setObjectName("label_11")
        self.lineEdit_7 = QLineEdit(Dialog)
        self.lineEdit_7.setGeometry(QRect(80, 400, 361, 25))
        self.lineEdit_7.setStyleSheet("border-style:none none solid none;background-color:transparent;")
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.line = QFrame(Dialog)
        self.line.setGeometry(QRect(140, 45, 301, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QFrame(Dialog)
        self.line_2.setGeometry(QRect(120, 88, 321, 16))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QFrame(Dialog)
        self.line_3.setGeometry(QRect(120, 128, 321, 16))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QFrame(Dialog)
        self.line_4.setGeometry(QRect(120, 168, 321, 16))
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QFrame(Dialog)
        self.line_5.setGeometry(QRect(150, 208, 291, 20))
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QFrame(Dialog)
        self.line_6.setGeometry(QRect(150, 378, 291, 20))
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QFrame(Dialog)
        self.line_7.setGeometry(QRect(80, 415, 361, 20))
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setGeometry(QRect(160, 475, 151, 31))
        self.pushButton.setStyleSheet("#pushButton{border-width: 0px; border-radius: 15px; background: #1E90FF; outline: none; color: white; font-size: 13px; }\n"
"#pushButton:hover{ background: #5599FF;}")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "手动添加Vmess配置"))
        self.label.setText(_translate("Dialog", "别名(remark)："))
        self.label_2.setText(_translate("Dialog", "地址(addr)："))
        self.label_3.setText(_translate("Dialog", "端口(port)："))
        self.label_4.setText(_translate("Dialog", "用户ID(id)："))
        self.label_5.setText(_translate("Dialog", "额外ID(alterId)："))
        self.label_6.setText(_translate("Dialog", "传输协议(net)："))
        self.label_7.setText(_translate("Dialog", "伪装类型(type)："))
        self.comboBox.setItemText(0, _translate("Dialog", "ws"))
        self.comboBox.setItemText(1, _translate("Dialog", "kcp"))
        self.comboBox.setItemText(2, _translate("Dialog", "tcp"))
        self.label_8.setText(_translate("Dialog", "下列配置无则保持默认"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "none"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "http"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "utp"))
        self.comboBox_2.setItemText(3, _translate("Dialog", "wechat-video"))
        self.comboBox_2.setItemText(4, _translate("Dialog", "dtls"))
        self.comboBox_2.setItemText(5, _translate("Dialog", "strp"))
        self.comboBox_2.setItemText(6, _translate("Dialog", "wireguard"))
        self.comboBox_3.setItemText(0, _translate("Dialog", ""))
        self.comboBox_3.setItemText(1, _translate("Dialog", "tls"))
        self.label_9.setText(_translate("Dialog", "伪装域名(host)："))
        self.label_10.setText(_translate("Dialog", "path："))
        self.label_11.setText(_translate("Dialog", "底层传输安全："))
        self.pushButton.setText(_translate("Dialog", "确认添加"))


class Ui_Subs_Dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(652, 350)
        dialog.setMinimumSize(QSize(652, 350))
        dialog.setMaximumSize(QSize(652, 350))
        dialog.setStyleSheet("#dialog{background:white; }")
        self.tableWidget = QTableWidget(dialog)
        self.tableWidget.setGeometry(QRect(0, 0, 651, 260))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.pushButton = QPushButton(dialog)
        self.pushButton.setGeometry(QRect(240, 290, 191, 41))
        self.pushButton.setStyleSheet(
            "#pushButton{border-width: 0px; border-radius: 15px; background: #1E90FF; outline: none; color: white; font-size: 18px; }\n"
            "#pushButton:hover{ background: #5599FF;}")
        self.pushButton.setObjectName("pushButton")

        self.tableWidget.setShowGrid(False)
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setFixedHeight(40)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        #self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.setItemDelegate(CenterDelegate())
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setColumnWidth(0, 30)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 425)
        self.tableWidget.setColumnWidth(3, 30)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget.setStyleSheet('''
                    #tableWidget{
                        selection-background-color:white;
                    }

                ''')
        self.tableWidget.setFocusPolicy(Qt.NoFocus)


        self.tableWidget.verticalScrollBar().setStyleSheet(
            "QScrollBar{background:transparent; width: 12px;}"
            "QScrollBar::handle{background:lightgray; border:2px solid transparent; border-radius:5px;}"
            "QScrollBar::handle:hover{background:gray;}"
            "QScrollBar::sub-line{background:transparent;}"
            "QScrollBar::add-line{background:transparent;}")

        self.retranslateUi(dialog)
        QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "v2rayL"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("dialog", "序号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("dialog", "别名"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("dialog", "订阅地址"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("dialog", ""))
        self.pushButton.setText(_translate("dialog", "新增订阅"))

def add_item(self, args):
        # self.tableWidget.setRowCount(self.num)
        item = QTableWidgetItem(str(args[0]))
        self.tableWidget.setItem(args[0] - 1, 0, item)
        item = QTableWidgetItem(args[1])
        self.tableWidget.setItem(args[0] - 1, 1, item)
        item = QTableWidgetItem(args[2][:57])
        self.tableWidget.setItem(args[0] - 1, 2, item)
        item = QTableWidgetItem("")
        self.tableWidget.setItem(args[0] - 1, 3, item)
        button1 = QPushButton("删除")
        button1.setObjectName("delbt")
        button1.setStyleSheet('''
                       #delbt{border-width: 0px; 
                       border-radius: 15px; 
                       background: red; 
                       outline: none; 
                       color: white; 
                       font-size: 13px; 
                       margin:5px;
                       }
                       #delbt:hover{ background: #FF6347;}
                   ''')
        button1.clicked.connect(lambda: args[3](args[0] - 1))
        self.tableWidget.setCellWidget(args[0] - 1, 3, button1)


class Ui_Add_Subs_Form(object):
    def setupUi(self, dialog):
        dialog.setObjectName("Form")
        dialog.resize(312, 278)
        dialog.setMinimumSize(QSize(312, 278))
        dialog.setMaximumSize(QSize(312, 278))
        self.label = QLabel(dialog)
        self.label.setGeometry(QRect(20, 10, 51, 31))
        self.label.setObjectName("label")
        self.textEdit = QTextEdit(dialog)
        self.textEdit.setGeometry(QRect(20, 120, 271, 101))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QLabel(dialog)
        self.label_2.setGeometry(QRect(20, 90, 67, 17))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QLineEdit(dialog)
        self.lineEdit.setGeometry(QRect(20, 50, 271, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QPushButton(dialog)
        self.pushButton.setGeometry(QRect(110, 240, 90, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet(
            "#pushButton{border-width: 0px; border-radius: 15px; background: #1E90FF; outline: none; color: white; font-size: 18px; }\n"
            "#pushButton:hover{ background: #5599FF;}")

        self.retranslateUi(dialog)
        QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "v2rayL"))
        self.label.setText(_translate("dialog", "别名："))
        self.label_2.setText(_translate("dialog", "地址："))
        self.pushButton.setText(_translate("dialog", "添加"))
        

def main():
    app = QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
