import ctypes
import requests
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel, QPushButton, QHBoxLayout,QVBoxLayout, QWidget
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pokemon Finder")
        self.base_url = "https://pokeapi.co/api/v2/"
        self.setWindowIcon(QIcon('E:\\Nihaal 1\\PICTURES\\pokeball.jpg'))
        self.setGeometry(700,300,500,300)
        self.setFixedSize(500,300)

        self.input = QLineEdit(self)
        self.search = QPushButton("Search", self)

        self.label1 = QLabel("Name :",self)
        self.label2 = QLabel("Id :", self)
        self.label3 = QLabel("Height :", self)
        self.label4 = QLabel("Weight :", self)
        self.label5 = QLabel("Key-Abilities :", self)
        self.error_label = QLabel(self)
        self.search.clicked.connect(self.onclick)
        self.input.returnPressed.connect(self.onclick)






        self.initUI()

    def initUI(self):


        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(self.input)
        hbox.addWidget(self.search)
        hbox.addStretch()

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(self.label1)
        vbox.addWidget(self.label2)
        vbox.addWidget(self.label3)
        vbox.addWidget(self.label4)
        vbox.addWidget(self.label5)
        central_widget.setLayout(vbox)

        self.label1.setGeometry(0,0,400,40)
        self.label2.setGeometry(0,0,400,40)
        self.label3.setGeometry(0,0,400,40)
        self.label4.setGeometry(0,0,400,40)
        self.label5.setGeometry(0,0,400,40)
        self.error_label.setGeometry(200,130,100,40)

        self.setStyleSheet("""
            QPushButton{
                font-size: 40 px;
                border-radius: 5px;
                border: 1px solid black;
                background-color: #ff1100;
            }
            QPushButton:hover{
                background-color: #d1291d;
            }
            QPushButton:pressed{
                background-color: #ad4740;
            }
            
            QLineEdit{
                font-size: 40 px;
                border-radius: 5px;
                border: 1px solid black;
            }
            
            vbox{
                font-size: 40 px;
            }
            QPushButton#error_label{
                font-size: 40 px;
            }
        """)
    def onclick(self):
        self.name_in_class = self.input.text()
        url = f"{self.base_url}/pokemon/{self.name_in_class}"
        response = requests.get(url)

        if response.status_code == 200:
            self.pokemon_data = response.json()
            if self.pokemon_data and response.status_code == 200:
                height = int(self.pokemon_data["height"]) * 10
                weight = int(self.pokemon_data["weight"]) / 10

                abilities_inp = self.pokemon_data["abilities"]
                abilities_list_raw = []
                for i in abilities_inp:
                    abi_dict = i["ability"]
                    name = abi_dict["name"]
                    abilities_list_raw.append(name)

                seperator = " , "
                abilities_list = seperator.join(abilities_list_raw)
                self.label1.setText(f"Name : {self.pokemon_data["name"]}".capitalize())
                self.label2.setText(f"Id : {self.pokemon_data["id"]}")
                self.label3.setText(f"Height : {height} cm")
                self.label4.setText((f"Weight : {weight} kg"))
                self.label5.setText(f"Key abilities : {abilities_list}")
                self.error_label.setText("")
        else:
            self.error_label.setText(f"⚠failed {response.status_code}⚠")
            self.label1.setText("")
            self.label2.setText("")
            self.label3.setText("")
            self.label4.setText("")
            self.label5.setText("")




def main():
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('com.pokefind.myapp')
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("E:\\Nihaal 1\\PICTURES\\pokeball.jpg"))
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()



