import os
import tkinter as tk
from tkinter import filedialog, messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf(file_path, text):
    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter

    # Add text to PDF
    c.drawString(100, height - 100, text)
    c.showPage()
    c.save()

def print_file(file_path):
    if os.name == 'nt':  # Windows
        os.startfile(file_path, 'print')
    elif os.name == 'posix':  # macOS or Linux
        os.system(f'lpr {file_path}')

def on_print():
    # Get the text from the Text widget
    text = text_widget.get("1.0", tk.END).strip()
    
    if not text:
        messagebox.showerror("Error", "Text box is empty!")
        return
    
    # Ask user where to save the PDF
    file_path = filedialog.asksaveasfilename(defaultextension=".pdf",
                                             filetypes=[("PDF files", "*.pdf")])
    if file_path:
        create_pdf(file_path, text)
        print_file(file_path)

# Set up Tkinter window
root = tk.Tk()
root.title("Print Example")

text_widget = tk.Text(root, wrap='word', width=50, height=20)
text_widget.pack(padx=10, pady=10)

print_button = tk.Button(root, text="Print", command=on_print)
print_button.pack(pady=10)

root.mainloop()
