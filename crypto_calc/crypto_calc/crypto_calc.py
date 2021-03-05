from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QComboBox, QLabel, QLineEdit,QStyleFactory, QTableWidget,QTableWidgetItem
import os
from PyQt5 import QtWidgets
import get_Realtime_C_USD
app = QApplication([])
app.setStyle("Fusion")

#window = QWidget()

#layout = QVBoxLayout()
#layout.addWidget(QPushButton('Top'))
#layout.addWidget(QPushButton('Bottom'))
#
#window.setGeometry(100,200,1000,800)
#
#window.setLayout(layout)
#
#
#
#window.show()
#app.exec()


class gui(QWidget):
    c=0
    def __init__(self, parent=None):
        QWidget.__init__(self,parent)
        
        self.Gui_layout()
        self.show_gui()
        
        pass

    def Gui_layout(self):
        # general setup of main window.
        
        
        self.setGeometry                (100,100,1000,600)

        self.ddm=QComboBox              (self)
        self.b1=QPushButton             ("Add token",self)
        self.del_coin=QPushButton       ("Delete token",self) 
        self.bought_b=QPushButton       ("Bought",self)
        self.sold_b=QPushButton         ("Sold",self)
        self.table=QTableWidget         (self)
        self.token=QLineEdit            (self)
        self.current_price=QLineEdit    (self)
        self.coins_in_w=QLabel          (self)
        self.avg_price=QLabel           (self)
        self.current_profit=QLabel      (self)
        self.ddm.setGeometry            (100,100,150,40)
        self.token.setGeometry          (100,200,150,40)
        self.b1.setGeometry             (200,300,80,40) 
        self.del_coin.setGeometry       (100,300,80,40) 
        self.table.setGeometry          (400,100,240,200)
        self.sold_b.setGeometry         (420,320,80,40)
        self.bought_b.setGeometry       (520,320,80,40)
        
        self.table.setRowCount(10)
        self.table.setColumnCount(2)
        
        self.initialize()
        self.actions()
    
    def initialize(self):
        # First setup of program after startup
        
        self.first_run=True
        self.setup_registered_tokens()
        self.setup_token_objects()
        self.show_coin_balance_table()
    def setup_registered_tokens(self):
        # Start writing all the stored items to the combobox
        c=0
        self.token_exist=False
        self.rootdir="C:\\Users\\jor.NORMATIC\\source\\repos\\crypto_calc\\files"
        t_register="\\token_register"
        os.chdir(self.rootdir)
        f=open(self.rootdir+t_register+"\\tokens.txt",'a')
        f.close()
        f=open(self.rootdir+t_register+"\\tokens.txt",'r')
        self.tokenfile=f.readlines()
        f.close()

        for tokens in self.tokenfile:
            if (tokens !=None):
                self.add_item_to_combobox_2(tokens)



    def setup_token_objects(self):
        c=0
        t_objects="\\token_objects\\"
        
        all_items=[self.ddm.itemText(i) for i in range(self.ddm.count())]
        
        for f in all_items:
            if (f.endswith("\n")):
                f=f[0:len(f)-1]
            x=open(self.rootdir+t_objects+f+".csv",'a')
            x.close()

    def show_coin_balance_table(self):
        self.table.clear()
        t_objects="\\token_objects\\"
        token=self.ddm.itemText(self.ddm.currentIndex())
        if(token.endswith("\n")):
            token=token[0:len(token)-1]
        #open the file containing coin detail
        f=open(self.rootdir+t_objects+token+".csv",'r')
        doc=f.readlines()
        f.close()
        
        #iterates over list of items
        i=1
        for d in doc:
            # iterates over the items in d
            g=d.split(";")
            j=0
            for e in g:
                if(e.endswith("\n") or e.endswith(" ")):
                    e=e[0:len(e)-1]
                item=QTableWidgetItem((e))
                self.table.setItem(i,j,item)
                j+=1
            i+=1
        self.table.setHorizontalHeaderLabels(["Coins","Price"])
    
        
        

    def actions(self):
        self.b1.released.connect(self.add_item_to_combobox)
        self.b1.released.connect(self.setup_token_objects)
        self.del_coin.released.connect(self.remove_token_data)
        self.ddm.currentIndexChanged.connect(self.show_coin_balance_table)
    def add_item_to_combobox(self):
      
        name=self.token.text()
        t_register="\\token_register"
        if name != "":
            self.ddm.addItem(name)
            f=open(self.rootdir+t_register+"\\tokens.txt",'a')
            f.write(name+"\n")
            #self.tokenfile.append(name+"\n")
            f.close()
        else:
            pass

    def remove_token_data(self):
        # When clicked remove token, all data of that token is removed from storage
        t_objects="\\token_objects\\"
        t_register="\\token_register\\"
        item=self.ddm.itemText(self.ddm.currentIndex())
        self.ddm.removeItem(self.ddm.currentIndex())
        item=item[0:len(item)-1]
        os.remove(self.rootdir+t_objects+item+".csv")

        all_items=[self.ddm.itemText(i) for i in range(self.ddm.count())]
        f=open(self.rootdir+t_register+"tokens.txt",'w')
        f.writelines(all_items)
        f.close()

    def add_item_to_combobox_2(self,token_names):
        name=token_names
        if name != "":
            self.ddm.addItem(name)
        else:
            pass


    def printer(self):
        self.c+=1
        print("clicked",self.c)


    def show_gui(self):
     
        self.show()
        app.exec()
#
if __name__ == "__main__":
    
    screen=gui()
    #screen.show_gui()
#    screen.show()
#    app.exec()
