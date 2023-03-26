from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout,QVBoxLayout, QSlider
from PyQt5.QtMultimedia import QMediaPlayer, QMediaPlaylist, QMediaContent
from PyQt5.QtCore import QUrl,Qt
from PyQt5.QtGui import QIcon
from AuditoFeaturePicture import testDraw



class BRLPlayer(QWidget):
    def __init__(self):
        super().__init__()
        self.playerList = None
        self.player = None
        self.btnPrev = None
        self.btnNext = None
        self.btnPlay = None
        self.fig = None
        self.initUI()


    def initUI(self):
        # 创建组件成员：三个按键
        self.btnPlay = QPushButton(self)
        self.btnNext = QPushButton(self)
        self.btnPrev = QPushButton(self)
        self.player = QMediaPlayer(self)
        self.playerList = QMediaPlaylist(self)
        self.playSlider = QSlider(Qt.Horizontal,self)
        self.fig = testDraw()


        # 各部件细节设置
        # 按键配置
        self.btnPlay.setText("Play")
        self.btnPrev.setText("Prev")
        self.btnNext.setText("Next")
        # 播放器部分设置
        self.player.setPlaylist(self.playerList)
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile("E:/download/Music/complexity.mp3")))
        self.player.stop()
        # 进度条设置
        #matplotlib绘图设置
        data = list(range(1000))
        self.fig.ax1.plot(data)

        # 布局设置
        lh1 = QHBoxLayout()
        lh1.addWidget(self.btnPrev)
        lh1.addWidget(self.btnPlay)
        lh1.addWidget(self.btnNext)
        lv1 = QVBoxLayout()
        lv1.addWidget(self.playSlider)
        lmain = QVBoxLayout()
        lmain.addWidget(self.fig)
        lmain.addLayout(lv1)
        lmain.addLayout(lh1)
        self.setLayout(lmain)










