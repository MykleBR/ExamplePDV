import os
from qt_core import *


class PyPushButton(QPushButton):
    def __init__(self,
        text ="",
        height = 40,
        minimum_width = 50,
        text_padding = 55,
        text_color = "",
        icon_path = "",
        icon_color = "",
        btn_color = "",
        btn_hover = "",
        btn_pressed = "",
        is_active = False
    ):
        super().__init__()
        
        # Parametros padrões
        self.setText(text)
        self.setMaximumHeight(height)
        self.setMinimumHeight(height)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        
        # Custom params
        self.minimum_width = minimum_width
        self.text_padding = text_padding
        self.text_color = text_color
        self.icon_path = icon_path
        self.icon_color = icon_color
        self.btn_color = btn_color
        self.btn_hover = btn_hover
        self.btn_pressed = btn_pressed
        self.is_active = is_active

        # set style
        self.set_style(
            text_padding = self.text_padding,
            text_color = self.text_color,
            btn_color = self.btn_color,
            btn_hover = self.btn_hover,
            btn_pressed = self.btn_pressed,
            is_active = self.is_active
        )
    
    def set_active(self, is_active_button):
        self.set_style(
            text_padding = self.text_padding,
            text_color = self.text_color,
            btn_color = self.btn_color,
            btn_hover = self.btn_hover,
            btn_pressed = self.btn_pressed,
            is_active = is_active_button
        )
    
       
    def set_style(
        self,
        text_padding = 55,
        text_color = "white",
        btn_color = "#1E2126",
        btn_hover = "#555D6B",
        btn_pressed = "#030317",
        is_active = True
    ):
        style = f"""
        QPushButton {{
            color: {text_color};
            background-color:{btn_color};
            padding-left: {text_padding}px;
            text-align: left;
            border: none;
        }}
        QPushButton:hover{{
            background-color:{btn_hover};  
        }}
        QPushButton:pressed{{
            background-color:{btn_pressed};  
        }}
        """
        
        active_style = f"""
        QPushButton {{
            background-color:{btn_color};
            border-right:6px solid #1F2C40;
            
        }}
        """
        if not is_active:
            self.setStyleSheet(style)
        else:
            self.setStyleSheet(style + active_style)
    
    def paintEvent(self, event):
        QPushButton.paintEvent(self, event)
        
        # Painter
        qpainter = QPainter()
        qpainter.begin(self)
        qpainter.setRenderHint(QPainter.RenderHint.Antialiasing)
        qpainter.setPen(Qt.PenStyle.NoPen)
        conteiner = QRect(0,0, self.minimum_width, self.height())
        self.carrega_icon(qpainter, self.icon_path, conteiner, self.icon_color)
        qpainter.end()
        
    
    def carrega_icon(self, qpainter, image, conteiner, color):
        
        # formata path
        app_path = os.path.abspath(os.getcwd())
        folder = "gui/images/icons"
        path = os.path.join(app_path, folder)
        icon_path = os.path.normpath(os.path.join(path, image))
        
        # desenhar icon
        icon = QPixmap(icon_path)
        qpfilho = QPainter(icon)
        qpfilho.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceIn)
        qpfilho.fillRect(icon.rect(), color)
        x = (conteiner.width() - icon.width()) / 2
        y = (conteiner.height() - icon.height()) / 2
        qpainter.drawPixmap(x,y,icon)
        qpfilho.end()
        