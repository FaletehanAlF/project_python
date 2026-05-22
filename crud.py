def main():
    tasks = []

    while True:
        print("\n===== To-Do List =====")
        print("1. Tambah Tugas")
        print("2. Lihat Tugas")
        print("3. Hapus Tugas")
        print("4. Keluar")

        choice = input("Pilih opsi (1-4): ")

        
        if choice == '1':
            n_tasks = int(input("\nBerapa banyak tugas yang ingin ditambahkan? "))

            for i in range(n_tasks):
                task = input("Masukkan tugas: ")
                tasks.append(task)
                print("Tugas berhasil ditambahkan!")

        
        elif choice == '2':
            print("\n===== Daftar Tugas =====")

            if not tasks:
                print("Belum ada tugas.")
            else:
                for index, task in enumerate(tasks):
                    print(f"{index + 1}. {task}")

        
        elif choice == '3':
            print("\n===== Hapus Tugas =====")

            if not tasks:
                print("Tidak ada tugas untuk dihapus.")
            else:
                for index, task in enumerate(tasks):
                    print(f"{index + 1}. {task}")

                task_index = int(input("\nMasukkan nomor tugas yang ingin dihapus: ")) - 1

                if 0 <= task_index < len(tasks):
                    removed_task = tasks.pop(task_index)
                    print(f"Tugas '{removed_task}' berhasil dihapus!")
                else:
                    print("Nomor tugas tidak valid.")

        
        elif choice == '4':
            print("\nProgram selesai. Terima kasih!")
            break

        else:
            print("\nPilihan tidak valid. Coba lagi.")


if __name__ == "__main__":
    main()