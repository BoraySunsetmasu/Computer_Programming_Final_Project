import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import requests
from PIL import Image, ImageTk
from io import BytesIO

def submit_form():
    number = number_entry.get()
    if number:
        try:
            response = requests.post('#此處輸入API', json={'number': number})
            response.raise_for_status()

            image_data = response.content
            display_chart(image_data)
        except requests.RequestException as e:
            messagebox.showerror("Error", f"Request failed: {e}")
    else:
        messagebox.showwarning("Input Error", "請輸入一個編號！")

def display_chart(image_data):
    image = Image.open(BytesIO(image_data))
    chart_image = ImageTk.PhotoImage(image)
    chart_label.config(image=chart_image)
    chart_label.image = chart_image

root = tk.Tk()
root.title("Final project前端demo")
root.geometry("500x400")

header_label = tk.Label(root, text="這是計算機程式期末專案網頁前端測試", font=("Arial", 16))
header_label.pack(pady=10)

form_frame = tk.Frame(root)
form_frame.pack(pady=20)

number_label = tk.Label(form_frame, text="編號：")
number_label.grid(row=0, column=0, padx=5)

number_entry = tk.Entry(form_frame)
number_entry.grid(row=0, column=1, padx=5)

submit_button = tk.Button(form_frame, text="提交", command=submit_form)
submit_button.grid(row=0, column=2, padx=5)

chart_label = tk.Label(root)
chart_label.pack(pady=20)

root.mainloop()
