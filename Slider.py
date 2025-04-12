import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QSlider, QVBoxLayout, QHBoxLayout
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor, QPalette


class FontColorAdjuster(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Font Size and Color Adjuster")

        # NIM dan Nama
        self.nim = "F1D022135"
        self.nama = "Maftuh Ahnan Al-Kautsar"

        # Label utama
        self.label = QLabel(self.nim)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Arial", 30))

        # Label nama (tambahan untuk autentikasi)
        self.label_nama = QLabel(f"Nama: {self.nama} | NIM: {self.nim}")
        self.label_nama.setAlignment(Qt.AlignCenter)
        self.label_nama.setFont(QFont("Arial", 10))

        # Slider ukuran font
        self.font_slider = QSlider(Qt.Horizontal)
        self.font_slider.setMinimum(20)
        self.font_slider.setMaximum(60)
        self.font_slider.setValue(30)
        self.font_slider.valueChanged.connect(self.update_font_size)

        # Slider warna background
        self.bg_slider = QSlider(Qt.Horizontal)
        self.bg_slider.setMinimum(0)
        self.bg_slider.setMaximum(255)
        self.bg_slider.setValue(255)
        self.bg_slider.valueChanged.connect(self.update_background_color)

        # Slider warna font
        self.font_color_slider = QSlider(Qt.Horizontal)
        self.font_color_slider.setMinimum(0)
        self.font_color_slider.setMaximum(255)
        self.font_color_slider.setValue(0)
        self.font_color_slider.valueChanged.connect(self.update_font_color)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.label_nama)

        # Font size
        layout.addLayout(self.labeled_slider("Font Size", self.font_slider))

        # Background
        layout.addLayout(self.labeled_slider("Background Color", self.bg_slider))

        # Font color
        layout.addLayout(self.labeled_slider("Font Color", self.font_color_slider))

        self.setLayout(layout)
        self.update_background_color()
        self.update_font_color()

    def labeled_slider(self, text, slider):
        layout = QHBoxLayout()
        label = QLabel(text)
        label.setFixedWidth(120)
        layout.addWidget(label)
        layout.addWidget(slider)
        return layout

    def update_font_size(self):
        size = self.font_slider.value()
        self.label.setFont(QFont("Arial", size))

    def update_background_color(self):
        gray = self.bg_slider.value()
        color = QColor(gray, gray, gray)
        palette = self.label.palette()
        palette.setColor(QPalette.Window, color)
        self.label.setAutoFillBackground(True)
        self.label.setPalette(palette)

    def update_font_color(self):
        gray = self.font_color_slider.value()
        color = QColor(gray, gray, gray)
        palette = self.label.palette()
        palette.setColor(QPalette.WindowText, color)
        self.label.setPalette(palette)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FontColorAdjuster()
    window.resize(400, 300)
    window.show()
    sys.exit(app.exec_())
