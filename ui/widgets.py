from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


class Ui_First_menu(object):
    def setupUi(self, First_menu):
        First_menu.setObjectName("First_menu")
        First_menu.setWindowModality(QtCore.Qt.NonModal)
        First_menu.resize(466, 377)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(First_menu.sizePolicy().hasHeightForWidth())
        First_menu.setSizePolicy(sizePolicy)
        First_menu.setMinimumSize(QtCore.QSize(466, 377))
        First_menu.setMaximumSize(QtCore.QSize(466, 377))
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        font.setPointSize(9)
        First_menu.setFont(font)
        First_menu.setFocusPolicy(QtCore.Qt.StrongFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/photo_data/latch.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        First_menu.setWindowIcon(icon)
        First_menu.setStyleSheet("QLineEdit{\n"
                                 "    border: 2px solid rgb(240, 240, 240);\n"
                                 "    border-radius: 10px;\n"
                                 "    padding-left: 10px;\n"
                                 "    padding-right: 10px;\n"
                                 "    }\n"
                                 "\n"
                                 "QLineEdit:hover{\n"
                                 "    border: 2px solid rgb(211, 211, 211)\n"
                                 "    }\n"
                                 "QLineEdit:focus{\n"
                                 "    border: 2px solid rgb(85, 170, 255);\n"
                                 "    }\n"
                                 "QPushButton {\n"
                                 "background-color: #0d6efd;\n"
                                 "border: 1px solid #343155; color: #fff;\n"
                                 "padding: 6px; border-radius: 10px;}\n"
                                 "\n"
                                 "QPushButton:hover, QPushButton:clicked { \n"
                                 "background-color: #0b5ed7; \n"
                                 "border: 1px solid #9ac3fe;}\n"
                                 "QPushButton:pressed {\n"
                                 "background-color:rgb(10, 87, 194) ;}")
        First_menu.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(First_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(466, 336))
        self.centralwidget.setMaximumSize(QtCore.QSize(466, 377))
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(-1, 6, -1, 0)
        self.gridLayout.setVerticalSpacing(7)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(108, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(202, 0))
        font = QtGui.QFont()
        font.setFamily("VAG World")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(108, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(219, 252))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("ui/photo_data/login_photo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 2)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(223, 0))
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.groupBox.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setVerticalSpacing(3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.login_edit = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_edit.sizePolicy().hasHeightForWidth())
        self.login_edit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        font.setPointSize(11)
        self.login_edit.setFont(font)
        self.login_edit.setStyleSheet("")
        self.login_edit.setText("")
        self.login_edit.setObjectName("login_edit")
        self.gridLayout_2.addWidget(self.login_edit, 0, 0, 1, 1)
        self.password_edit = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password_edit.sizePolicy().hasHeightForWidth())
        self.password_edit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        font.setPointSize(11)
        self.password_edit.setFont(font)
        self.password_edit.setStyleSheet("")
        self.password_edit.setText("")
        self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_edit.setObjectName("password_edit")
        self.gridLayout_2.addWidget(self.password_edit, 1, 0, 1, 1)
        self.password_repeat_edit = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password_repeat_edit.sizePolicy().hasHeightForWidth())
        self.password_repeat_edit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        font.setPointSize(11)
        self.password_repeat_edit.setFont(font)
        self.password_repeat_edit.setStyleSheet("")
        self.password_repeat_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_repeat_edit.setClearButtonEnabled(False)
        self.password_repeat_edit.setObjectName("password_repeat_edit")
        self.gridLayout_2.addWidget(self.password_repeat_edit, 2, 0, 1, 1)
        self.btn_registration = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_registration.sizePolicy().hasHeightForWidth())
        self.btn_registration.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_registration.setFont(font)
        self.btn_registration.setObjectName("btn_registration")
        self.gridLayout_2.addWidget(self.btn_registration, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 2, 2, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.have_account_btn = QtWidgets.QRadioButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.have_account_btn.sizePolicy().hasHeightForWidth())
        self.have_account_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        font.setPointSize(11)
        self.have_account_btn.setFont(font)
        self.have_account_btn.setStyleSheet("QRadioButton:hover{\n"
                                            "    border: 2px solid rgb(39, 194, 126);\n"
                                            "    border-radius: 1px;\n"
                                            "    }")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui/photo_data/check_mark.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.have_account_btn.setIcon(icon1)
        self.have_account_btn.setChecked(True)
        self.have_account_btn.setObjectName("have_account_btn")
        self.horizontalLayout.addWidget(self.have_account_btn)
        self.no_account_btn = QtWidgets.QRadioButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.no_account_btn.sizePolicy().hasHeightForWidth())
        self.no_account_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        font.setPointSize(11)
        self.no_account_btn.setFont(font)
        self.no_account_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.no_account_btn.setStyleSheet("QRadioButton:hover{\n"
                                          "    border: 2px solid rgb(219, 36, 34);\n"
                                          "    border-radius: 1px;\n"
                                          "    }")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ui/photo_data/cross.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.no_account_btn.setIcon(icon2)
        self.no_account_btn.setChecked(False)
        self.no_account_btn.setObjectName("no_account_btn")
        self.horizontalLayout.addWidget(self.no_account_btn)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 4)
        First_menu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(First_menu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 466, 21))
        self.menubar.setObjectName("menubar")
        First_menu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(First_menu)
        self.statusbar.setStatusTip("")
        self.statusbar.setObjectName("statusbar")
        First_menu.setStatusBar(self.statusbar)

        self.retranslateUi(First_menu)
        QtCore.QMetaObject.connectSlotsByName(First_menu)

    def retranslateUi(self, First_menu):
        _translate = QtCore.QCoreApplication.translate
        First_menu.setWindowTitle(_translate("First_menu", "Вход  / регистрация"))
        self.label_2.setText(_translate("First_menu", "Your CardGame"))
        self.groupBox.setTitle(_translate("First_menu", "Зарегистрироваться"))
        self.login_edit.setPlaceholderText(_translate("First_menu", "Логин"))
        self.password_edit.setPlaceholderText(_translate("First_menu", "Пароль"))
        self.password_repeat_edit.setPlaceholderText(_translate("First_menu", "Повторите пароль"))
        self.btn_registration.setText(_translate("First_menu", "Зарегистрироваться"))
        self.have_account_btn.setText(_translate("First_menu", "Есть аккаунт"))
        self.no_account_btn.setText(_translate("First_menu", "Нет аккаунта"))

    def keyPressEvent(self, event):
        if event.key() == 16777220:
            self.btn_registration.click()


