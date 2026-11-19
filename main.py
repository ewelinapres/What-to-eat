import tkinter as tk

def start_quiz():
    label_status.config(text="Quiz uruchomiony! (Kolejny krok: pytania)")

#Konfiguracja głównego okna
root = tk.Tk()
root.title("What to eat")
root.geometry("450x300")

#Nagłówek
label_title = tk.Label(root, text="What to eat", font=("Arial", 20, "bold"))
label_title.pack(pady=30)

#Opis
label_desc = tk.Label(
    root,
    text="Nie wiesz co dzisiaj zjeść?\nOdpowiedz na kilka krótkich pytań!",
    font = ("Arial", 12)
)
label_desc.pack(pady=10)

#Przycisk startu
btn_start = tk.Button(
    root,
    text = "Rozpocznij quiz",
    font = ("Arial", 12, "bold"),
    padx = 20,
    pady = 10,
    command = start_quiz,
)
btn_start.pack(pady=20)

#Etykieta testowa (potwierdzenie kliknięcia)
label_status = tk.Label(root, text="", font=("Arial", 10), fg = "green")
label_status.pack(pady=5)

root.mainloop()