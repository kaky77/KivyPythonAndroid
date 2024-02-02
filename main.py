from kivy.app import App
from kivy.uix.widget import Widget
import datetime
from PIL import ImageGrab
import numpy as np
import cv2

class MainWidget(Widget):
    
    def ScreenRecord(self):
        img_size = ImageGrab.grab()
        ScreenSize = list(img_size.size)
        width = ScreenSize[0]
        height = ScreenSize[1]

        time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        file_name = f'{time_stamp}.mp4'

        fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
        captured_video = cv2.VideoWriter(file_name,fourcc,20.0,(width,height))
        while True:
            img = ImageGrab.grab(bbox=(0,0,width,height))
            img_np = np.array(img)
            img_final = cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)
            cv2.imshow('Secret Capture', img_final)
            captured_video.write(img_final)
            if cv2.waitKey(10) == ord('q'):
                break


class TestApp(App):
    def build(self):
        return MainWidget()
    pass


if __name__ == '__main__':
    TestApp().run()
