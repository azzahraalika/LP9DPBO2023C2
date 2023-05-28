from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from tkinter import *
from PIL import ImageTk, Image

hunians = []
hunians.append(Apartemen("Choi Seungcheol", 2, 3, 10000000, "Apgujeong", "assets/image/apart.jpg"))
hunians.append(Rumah("Jeong Jaehyun", 5, 2, 500000000, "Gangnam", "assets/image/home.jpg"))
hunians.append(Indekos("Alika", "Taeyong", "4000000", "Hongdae", "assets/image/kos.jpg"))
hunians.append(Rumah("Na Jaemin", 1, 4, 900000000, "Busan", "assets/image/busan.jpg"))
hunians.append(Indekos("Alika", "Mark", "4000000", "Hongdae", "assets/image/kos.jpg"))

root = Tk()
root.title("Latihan Praktikum 9")

# membuat landing page 
landing = Label(root, text="SELAMAT DATANG!", padx=50, pady=50)
landing.pack(padx=50, pady=50)
# mengatur button untuk masuk ke halaman utama
page = Button(root, text="Masuk", command=lambda: home(), padx=5, pady=5, width= 10, height=1)
page.pack()

# fungsi untuk menampilkan detail dari tabel
def details(index):
    top = Toplevel()
    top.title("Detail " + hunians[index].get_jenis())

    d_frame = LabelFrame(top, text="Data Residen", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    # menampilkan penjelasan pada detail 
    d_summary = Label(d_frame, text="Summary\n" + hunians[index].get_detail() + hunians[index].get_summary() + "\n" + hunians[index].get_dokumen(), anchor="w", justify=LEFT).grid(row=0, column=0, sticky="w")

    # untuk insert foto pada detail 
    image = Image.open(hunians[index].get_foto())
    image = image.resize((200, 200)) 
    img = ImageTk.PhotoImage(image)
    photo_label = Label(d_frame, image=img)
    photo_label.grid(row=2, column=0, sticky="s")
    photo_label.image = img

# fungsi untuk menampilkan halaman utama
def home():
    root = Tk()
    root.title("Daftar Residen")

    frame = LabelFrame(root, text="Data Seluruh Residen", padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    opts = LabelFrame(root, padx=10, pady=10)
    opts.pack(padx=10, pady=10)

    b_add = Button(opts, text="Add Data", state="disabled")
    b_add.grid(row=0, column=0)

    b_exit = Button(opts, text="Exit", command=root.quit)
    b_exit.grid(row=0, column=1)

    for index, h in enumerate(hunians):
        idx = Label(frame, text=str(index+1), width=5, borderwidth=1, relief="solid")
        idx.grid(row=index, column=0)

        type = Label(frame, text=h.get_jenis(), width=15, borderwidth=1, relief="solid")
        type.grid(row=index, column=1)

        if h.get_jenis() != "Indekos": 
            name = Label(frame, text=" " + h.get_nama_pemilik(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)
        else:
            name = Label(frame, text=" " + h.get_nama_penghuni(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)

        b_detail = Button(frame, text="Details ", command=lambda index=index: details(index))
        b_detail.grid(row=index, column=3)


root.mainloop()
