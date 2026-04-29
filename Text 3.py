# 导入系统模块，用于程序退出
import sys
# 从 PySide6 导入所需的控件库
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QPushButton, QLabel, QTextEdit, QFrame
)
# 导入绘图相关的模块，用于显示图形
from PySide6.QtGui import QPixmap, QPainter, QColor
# 导入核心模块，用于对齐设置
from PySide6.QtCore import Qt

# 定义主窗口类，继承自 QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 设置窗口标题和大小
        self.setWindowTitle("Python GUI 实验")
        self.resize(600, 500)

        # 创建中心部件和垂直布局
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)

        # --------------------------
        # 1. 按钮控件（交互用）
        # --------------------------
        self.button = QPushButton("点击")
        # 绑定按钮点击事件到自定义函数
        self.button.clicked.connect(self.on_button_clicked)
        layout.addWidget(self.button)

        # --------------------------
        # 2. 信息显示框（文本用）
        # --------------------------
        self.info_box = QTextEdit()
        self.info_box.setPlaceholderText("点击上方按钮，这里会显示信息...")
        self.info_box.setReadOnly(True)  # 设置为只读，防止用户修改
        layout.addWidget(self.info_box)

        # --------------------------
        # 3. 图形显示框（绘图用）
        # --------------------------
        self.graph_frame = QFrame()
        self.graph_frame.setFrameShape(QFrame.Box)
        self.graph_frame.setFixedHeight(200)
        self.graph_layout = QVBoxLayout(self.graph_frame)

        self.graph_label = QLabel()
        self.graph_label.setAlignment(Qt.AlignCenter)
        self.graph_layout.addWidget(self.graph_label)
        layout.addWidget(self.graph_frame)

    # 按钮点击事件处理函数
    def on_button_clicked(self):
        # 更新信息显示框的文本
        self.info_box.setText("按钮已成功点击！\n"
                              "1. 信息显示框\n"
                              "2. VSCode 运行 Python GUI 程序正常")

        # 在内存中创建一个图片，用于显示
        pixmap = QPixmap(400, 150)
        pixmap.fill(QColor(230, 240, 255))  # 设置背景色
        painter = QPainter(pixmap)
        # 画一个矩形和文字
        painter.setPen(QColor(0, 100, 200))
        painter.drawRect(50, 30, 300, 90)
        painter.drawText(130, 80, "Python GUI 程序正常")
        painter.end()

        # 把绘制好的图片放到图形显示框里
        self.graph_label.setPixmap(pixmap)

# 程序入口
if __name__ == "__main__":
    # 创建应用实例
    app = QApplication(sys.argv)
    # 创建主窗口实例
    window = MainWindow()
    # 显示窗口
    window.show()
    # 进入事件循环，等待用户操作
    sys.exit(app.exec())