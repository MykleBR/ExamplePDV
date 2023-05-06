import sys
import os
from qt_core import *
from gui.windows.main_window.ui_main_window import Ui_MainWindow



class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Central de softwares")
        self.ui = Ui_MainWindow()
        self.ui.setup_ui(self)
        
        self.ui.btn_toggle.clicked.connect(self.toggle_button)
        self.ui.botao_home.clicked.connect(self.show_page_home)
        self.ui.botao_jogos.clicked.connect(self.show_page_games)
        self.ui.botao_ferramentas.clicked.connect(self.show_page_devtools)
        self.ui.btn_config.clicked.connect(self.show_page_config)
        self.ui.label_direita.clicked.connect(self.botao_sair)
        
        # Exibi a tela
        self.show()
    
    def botao_sair(self):
        QApplication.quit()
    
    def disable_select(self):
        for btn in self.ui.menu_esquerda.findChildren(QPushButton):
            try:
                btn.set_active(False)
            except:
                pass
    
    def show_page_home(self):
        self.ui.paginas.setCurrentWidget(self.ui.ui_pages.page1)
        self.disable_select()
        self.ui.botao_home.set_active(True)
    
    def show_page_games(self):
        self.ui.paginas.setCurrentWidget(self.ui.ui_pages.page2)
        self.disable_select()
        self.ui.botao_jogos.set_active(True)
    
    def show_page_devtools(self):
        self.ui.paginas.setCurrentWidget(self.ui.ui_pages.page3)
        self.disable_select()
        self.ui.botao_ferramentas.set_active(True)
        
    def show_page_config(self):
        self.ui.paginas.setCurrentWidget(self.ui.ui_pages.page4)
        self.disable_select()
        self.ui.btn_config.set_active(True)
        
    def toggle_button(self):
        # get width    
        menu_width = self.ui.menu_esquerda.width()
        # check width
        width = 50
        if menu_width == 50:
            width = 240     
        # animação de transição
        self.animation = QPropertyAnimation(self.ui.menu_esquerda, b'minimumWidth')
        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.Type.InOutBack)
        self.animation.start()  
    
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())





