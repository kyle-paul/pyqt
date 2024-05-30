import PySide6.QtWidgets as qtw
import PySide6.QtGui as qtg

class Form(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registration Form")
        self.form = qtw.QFormLayout(self)
        label_1 = qtw.QLabel("Enter your information")
        f_name = qtw.QLineEdit(self)
        l_name = qtw.QLineEdit(self)
        button = qtw.QPushButton("Register now")
        
        self.form.addRow(label_1)
        self.form.addRow('First Name', f_name)
        self.form.addRow('Last Name', l_name)
        self.form.addRow(button)
        
        self.show()
        

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("3D simulation")
        self.resize(800, 600)
        self.layout = qtw.QVBoxLayout(self)
        
        self.text = qtw.QLabel("Welcome")
        self.text.setFont(qtg.QFont("Helvetica", 18))
        
        entry = qtw.QLineEdit()
        entry.setObjectName("name_field")
        entry.setText("Placeholder text")
        
        button = qtw.QPushButton("Click now", clicked=lambda: self.press())
        
        self.combo = qtw.QComboBox(
            self, editable=True, 
            insertPolicy=qtw.QComboBox.InsertAtTop
        )
        combo_list = ['Deep1', 'Deep2', 'Deep3']
        self.combo.addItems(combo_list)
        
        
        self.spin = qtw.QDoubleSpinBox(
            self, value=10.5, maximum=100, minimum=0, 
            singleStep=5, prefix="I want ", suffix=" epochs"   
        )
        
        self.text_box = qtw.QTextEdit(self,
            html="<h1><strong>Heading 1</strong></h1>",
            LineWrapMode=qtw.QTextEdit.FixedColumnWidth,
            LineWrapColumnOrWidth=50,
            readOnly=False, 
            acceptRichText=True
        )
                
        self.layout.addWidget(self.text)
        self.layout.addWidget(entry)
        self.layout.addWidget(button)
        self.layout.addWidget(self.combo)
        self.layout.addWidget(self.spin)
        self.layout.addWidget(self.text_box)
        
        self.show()
        
    def press(self):
        self.form = Form()
        
        
if __name__ == "__main__":
    app = qtw.QApplication([])
    window = MainWindow()
    app.exec()