class Ui_Collections_and_card_menu(object):
    def setupUi(self, Collections_and_card_menu):
        Collections_and_card_menu.setObjectName("Collections_and_card_menu")
        Collections_and_card_menu.resize(700, 677)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Collections_and_card_menu.sizePolicy().hasHeightForWidth())
        Collections_and_card_menu.setSizePolicy(sizePolicy)
        Collections_and_card_menu.setMinimumSize(QtCore.QSize(700, 676))
        Collections_and_card_menu.setMaximumSize(QtCore.QSize(16777215, 16777215))
        Collections_and_card_menu.setFocusPolicy(QtCore.Qt.StrongFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/photo_data/window_icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Collections_and_card_menu.setWindowIcon(icon)
        Collections_and_card_menu.setToolTip("")
        self.centralwidget = QtWidgets.QWidget(Collections_and_card_menu)
        self.centralwidget.setMinimumSize(QtCore.QSize(700, 0))
        self.centralwidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(6, 3, 6, 3)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_statistics = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_statistics.sizePolicy().hasHeightForWidth())
        self.btn_statistics.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        font.setPointSize(11)
        self.btn_statistics.setFont(font)
        self.btn_statistics.setStyleSheet("QPushButton {\n"
                                          "background-color: rgb(0,0,0);\n"
                                          "border: 1px solid #343155;color: #FFF;\n"
                                          "padding: 6px; border-radius: 10px;}\n"
                                          "\n"
                                          "QPushButton:hover, QPushButton:clicked { \n"
                                          "background-color: rgb(43, 43, 43); \n"
                                          "border: 1px solid #FFF;}\n"
                                          "QPushButton:pressed {\n"
                                          "background-color: rgb(127, 127, 127);}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui/photo_data/statistics_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_statistics.setIcon(icon1)
        self.btn_statistics.setObjectName("btn_statistics")
        self.horizontalLayout_3.addWidget(self.btn_statistics)
        self.profile_login_browse = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.profile_login_browse.sizePolicy().hasHeightForWidth())
        self.profile_login_browse.setSizePolicy(sizePolicy)
        self.profile_login_browse.setMinimumSize(QtCore.QSize(565, 29))
        self.profile_login_browse.setMaximumSize(QtCore.QSize(16777215, 29))
        self.profile_login_browse.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.profile_login_browse.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.profile_login_browse.setFrameShadow(QtWidgets.QFrame.Plain)
        self.profile_login_browse.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.profile_login_browse.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.profile_login_browse.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.profile_login_browse.setTabChangesFocus(False)
        self.profile_login_browse.setUndoRedoEnabled(False)
        self.profile_login_browse.setOverwriteMode(False)
        self.profile_login_browse.setObjectName("profile_login_browse")
        self.horizontalLayout_3.addWidget(self.profile_login_browse)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.collection_box = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.collection_box.sizePolicy().hasHeightForWidth())
        self.collection_box.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.collection_box.setFont(font)
        self.collection_box.setStyleSheet("/* Стиль для коибо */\n"
                                          "#collection_box{\n"
                                          "    border: 1 px solid #ced4da;\n"
                                          "    border-radius: 4px;\n"
                                          "    padding-left: 10px;}\n"
                                          "\n"
                                          "/* Стиль для арены со стрелкой */\n"
                                          "#collection_box::drop-down{\n"
                                          "    border:0px;}\n"
                                          "\n"
                                          "#collection_box::down-arrow{\n"
                                          "    image: url(ui/photo_data/down_arrow_list.png);\n"
                                          "    width: 13 px;\n"
                                          "    height: 13px;\n"
                                          "    margin-right: 15px;\n"
                                          "}\n"
                                          "\n"
                                          "#collection_box:on{\n"
                                          "    border: 4px solid #c2dbfe;\n"
                                          "}\n"
                                          "\n"
                                          "\n"
                                          "#collection_box QListView{\n"
                                          "    font-size: 12px;\n"
                                          "    border: 1px solid rgba(0, 0, 0, 10%);\n"
                                          "    border-radius: 8px;\n"
                                          "    padding: 5px;\n"
                                          "    background-color: #fff;\n"
                                          "    outline: 0px;\n"
                                          "}\n"
                                          "\n"
                                          "#collection_box QListView::item{\n"
                                          "    padding-left: 10px;\n"
                                          "    background-color: #fff;\n"
                                          "}\n"
                                          "\n"
                                          "#collection_box QListView::item:hover{\n"
                                          "    background-color: #1e90ff;\n"
                                          "}\n"
                                          "\n"
                                          "#collection_box QListView::item:selected{\n"
                                          "    background-color: #1e90ff;\n"
                                          "}")
        self.collection_box.setMaxVisibleItems(3)
        self.collection_box.setObjectName("collection_box")
        self.collection_box.addItem("")
        self.horizontalLayout_2.addWidget(self.collection_box)
        self.btn_add_collection = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_add_collection.sizePolicy().hasHeightForWidth())
        self.btn_add_collection.setSizePolicy(sizePolicy)
        self.btn_add_collection.setMinimumSize(QtCore.QSize(55, 31))
        self.btn_add_collection.setMaximumSize(QtCore.QSize(55, 31))
        self.btn_add_collection.setStatusTip("")
        self.btn_add_collection.setWhatsThis("")
        self.btn_add_collection.setAccessibleName("")
        self.btn_add_collection.setAccessibleDescription("")
        self.btn_add_collection.setStyleSheet("QPushButton {\n"
                                              "background-color: rgb(225, 225, 225);\n"
                                              "border: 1px solid #343155; color: #fff;\n"
                                              "padding: 6px; border-radius: 10px;}\n"
                                              "\n"
                                              "QPushButton:hover, QPushButton:clicked { \n"
                                              "background-color: rgb(208, 208, 208); \n"
                                              "border: 1px solid rgb(171, 226, 81);}\n"
                                              "QPushButton:pressed {\n"
                                              "background-color:rgb(153, 218, 51) ;}")
        self.btn_add_collection.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ui/photo_data/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_add_collection.setIcon(icon2)
        self.btn_add_collection.setIconSize(QtCore.QSize(32, 20))
        self.btn_add_collection.setObjectName("btn_add_collection")
        self.horizontalLayout_2.addWidget(self.btn_add_collection)
        self.btn_del_collection = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_del_collection.sizePolicy().hasHeightForWidth())
        self.btn_del_collection.setSizePolicy(sizePolicy)
        self.btn_del_collection.setMinimumSize(QtCore.QSize(55, 31))
        self.btn_del_collection.setMaximumSize(QtCore.QSize(55, 31))
        self.btn_del_collection.setStyleSheet("QPushButton {\n"
                                              "background-color: rgb(225, 225, 225);\n"
                                              "border: 1px solid #343155; color: #fff;\n"
                                              "padding: 6px; border-radius: 10px;}\n"
                                              "\n"
                                              "QPushButton:hover, QPushButton:clicked { \n"
                                              "background-color: rgb(208, 208, 208); \n"
                                              "border: 1px solid rgb(225, 78, 78);}\n"
                                              "QPushButton:pressed {\n"
                                              "background-color:rgb(211, 79, 79);}")
        self.btn_del_collection.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("ui/photo_data/min.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_del_collection.setIcon(icon3)
        self.btn_del_collection.setIconSize(QtCore.QSize(32, 20))
        self.btn_del_collection.setObjectName("btn_del_collection")
        self.horizontalLayout_2.addWidget(self.btn_del_collection)
        self.btn_edit_collection = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_edit_collection.sizePolicy().hasHeightForWidth())
        self.btn_edit_collection.setSizePolicy(sizePolicy)
        self.btn_edit_collection.setMinimumSize(QtCore.QSize(55, 31))
        self.btn_edit_collection.setMaximumSize(QtCore.QSize(55, 31))
        self.btn_edit_collection.setStyleSheet("QPushButton {\n"
                                               "background-color: rgb(225, 225, 225);\n"
                                               "border: 1px solid #343155; color: #fff;\n"
                                               "padding: 6px; border-radius: 10px;}\n"
                                               "\n"
                                               "QPushButton:hover, QPushButton:clicked { \n"
                                               "background-color: rgb(208, 208, 208); \n"
                                               "border: 1px solid rgb(255, 152, 1);}\n"
                                               "QPushButton:pressed {\n"
                                               "background-color: rgb(218, 127, 0);}")
        self.btn_edit_collection.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("ui/photo_data/pencil.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_edit_collection.setIcon(icon4)
        self.btn_edit_collection.setIconSize(QtCore.QSize(32, 20))
        self.btn_edit_collection.setCheckable(False)
        self.btn_edit_collection.setObjectName("btn_edit_collection")
        self.horizontalLayout_2.addWidget(self.btn_edit_collection)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 9, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.btn_add_card = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add_card.setMinimumSize(QtCore.QSize(55, 31))
        self.btn_add_card.setMaximumSize(QtCore.QSize(55, 31))
        self.btn_add_card.setStyleSheet("QPushButton {\n"
                                        "background-color: rgb(225, 225, 225);\n"
                                        "border: 1px solid #343155; color: #fff;\n"
                                        "padding: 6px; border-radius: 10px;}\n"
                                        "\n"
                                        "QPushButton:hover, QPushButton:clicked { \n"
                                        "background-color: rgb(208, 208, 208); \n"
                                        "border: 1px solid rgb(171, 226, 81);}\n"
                                        "QPushButton:pressed {\n"
                                        "background-color:rgb(153, 218, 51) ;}")
        self.btn_add_card.setText("")
        self.btn_add_card.setIcon(icon2)
        self.btn_add_card.setIconSize(QtCore.QSize(32, 20))
        self.btn_add_card.setObjectName("btn_add_card")
        self.horizontalLayout.addWidget(self.btn_add_card)
        self.btn_del_card = QtWidgets.QPushButton(self.centralwidget)
        self.btn_del_card.setMinimumSize(QtCore.QSize(55, 31))
        self.btn_del_card.setMaximumSize(QtCore.QSize(55, 31))
        self.btn_del_card.setStyleSheet("QPushButton {\n"
                                        "background-color: rgb(225, 225, 225);\n"
                                        "border: 1px solid #343155; color: #fff;\n"
                                        "padding: 6px; border-radius: 10px;}\n"
                                        "\n"
                                        "QPushButton:hover, QPushButton:clicked { \n"
                                        "background-color: rgb(208, 208, 208); \n"
                                        "border: 1px solid rgb(225, 78, 78);}\n"
                                        "QPushButton:pressed {\n"
                                        "background-color:rgb(211, 79, 79);}")
        self.btn_del_card.setText("")
        self.btn_del_card.setIcon(icon3)
        self.btn_del_card.setIconSize(QtCore.QSize(32, 20))
        self.btn_del_card.setObjectName("btn_del_card")
        self.horizontalLayout.addWidget(self.btn_del_card)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.cards_in_collection = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cards_in_collection.sizePolicy().hasHeightForWidth())
        self.cards_in_collection.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cards_in_collection.setFont(font)
        self.cards_in_collection.setStyleSheet("QListWidget{\n"
                                               "    border: 1 px solid black;\n"
                                               "    border-radius: 1px;}")
        self.cards_in_collection.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.cards_in_collection.setIconSize(QtCore.QSize(20, 20))
        self.cards_in_collection.setMovement(QtWidgets.QListView.Static)
        self.cards_in_collection.setViewMode(QtWidgets.QListView.ListMode)
        self.cards_in_collection.setObjectName("cards_in_collection")
        item = QtWidgets.QListWidgetItem()
        self.cards_in_collection.addItem(item)
        self.verticalLayout.addWidget(self.cards_in_collection)
        self.label_for_descript = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_for_descript.sizePolicy().hasHeightForWidth())
        self.label_for_descript.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_for_descript.setFont(font)
        self.label_for_descript.setAlignment(QtCore.Qt.AlignCenter)
        self.label_for_descript.setObjectName("label_for_descript")
        self.verticalLayout.addWidget(self.label_for_descript)
        self.btn_start_game = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_start_game.sizePolicy().hasHeightForWidth())
        self.btn_start_game.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.btn_start_game.setFont(font)
        self.btn_start_game.setStatusTip("")
        self.btn_start_game.setStyleSheet("QPushButton {\n"
                                          "background-color: rgb(225, 225, 225);\n"
                                          "border: 1px solid #343155;\n"
                                          "padding: 6px; border-radius: 20px;}\n"
                                          "\n"
                                          "QPushButton:hover, QPushButton:clicked { \n"
                                          "background-color: rgb(208, 208, 208); \n"
                                          "border: 1px solid rgb(26, 71, 24);}\n"
                                          "QPushButton:pressed {\n"
                                          "background-color: rgb(60, 166, 57);}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("ui/photo_data/start_game.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_start_game.setIcon(icon5)
        self.btn_start_game.setIconSize(QtCore.QSize(32, 32))
        self.btn_start_game.setObjectName("btn_start_game")
        self.verticalLayout.addWidget(self.btn_start_game)
        self.gridLayout.addLayout(self.verticalLayout, 4, 0, 1, 1)
        Collections_and_card_menu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Collections_and_card_menu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 22))
        self.menubar.setToolTip("")
        self.menubar.setAccessibleName("")
        self.menubar.setAccessibleDescription("")
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        self.menu_help = QtWidgets.QMenu(self.menubar)
        self.menu_help.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.menu_help.setStatusTip("")
        self.menu_help.setWhatsThis("")
        self.menu_help.setAccessibleName("")
        self.menu_help.setAccessibleDescription("")
        self.menu_help.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menu_help.setStyleSheet("")
        self.menu_help.setTearOffEnabled(False)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("ui/photo_data/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_help.setIcon(icon6)
        self.menu_help.setSeparatorsCollapsible(False)
        self.menu_help.setToolTipsVisible(False)
        self.menu_help.setObjectName("menu_help")
        Collections_and_card_menu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Collections_and_card_menu)
        self.statusbar.setObjectName("statusbar")
        Collections_and_card_menu.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(Collections_and_card_menu)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("ui/photo_data/question_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action.setIcon(icon7)
        self.action.setObjectName("action")
        self.menu_help.addAction(self.action)
        self.menubar.addAction(self.menu_help.menuAction())

        self.retranslateUi(Collections_and_card_menu)
        QtCore.QMetaObject.connectSlotsByName(Collections_and_card_menu)

    def retranslateUi(self, Collections_and_card_menu):
        _translate = QtCore.QCoreApplication.translate
        Collections_and_card_menu.setWindowTitle(_translate("Collections_and_card_menu", "Your CardMemory"))
        self.btn_statistics.setText(_translate("Collections_and_card_menu", " Статистика"))
        self.profile_login_browse.setHtml(_translate("Collections_and_card_menu",
                                                     "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                     "p, li { white-space: pre-wrap; }\n"
                                                     "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:6.6pt; font-weight:400; font-style:normal;\">\n"
                                                     "<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Ваш профиль: </span><span style=\" font-size:11pt; font-weight:600;\">DSDAD</span></p></body></html>"))
        self.collection_box.setToolTip(_translate("Collections_and_card_menu", "Ваши коллекции"))
        self.collection_box.setItemText(0, _translate("Collections_and_card_menu", "NBTRNR"))
        self.btn_add_collection.setToolTip(_translate("Collections_and_card_menu", "Добавить коллекцию"))
        self.btn_del_collection.setToolTip(_translate("Collections_and_card_menu", "Удалить коллекцию"))
        self.btn_edit_collection.setToolTip(_translate("Collections_and_card_menu", "Изменить название коллекции"))
        self.label.setText(_translate("Collections_and_card_menu", "Ваши карточки"))
        self.btn_add_card.setToolTip(_translate("Collections_and_card_menu", "Добавить карточку в коллекцию"))
        self.btn_del_card.setToolTip(_translate("Collections_and_card_menu", "Удалить карточку из коллекции"))
        self.cards_in_collection.setSortingEnabled(True)
        __sortingEnabled = self.cards_in_collection.isSortingEnabled()
        self.cards_in_collection.setSortingEnabled(False)
        item = self.cards_in_collection.item(0)
        item.setText(_translate("Collections_and_card_menu", "ASDSAD"))
        self.cards_in_collection.setSortingEnabled(__sortingEnabled)
        self.label_for_descript.setText(_translate("Collections_and_card_menu", "Затычка"))
        self.btn_start_game.setToolTip(_translate("Collections_and_card_menu", "Начать игру с карточками из коллекции"))
        self.btn_start_game.setText(_translate("Collections_and_card_menu", " Начать игру"))
        self.menu_help.setToolTip(_translate("Collections_and_card_menu", "Помощь"))
        self.menu_help.setTitle(_translate("Collections_and_card_menu", "Помощь"))
        self.action.setText(_translate("Collections_and_card_menu", "Некоторые подсказки"))


class Ui_Collection_add(object):
    def setupUi(self, Collection_add):
        Collection_add.setObjectName("Collection_add")
        Collection_add.resize(577, 93)
        Collection_add.setMinimumSize(QtCore.QSize(577, 93))
        Collection_add.setMaximumSize(QtCore.QSize(577, 93))
        Collection_add.setFocusPolicy(QtCore.Qt.StrongFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/photo_data/add_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Collection_add.setWindowIcon(icon)
        Collection_add.setStyleSheet("QLineEdit{\n"
                                     "    border: 2px solid rgb(240, 240, 240);\n"
                                     "    border-radius: 10px;\n"
                                     "    padding-left: 10px;\n"
                                     "    padding-right: 10px;\n"
                                     "    }\n"
                                     "\n"
                                     "QLineEdit:hover{\n"
                                     "    border: 2px solid rgb(211, 211, 211)\n"
                                     "    }\n"
                                     "QLineEdit:focus{\n"
                                     "    border: 2px solid rgb(85, 170, 255);\n"
                                     "    }")
        self.gridLayout = QtWidgets.QGridLayout(Collection_add)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_collection_name = QtWidgets.QLineEdit(Collection_add)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_collection_name.sizePolicy().hasHeightForWidth())
        self.lineEdit_collection_name.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        font.setPointSize(11)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lineEdit_collection_name.setFont(font)
        self.lineEdit_collection_name.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.lineEdit_collection_name.setStyleSheet("QLineEdit{\n"
                                                    "    border: 2px solid rgb(240, 240, 240);\n"
                                                    "    border-radius: 10px;\n"
                                                    "    padding-left: 10px;\n"
                                                    "    padding-right: 10px;\n"
                                                    "    }\n"
                                                    "\n"
                                                    "QLineEdit:hover{\n"
                                                    "    border: 2px solid rgb(211, 211, 211)\n"
                                                    "    }\n"
                                                    "QLineEdit:focus{\n"
                                                    "    border: 2px solid rgb(85, 170, 255);\n"
                                                    "    }")
        self.lineEdit_collection_name.setText("")
        self.lineEdit_collection_name.setObjectName("lineEdit_collection_name")
        self.horizontalLayout.addWidget(self.lineEdit_collection_name)
        self.btn_save_collection = QtWidgets.QPushButton(Collection_add)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_save_collection.sizePolicy().hasHeightForWidth())
        self.btn_save_collection.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        font.setPointSize(10)
        self.btn_save_collection.setFont(font)
        self.btn_save_collection.setStyleSheet("QPushButton {\n"
                                               "background-color: rgb(225, 225, 225);\n"
                                               "border: 1px solid #343155;\n"
                                               "padding: 6px; border-radius: 15px;}\n"
                                               "\n"
                                               "QPushButton:hover, QPushButton:clicked { \n"
                                               "background-color: rgb(208, 208, 208); \n"
                                               "border: 1px solid rgb(171, 226, 81);}\n"
                                               "QPushButton:pressed {\n"
                                               "background-color:rgb(153, 218, 51) ;}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui/photo_data/check_mark.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_save_collection.setIcon(icon1)
        self.btn_save_collection.setAutoDefault(False)
        self.btn_save_collection.setObjectName("btn_save_collection")
        self.horizontalLayout.addWidget(self.btn_save_collection)
        self.btn_cancel = QtWidgets.QPushButton(Collection_add)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cancel.sizePolicy().hasHeightForWidth())
        self.btn_cancel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        font.setPointSize(10)
        self.btn_cancel.setFont(font)
        self.btn_cancel.setStyleSheet("QPushButton {\n"
                                      "background-color: rgb(225, 225, 225);\n"
                                      "border: 1px solid #343155;\n"
                                      "padding: 6px; border-radius: 15px;}\n"
                                      "\n"
                                      "QPushButton:hover, QPushButton:clicked { \n"
                                      "background-color: rgb(208, 208, 208); \n"
                                      "border: 1px solid rgb(225, 78, 78);}\n"
                                      "QPushButton:pressed {\n"
                                      "background-color:rgb(211, 79, 79);}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ui/photo_data/cross.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cancel.setIcon(icon2)
        self.btn_cancel.setAutoDefault(False)
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout.addWidget(self.btn_cancel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_error = QtWidgets.QLabel(Collection_add)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_error.setFont(font)
        self.label_error.setObjectName("label_error")
        self.verticalLayout.addWidget(self.label_error)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Collection_add)
        QtCore.QMetaObject.connectSlotsByName(Collection_add)

    def retranslateUi(self, Collection_add):
        _translate = QtCore.QCoreApplication.translate
        Collection_add.setWindowTitle(_translate("Collection_add", "Добавить коллекцию"))
        self.lineEdit_collection_name.setPlaceholderText(_translate("Collection_add", "Название коллекции"))
        self.btn_save_collection.setToolTip(_translate("Collection_add", "Добавить коллекцию"))
        self.btn_save_collection.setText(_translate("Collection_add", " Добавить"))
        self.btn_cancel.setToolTip(_translate("Collection_add", "Выйти обратно"))
        self.btn_cancel.setText(_translate("Collection_add", " Отмена"))
        self.label_error.setText(_translate("Collection_add", "Ошибка"))

    def keyPressEvent(self, event):
        if event.key() == 16777220:
            self.btn_save_collection.click()
        elif event.key() == Qt.Key_Escape:
            self.btn_cancel.click()


class Ui_Add_and_change_card(object):
    def setupUi(self, Add_and_change_card):
        Add_and_change_card.setObjectName("Add_and_change_card")
        Add_and_change_card.resize(990, 620)
        Add_and_change_card.setMinimumSize(QtCore.QSize(990, 620))
        Add_and_change_card.setFocusPolicy(QtCore.Qt.StrongFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/photo_data/add_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Add_and_change_card.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Add_and_change_card)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(264, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.comboBox = QtWidgets.QComboBox(Add_and_change_card)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QtCore.QSize(190, 0))
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        font.setPointSize(11)
        self.comboBox.setFont(font)
        self.comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox.setStyleSheet("/* Стиль для коибо */\n"
                                    "#comboBox{\n"
                                    "    border: 1 px solid #ced4da;\n"
                                    "    border-radius: 4px;\n"
                                    "    padding-left: 10px;}\n"
                                    "\n"
                                    "/* Стиль для арены со стрелкой */\n"
                                    "#comboBox::drop-down{\n"
                                    "    border:0px;}\n"
                                    "\n"
                                    "#comboBox::down-arrow{\n"
                                    "    image: url(ui/photo_data/down_arrow_list.png);\n"
                                    "    width: 13 px;\n"
                                    "    height: 13px;\n"
                                    "    margin-right: 15px;\n"
                                    "}\n"
                                    "\n"
                                    "#comboBox:on{\n"
                                    "    border: 4px solid #c2dbfe;\n"
                                    "}\n"
                                    "\n"
                                    "\n"
                                    "#comboBox QListView{\n"
                                    "    font-size: 12px;\n"
                                    "    border: 1px solid rgba(0, 0, 0, 10%);\n"
                                    "    border-radius: 8px;\n"
                                    "    padding: 5px;\n"
                                    "    background-color: #fff;\n"
                                    "    outline: 0px;\n"
                                    "}\n"
                                    "\n"
                                    "#comboBox QListView::item{\n"
                                    "    padding-left: 10px;\n"
                                    "    background-color: #fff;\n"
                                    "}\n"
                                    "\n"
                                    "#comboBox QListView::item:hover{\n"
                                    "    background-color: #1e90ff;\n"
                                    "}\n"
                                    "\n"
                                    "#comboBox QListView::item:selected{\n"
                                    "    background-color: #1e90ff;\n"
                                    "}")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox)
        spacerItem2 = QtWidgets.QSpacerItem(39, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.btn_change_card = QtWidgets.QPushButton(Add_and_change_card)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_change_card.sizePolicy().hasHeightForWidth())
        self.btn_change_card.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_change_card.setFont(font)
        self.btn_change_card.setStyleSheet("QPushButton {\n"
                                           "background-color: rgb(225, 225, 225);\n"
                                           "border: 1px solid #343155; \n"
                                           "padding: 6px; border-radius: 10px;}\n"
                                           "\n"
                                           "QPushButton:hover, QPushButton:clicked { \n"
                                           "background-color: rgb(208, 208, 208); \n"
                                           "border: 1px solid rgb(255, 152, 1);}\n"
                                           "QPushButton:pressed {\n"
                                           "background-color: rgb(218, 127, 0);}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui/photo_data/pencil.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_change_card.setIcon(icon1)
        self.btn_change_card.setObjectName("btn_change_card")
        self.horizontalLayout_3.addWidget(self.btn_change_card)
        spacerItem4 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.btn_cancel = QtWidgets.QPushButton(Add_and_change_card)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cancel.sizePolicy().hasHeightForWidth())
        self.btn_cancel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        font.setPointSize(10)
        self.btn_cancel.setFont(font)
        self.btn_cancel.setStyleSheet("QPushButton {\n"
                                      "background-color: rgb(225, 225, 225);\n"
                                      "border: 1px solid #343155;\n"
                                      "padding: 6px; border-radius: 16px; padding-right: 10px}\n"
                                      "\n"
                                      "QPushButton:hover, QPushButton:clicked { \n"
                                      "background-color: rgb(208, 208, 208); \n"
                                      "border: 1px solid rgb(225, 78, 78);}\n"
                                      "QPushButton:pressed {\n"
                                      "background-color:rgb(211, 79, 79);}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ui/photo_data/cross.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cancel.setIcon(icon2)
        self.btn_cancel.setAutoDefault(False)
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout_3.addWidget(self.btn_cancel)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        spacerItem5 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_6.addItem(spacerItem5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem6 = QtWidgets.QSpacerItem(155, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        spacerItem7 = QtWidgets.QSpacerItem(22, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.label = QtWidgets.QLabel(Add_and_change_card)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setItalic(True)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem8 = QtWidgets.QSpacerItem(184, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        spacerItem9 = QtWidgets.QSpacerItem(334, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem10)
        self.label_2 = QtWidgets.QLabel(Add_and_change_card)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setItalic(True)
        font.setUnderline(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem11 = QtWidgets.QSpacerItem(169, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem11)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stackedWidget_front = QtWidgets.QStackedWidget(Add_and_change_card)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget_front.sizePolicy().hasHeightForWidth())
        self.stackedWidget_front.setSizePolicy(sizePolicy)
        self.stackedWidget_front.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stackedWidget_front.setObjectName("stackedWidget_front")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textEdit_front = QtWidgets.QTextEdit(self.page_2)
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        font.setPointSize(11)
        self.textEdit_front.setFont(font)
        self.textEdit_front.setStyleSheet("QTextEdit{border:0px;}")
        self.textEdit_front.setObjectName("textEdit_front")
        self.verticalLayout_2.addWidget(self.textEdit_front)
        self.stackedWidget_front.addWidget(self.page_2)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_photo_front = QtWidgets.QLabel(self.page)
        self.label_photo_front.setText("")
        self.label_photo_front.setScaledContents(True)
        self.label_photo_front.setObjectName("label_photo_front")
        self.verticalLayout.addWidget(self.label_photo_front)
        self.stackedWidget_front.addWidget(self.page)
        self.horizontalLayout.addWidget(self.stackedWidget_front)
        spacerItem12 = QtWidgets.QSpacerItem(139, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem12)
        self.stackedWidget_back = QtWidgets.QStackedWidget(Add_and_change_card)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget_back.sizePolicy().hasHeightForWidth())
        self.stackedWidget_back.setSizePolicy(sizePolicy)
        self.stackedWidget_back.setObjectName("stackedWidget_back")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.textEdit_back = QtWidgets.QTextEdit(self.page_3)
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        font.setPointSize(11)
        self.textEdit_back.setFont(font)
        self.textEdit_back.setStyleSheet("QTextEdit{border:0px;}")
        self.textEdit_back.setObjectName("textEdit_back")
        self.verticalLayout_4.addWidget(self.textEdit_back)
        self.stackedWidget_back.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_photo_back = QtWidgets.QLabel(self.page_4)
        self.label_photo_back.setText("")
        self.label_photo_back.setObjectName("label_photo_back")
        self.verticalLayout_3.addWidget(self.label_photo_back)
        self.stackedWidget_back.addWidget(self.page_4)
        self.horizontalLayout.addWidget(self.stackedWidget_back)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem13)
        self.btn_add_photo_front = QtWidgets.QPushButton(Add_and_change_card)
        self.btn_add_photo_front.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_add_photo_front.sizePolicy().hasHeightForWidth())
        self.btn_add_photo_front.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        font.setPointSize(10)
        self.btn_add_photo_front.setFont(font)
        self.btn_add_photo_front.setStyleSheet("QPushButton {\n"
                                               "background-color: rgb(225, 225, 225);\n"
                                               "border: 1px solid #343155;\n"
                                               "padding: 6px; border-radius: 15px;}\n"
                                               "\n"
                                               "QPushButton:hover, QPushButton:clicked { \n"
                                               "background-color: rgb(208, 208, 208); \n"
                                               "border: 1px solid rgb(171, 226, 81);}\n"
                                               "QPushButton:pressed {\n"
                                               "background-color:rgb(85, 255, 127) ;}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("ui/photo_data/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_add_photo_front.setIcon(icon3)
        self.btn_add_photo_front.setAutoDefault(False)
        self.btn_add_photo_front.setObjectName("btn_add_photo_front")
        self.horizontalLayout_4.addWidget(self.btn_add_photo_front)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem14)
        self.lineEdit_card_name = QtWidgets.QLineEdit(Add_and_change_card)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_card_name.sizePolicy().hasHeightForWidth())
        self.lineEdit_card_name.setSizePolicy(sizePolicy)
        self.lineEdit_card_name.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        font.setPointSize(11)
        self.lineEdit_card_name.setFont(font)
        self.lineEdit_card_name.setStyleSheet("QLineEdit{\n"
                                              "    border: 2px solid rgb(240, 240, 240);\n"
                                              "    border-radius: 10px;\n"
                                              "    padding-left: 10px;\n"
                                              "    padding-right: 10px;\n"
                                              "    }\n"
                                              "\n"
                                              "QLineEdit:hover{\n"
                                              "    border: 2px solid rgb(211, 211, 211)\n"
                                              "    }\n"
                                              "QLineEdit:focus{\n"
                                              "    border: 2px solid rgb(85, 170, 255);\n"
                                              "    }")
        self.lineEdit_card_name.setReadOnly(True)
        self.lineEdit_card_name.setObjectName("lineEdit_card_name")
        self.horizontalLayout_4.addWidget(self.lineEdit_card_name)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem15)
        self.btn_add_photo_back = QtWidgets.QPushButton(Add_and_change_card)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_add_photo_back.sizePolicy().hasHeightForWidth())
        self.btn_add_photo_back.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        font.setPointSize(10)
        self.btn_add_photo_back.setFont(font)
        self.btn_add_photo_back.setStyleSheet("QPushButton {\n"
                                              "background-color: rgb(225, 225, 225);\n"
                                              "border: 1px solid #343155;\n"
                                              "padding: 6px; border-radius: 15px;}\n"
                                              "\n"
                                              "QPushButton:hover, QPushButton:clicked { \n"
                                              "background-color: rgb(208, 208, 208); \n"
                                              "border: 1px solid rgb(171, 226, 81);}\n"
                                              "QPushButton:pressed {\n"
                                              "background-color:rgb(85, 255, 127) ;}")
        self.btn_add_photo_back.setIcon(icon3)
        self.btn_add_photo_back.setAutoDefault(False)
        self.btn_add_photo_back.setObjectName("btn_add_photo_back")
        self.horizontalLayout_4.addWidget(self.btn_add_photo_back)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem16)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.label_error = QtWidgets.QLabel(Add_and_change_card)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_error.setFont(font)
        self.label_error.setAlignment(QtCore.Qt.AlignCenter)
        self.label_error.setObjectName("label_error")
        self.verticalLayout_5.addWidget(self.label_error)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem17)
        self.btn_event_card = QtWidgets.QPushButton(Add_and_change_card)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_event_card.sizePolicy().hasHeightForWidth())
        self.btn_event_card.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        font.setPointSize(10)
        self.btn_event_card.setFont(font)
        self.btn_event_card.setStyleSheet("QPushButton {\n"
                                          "background-color: rgb(225, 225, 225);\n"
                                          "border: 1px solid #343155;\n"
                                          "padding: 6px; border-radius: 10px;}\n"
                                          "\n"
                                          "QPushButton:hover, QPushButton:clicked { \n"
                                          "background-color: rgb(208, 208, 208); \n"
                                          "border: 1px solid rgb(171, 226, 81);}\n"
                                          "QPushButton:pressed {\n"
                                          "background-color:rgb(153, 218, 51) ;}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("ui/photo_data/check_mark.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_event_card.setIcon(icon4)
        self.btn_event_card.setAutoDefault(False)
        self.btn_event_card.setObjectName("btn_event_card")
        self.horizontalLayout_5.addWidget(self.btn_event_card)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem18)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.gridLayout.addLayout(self.verticalLayout_6, 0, 0, 1, 1)

        self.retranslateUi(Add_and_change_card)
        self.stackedWidget_front.setCurrentIndex(0)
        self.stackedWidget_back.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Add_and_change_card)

    def retranslateUi(self, Add_and_change_card):
        _translate = QtCore.QCoreApplication.translate
        Add_and_change_card.setWindowTitle(_translate("Add_and_change_card", "Добавление карты"))
        self.comboBox.setToolTip(_translate("Add_and_change_card", "Типы карточек"))
        self.comboBox.setItemText(0, _translate("Add_and_change_card", "Текст -> Текст"))
        self.comboBox.setItemText(1, _translate("Add_and_change_card", "Текст -> Картинка"))
        self.comboBox.setItemText(2, _translate("Add_and_change_card", "Картинка -> Текст"))
        self.comboBox.setItemText(3, _translate("Add_and_change_card", "Картинка -> Картинка"))
        self.btn_change_card.setToolTip(_translate("Add_and_change_card", "Начать процесс редактирования карты"))
        self.btn_change_card.setText(_translate("Add_and_change_card", "Изменить карту"))
        self.btn_cancel.setToolTip(_translate("Add_and_change_card", "Выйти в меню"))
        self.btn_cancel.setText(_translate("Add_and_change_card", "Отмена"))
        self.label.setText(_translate("Add_and_change_card", "Лицевая сторона"))
        self.label_2.setText(_translate("Add_and_change_card", "Задняя сторона"))
        self.textEdit_front.setHtml(_translate("Add_and_change_card",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'Open Sans Light\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                               "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p></body></html>"))
        self.textEdit_back.setHtml(_translate("Add_and_change_card",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'Open Sans Light\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.btn_add_photo_front.setToolTip(_translate("Add_and_change_card", "Картинка на лицевую сторону"))
        self.btn_add_photo_front.setText(_translate("Add_and_change_card", "Добавить картинку"))
        self.lineEdit_card_name.setToolTip(_translate("Add_and_change_card", "Название карты"))
        self.lineEdit_card_name.setPlaceholderText(_translate("Add_and_change_card", "Название карты"))
        self.btn_add_photo_back.setToolTip(_translate("Add_and_change_card", "Картинка на заднюю сторону"))
        self.btn_add_photo_back.setText(_translate("Add_and_change_card", "Добавить картинку"))
        self.label_error.setText(_translate("Add_and_change_card", "ОШИБКА"))
        self.btn_event_card.setToolTip(_translate("Add_and_change_card", "Изменить карту в коллекции"))
        self.btn_event_card.setText(_translate("Add_and_change_card", "Добавить карту"))


class Ui_Card_amount(object):
    def setupUi(self, Card_amount):
        Card_amount.setObjectName("Card_amount")
        Card_amount.resize(600, 66)
        Card_amount.setMinimumSize(QtCore.QSize(580, 50))
        Card_amount.setMaximumSize(QtCore.QSize(600, 78))
        font = QtGui.QFont()
        font.setPointSize(8)
        Card_amount.setFont(font)
        Card_amount.setFocusPolicy(QtCore.Qt.StrongFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/photo_data/question_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Card_amount.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Card_amount)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Card_amount)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.spinBox_cards = QtWidgets.QSpinBox(Card_amount)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_cards.sizePolicy().hasHeightForWidth())
        self.spinBox_cards.setSizePolicy(sizePolicy)
        self.spinBox_cards.setMouseTracking(False)
        self.spinBox_cards.setWhatsThis("")
        self.spinBox_cards.setAccessibleName("")
        self.spinBox_cards.setStyleSheet("selection-color: rgb(0, 0, 0);\n"
                                         "selection-background-color: rgb(255, 255, 255);")
        self.spinBox_cards.setWrapping(False)
        self.spinBox_cards.setFrame(False)
        self.spinBox_cards.setAccelerated(True)
        self.spinBox_cards.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.spinBox_cards.setKeyboardTracking(True)
        self.spinBox_cards.setSuffix("")
        self.spinBox_cards.setPrefix("")
        self.spinBox_cards.setMinimum(1)
        self.spinBox_cards.setMaximum(100)
        self.spinBox_cards.setObjectName("spinBox_cards")
        self.horizontalLayout.addWidget(self.spinBox_cards)
        self.btn_continue = QtWidgets.QPushButton(Card_amount)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_continue.sizePolicy().hasHeightForWidth())
        self.btn_continue.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.btn_continue.setFont(font)
        self.btn_continue.setStyleSheet("QPushButton {\n"
                                        "background-color: rgb(225, 225, 225);\n"
                                        "border: 1px solid #343155;\n"
                                        "padding: 6px; border-radius: 12px;}\n"
                                        "\n"
                                        "QPushButton:hover, QPushButton:clicked { \n"
                                        "background-color: rgb(208, 208, 208); \n"
                                        "border: 1px solid rgb(26, 71, 24);}\n"
                                        "QPushButton:pressed {\n"
                                        "background-color: rgb(60, 166, 57);}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui/photo_data/next_strelka.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_continue.setIcon(icon1)
        self.btn_continue.setAutoDefault(False)
        self.btn_continue.setObjectName("btn_continue")
        self.horizontalLayout.addWidget(self.btn_continue)
        self.btn_cancel = QtWidgets.QPushButton(Card_amount)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cancel.sizePolicy().hasHeightForWidth())
        self.btn_cancel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.btn_cancel.setFont(font)
        self.btn_cancel.setStyleSheet("QPushButton {\n"
                                      "background-color: rgb(225, 225, 225);\n"
                                      "border: 1px solid #343155;\n"
                                      "padding: 6px; border-radius: 12px;}\n"
                                      "\n"
                                      "QPushButton:hover, QPushButton:clicked { \n"
                                      "background-color: rgb(208, 208, 208); \n"
                                      "border: 1px solid rgb(225, 78, 78);}\n"
                                      "QPushButton:pressed {\n"
                                      "background-color:rgb(211, 79, 79);}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ui/photo_data/cross.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cancel.setIcon(icon2)
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout.addWidget(self.btn_cancel)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.retranslateUi(Card_amount)
        QtCore.QMetaObject.connectSlotsByName(Card_amount)

    def retranslateUi(self, Card_amount):
        _translate = QtCore.QCoreApplication.translate
        Card_amount.setWindowTitle(_translate("Card_amount", "Количество карточек"))
        self.label.setText(_translate("Card_amount", "Количество карточек на игру:"))
        self.btn_continue.setToolTip(_translate("Card_amount", "Начать игру"))
        self.btn_continue.setText(_translate("Card_amount", "Продолжить"))
        self.btn_cancel.setToolTip(_translate("Card_amount", "Выйти к коллекциям с картами"))
        self.btn_cancel.setText(_translate("Card_amount", "Отмена"))

    def keyPressEvent(self, event):
        if event.key() == 16777220:
            self.btn_continue.click()
        elif event.key() == Qt.Key_Escape:
            self.btn_cancel.click()


class Ui_Card_game(object):
    def setupUi(self, Card_game):
        Card_game.setObjectName("Card_game")
        Card_game.resize(970, 520)
        Card_game.setMinimumSize(QtCore.QSize(970, 520))
        Card_game.setMaximumSize(QtCore.QSize(16777215, 16777215))
        Card_game.setFocusPolicy(QtCore.Qt.StrongFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/photo_data/window_icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Card_game.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Card_game)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(6, 5, 6, -1)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(7)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_rate = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_rate.setFont(font)
        self.label_rate.setStyleSheet("color: blue;")
        self.label_rate.setObjectName("label_rate")
        self.horizontalLayout.addWidget(self.label_rate)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_back_to_menu = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_back_to_menu.sizePolicy().hasHeightForWidth())
        self.btn_back_to_menu.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_back_to_menu.setFont(font)
        self.btn_back_to_menu.setStyleSheet("QPushButton {\n"
                                            "background-color: rgb(225, 225, 225);\n"
                                            "border: 1px solid #343155;\n"
                                            "padding: 6px; border-radius: 10px;}\n"
                                            "\n"
                                            "QPushButton:hover, QPushButton:clicked { \n"
                                            "background-color: rgb(208, 208, 208); \n"
                                            "border: 1px solid rgb(81, 81, 81);}\n"
                                            "QPushButton:pressed {\n"
                                            "background-color: rgb(154, 154, 154);}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui/photo_data/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_back_to_menu.setIcon(icon1)
        self.btn_back_to_menu.setFlat(False)
        self.btn_back_to_menu.setObjectName("btn_back_to_menu")
        self.horizontalLayout.addWidget(self.btn_back_to_menu)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_card_number = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_card_number.setFont(font)
        self.label_card_number.setAlignment(QtCore.Qt.AlignCenter)
        self.label_card_number.setObjectName("label_card_number")
        self.horizontalLayout_2.addWidget(self.label_card_number)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.stackedWidget_front = QtWidgets.QStackedWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget_front.sizePolicy().hasHeightForWidth())
        self.stackedWidget_front.setSizePolicy(sizePolicy)
        self.stackedWidget_front.setObjectName("stackedWidget_front")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout.setObjectName("verticalLayout")
        self.card_text_front = QtWidgets.QTextBrowser(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.card_text_front.sizePolicy().hasHeightForWidth())
        self.card_text_front.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        self.card_text_front.setFont(font)
        self.card_text_front.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.card_text_front.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.card_text_front.setObjectName("card_text_front")
        self.verticalLayout.addWidget(self.card_text_front)
        self.stackedWidget_front.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_front_photo = QtWidgets.QLabel(self.page_2)
        self.label_front_photo.setText("")
        self.label_front_photo.setObjectName("label_front_photo")
        self.verticalLayout_2.addWidget(self.label_front_photo)
        self.stackedWidget_front.addWidget(self.page_2)
        self.horizontalLayout_3.addWidget(self.stackedWidget_front)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.btn_remember = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_remember.sizePolicy().hasHeightForWidth())
        self.btn_remember.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.btn_remember.setFont(font)
        self.btn_remember.setStyleSheet("QPushButton {\n"
                                        "background-color: rgb(225, 225, 225);\n"
                                        "border: 1px solid #343155;\n"
                                        "padding: 6px; border-radius: 10px;}\n"
                                        "\n"
                                        "QPushButton:hover, QPushButton:clicked { \n"
                                        "background-color: rgb(208, 208, 208); \n"
                                        "border: 1px solid rgb(171, 226, 81);}\n"
                                        "QPushButton:pressed {\n"
                                        "background-color:rgb(85, 255, 127) ;}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ui/photo_data/ik.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_remember.setIcon(icon2)
        self.btn_remember.setIconSize(QtCore.QSize(25, 25))
        self.btn_remember.setObjectName("btn_remember")
        self.verticalLayout_5.addWidget(self.btn_remember)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.btn_open_card = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_open_card.sizePolicy().hasHeightForWidth())
        self.btn_open_card.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.btn_open_card.setFont(font)
        self.btn_open_card.setStyleSheet("QPushButton {\n"
                                         "background-color: rgb(225, 225, 225);\n"
                                         "border: 1px solid #343155;\n"
                                         "padding: 6px; border-radius: 10px;}\n"
                                         "\n"
                                         "QPushButton:hover, QPushButton:clicked { \n"
                                         "background-color: rgb(208, 208, 208); \n"
                                         "border: 1px solid rgb(229, 170, 23);}\n"
                                         "QPushButton:pressed {\n"
                                         "background-color:  rgb(229, 170, 23);}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("ui/photo_data/open_card_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_open_card.setIcon(icon3)
        self.btn_open_card.setFlat(False)
        self.btn_open_card.setObjectName("btn_open_card")
        self.verticalLayout_5.addWidget(self.btn_open_card)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem4)
        self.btn_forgot = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_forgot.sizePolicy().hasHeightForWidth())
        self.btn_forgot.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.btn_forgot.setFont(font)
        self.btn_forgot.setStyleSheet("QPushButton {\n"
                                      "background-color: rgb(225, 225, 225);\n"
                                      "border: 1px solid #343155;\n"
                                      "padding: 6px; border-radius: 10px;}\n"
                                      "\n"
                                      "QPushButton:hover, QPushButton:clicked { \n"
                                      "background-color: rgb(208, 208, 208); \n"
                                      "border: 1px solid rgb(225, 78, 78);}\n"
                                      "QPushButton:pressed {\n"
                                      "background-color:rgb(211, 79, 79);}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("ui/photo_data/idk.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_forgot.setIcon(icon4)
        self.btn_forgot.setIconSize(QtCore.QSize(25, 25))
        self.btn_forgot.setObjectName("btn_forgot")
        self.verticalLayout_5.addWidget(self.btn_forgot)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.stackedWidget_back = QtWidgets.QStackedWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget_back.sizePolicy().hasHeightForWidth())
        self.stackedWidget_back.setSizePolicy(sizePolicy)
        self.stackedWidget_back.setObjectName("stackedWidget_back")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.card_text_back = QtWidgets.QTextBrowser(self.page_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.card_text_back.sizePolicy().hasHeightForWidth())
        self.card_text_back.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        self.card_text_back.setFont(font)
        self.card_text_back.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.card_text_back.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.card_text_back.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.card_text_back.setObjectName("card_text_back")
        self.verticalLayout_3.addWidget(self.card_text_back)
        self.stackedWidget_back.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_back_photo = QtWidgets.QLabel(self.page_4)
        self.label_back_photo.setText("")
        self.label_back_photo.setScaledContents(False)
        self.label_back_photo.setObjectName("label_back_photo")
        self.verticalLayout_4.addWidget(self.label_back_photo)
        self.stackedWidget_back.addWidget(self.page_4)
        self.horizontalLayout_3.addWidget(self.stackedWidget_back)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout_6, 0, 0, 1, 1)
        Card_game.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Card_game)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 970, 21))
        self.menubar.setObjectName("menubar")
        Card_game.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Card_game)
        self.statusbar.setObjectName("statusbar")
        Card_game.setStatusBar(self.statusbar)

        self.retranslateUi(Card_game)
        self.stackedWidget_front.setCurrentIndex(0)
        self.stackedWidget_back.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Card_game)

    def retranslateUi(self, Card_game):
        _translate = QtCore.QCoreApplication.translate
        Card_game.setWindowTitle(_translate("Card_game", "Игра"))
        self.label_rate.setText(_translate("Card_game", "Описание рейтинга карты"))
        self.btn_back_to_menu.setText(_translate("Card_game", " Выйти в меню"))
        self.label_card_number.setText(_translate("Card_game", "Номер карты"))
        self.card_text_front.setHtml(_translate("Card_game",
                                                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "</style></head><body style=\" font-family:\'Open Sans Light\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Вавыаы</span></p></body></html>"))
        self.btn_remember.setText(_translate("Card_game", "Помню"))
        self.btn_open_card.setText(_translate("Card_game", " Открыть"))
        self.btn_forgot.setText(_translate("Card_game", "Не помню"))
        self.card_text_back.setHtml(_translate("Card_game",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'Open Sans Light\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Вавыаы</span></p></body></html>"))

    def keyPressEvent(self, event):
        if event.key() == 16777220 or event.key() == Qt.Key_Space:
            self.btn_open_card.click()
        elif event.key() == Qt.Key_Escape:
            self.btn_back_to_menu.click()


class Ui_Delete_window(object):
    def setupUi(self, Delete_window):
        Delete_window.setObjectName("Delete_window")
        Delete_window.resize(370, 120)
        Delete_window.setMinimumSize(QtCore.QSize(370, 120))
        Delete_window.setMaximumSize(QtCore.QSize(370, 120))
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        font.setPointSize(9)
        Delete_window.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/photo_data/trash_can.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Delete_window.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Delete_window)
        self.gridLayout.setContentsMargins(5, 1, 5, 5)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser_delete = QtWidgets.QTextBrowser(Delete_window)
        self.textBrowser_delete.setMaximumSize(QtCore.QSize(16777215, 92))
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        font.setPointSize(10)
        self.textBrowser_delete.setFont(font)
        self.textBrowser_delete.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.textBrowser_delete.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_delete.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_delete.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_delete.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.textBrowser_delete.setObjectName("textBrowser_delete")
        self.verticalLayout.addWidget(self.textBrowser_delete)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_delete = QtWidgets.QPushButton(Delete_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_delete.sizePolicy().hasHeightForWidth())
        self.btn_delete.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        font.setPointSize(10)
        self.btn_delete.setFont(font)
        self.btn_delete.setStyleSheet("QPushButton {\n"
                                      "background-color: rgb(225, 225, 225);\n"
                                      "border: 1px solid #343155;\n"
                                      "padding: 6px; border-radius: 10px;}\n"
                                      "\n"
                                      "QPushButton:hover, QPushButton:clicked { \n"
                                      "background-color: rgb(208, 208, 208); \n"
                                      "border: 1px solid rgb(106, 106, 106);}\n"
                                      "QPushButton:pressed {\n"
                                      "background-color: rgb(84, 84, 84) ;}")
        self.btn_delete.setIcon(icon)
        self.btn_delete.setAutoDefault(False)
        self.btn_delete.setObjectName("btn_delete")
        self.horizontalLayout.addWidget(self.btn_delete)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_cancel = QtWidgets.QPushButton(Delete_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cancel.sizePolicy().hasHeightForWidth())
        self.btn_cancel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        font.setPointSize(10)
        self.btn_cancel.setFont(font)
        self.btn_cancel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_cancel.setStyleSheet("QPushButton {\n"
                                      "background-color: rgb(225, 225, 225);\n"
                                      "border: 1px solid #343155;\n"
                                      "padding: 6px; border-radius: 10px;}\n"
                                      "\n"
                                      "QPushButton:hover, QPushButton:clicked { \n"
                                      "background-color: rgb(208, 208, 208); \n"
                                      "border: 1px solid rgb(225, 78, 78);}\n"
                                      "QPushButton:pressed {\n"
                                      "background-color:rgb(211, 79, 79);}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui/photo_data/cross.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cancel.setIcon(icon1)
        self.btn_cancel.setAutoDefault(False)
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout.addWidget(self.btn_cancel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Delete_window)
        QtCore.QMetaObject.connectSlotsByName(Delete_window)

    def retranslateUi(self, Delete_window):
        _translate = QtCore.QCoreApplication.translate
        Delete_window.setWindowTitle(_translate("Delete_window", "Удалить коллекцию"))
        self.textBrowser_delete.setHtml(_translate("Delete_window",
                                                   "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                   "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                   "p, li { white-space: pre-wrap; }\n"
                                                   "</style></head><body style=\" font-family:\'Open Sans Light\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                                   "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Удалить карту </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-weight:600;\">&quot;КРУТАЯ КАРТА ОМЕР 23141&quot;</span><span style=\" font-family:\'MS Shell Dlg 2\';\"> из коллекции </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-weight:600;\">&quot;2131&quot;</span><span style=\" font-family:\'MS Shell Dlg 2\';\">?</span></p></body></html>"))
        self.btn_delete.setText(_translate("Delete_window", "Удалить"))
        self.btn_cancel.setText(_translate("Delete_window", "Отмена"))

    def keyPressEvent(self, event):
        if event.key() == 16777220 or event.key() == Qt.Key_Space:
            self.btn_delete.click()
        elif event.key() == Qt.Key_Escape:
            self.btn_cancel.click()


# "    image: url(ui/photo_data/down_arrow_list.png);\n"
class Ui_EndGame(object):
    def setupUi(self, EndGame):
        EndGame.setObjectName("EndGame")
        EndGame.resize(388, 160)
        EndGame.setMinimumSize(QtCore.QSize(362, 160))
        EndGame.setMaximumSize(QtCore.QSize(388, 198))
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        EndGame.setFont(font)
        EndGame.setFocusPolicy(QtCore.Qt.StrongFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/photo_data/end_game_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        EndGame.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(EndGame)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(4, 0, 4, 4)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser_card_kol = QtWidgets.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.textBrowser_card_kol.setFont(font)
        self.textBrowser_card_kol.setStyleSheet("background-color: rgb(240, 240, 240);\n"
                                                "gridline-color: rgb(255, 255, 255);")
        self.textBrowser_card_kol.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_card_kol.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_card_kol.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_card_kol.setObjectName("textBrowser_card_kol")
        self.gridLayout.addWidget(self.textBrowser_card_kol, 0, 0, 1, 1)
        self.textBrowser_rating = QtWidgets.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        font.setPointSize(8)
        self.textBrowser_rating.setFont(font)
        self.textBrowser_rating.setStyleSheet("background-color: rgb(240, 240, 240);\n"
                                              "gridline-color: rgb(255, 255, 255);")
        self.textBrowser_rating.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_rating.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_rating.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_rating.setObjectName("textBrowser_rating")
        self.gridLayout.addWidget(self.textBrowser_rating, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_restart_game = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        font.setPointSize(9)
        self.btn_restart_game.setFont(font)
        self.btn_restart_game.setStyleSheet("QPushButton {\n"
                                            "background-color:#0d6efd;\n"
                                            "border: 1px solid #343155; color: #FFF;\n"
                                            "padding: 6px; border-radius: 12px;}\n"
                                            "\n"
                                            "QPushButton:hover, QPushButton:clicked { \n"
                                            "background-color: #0b5ed7; \n"
                                            "border: 1px solid #9ac3fe;}\n"
                                            "QPushButton:pressed {\n"
                                            "background-color:rgb(10, 87, 194) ;}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui/photo_data/repeat_image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_restart_game.setIcon(icon1)
        self.btn_restart_game.setObjectName("btn_restart_game")
        self.horizontalLayout.addWidget(self.btn_restart_game)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_back_to_menu = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        font.setPointSize(9)
        self.btn_back_to_menu.setFont(font)
        self.btn_back_to_menu.setStyleSheet("QPushButton {\n"
                                            "background-color: #0d6efd;\n"
                                            "border: 1px solid #343155; color: #fff;\n"
                                            "padding: 6px; border-radius: 12px;}\n"
                                            "\n"
                                            "QPushButton:hover, QPushButton:clicked { \n"
                                            "background-color: #0b5ed7; \n"
                                            "border: 1px solid #9ac3fe;}\n"
                                            "QPushButton:pressed {\n"
                                            "background-color:rgb(10, 87, 194) ;}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ui/photo_data/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_back_to_menu.setIcon(icon2)
        self.btn_back_to_menu.setFlat(False)
        self.btn_back_to_menu.setObjectName("btn_back_to_menu")
        self.horizontalLayout.addWidget(self.btn_back_to_menu)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        EndGame.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EndGame)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 388, 23))
        self.menubar.setObjectName("menubar")
        EndGame.setMenuBar(self.menubar)

        self.retranslateUi(EndGame)
        QtCore.QMetaObject.connectSlotsByName(EndGame)

    def retranslateUi(self, EndGame):
        _translate = QtCore.QCoreApplication.translate
        EndGame.setWindowTitle(_translate("EndGame", "Конец игры"))
        self.textBrowser_card_kol.setHtml(_translate("EndGame",
                                                     "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                     "p, li { white-space: pre-wrap; }\n"
                                                     "</style></head><body style=\" font-family:\'Algerian\',\'Open Sans Light\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
                                                     "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:9pt;\">Количество правильных ответов: {n}</span></p>\n"
                                                     "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt;\">Всего карт было: {m}</span></p></body></html>"))
        self.textBrowser_rating.setHtml(_translate("EndGame",
                                                   "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                   "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                   "p, li { white-space: pre-wrap; }\n"
                                                   "</style></head><body style=\" font-family:\'Open Sans Light\',\'Open Sans Light\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
                                                   "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">У вас есть потенциал для улучшения. Продолжайте стараться, и ваши навыки улучшатся с каждой попыткой.</span></p></body></html>"))
        self.btn_restart_game.setText(_translate("EndGame", " Начать игру заново"))
        self.btn_back_to_menu.setText(_translate("EndGame", " Выйти к коллекциям"))


class Ui_Rename_collection(object):
    def setupUi(self, Rename_collection):
        Rename_collection.setObjectName("Rename_collection")
        Rename_collection.resize(551, 169)
        Rename_collection.setMinimumSize(QtCore.QSize(551, 169))
        Rename_collection.setMaximumSize(QtCore.QSize(551, 169))
        Rename_collection.setFocusPolicy(QtCore.Qt.StrongFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/photo_data/pencil.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Rename_collection.setWindowIcon(icon)
        Rename_collection.setStyleSheet("QLineEdit{\n"
                                        "    border: 2px solid rgb(240, 240, 240);\n"
                                        "    border-radius: 10px;\n"
                                        "    padding-left: 10px;\n"
                                        "    padding-right: 10px;\n"
                                        "    }\n"
                                        "\n"
                                        "QLineEdit:hover{\n"
                                        "    border: 2px solid rgb(211, 211, 211)\n"
                                        "    }\n"
                                        "QLineEdit:focus{\n"
                                        "    border: 2px solid rgb(85, 170, 255);\n"
                                        "    }")
        self.gridLayout = QtWidgets.QGridLayout(Rename_collection)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(Rename_collection)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(Rename_collection)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_old = QtWidgets.QLineEdit(Rename_collection)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_old.sizePolicy().hasHeightForWidth())
        self.lineEdit_old.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        font.setPointSize(11)
        self.lineEdit_old.setFont(font)
        self.lineEdit_old.setReadOnly(True)
        self.lineEdit_old.setObjectName("lineEdit_old")
        self.verticalLayout.addWidget(self.lineEdit_old)
        self.lineEdit_new = QtWidgets.QLineEdit(Rename_collection)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_new.sizePolicy().hasHeightForWidth())
        self.lineEdit_new.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        font.setPointSize(11)
        self.lineEdit_new.setFont(font)
        self.lineEdit_new.setObjectName("lineEdit_new")
        self.verticalLayout.addWidget(self.lineEdit_new)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.label_error = QtWidgets.QLabel(Rename_collection)
        self.label_error.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_error.setFont(font)
        self.label_error.setAlignment(QtCore.Qt.AlignCenter)
        self.label_error.setObjectName("label_error")
        self.verticalLayout_3.addWidget(self.label_error)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_rename_collection = QtWidgets.QPushButton(Rename_collection)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_rename_collection.sizePolicy().hasHeightForWidth())
        self.btn_rename_collection.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        font.setPointSize(10)
        self.btn_rename_collection.setFont(font)
        self.btn_rename_collection.setStyleSheet("QPushButton {\n"
                                                 "background-color: rgb(225, 225, 225);\n"
                                                 "border: 1px solid #343155;\n"
                                                 "padding: 6px; border-radius: 10px;}\n"
                                                 "\n"
                                                 "QPushButton:hover, QPushButton:clicked { \n"
                                                 "background-color: rgb(208, 208, 208); \n"
                                                 "border: 1px solid rgb(171, 226, 81);}\n"
                                                 "QPushButton:pressed {\n"
                                                 "background-color:rgb(153, 218, 51) ;}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui/photo_data/check_mark.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_rename_collection.setIcon(icon1)
        self.btn_rename_collection.setAutoDefault(False)
        self.btn_rename_collection.setObjectName("btn_rename_collection")
        self.horizontalLayout.addWidget(self.btn_rename_collection)
        self.btn_cancel = QtWidgets.QPushButton(Rename_collection)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cancel.sizePolicy().hasHeightForWidth())
        self.btn_cancel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        font.setPointSize(10)
        self.btn_cancel.setFont(font)
        self.btn_cancel.setStyleSheet("QPushButton {\n"
                                      "background-color: rgb(225, 225, 225);\n"
                                      "border: 1px solid #343155;\n"
                                      "padding: 6px; border-radius: 10px; padding-right: 10px}\n"
                                      "\n"
                                      "QPushButton:hover, QPushButton:clicked { \n"
                                      "background-color: rgb(208, 208, 208); \n"
                                      "border: 1px solid rgb(225, 78, 78);}\n"
                                      "QPushButton:pressed {\n"
                                      "background-color:rgb(211, 79, 79);}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ui/photo_data/cross.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cancel.setIcon(icon2)
        self.btn_cancel.setAutoDefault(False)
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout.addWidget(self.btn_cancel)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.retranslateUi(Rename_collection)
        QtCore.QMetaObject.connectSlotsByName(Rename_collection)

    def retranslateUi(self, Rename_collection):
        _translate = QtCore.QCoreApplication.translate
        Rename_collection.setWindowTitle(_translate("Rename_collection", "Изменить имя коллекции"))
        self.label.setText(_translate("Rename_collection", "Старое имя коллекции"))
        self.label_2.setText(_translate("Rename_collection", "Новое имя коллекции"))
        self.lineEdit_old.setText(_translate("Rename_collection", "СТАРОЕ ИМЯ"))
        self.lineEdit_new.setText(_translate("Rename_collection", "НОВОЕ ИМЯ"))
        self.label_error.setText(_translate("Rename_collection", "ОШИБКА"))
        self.btn_rename_collection.setToolTip(_translate("Rename_collection", "Добавить карту в коллекцию"))
        self.btn_rename_collection.setText(_translate("Rename_collection", "Изменить имя коллекции"))
        self.btn_cancel.setToolTip(_translate("Rename_collection", "Выйти в меню"))
        self.btn_cancel.setText(_translate("Rename_collection", "Отмена"))

    def keyPressEvent(self, event):
        if event.key() == 16777220 or event.key() == Qt.Key_Space:
            self.btn_rename_collection.click()
        elif event.key() == Qt.Key_Escape:
            self.btn_cancel.click()


class Ui_Help_menu(object):
    def setupUi(self, Help_menu):
        Help_menu.setObjectName("Help_menu")
        Help_menu.resize(900, 340)
        Help_menu.setMinimumSize(QtCore.QSize(900, 340))
        Help_menu.setMaximumSize(QtCore.QSize(900, 16777215))
        Help_menu.setFocusPolicy(QtCore.Qt.StrongFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/photo_data/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Help_menu.setWindowIcon(icon)
        Help_menu.setStyleSheet("QPushButton {\n"
                                "background-color: rgb(225, 225, 225);\n"
                                "border: 1px solid #343155;\n"
                                "padding: 6px; border-radius: 14px;}\n"
                                "\n"
                                "QPushButton:hover, QPushButton:clicked { \n"
                                "background-color: ; \n"
                                "border: 1px solid rgb(37, 183, 211);}\n"
                                "QPushButton:pressed {\n"
                                "background-color:rgb(34, 169, 193);}\n"
                                "QTextBrowser{border: 0px;}")
        self.gridLayout = QtWidgets.QGridLayout(Help_menu)
        self.gridLayout.setContentsMargins(7, 7, 7, 7)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_exit = QtWidgets.QPushButton(Help_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        font.setPointSize(11)
        self.btn_exit.setFont(font)
        self.btn_exit.setStyleSheet("QPushButton:hover, QPushButton:clicked { \n"
                                    "background-color: rgb(208, 208, 208); \n"
                                    "border: 1px solid rgb(225, 78, 78);}\n"
                                    "QPushButton:pressed {\n"
                                    "background-color:rgb(211, 79, 79);}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui/photo_data/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_exit.setIcon(icon1)
        self.btn_exit.setObjectName("btn_exit")
        self.horizontalLayout.addWidget(self.btn_exit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_about_what = QtWidgets.QLabel(Help_menu)
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_about_what.setFont(font)
        self.label_about_what.setObjectName("label_about_what")
        self.horizontalLayout.addWidget(self.label_about_what)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btn_left = QtWidgets.QPushButton(Help_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_left.sizePolicy().hasHeightForWidth())
        self.btn_left.setSizePolicy(sizePolicy)
        self.btn_left.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ui/photo_data/arrow_left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_left.setIcon(icon2)
        self.btn_left.setIconSize(QtCore.QSize(25, 25))
        self.btn_left.setObjectName("btn_left")
        self.horizontalLayout.addWidget(self.btn_left)
        self.btn_right = QtWidgets.QPushButton(Help_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_right.sizePolicy().hasHeightForWidth())
        self.btn_right.setSizePolicy(sizePolicy)
        self.btn_right.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("ui/photo_data/arrow_right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_right.setIcon(icon3)
        self.btn_right.setIconSize(QtCore.QSize(25, 25))
        self.btn_right.setObjectName("btn_right")
        self.horizontalLayout.addWidget(self.btn_right)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.stackedWidget_help = QtWidgets.QStackedWidget(Help_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget_help.sizePolicy().hasHeightForWidth())
        self.stackedWidget_help.setSizePolicy(sizePolicy)
        self.stackedWidget_help.setObjectName("stackedWidget_help")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 41))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("ui/photo_data/first_help_page.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.page)
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout_2.addWidget(self.textBrowser)
        spacerItem2 = QtWidgets.QSpacerItem(444, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.page)
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.horizontalLayout_2.addWidget(self.textBrowser_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.stackedWidget_help.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_3.setContentsMargins(0, -1, 0, -1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(0, 43))
        self.label_4.setMaximumSize(QtCore.QSize(496, 16777215))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("ui/photo_data/second_help_page_1.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.page_2)
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        self.textBrowser_3.setFont(font)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.verticalLayout_3.addWidget(self.textBrowser_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(0, 43))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("ui/photo_data/second_help_page_2.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_5.sizePolicy().hasHeightForWidth())
        self.textBrowser_5.setSizePolicy(sizePolicy)
        self.textBrowser_5.setMaximumSize(QtCore.QSize(137, 16777215))
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        self.textBrowser_5.setFont(font)
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.horizontalLayout_3.addWidget(self.textBrowser_5)
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_6.sizePolicy().hasHeightForWidth())
        self.textBrowser_6.setSizePolicy(sizePolicy)
        self.textBrowser_6.setMaximumSize(QtCore.QSize(137, 16777215))
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        self.textBrowser_6.setFont(font)
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.horizontalLayout_3.addWidget(self.textBrowser_6)
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_7.sizePolicy().hasHeightForWidth())
        self.textBrowser_7.setSizePolicy(sizePolicy)
        self.textBrowser_7.setMaximumSize(QtCore.QSize(137, 16777215))
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        self.textBrowser_7.setFont(font)
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.horizontalLayout_3.addWidget(self.textBrowser_7)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.stackedWidget_help.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.page_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(0, 43))
        self.label_6.setMaximumSize(QtCore.QSize(524, 16777215))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("ui/photo_data/third_help_page_1.jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.label_6)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem3)
        self.horizontalLayout_6.addLayout(self.verticalLayout_6)
        spacerItem4 = QtWidgets.QSpacerItem(587, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.page_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QtCore.QSize(0, 43))
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("ui/photo_data/third_help_page_2.jpg"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.page_3)
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        self.textBrowser_4.setFont(font)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.horizontalLayout_5.addWidget(self.textBrowser_4)
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.page_3)
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        self.textBrowser_8.setFont(font)
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.horizontalLayout_5.addWidget(self.textBrowser_8)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        self.gridLayout_4.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
        self.stackedWidget_help.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.page_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QtCore.QSize(0, 43))
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("ui/photo_data/fourth_help_page.jpg"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_7.addWidget(self.label_8)
        self.textBrowser_9 = QtWidgets.QTextBrowser(self.page_4)
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        self.textBrowser_9.setFont(font)
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.verticalLayout_7.addWidget(self.textBrowser_9)
        self.gridLayout_5.addLayout(self.verticalLayout_7, 0, 0, 1, 1)
        self.stackedWidget_help.addWidget(self.page_4)
        self.verticalLayout.addWidget(self.stackedWidget_help)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Help_menu)
        self.stackedWidget_help.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Help_menu)

    def retranslateUi(self, Help_menu):
        _translate = QtCore.QCoreApplication.translate
        Help_menu.setWindowTitle(_translate("Help_menu", "Меню помощи"))
        self.btn_exit.setToolTip(_translate("Help_menu", "Выйти из меню помощи"))
        self.btn_exit.setText(_translate("Help_menu", "Выйти"))
        self.label_about_what.setText(_translate("Help_menu", "По чему помощь"))
        self.btn_left.setToolTip(_translate("Help_menu", "Перелестнуть страницу влево"))
        self.btn_right.setToolTip(_translate("Help_menu", "Перелистнуть страницу вправо"))
        self.textBrowser.setHtml(_translate("Help_menu",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'Open Sans Light\'; font-size:6.6pt; font-weight:400; font-style:normal;\">\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Ваша статистика за все игры</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("Help_menu",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'Open Sans Light\'; font-size:6.6pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Имя вашего профиля</span></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("Help_menu",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'Open Sans Light\'; font-size:6.6pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Все коллекции, которые у вас есть</span></p></body></html>"))
        self.textBrowser_5.setHtml(_translate("Help_menu",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'Open Sans Light\'; font-size:6.6pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Добавить новую коллекцию</span></p></body></html>"))
        self.textBrowser_6.setHtml(_translate("Help_menu",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'Open Sans Light\'; font-size:6.6pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Удалить коллекцию, которая выбрана сейчас</span></p></body></html>"))
        self.textBrowser_7.setHtml(_translate("Help_menu",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'Open Sans Light\'; font-size:6.6pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Изменить название коллекции, которая выбрана сейчас</span></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("Help_menu",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'Open Sans Light\'; font-size:6.6pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Добавить карточку</span></p></body></html>"))
        self.textBrowser_8.setHtml(_translate("Help_menu",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'Open Sans Light\'; font-size:6.6pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Удалить выделенную карту</span></p></body></html>"))
        self.textBrowser_9.setHtml(_translate("Help_menu",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'Open Sans Light\'; font-size:6.6pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Чтобы зайти в карточку, изменить её или посмотреть что это вообще за карта, нажмите на неё дважды</span></p></body></html>"))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Left:
            self.btn_left.click()
        elif event.key() == Qt.Key_Right:
            self.btn_right.click()
        elif event.key() == Qt.Key_Escape:
            self.btn_exit.click()
