from pygrabber.dshow_graph import FilterGraph
import tkinter as tk
from tkinter import ttk
import threading
import time
import cv2
import keyboard
from tkinter import messagebox
import os

key_conversion =  {
    "esc": "Escape",
    "enter": "Return",
    "delete": "Delete",
    "home": "Home",
    "end": "End",
    "page up": "Prior",
    "page down": "Next",
    "up": "Up",
    "down": "Down",
    "left": "Left",
    "right": "Right",
    "tab": "Tab",
    "backspace": "BackSpace",
    "caps lock": "Caps_Lock",
    "ctrl": "Control",
    "shift": "Shift",
    "alt": "Alt",
    "f1": "F1",
    "f2": "F2",
    "f3": "F3",
    "f4": "F4",
    "f5": "F5",
    "f6": "F6",
    "f7": "F7",
    "f8": "F8",
    "f9": "F9",
    "f10": "F10",
    "f11": "F11",
    "f12": "F12",
    "space": "space",
    "quote": "apostrophe",
    "semicolon": "semicolon",
    "comma": "comma",
    "period": "period",
    "slash": "slash",
    "backslash": "backslash",
    "minus": "minus",
    "equal": "equal",
    "bracketleft": "bracketleft",
    "bracketright": "bracketright",
    "backquote": "grave",
    "A":"a",
    "B":"b",
    "C":"c",
    "D":"d",
    "E":"e",
    "F":"f",
    "G":"g",
    "H":"h",
    "I":"i",
    "J":"j",
    "K":"k",
    "L":"l",
    "M":"m",
    "N":"n",
    "O":"o",
    "P":"p",
    "Q":"q",
    "R":"r",
    "S":"s",
    "T":"t",
    "U":"u",
    "V":"v",
    "W":"w",
    "X":"x",
    "Y":"y",
    "Z":"z",
}



