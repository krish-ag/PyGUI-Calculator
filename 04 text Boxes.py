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

        # Text Box
        textB = qtw.QTextEdit(
            lineWrapMode=qtw.QTextEdit.FixedColumnWidth,
            lineWrapColumnOrWidth=25,
            placeholderText="Hello World!",
            # html="<h1> the html </h1>"

            # plainText="The Real Text Value"
            # readOnly=True,  # default False
            # acceptRichText=True  # able to bring formatting

        )
        textB.setFont(qtg.QFont("Arial", 14))

        self.layout().addWidget(textB)

        def submit():
            lab.setText(f"Value= {textB.toPlainText()}")
            # textB.setText("")
            textB.setPlainText("")  # both are same in this case

        # Create a Button
        btn = qtw.QPushButton("Submit", clicked=submit)
        self.layout().addWidget(btn)

        self.show()


app = qtw.QApplication([])
mw = MainWindow()

sys.exit(app.exec_())
