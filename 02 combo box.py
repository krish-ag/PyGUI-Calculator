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

        # Combo Box
        combo = qtw.QComboBox(
            editable=True,  # defines new elements for user
            insertPolicy=qtw.QComboBox.InsertAtTop   # defines position for new elements
        )
        # Adding Items
        combo.addItem("Pep", "Pep's Data")
        combo.addItems(["Cheese", "Mushrooms"])
        combo.insertItem(1, "Inserted")  # insert item on a specific idx
        # combo.insertItems(0, ["items"])  # insert items on a specific idx

        self.layout().addWidget(combo)




        def submit():
            lab.setText(f"You Picked: {combo.currentText()}!")
            # lab.setText(f"You Picked: {combo.currentData()}!")
            # lab.setText(f"You Picked: {combo.currentIndex()}!")

        # Create a Button
        btn = qtw.QPushButton("Submit", clicked=submit)
        self.layout().addWidget(btn)

        self.show()




app = qtw.QApplication([])
mw = MainWindow()

sys.exit(app.exec_())
