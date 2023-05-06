# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designeruXvZrf.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *


import ctypes
class Ui_Ui_apllication_pages(object):
    def setupUi(self, Ui_apllication_pages):
        if not Ui_apllication_pages.objectName():
            Ui_apllication_pages.setObjectName(u"Ui_apllication_pages")
        Ui_apllication_pages.resize(400, 300)

        self.page1 = self.create_page1()
        Ui_apllication_pages.addWidget(self.page1)

        self.page2 = self.create_page2()
        Ui_apllication_pages.addWidget(self.page2)

        self.page3 = self.create_page3()
        Ui_apllication_pages.addWidget(self.page3)

        self.page4 = self.create_page4()
        Ui_apllication_pages.addWidget(self.page4)

        self.retranslateUi(Ui_apllication_pages)

        QMetaObject.connectSlotsByName(Ui_apllication_pages)

    def retranslateUi(self, Ui_apllication_pages):
        Ui_apllication_pages.setWindowTitle(QCoreApplication.translate("Ui_apllication_pages", u"StackedWidget", None))
        
    
    def create_page1(self):
        page = QFrame()
        page.setObjectName("page1")
        page.setStyleSheet("""
            #page1 {
                background-color: #1F2C40;
            }
            QGroupBox {
                background-color: white;
                border: none;
                border-radius: 5px;
                padding: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                background-color: #1F2C40;
                padding: 5px;
                border: 1px solid #C0C0C0;
            }
            QTableWidget {
                color: black
            }
            #box1 {
                border: 2px solid #606060;
            }
            #box2 {
                border: 2px solid #606060;
            }
            #box3 {
                border: 2px solid #606060;
            }
            #box4 {
                border: 2px solid #606060;
            }
        """)

        layout = QGridLayout(page)
        layout.setObjectName("gridLayout")
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setHorizontalSpacing(20)
        layout.setVerticalSpacing(20)

        # Box 1 - ocupa coluna 0 e estende da linha 0 até a linha 2
        box1 = QGroupBox(page)
        box1.setObjectName("box1")
        box1.setTitle("Carrinho")
        box1.setStyleSheet('QGroupBox::title {subcontrol-origin: margin; background-color: black; padding: 5px; border: 1px solid #C0C0C0;}')
        layout.addWidget(box1, 0, 0, 4, 1)

        # Cria a tabela com 5 colunas
        table = QTableWidget(box1)
        table.setColumnCount(5)
        table.setColumnWidth(0, 75)
        table.setStyleSheet('background:#1F2C40; color:black; font-size: 32px; font-family: Arial sans')

        # Define a altura das linhas
        table.verticalHeader().setDefaultSectionSize(30)

        # Define o nome das colunas
        table.setHorizontalHeaderLabels(["Código", "Unidades", "Produto", "Val Unitario", "Val Total"])

        # Adiciona a tabela no layout do box1
        tabela_layout = QVBoxLayout(box1)
        tabela_layout.setContentsMargins(0,30,0,0)
        tabela_layout.addWidget(table)
        
        # Diminua a largura da coluna 0 para 50
        table.setColumnWidth(0, 110)
        table.setColumnWidth(1, 150)
        table.setColumnWidth(2, 235)
        table.setColumnWidth(3, 175)
        table.setColumnWidth(4, 175)

        # Diminua a largura do box1 para 180
        box1.setMaximumWidth(900)
        box1.setMinimumWidth(900)
        
        # Cria uma nova linha na tabela
        rowPosition = table.rowCount()
        table.insertRow(rowPosition)

        # Define os valores de cada célula na linha
        codigo = QTableWidgetItem("1234")
        unidades = QTableWidgetItem("2")
        produto = QTableWidgetItem("Produto A")
        val_unit = QTableWidgetItem("10.00")
        val_tot = QTableWidgetItem("20.00")

        # Adiciona as células na linha
        table.setItem(rowPosition, 0, codigo)
        table.setItem(rowPosition, 1, unidades)
        table.setItem(rowPosition, 2, produto)
        table.setItem(rowPosition, 3, val_unit)
        table.setItem(rowPosition, 4, val_tot)
        
        table.insertRow(rowPosition)
        # Define os valores de cada célula na linha
        codigo = QTableWidgetItem("1234")
        unidades = QTableWidgetItem("2")
        produto = QTableWidgetItem("Produto A")
        val_unit = QTableWidgetItem("10.00")
        val_tot = QTableWidgetItem("20.00")

        # Adiciona as células na linha
        table.setItem(rowPosition, 0, codigo)
        table.setItem(rowPosition, 1, unidades)
        table.setItem(rowPosition, 2, produto)
        table.setItem(rowPosition, 3, val_unit)
        table.setItem(rowPosition, 4, val_tot)
        
        table.insertRow(rowPosition)
        # Define os valores de cada célula na linha
        codigo = QTableWidgetItem("1234")
        unidades = QTableWidgetItem("2")
        produto = QTableWidgetItem("Produto A")
        val_unit = QTableWidgetItem("10.00")
        val_tot = QTableWidgetItem("20.00")

        # Adiciona as células na linha
        table.setItem(rowPosition, 0, codigo)
        table.setItem(rowPosition, 1, unidades)
        table.setItem(rowPosition, 2, produto)
        table.setItem(rowPosition, 3, val_unit)
        table.setItem(rowPosition, 4, val_tot)
        
        table.insertRow(rowPosition)
        # Define os valores de cada célula na linha
        codigo = QTableWidgetItem("1234")
        unidades = QTableWidgetItem("2")
        produto = QTableWidgetItem("Produto A")
        val_unit = QTableWidgetItem("10.00")
        val_tot = QTableWidgetItem("20.00")

        # Adiciona as células na linha
        table.setItem(rowPosition, 0, codigo)
        table.setItem(rowPosition, 1, unidades)
        table.setItem(rowPosition, 2, produto)
        table.setItem(rowPosition, 3, val_unit)
        table.setItem(rowPosition, 4, val_tot)
        
        table.insertRow(rowPosition)
        # Define os valores de cada célula na linha
        codigo = QTableWidgetItem("1234")
        unidades = QTableWidgetItem("2")
        produto = QTableWidgetItem("Produto A")
        val_unit = QTableWidgetItem("10.00")
        val_tot = QTableWidgetItem("20.00")

        # Adiciona as células na linha
        table.setItem(rowPosition, 0, codigo)
        table.setItem(rowPosition, 1, unidades)
        table.setItem(rowPosition, 2, produto)
        table.setItem(rowPosition, 3, val_unit)
        table.setItem(rowPosition, 4, val_tot)
        
        table.insertRow(rowPosition)
        # Define os valores de cada célula na linha
        codigo = QTableWidgetItem("1234")
        unidades = QTableWidgetItem("2")
        produto = QTableWidgetItem("Produto A")
        val_unit = QTableWidgetItem("10.00")
        val_tot = QTableWidgetItem("20.00")

        # Adiciona as células na linha
        table.setItem(rowPosition, 0, codigo)
        table.setItem(rowPosition, 1, unidades)
        table.setItem(rowPosition, 2, produto)
        table.setItem(rowPosition, 3, val_unit)
        table.setItem(rowPosition, 4, val_tot)

        # Box 2 - ocupa 50% da altura da coluna 1 e linha 0
        box2 = QGroupBox(page)
        box2.setObjectName("box2")
        box2.setTitle("Imagem do produto")
        box2.setStyleSheet('QGroupBox::title {subcontrol-origin: margin; background-color: black; padding: 5px; border: 1px solid #C0C0C0;}')
        layout.addWidget(box2, 0, 1, 2, 1)

        # Box 3 - ocupa 25% da altura da coluna 1 e linha 1
        box3 = QGroupBox(page)
        box3.setObjectName("box3")
        box3.setTitle("Valor total")
        box3.setStyleSheet('QGroupBox::title {subcontrol-origin: margin; background-color: black; padding: 5px; border: 1px solid #C0C0C0;}')
        layout.addWidget(box3, 2, 1, 1, 1)

        # Box 4 - ocupa 25% da altura da coluna 1 e linha 2
        box4 = QGroupBox(page)
        box4.setObjectName("box4")
        box4.setTitle("Informações de pagamento")
        box4.setStyleSheet('QGroupBox::title {subcontrol-origin: margin; background-color: black; padding: 5px; border: 1px solid #C0C0C0;}')
        layout.addWidget(box4, 3, 1, 1, 1)

        return page

    def create_page2(self):
        page = QWidget()
        page.setObjectName(u"page2")

        layout = QVBoxLayout(page)
        layout.setObjectName(u"verticalLayout_2")

        search_layout = QHBoxLayout()
        search_layout.setObjectName(u"search_layout")

        search_label = QLabel(page)
        search_label.setObjectName(u"search_label")
        search_label.setText("Buscar:")
        search_layout.addWidget(search_label)

        search_box = QLineEdit(page)
        search_box.setObjectName(u"search_box")
        search_layout.addWidget(search_box)

        filters_box = QComboBox(page)
        filters_box.setObjectName(u"filters_box")
        filters_box.addItem("Código")
        filters_box.addItem("Produto")
        search_layout.addWidget(filters_box)

        layout.addLayout(search_layout)

        table = QTableWidget(page)
        table.setObjectName(u"table")
        table.setColumnCount(5)
        table.setHorizontalHeaderLabels(["Código", "Unidades", "Produto", "Val. Unitário", "Val. Total"])
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(table)

        return page

    def create_page3(self):
        page = QWidget()
        page.setObjectName(u"page3")

        layout = QFormLayout(page)
        layout.setObjectName(u"formLayout")
        layout.setLabelAlignment(Qt.AlignLeft)
        layout.setFormAlignment(Qt.AlignLeft)

        codigo_edit = QLineEdit(page)
        codigo_edit.setObjectName(u"codigo_edit")
        codigo_edit.setPlaceholderText("Digite o código")
        layout.addRow("Código:", codigo_edit)

        unidades_edit = QLineEdit(page)
        unidades_edit.setObjectName(u"unidades_edit")
        unidades_edit.setPlaceholderText("Digite as unidades")
        layout.addRow("Unidades:", unidades_edit)

        produto_edit = QLineEdit(page)
        produto_edit.setObjectName(u"produto_edit")
        produto_edit.setPlaceholderText("Digite o produto")
        layout.addRow("Produto:", produto_edit)

        val_unitario_edit = QLineEdit(page)
        val_unitario_edit.setObjectName(u"val_unitario_edit")
        val_unitario_edit.setPlaceholderText("Digite o valor unitário")
        layout.addRow("Val. Unitário:", val_unitario_edit)

        val_total_edit = QLineEdit(page)
        val_total_edit.setObjectName(u"val_total_edit")
        val_total_edit.setPlaceholderText("Digite o valor total")
        layout.addRow("Val. Total:", val_total_edit)

        button = QPushButton(page)
        button.setObjectName(u"button")
        button.setText("Salvar")
        button.setStyleSheet("""
            background-color: #4CAF50;
            border: none;
            color: white;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            border-radius: 8px;
            """)
        layout.addRow("", button)

        return page

    def create_page4(self):
        page = QWidget()
        page.setObjectName("page4")
        page.setStyleSheet("color: #1e1e1e")

        layout = QVBoxLayout(page)
        layout.setContentsMargins(0, 0, 0, 0)

        # Group box 1 - Display Settings
        display_groupbox = QGroupBox("Configurações")
        display_groupbox.setStyleSheet("font-size: 16px; font-weight: bold")
        display_layout = QGridLayout(display_groupbox)

        resolution_label = QLabel("Resolução:")
        resolution_combobox = QComboBox()
        resolution_combobox.addItems(["800x600", "1024x768", "1280x720", "1360x768", "1600x900", "1920x1080"])
        resolution_combobox.setStyleSheet("background: #f5f5f5; border: 1px solid #d9d9d9; padding: 5px; font-size: 12px")
        resolution_label.setStyleSheet("color: black")
        display_layout.addWidget(resolution_label, 0, 0)
        display_layout.addWidget(resolution_combobox, 0, 1)

        theme_label = QLabel("Tema:")
        theme_combobox = QComboBox()
        theme_combobox.addItems(["Daltônico", "Claro", "Escuro"])
        theme_combobox.setStyleSheet("background: #f5f5f5; border: 1px solid #d9d9d9; padding: 5px; font-size: 12px")
        theme_label.setStyleSheet("color: black")
        display_layout.addWidget(theme_label, 1, 0)
        display_layout.addWidget(theme_combobox, 1, 1)

        language_label = QLabel("Idioma:")
        language_combobox = QComboBox()
        language_combobox.addItems(["Português", "Inglês", "Chinês"])
        language_combobox.setStyleSheet("background: #f5f5f5; border: 1px solid #d9d9d9; padding: 5px; font-size: 12px")
        language_label.setStyleSheet("color: black")
        display_layout.addWidget(language_label, 2, 0)
        display_layout.addWidget(language_combobox, 2, 1)

        # Group box 2 - Reset Options
        reset_groupbox = QGroupBox("Redefinições")
        reset_groupbox.setStyleSheet("font-size: 16px; font-weight: bold")
        reset_layout = QHBoxLayout(reset_groupbox)

        reset_password_button = QPushButton("Redefinir Senha")
        reset_password_button.setStyleSheet("background-color: #4CAF50; color: white; border: 2px solid #4CAF50; padding: 8px; font-size: 12px")
        reset_layout.addWidget(reset_password_button)

        reset_factory_button = QPushButton("Redefinir de Fábrica")
        reset_factory_button.setStyleSheet("background-color: #F44336; color: white; border: 2px solid #F44336; padding: 8px; font-size: 12px")
        reset_layout.addWidget(reset_factory_button)

        # Add group boxes to main layout
        layout.addWidget(display_groupbox)
        layout.addWidget(reset_groupbox)

        return page