class WebcamThread(threading.Thread):
    def __init__(self, app, camera_index):
        threading.Thread.__init__(self)
        self.camera_index = camera_index
        self.camera = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW)
        
        self.running = True
        self.face_detected = False
        self.face_detected_time = None
        self.app = app
        


    def run(self):
        while self.running:
            ret, frame = self.camera.read()
            if not ret:
                break
            if self.app.transparent_window: 
                self.app.transparent_window.lift()
                self.app.transparent_window.attributes('-topmost',True)
                self.app.transparent_window.after_idle(root.attributes,'-topmost',False)
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.5, minNeighbors=2, minSize=(30, 30))

            if len(faces) > 0:
                print("有臉")
                if not self.face_detected:
                    self.face_detected = True
                    self.face_detected_time = time.time()
                else:
                    current_time = time.time()
                    if current_time - self.face_detected_time >= self.app.time_threshold:
                        self.app.show_face_detected_message()
                
            else:
                self.face_detected = False
                self.face_detected_time = None
                if self.app.black_window_open:  # 如果黑色視窗已經開啟
                    self.app.close_face_detected_window(None)  # 關閉黑色視窗
                    self.app.black_window_open = False
            time.sleep(0.1)

        self.camera.release()
    def stop(self):
        self.running = False

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("kid leave computer")
        self.root.geometry("400x400")

        self.camera_index_var = tk.StringVar(value="")
        self.camera_menu = ttk.Combobox(self.root, textvariable=self.camera_index_var, state="readonly")
        self.camera_menu.pack(pady=20)
        self.webcam_display_thread = None  # 新增一個執行緒變數

        self.populate_camera_menu()

        self.start_webcam_button = ttk.Button(self.root, text="Start Webcam", command=self.start_webcam)
        self.start_webcam_button.pack(pady=10)
        
        self.start_webcam_button = ttk.Button(self.root, text="test Webcam(press esc close)", command=self.display_camera2)
        self.start_webcam_button.pack(pady=10)

        self.start_recording_button = ttk.Button(self.root, text="Start Recording", command=self.start_recording)
        self.start_recording_button.pack(pady=10)

        self.stop_recording_button = ttk.Button(self.root, text="Stop Recording", command=self.stop_recording)
        self.stop_recording_button.pack(pady=10)
        self.stop_recording_button.config(state=tk.DISABLED)

        self.recorded_hotkey_var = tk.StringVar(value="Control-Alt-q")
        self.hotkey_label = tk.Label(self.root, text="Record Hotkey:")
        self.hotkey_label.pack(pady=5)
        self.hotkey_display = tk.Label(self.root, textvariable=self.recorded_hotkey_var)
        self.hotkey_display.pack()

        self.hotkey="Control-Alt-q"
        self.time_threshold = 0.25     # 默認的時間閾值

        self.time_label = tk.Label(self.root, text="Time threshold (seconds):")
        self.time_label.pack(pady=5)
        self.time_entry = tk.Entry(self.root)
        self.time_entry.insert(0, str(self.time_threshold))
        self.time_entry.pack()

        self.recording = False
        self.recorded_events = []
    
        self.webcam_thread = None

        self.black_window_open = False  # 新增黑色視窗狀態的變數

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        #self.root.after(100, self.check_hotkey_press)  # 開始檢查快捷鍵
        # with pynput_keyboard.Listener(on_press=self.on_key_press) as listener:
        #     listener.join()

    def on_close(self,event=None):
        print("on_close")
        try:
            self.root.destroy()
        except Exception as e:
            print("Failed to destroy",e)
            
        print("successfully closed?")
        self.root.quit()
        print("successfully closed!")
        os._exit(0) 
        

    def populate_camera_menu(self):
        cameras = self.get_available_cameras()
        if cameras:
            self.camera_menu["values"] = list(cameras.values())
            self.camera_index = list(cameras.keys())[0]
            self.camera_menu.set(list(cameras.values())[0])
        else:
            self.camera_menu["values"] = ["No Cameras Available"]
            self.camera_menu.set("No Cameras Available")

    def get_available_cameras(self):
        devices = FilterGraph().get_input_devices()
        available_cameras = {}
        for device_index, device_name in enumerate(devices):
            available_cameras[device_index] = device_name
        return available_cameras

    def start_recording(self):
        self.time_threshold = float(self.time_entry.get())

        self.recording = True
        self.recorded_events = []
        self.start_recording_button.config(state=tk.DISABLED)
        self.stop_recording_button.config(state=tk.NORMAL)
        self.recorded_hotkey_var.set("Recording...")
        keyboard.hook(self.on_key)

    def stop_recording(self):
        self.recording = False
        self.start_recording_button.config(state=tk.NORMAL)
        self.stop_recording_button.config(state=tk.DISABLED)
        print((self.recorded_events))
        self.recorded_events=self.mapping(self.recorded_events)
        hotkey_str = '-'.join(self.recorded_events)
        self.hotkey=hotkey_str
        self.recorded_hotkey_var.set(hotkey_str)
        keyboard.unhook_all()
        

    def on_key(self, e):
        if self.recording:
            if e.event_type == keyboard.KEY_DOWN:
                self.recorded_events.append(e.name)

    def mapping(self, recordings):
        converted_recordings = []
        for recording in recordings:
            if recording in key_conversion:
                converted_recordings.append(key_conversion[recording])
            else:
                converted_recordings.append(recording)
        return converted_recordings
    

    def start_webcam(self):
        if self.camera_index is not None:
            print(self.hotkey)
            self.root.bind("<"+self.hotkey+">",self.on_close)
            
            # 將視窗設置為全屏透明
            # # 设置窗口为全屏透明并将焦点放在窗口上
            self.show_transparent_window()
            self.webcam_thread = WebcamThread(self, self.camera_menu.current())
            self.webcam_thread.start()

            # 啟動影像顯示執行緒
            self.webcam_display_thread = threading.Thread(target=self.display_webcam)
            self.webcam_display_thread.start()
            # while 1:
            #     self.root.focus_set()
    def display_webcam(self):
        print("webcam display thread started")

    def display_camera2(self):
        print("camera2 display thread started")
        try:
            index=self.camera_menu.current()
            cap =cv2.VideoCapture(index)
            print(index)
            while True:
                ret, frame = cap.read()
                print("read")
                if ret:
                    print("imshow")
                    cv2.imshow("Webcam Output", frame)
                else:
                    break
                
                key = cv2.waitKey(10)  & 0xFF
                if key == 27:# or cv2.getWindowProperty('frame', cv2.WND_PROP_VISIBLE) < 1.0: 
                    break
            cv2.destroyAllWindows()
        except Exception as e:
            print(e)
        
        

    def stop_webcam(self):
        if self.webcam_thread:
            self.webcam_thread.stop()
            self.webcam_thread.join()
            self.webcam_thread = None
    def show_transparent_window(self):
        self.transparent_window = tk.Toplevel(self.root)
        self.transparent_window.attributes("-fullscreen", True)
        self.transparent_window.attributes("-alpha", 0.01)
        self.transparent_window.focus_set()
        self.root.attributes("-alpha", 0.01)  # 將主視窗也設置為透明
        self.transparent_window.protocol("WM_DELETE_WINDOW", self.on_close)
        self.root.focus_set()  # 將焦點恢復到主視窗

    def show_face_detected_message(self):
        if not self.black_window_open:  # 檢查黑色視窗是否已經開啟
            #self.root.withdraw()  # 隱藏主視窗
            self.face_detected_window = tk.Toplevel(self.root)
            self.face_detected_window.attributes("-fullscreen", True)
            self.face_detected_window.configure(bg="black")
            self.face_detected_window.wm_attributes("-topmost", 1)  # 設置黑色視窗在最上層
            self.face_detected_window.bind("<Escape>", self.close_face_detected_window)  # 按下 Esc 關閉視窗
            self.black_window_open = True  # 設置黑色視窗狀態為已開啟

    def close_face_detected_window(self, event):
        if self.black_window_open:  # 檢查黑色視窗是否已經開啟
            self.face_detected_window.destroy()  # 關閉偵測到人臉的視窗
            self.root.deiconify()  # 重新顯示主視窗
            self.black_window_open = False  # 設置黑色視窗狀態為已關閉
    # def check_hotkey_press(self):
    #     hotkey_str = '-'.join(self.recorded_events)
    #     if hotkey_str == self.hotkey:
    #         self.root.destroy()
    #     self.root.after(100, self.check_hotkey_press)


if __name__ == "__main__":
    try:
        root = tk.Tk()
        root.title('kids leave computer')
        root.iconbitmap('autodraw.ico')
        app = App(root)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
