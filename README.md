# pdf-to-audio
PDF Audio Reader is a simple Python GUI application that reads PDF files aloud. Using PyPDF2 to extract text from PDFs and pyttsx3 for text-to-speech, this project allows users to select any PDF and listen to its contents.
## Features
- Select a PDF file through a user-friendly GUI.
- Read the PDF aloud page by page.
- Stop the reading at any time.
- Lightweight and easy to use.

## Technologies Used
- Python 3.x
- PyPDF2 (for reading PDF content)
- pyttsx3 (for text-to-speech)
- Tkinter (for GUI)
- Threading (to keep GUI responsive while reading)

## Installation
1. Make sure Python 3.x is installed on your system.
2. Install required Python packages using pip:

```bash
pip install pyttsx3 PyPDF2
