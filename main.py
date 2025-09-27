import pyttsx3
import PyPDF2
from tkinter import *
from tkinter import filedialog
from threading import Thread

player = pyttsx3.init()
stop_flag = False
reading_thread = None


def speak_text(text):
 
    global stop_flag
    if text:
        player.say(text)
        player.runAndWait()
        if stop_flag:
            player.stop()

def read_pdf(file_path):

    global stop_flag
    stop_flag = False
    with open(file_path, "rb") as pdf_file:
        pdfreader = PyPDF2.PdfReader(pdf_file)
        pages = len(pdfreader.pages)
        for i in range(pages):
            if stop_flag:
                break
            page = pdfreader.pages[i]
            text = page.extract_text()
            if text:
                speak_text(text)

def start_reading():

    global reading_thread
    if reading_thread and reading_thread.is_alive():
        print("Already reading. Stop first.")
        return
    book = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if book:
        reading_thread = Thread(target=read_pdf, args=(book,))
        reading_thread.start()

def stop_reading():
   
    global stop_flag
    stop_flag = True
    player.stop()


root = Tk()
root.title("PDF Audio Reader")
root.geometry("300x150")

Label(root, text="PDF Audio Reader", font=("Arial", 14)).pack(pady=10)

Button(root, text="Start Reading", command=start_reading, width=25, bg="green", fg="white").pack(pady=5)
Button(root, text="Stop", command=stop_reading, width=25, bg="red", fg="white").pack(pady=5)

root.mainloop()

