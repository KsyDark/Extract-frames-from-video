import cv2
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def extract_frames(video_path, output_dir, image_format):
    # Открываем видеофайл
    video = cv2.VideoCapture(video_path)
    
    # Проверяем, удалось ли открыть видеофайл
    if not video.isOpened():
        messagebox.showinfo("Ошибка", "Ошибка при загрузке видео.")
        return
    
    # Создаем директорию для сохранения кадров, если она еще не существует
    os.makedirs(output_dir.encode('utf-8'), exist_ok=True)
    frame_count = 0
    
    while True:
        # Читаем следующий кадр из видеофайла
        ret, frame = video.read()
        # Если кадр не удалось прочитать, значит видео закончилось
        if not ret:
            break
        # Сохраняем кадр в выбранном формате
        frame_name = f"frame_{frame_count}.{image_format}".encode('utf-8')
        frame_path = os.path.join(output_dir.encode('utf-8'), frame_name)
        # Преобразуем изображение из формата BGR (используется OpenCV) в формат RGB (используется Pillow)
        image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        # Сохраняем изображение с помощью библиотеки Pillow
        image.save(frame_path.decode('utf-8'))
        frame_count += 1
    # Освобождаем ресурсы, занятые видеофайлом
    video.release()

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Извлечение кадров из видео 1.0")
        self.resizable(width=False, height=False)
        self.geometry("400x270")
        
        try:
            self.iconbitmap(r'ico.ico')
        except:
            pass

        #Закрыть главное окно
        def exit_root(event):
            self.quit()
        self.bind('<Escape>', exit_root)
        
        def reference1(self):
            messagebox.showinfo("Справка", "Извлечение кадров из видео 1.0\n" "\nДанная программа предназначена \nдля ситуации, когда необходимо разложить \nвидео ролик на отдельные кадры и сохранить их. \n\nF1 = Справка\nEsc = Закрыть окно")
        #Вызов окна справки
        self.bind('<F1>', reference1)
        
        # Создание кнопки выбора видеофайла
        self.select_video_button = tk.Button(self, text="Выбрать видео", command=self.select_video)
        self.select_video_button.pack(pady=10)
        
        # Создание выпадающего меню для выбора формата кадров
        self.image_format_var = tk.StringVar(self)
        self.image_format_var.set("png")  # Значение по умолчанию
        
        self.image_format_label = tk.Label(self, text="Формат кадров:")
        self.image_format_label.pack(pady=5)
        
        self.image_format_menu = tk.OptionMenu(self, self.image_format_var, "png", "jpg")
        self.image_format_menu.pack(pady=5)
        
        # Создание кнопки выбора папки для сохранения кадров
        self.select_output_dir_button = tk.Button(self, text="Выбрать папку сохранения", command=self.select_output_dir)
        self.select_output_dir_button.pack(pady=10)
        
        # Создание кнопки извлечения кадров
        self.extract_frames_button = tk.Button(self, text="Извлечь кадры", command=self.extract_frames)
        self.extract_frames_button.pack(pady=10)
        
         # Создание кнопки справки
        self.extract_frames_button = tk.Button(self, text="Справка", command=self.reference)
        self.extract_frames_button.pack(pady=10)
        
        # Путь к выбранному видеофайлу и директории для сохранения кадров
        self.video_path = ""
        self.output_dir = ""
        
    def select_video(self):
         # Открываем диалоговое окно для выбора видеофайла
         self.video_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.avi;*.webm;*.mkv;*.wmv;*.mov;")])
         
    def select_output_dir(self):
         # Открываем диалоговое окно для выбора директории для сохранения кадров
         self.output_dir = filedialog.askdirectory()
         
    def extract_frames(self):
         # Проверяем, что пользователь выбрал видеофайл и директорию для сохранения кадров
         if self.video_path and self.output_dir:
             # Получаем выбранный формат изображения
             image_format = self.image_format_var.get()
             # Извлекаем кадры из видеофайла
             extract_frames(self.video_path, self.output_dir, image_format)
             messagebox.showinfo("Результат", "Извлечение кадров завершено.")
         else:
             messagebox.showwarning("Ошибка", "Выберите видео и папку сохранения.")
             
    def reference(self):
        messagebox.showinfo("Справка", "Извлечение кадров из видео 1.0\n" "\nДанная программа предназначена \nдля ситуации, когда необходимо разложить \nвидео ролик на отдельные кадры и сохранить их. \n\nF1 = Справка\nEsc = Закрыть окно")

app = Application()
app.mainloop()
