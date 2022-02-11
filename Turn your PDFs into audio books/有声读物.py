# @Time:2022/2/120:29
# @Author:中意灬
# @File:有声读物.py
# @ps:tutu qqnum:2117472285

import pyttsx3
import pdfplumber
pdf=pdfplumber.open(input('请输入书名:'))
pg_no=int(input("请输入你想从第几页读着走："))
#总页数
numpages=len(pdf.pages)
for num in range((pg_no-1),numpages):
    #获取指定文章页数位置的内容
    first_page=pdf.pages[num]
    #获取文本内容
    text=first_page.extract_text()
    #初始化
    speaker=pyttsx3.init()
    #去掉文章中的换行符
    text=text.replace('\n','')
    #调整人声类型，voice[0]为中文女声，可自己切换其他的，但注意英文女声无法读取中文
    voices=speaker.getProperty('voices')
    speaker.setProperty('voice',voices[0].id)
    #调整语速
    rate=speaker.getProperty('rate')
    speaker.setProperty('rate',150)
    #调整音量,单位为0-1
    volume=speaker.getProperty('volume')
    speaker.setProperty('volume',1)
    #读
    speaker.say(text)
    #保存音频
    # speaker.save_to_file(text, 'T1.mp3')
    speaker.runAndWait()
