import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from ui.main_window import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
  def __init__(self, parent=None):
    super(MainWindow, self).__init__(parent=parent)
    self.setupUi(self)
    self.setFixedSize(self.size())

    self.value = 0.0
    self.multiplier = 0

    self.input.textChanged.connect(self.process_input_change)
    self.input_multiplier.currentIndexChanged.connect(self.input_multiplier_change)

  def process_input_change(self, text):
    text = "".join(c for c in text if c.isdigit() or c == ".")
    self.input.setText(text)

    if text != "":
      self.value = float(text)
    else:
      self.value = 0.0

    self.recalculate_output()

  def input_multiplier_change(self, index):
    self.multiplier = index * 3

    self.recalculate_output()

  def recalculate_output(self):
    additional_multiplier = 0
    value = self.value
    while value >= 10:
      value /= 10
      additional_multiplier += 1

    while value < 1 and value != 0:
      value *= 10
      additional_multiplier -= 1

    final_multiplier = self.multiplier + additional_multiplier
    self.output.setText(f"{self.value}" if final_multiplier == 0 or value == 0 else f"{value}e{final_multiplier}")

if __name__ == '__main__':
  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  sys.exit(app.exec())