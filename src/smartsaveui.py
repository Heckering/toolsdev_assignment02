import maya.OpenMayaUI as omui
from PySide2 import QtWidgets, QtCore
from shiboken2 import wrapInstance


def maya_main_window():
    """return the maya main window widget"""
    main_window = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window), QtWidgets.QWidget)


class SmartSaveUI(QtWidgets.QDialog):
    """simple UI Class"""

    def __init__(self):
        """constructor"""
        # Passing the object smartsaveui as an argument to super()
        # makes this line python 2 and 3 compatible
        super(SmartSaveUI, self).__init__(parent=maya_main_window())
        self.setWindowTitle("Smart Save")
        self.resize(500, 200)
        self.setWindowFlags(self.windowFlags() ^
                            QtCore.Qt.WindowContextHelpButtonHint)
        self.create_witgets()
        self.create_layout()
        self.create_connections()
    
    def create_witgets(self):
        """create widgets for our ui"""
        self.title_lbl = QtWidgets.QLabel("Smart Save")
        self.title_lbl.setStyleSheet("font: bold 40px")
        self.dir_lbl = QtWidgets.QLabel("Directory")
        self.dir_le = QtWidgets.QLineEdit()
        self.brows_btn = QtWidgets.QPushButton("Browse...")
        self.descriptor_lbl = QtWidgets.QLabel("Descriptor")
        self.descriptor_le = QtWidgets.QLineEdit()
        self.version_lbl = QtWidgets.QLabel("Version")
        self.version_spinbox = QtWidgets.QSpinBox()
        self.version_spinbox.setValue(1)
        self.ext_lbl = QtWidgets.QLabel("Extension")
        self.ext_le = QtWidgets.QLineEdit("ma")
        self.save_btn = QtWidgets.QPushButton("Save")
        self.cancel_btn = QtWidgets.QPushButton("Cancel")

    def create_layout(self):
        """lay out our widgets in the ui"""
        self.directory_lay = QtWidgets.QHBoxLayout()
        self.directory_lay.addWidget(self.dir_lbl)
        self.directory_lay.addWidget(self.dir_le)
        self.directory_lay.addWidget(self.brows_btn)

        self.descriptor_lay = QtWidgets.QHBoxLayout()
        self.descriptor_lay.addWidget(self.descriptor_lbl)
        self.descriptor_lay.addWidget(self.descriptor_le)

        self.version_lay = QtWidgets.QHBoxLayout()
        self.version_lay.addWidget(self.version_lbl)
        self.version_lay.addWidget(self.version_spinbox)

        self.ext_lay = QtWidgets.QHBoxLayout()
        self.ext_lay.addWidget(self.ext_lbl)
        self.ext_lay.addWidget(self.ext_le)

        self.bottom_btn_lay = QtWidgets.QHBoxLayout()
        self.bottom_btn_lay.addWidget(self.save_btn)
        self.bottom_btn_lay.addWidget(self.cancel_btn)

        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.addWidget(self.title_lbl)
        self.main_layout.addLayout(self.directory_lay)
        self.main_layout.addLayout(self.descriptor_lay)
        self.main_layout.addLayout(self.version_lay)
        self.main_layout.addLayout(self.ext_lay)

        self.main_layout.addStretch()

        self.main_layout.addLayout(self.bottom_btn_lay)

        self.setLayout(self.main_layout)

    def create_connections(self):
        """connects our witget signals to slots"""
        self.cancel_btn.clicked.connect(self.cancel)

    @QtCore.Slot()
    def cancel(self):
        """quits the dialog"""
        self.close()