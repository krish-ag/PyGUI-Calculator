import sys
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class MainWindow(qtw.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Hello World!")

        # Set QForm Layout
        layout = qtw.QFormLayout()
        self.setLayout(layout)

        # Widgets
        lab = qtw.QLabel("Label Row")
        lab.setFont(qtg.QFont("Arial", 20))

        fName = qtw.QLineEdit()
        lName = qtw.QLineEdit()

        def submit():
            lab.setText(f"Hello {fName.text()} {lName.text()}!")
            fName.setText("")
            lName.setText("")

        # Create a Button
        btn = qtw.QPushButton("Submit", clicked=submit)

        # Add rows
        layout.addRow(lab)
        layout.addRow("F name", fName)
        layout.addRow("L name", lName)
        layout.addRow(btn)


        self.show()


app = qtw.QApplication([])
mw = MainWindow()

sys.exit(app.exec_())
