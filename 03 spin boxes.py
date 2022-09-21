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

        # Spin Box
        spinB = qtw.QSpinBox(   # QDoubleSpinBox for float values
            value=10, 
            maximum=100,
            minimum=0,
            singleStep=10,
            prefix="Value: "
            # suffix="something"
        )
        spinB.setFont(qtg.QFont("Arial", 20))
        

        self.layout().addWidget(spinB)




        def submit():
            # lab.setText(f"Value= {spinB.text()}")   # with its prefix and suffix
            lab.setText(f"Value= {spinB.value()}")  # just the value

        # Create a Button
        btn = qtw.QPushButton("Submit", clicked=submit)
        self.layout().addWidget(btn)

        self.show()




app = qtw.QApplication([])
mw = MainWindow()

sys.exit(app.exec_())
