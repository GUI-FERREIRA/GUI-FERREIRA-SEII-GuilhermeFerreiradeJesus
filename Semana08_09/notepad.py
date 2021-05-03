#!/usr/bin/python3
# notepad.py
# importing required libraries
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *
import os
import sys

class MainWindow(QMainWindow):

	# construtor
	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)

		self.setGeometry(100, 100, 600, 400)
		layout = QVBoxLayout()
		self.editor = QPlainTextEdit()

		generalfont = QFontDatabase.systemFont(QFontDatabase.GeneralFont)
		generalfont.setPointSize(12)
		self.editor.setFont(generalfont)

		self.path = None

		layout.addWidget(self.editor)

		container = QWidget()
		container.setLayout(layout)

		self.setCentralWidget(container)

		self.status = QStatusBar()
		self.setStatusBar(self.status)

		# creating a file menu
		file_menu = self.menuBar().addMenu("&File")

		open_file_action = QAction("Abrir", self)
		open_file_action.setStatusTip("Open file")
		open_file_action.triggered.connect(self.file_open)
		file_menu.addAction(open_file_action)

		save_file_action = QAction("Salvar", self)
		save_file_action.setStatusTip("Save current page")
		save_file_action.triggered.connect(self.file_save)
		file_menu.addAction(save_file_action)

		saveas_file_action = QAction("Salvar como", self)
		saveas_file_action.setStatusTip("Save current page to specified file")
		saveas_file_action.triggered.connect(self.file_saveas)
		file_menu.addAction(saveas_file_action)

		# creating a edit menu bar
		edit_menu = self.menuBar().addMenu("&Edit")

		# cut action
		cut_action = QAction("Cut", self)
		cut_action.setStatusTip("Cut selected text")
		cut_action.triggered.connect(self.editor.cut)
		edit_menu.addAction(cut_action)

		# copy action
		copy_action = QAction("Copy", self)
		copy_action.setStatusTip("Copy selected text")
		copy_action.triggered.connect(self.editor.copy)
		edit_menu.addAction(copy_action)

		# paste action
		paste_action = QAction("Paste", self)
		paste_action.setStatusTip("Paste from clipboard")
		paste_action.triggered.connect(self.editor.paste)
		edit_menu.addAction(paste_action)

		# select all action
		select_action = QAction("Select all", self)
		select_action.setStatusTip("Select all text")
		select_action.triggered.connect(self.editor.selectAll)
		edit_menu.addAction(select_action)


		# wrap action
		wrap_action = QAction("Wrap text to window", self)
		wrap_action.setStatusTip("Check to wrap text to window")
		wrap_action.setCheckable(True)
		wrap_action.setChecked(True)
		wrap_action.triggered.connect(self.edit_toggle_wrap)
		edit_menu.addAction(wrap_action)

		self.update_title()
		self.show()

	def dialog_critical(self, s):
		dlg = QMessageBox(self)
		dlg.setText(s)
		dlg.setIcon(QMessageBox.Critical)
		dlg.show()

	def file_open(self):
		path, _ = QFileDialog.getOpenFileName(self, "Open file", "",
							"Text documents (*.txt);All files (*.*)")
		if path:
			try:
				with open(path, 'rU') as f:
					text = f.read()
			except Exception as e:
				self.dialog_critical(str(e))
			else:
				self.path = path
				self.editor.setPlainText(text)
				self.update_title()

	def file_save(self):
		if self.path is None:
			return self.file_saveas()
		self._save_to_path(self.path)

	# action called by save as action
	def file_saveas(self):
		path, _ = QFileDialog.getSaveFileName(self, "Save file", "",
							"Text documents (*.txt)")
		if not path:
			return
		# else call save to path method
		self._save_to_path(path)

	# save to path method
	def _save_to_path(self, path):
		text = self.editor.toPlainText()
		try:
			with open(path, 'w') as f:
				f.write(text)
		except Exception as e:
			self.dialog_critical(str(e))
		else:
			self.path = path
			self.update_title()

	def update_title(self):
		self.setWindowTitle("%s - Bloco de notas" %(os.path.basename(self.path)
												if self.path else "Untitled"))

	def edit_toggle_wrap(self):
		self.editor.setLineWrapMode(1 if self.editor.lineWrapMode() == 0 else 0 )

if __name__ == '__main__':
	app = QApplication(sys.argv)
	app.setApplicationName("Bloco de notas")
	window = MainWindow()
	app.exec_()
