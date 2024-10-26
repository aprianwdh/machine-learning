import tkinter as tk
from tkinter import messagebox

# Membuat jendela utama
root = tk.Tk()
root.title("To-Do List")
root.geometry("300x400")

# Daftar tugas
tasks = []

# Fungsi untuk memperbarui tampilan daftar tugas
def update_tasks():
    # Hapus semua item yang ada di listbox
    listbox_tasks.delete(0, tk.END)
    # Tambahkan setiap tugas dalam listbox
    for task in tasks:
        listbox_tasks.insert(tk.END, task)

# Fungsi untuk menambah tugas
def add_task():
    task = entry_task.get()
    if task:
        tasks.append(task)
        entry_task.delete(0, tk.END)
        update_tasks()
    else:
        messagebox.showwarning("Peringatan", "Tugas tidak boleh kosong!")

# Fungsi untuk menghapus tugas yang dipilih
def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        tasks.pop(selected_task_index)
        update_tasks()
    except IndexError:
        messagebox.showwarning("Peringatan", "Pilih tugas yang ingin dihapus!")

# Komponen GUI
frame = tk.Frame(root)
frame.pack(pady=10)

listbox_tasks = tk.Listbox(
    frame, width=25, height=10, font=("Arial", 12), selectmode=tk.SINGLE
)
listbox_tasks.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar_tasks = tk.Scrollbar(frame)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=26, font=("Arial", 12))
entry_task.pack(pady=10)

button_add_task = tk.Button(root, text="Tambah Tugas", width=15, command=add_task)
button_add_task.pack(pady=5)

button_delete_task = tk.Button(root, text="Hapus Tugas", width=15, command=delete_task)
button_delete_task.pack(pady=5)

# Menjalankan aplikasi
root.mainloop()
