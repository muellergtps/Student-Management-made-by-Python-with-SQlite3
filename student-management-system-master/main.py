import os

def show_menu() -> None:
    menus: list = ["Insert data", "Remove data", "View data"]
    print("0. Keluar")
    for i in range(len(menus)):
        print(f"{i+1}. {menus[i]}")

def clear_data() -> None:
    with open("local/data.db", "w") as local_data:
        local_data.write("")
        local_data.close()

def write_data(data: str, appendNewLine: bool = True) -> None:
    with open("local/data.db", "a+") as local_data:
        local_data.write(f"{data}\n")
        local_data.close()

def get_data() -> list:
    with open("local/data.db", "r") as local_data:
        return [data for data in local_data.readlines()]

def insert_data() -> None:
    while True:
        os.system("cls")
        print("Masukkan data dengan tepat!, ketik '-BACK-' untuk kembali!")
        nama = str(input("Nama: "))
        if nama == "-BACK-":
            break
        nama = nama.title()
        kelas = int(input("Kelas: "))
        asal_sekolah = str(input("Asal sekolah: ")).capitalize()
        kota = str(input("Kota: ")).title()
        provinsi = str(input("Provinsi: ")).title()

        formatted_user_input = f"{nama}, {kelas}, {asal_sekolah}, {kota}, {provinsi}"

        # Check kalo ada data yang sama
        data_get = get_data()
        data_sama = False
        for data in data_get:
            s_data = data.split(",")

            # DEBUG
            # for i in range(len(s_data)):
            #     if i == len(s_data) - 1: print(f"data check {i}: {s_data[i][1:-1]}, len: {s_data[i][1:-1].__len__()}")
            #     else: 
            #         if i == 0: print(f"data check {i}: {s_data[i]}, len: {s_data[i].__len__()}")
            #         else: print(f"data check {i}: {s_data[i][1:]}, len: {s_data[i][1:].__len__()}")

            if s_data[0] == nama and int(s_data[1][1:]) == kelas and s_data[2][1:] == asal_sekolah and s_data[3][1:] == kota and s_data[4][1:-1] == provinsi:
                print("Data telah tersedia, data gagal ditambahkan!")
                data_sama = True
                break

        if not data_sama: 
            write_data(formatted_user_input)
            print("Data telah ditambahkan")
        if input(f"\nApakah anda ingin menambahkan data {'baru' if not data_sama else 'yang lain'}? [y/n]: ") == "n":
            break

def remove_data() -> None:
    while True:
        os.system("cls")
        data_get = get_data()
        
        # Nampilin data yang ada di database
        print("Data yang tersedia: ")
        for i in range(len(data_get)):
            print(f"{i+1}. {data_get[i][:-1]}")

        # menghapus data yang dipilih
        urutan_data_terpilih = int(input("\nKetik 0 untuk kembali\nPilihan> "))
        if urutan_data_terpilih == 0:
            break
        print(f"\n{data_get[urutan_data_terpilih - 1]}")
        if input("Apakah anda yakin akan menghapus data tersebut? [y/n]: ") == "y":
            # proses hapus data lokal
            selected_data: list = []
            for data in data_get:
                if data == data_get[urutan_data_terpilih - 1]:
                    continue
                selected_data.append(data)

            # menulis ulang data ke database lokal
            clear_data()
            [write_data(data[:-1]) for data in selected_data]
            print("Data telah terhapus!")
        if input("\nApakah anda ingin menghapus data lainnnya? [y/n]: ") == "n":
            break

def view_data() -> None:
    while True:
        os.system("cls")
        data_get = get_data()
        if len(data_get) is not 0: 
            print("Data tersedia: ")
            for i in range(len(data_get)):
                print(f"{i + 1}. {data_get[i][:-1]}")
        else:
            print("Data kosong!")

        if input("\nkemabali ke menu? [y/n]: ") == "y":
            break

def process_user_input(inp: int) -> None:
    os.system("cls")
    if inp == 0 or inp == 99: exit(0)
    elif inp == 1: insert_data()
    elif inp == 2: remove_data()
    elif inp == 3: view_data()
    else: print("input salah!")

if __name__ == '__main__':
    while True:
        os.system("cls")
        print("Welcome to Student Management!")
        show_menu()
        process_user_input(int(input("\nOpsi> ")))
    
    