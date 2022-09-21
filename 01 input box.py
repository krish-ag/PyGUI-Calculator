import sys
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class MainWindow(qtw.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Hello World!")

        # Set Vertical Layout
        self.setLayout(qtw.QVBoxLayout())

        # Label
        lab = qtw.QLabel("Whats Your Name?")
        lab.setFont(qtg.QFont("Arial", 20))
        self.layout().addWidget(lab)

        # input entry box
        entry = qtw.QLineEdit()
        entry .setObjectName("Name_field")
        # entry.setText("")  #  placeholder
        self.layout().addWidget(entry)

        def submit():
            lab.setText(f"Hello {entry.text()}!")
            entry.setText("")


        # Create a Button
        btn = qtw.QPushButton("Submit", clicked=submit)
        self.layout().addWidget(btn)

        self.show()




app = qtw.QApplication([])
mw = MainWindow()

sys.exit(app.exec_())
