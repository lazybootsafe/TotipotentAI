#coding:utf-8
#by finger on 02.md

from gtts import gTTS
import os
tts = gTTS(text='您好，我是您的私人助手，我叫zcc', lang='zh-tw')
tts.save("hello.mp3")
os.system("mpg321 hello.mp3")
