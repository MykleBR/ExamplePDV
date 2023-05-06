from qt_core import *
from gui.pages.ui_pages import Ui_Ui_apllication_pages
from gui.widgets.py_push_button import PyPushButton

class Ui_MainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")
        
        # Set params initials
        parent.resize(1200, 720)
        parent.setMinimumSize(960, 540)
        
        # Create central widget
        self.central_frame              = QFrame()
        self.central_frame              .setStyleSheet("background-color: #080826")
        
        # Main layout
        self.main_layout                = QHBoxLayout(self.central_frame)
        self.main_layout                .setContentsMargins(0,0,0,0)
        self.main_layout                .setSpacing(0)
        
        # Menu a esquerda
        self.menu_esquerda              = QFrame()
        self.menu_esquerda              .setStyleSheet("background-color: #1E2126")
        self.menu_esquerda              .setMaximumWidth(50)
        self.menu_esquerda              .setMinimumWidth(50)
        
        # layout menu 
        self.layout_menu                = QVBoxLayout(self.menu_esquerda)
        self.layout_menu                .setContentsMargins(0,0,0,0)
        self.layout_menu                .setSpacing(0)
        
        # Frame superior menu
        self.top_frame_menu             = QFrame()
        self.top_frame_menu             .setMinimumHeight(40)
        self.top_frame_menu             .setObjectName("top_frame_menu")
        
        # Layout superior do menu
        self.left_menu_top_layout       = QVBoxLayout(self.top_frame_menu)
        self.left_menu_top_layout       .setContentsMargins(0,0,0,0)
        self.left_menu_top_layout       .setSpacing(0)
                
        # Botoes do frame superior
        self.btn_toggle                 = PyPushButton(text ="Menu Principal",
                                                    height = 50,
                                                    minimum_width = 50,
                                                    text_padding = 55,
                                                    text_color = "white",
                                                    icon_path = "icon_menu.svg",
                                                    icon_color="white",
                                                    btn_color = "#1E2126",
                                                    btn_hover = "#555D6B",
                                                    btn_pressed = "#030317",
                                                    is_active = False)
        
        self.botao_home                 = PyPushButton(text ="Pagina Inicial",
                                                    height = 50,
                                                    minimum_width = 50,
                                                    text_padding = 55,
                                                    text_color = "white",
                                                    icon_path = "icon_home.svg",
                                                    icon_color="white",
                                                    btn_color = "#1E2126",
                                                    btn_hover = "#555D6B",
                                                    btn_pressed = "#030317",
                                                    is_active = True)
        
        self.botao_jogos                = PyPushButton(text ="Games",
                                                    height = 50,
                                                    minimum_width = 50,
                                                    text_padding = 55,
                                                    text_color = "white",
                                                    icon_path = "icon_games.svg",
                                                    icon_color="white",
                                                    btn_color = "#1E2126",
                                                    btn_hover = "#555D6B",
                                                    btn_pressed = "#030317",
                                                    is_active = False)
        
        self.botao_ferramentas          = PyPushButton(text ="Dev Tools",
                                                    height = 50,
                                                    minimum_width = 50,
                                                    text_padding = 55,
                                                    text_color = "white",
                                                    icon_path = "icon_devtools.svg",
                                                    icon_color = "white",
                                                    btn_color = "#1E2126",
                                                    btn_hover = "#555D6B",
                                                    btn_pressed = "#030317",
                                                    is_active = False)
        
        # adicionar widgets ao layout superior
        self.left_menu_top_layout       .addWidget(self.btn_toggle)
        self.left_menu_top_layout       .addWidget(self.botao_home)
        self.left_menu_top_layout       .addWidget(self.botao_jogos)
        self.left_menu_top_layout       .addWidget(self.botao_ferramentas)
        
        # espaçador menu
        self.espacador_frame_menu       = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        
        # Frame inferior menu
        self.bottom_frame_menu          = QFrame()
        self.bottom_frame_menu          .setMinimumHeight(50)
        self.bottom_frame_menu          .setObjectName("bottom_frame_menu")
        
        # Layout inferior do menu
        self.left_menu_bottom_layout    = QVBoxLayout(self.bottom_frame_menu)
        self.left_menu_bottom_layout    .setContentsMargins(0,0,0,0)
        self.left_menu_bottom_layout    .setSpacing(0)
                
        # Botoes do frame inferior
        self.btn_config                 = PyPushButton( text="Configurações",
                                                        height = 50,
                                                        minimum_width = 50,
                                                        text_padding = 55,
                                                        icon_path = "icon_config.svg",
                                                        icon_color = "white",
                                                        text_color = "white",
                                                        btn_color = "#1E2126",
                                                        btn_hover = "#555D6B",
                                                        btn_pressed = "#030317",
                                                        is_active = False
                                                      )
        
        # Adicionar Botoes ao layout do menu do frame inferior
        self.left_menu_bottom_layout    .addWidget(self.btn_config)
        
        # Frame Versionamento
        self.versao_frame_menu          = QLabel("V1.0.0")
        self.versao_frame_menu          .setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.versao_frame_menu          .setStyleSheet("background-color: green")
        self.versao_frame_menu          .setMaximumHeight(30)
        self.versao_frame_menu          .setMinimumHeight(30)

        # Conteudo      
        self.conteudo                   = QFrame()
        self.conteudo                   .setStyleSheet("background-color: #1F2C40")

        # layout do conteudo        
        self.layout_conteudo            = QVBoxLayout(self.conteudo)
        self.layout_conteudo            .setContentsMargins(0,0,0,0)
        self.layout_conteudo            .setSpacing(0)

        # Top bar       
        self.top_bar                    = QFrame()     
        self.top_bar                    .setStyleSheet("background-color: black")
        self.top_bar                    .setMaximumHeight(40)
        self.top_bar                    .setMinimumHeight(40)
        self.top_bar_layout             = QHBoxLayout(self.top_bar)

        # Label esquerda da barra do topo
        self.label_esquerda             = QLabel("Central de softwares")
        self.label_esquerda             .setStyleSheet("background-color: black")

        # Label separadora da barra do topo
        self.label_separador            = QSpacerItem(20,20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        # Label direita da barra do topo
        self.label_direita              = QPushButton("Sair")
        self.label_direita              .setStyleSheet("background-color: red; font-size: 12pt; color: white")

        # Top bar       
        self.bottom_bar                 = QFrame()
        self.bottom_bar                 .setStyleSheet("background-color: black")
        self.bottom_bar                 .setMaximumHeight(30)
        self.bottom_bar                 .setMinimumHeight(30)
        self.bottom_bar_layout          = QHBoxLayout(self.bottom_bar)

        # Label esquerda da barra do topo
        self.bottom_left_bar            = QLabel("Powered by Michael Lima")
        self.bottom_left_bar            .setStyleSheet("background-color: black; font-size: 9pt; color: white")

        # Label separadora da barra do topo
        self.bottom_spacer_bar          = QSpacerItem(20,20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        # Label direita da barra do topo
        self.right_bottom_bar           = QLabel("©2023.")
        self.right_bottom_bar           .setStyleSheet("background-color: black; font-size: 9pt; color: white")

        # aplicação de paginas      
        self.paginas                    = QStackedWidget()
        self.paginas                    .setStyleSheet("font-size: 12pt; color: white")
        self.ui_pages                   = Ui_Ui_apllication_pages()
        self.ui_pages                   .setupUi(self.paginas)
        self.paginas                    .setCurrentWidget(self.ui_pages.page1)

        # adicionar ao layout do menu
        self.layout_menu                .addWidget(self.top_frame_menu)
        self.layout_menu                .addItem(self.espacador_frame_menu)
        self.layout_menu                .addWidget(self.bottom_frame_menu)
        self.layout_menu                .addWidget(self.versao_frame_menu)
        
        # adicionar ao layout da barra do topo
        self.top_bar_layout             .addWidget(self.label_esquerda)
        self.top_bar_layout             .addItem(self.label_separador)
        self.top_bar_layout             .addWidget(self.label_direita)

        # adicionar ao layout da barra do top
        self.bottom_bar_layout          .addWidget(self.bottom_left_bar)
        self.bottom_bar_layout          .addItem(self.bottom_spacer_bar)
        self.bottom_bar_layout          .addWidget(self.right_bottom_bar)


        # adicionar ao layout do conteudo
        self.layout_conteudo            .addWidget(self.top_bar)
        self.layout_conteudo            .addWidget(self.paginas)
        self.layout_conteudo            .addWidget(self.bottom_bar)

        # Adicionar os widget       
        self.main_layout                .addWidget(self.menu_esquerda)
        self.main_layout                .addWidget(self.conteudo)

        # Set Central widget        
        parent                          .setCentralWidget(self.central_frame)
        
        
        
        