from myConvexHull import *
from Visualisasi import *

# Print Logo
def printlogo():
    print("[]=========================================================================================[]")
    print("||    _ _              _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _       _ _ _ _ _ _ _ _ _   ||")
    print("||   /   |            |   \     __ _|   |    _ _ _ _|     \     \     /     |     __ _ _|  ||")
    print("||  /   /     _ __     \   \   /_ __    |   |  /   _ _ _   \     \_ _/      |    /_ _ __   ||")
    print("||  \   \    /    \    /   /        |   |   | /   /     \   \               |           |  ||")
    print("||   \   \  /  /\  \  /   /   _ _ __|   |   | \   \_ _ _/   / |\       /|   |    _ _ _ _|  ||")
    print("||    \   \/  /__\  \/   /    \_ _ _    |_ _|_ \_ __       /  | \_ _ _/ |   |    \_ _ __   ||")
    print("||     \_ _ _ _ _ _ _ __/_ _ _ _ _ _|_ _ _ _ _|_ _ _|_ _ _/_ _|         |_ _|__ _ _ _ _ |  ||")
    print("||                                 _ _ _ _ _ ___ _ _ _ _                                   ||")
    print("||                                |_ __    _ __|        \                                  ||")
    print("||                                     |  |  /    _ _    \                                 ||")
    print("||                                     |  | /    /   \    \                                ||")
    print("||                                     |  | \    \_ _/    /                                ||")
    print("||                                     |  |  \           /                                 ||")
    print("||                                     |__|   \ _ _ _ __/                                  ||")
    print("||   _ _ _ _ _ _ _ _ _ _ _      _ _ _           _ _ _ _ _ _ _        _ _ _                 ||")
    print("||  |    _ _ _|      \    \    |   |  \        /    /  _ _ _ |\     /    /                 ||")
    print("||  |   |   /   _ _   \    \   |   |   \      /    /  /_ _\__  \_ _/    /                  ||")
    print("||  |   |  /   /   \   \    \  |   |    \    /    /          |  _ _    /                   ||")
    print("||  |   |  \   \_ _/   /     \ |   |\    \_ /    /     _ _ __| /   \   \                   ||")
    print("||  |   |_ _\_        /       \|   | \          /     \_ _/__ /     \   \                  ||")
    print("||  |_ _ _ _ _|_ _ _ /|_ _|\_ _ _ _|  \_ _ _ __/_ _ _ _ _ _ _|       \_ _\                 ||")
    print("||                                              _ __      _ _ _ _       _ _ _ _ _ _        ||")
    print("||                                             |    |    |   |   |     |   |   |   |       ||")
    print("||                                             |    |    |   |   |     |   |   |   |       ||")
    print("||                                             |    |_ __|   |   |     |   |   |   |       ||")
    print("||                                             |     _ __    |   |     |   |   |   |       ||")
    print("||                                             |    |    |   |   |_ _ _|   |   |   |       ||")
    print("||                                             |    |    |   |             |   |_ _|_ _ _  ||")
    print("||                                             |_ __|    |_ _|_ _ _ _ _ _ _|_ _ _ _ _|_ _| ||")
    print("||                _ _ __ __ _ _ _ _ _ __ _ _         _ _ _ _ _ __ _ _ _ _ _                ||")
    print("||               /    _ _ _|       \    |   \       /    /  _ _ _|   _ _   |               ||")
    print("||              /    /   /    _ _   \   |    \     /    /  /_ _ _   |_ _|  |               ||")
    print("||              \    \  /    /   \   \  |\    \   /    /         |        /                ||")
    print("||               \    \ \    \_ _/   /  | \    \_/    /    _ _ __|   |\   \                ||")
    print("||            __ _\    \ \          /   |_ \_ __     /     \_ _ _    | \   \               ||")
    print("||           |_ _ _ _ _/  \_ _ _ _ /_ _ _ _ _ _|_ _ /_ _ _ _ _ _ |_ _|  \_ _\              ||")
    print("||                                                                                         ||")
    print("[]=========================================================================================[]")
    print("||>>>>>>>>>>>>>>>>>>>> Dibuat oleh Muhammad Gilang Ramadhan (13520137) <<<<<<<<<<<<<<<<<<<<||")
    print("||>>>>>>>>>>>>>>>>>>>>>>>> Tugas Kecil 2 IF2211 Strategi Algoritma <<<<<<<<<<<<<<<<<<<<<<<<||")
    print("[]=========================================================================================[]")

def logo_penutup():
    print("[]=========================================================================================[]")
    print("||              _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _         _ __ _ _ _ _ _ __              ||")
    print("||             |_ _   _ _|  _ _ _|  _ _  |   |     \       /    |     _ _    |             ||")
    print("||                 |  |    /_ _ _  |_ _| |   |      \     /     |    /_ _\   |             ||")
    print("||                 |  |          |      /|   |       \_ _/      |    _ __    |             ||")
    print("||                 |  |     _ _ _| |\   \|   |   |\        /|   |   |    |   |             ||")
    print("||                 |  |     \ _ __ | \   \   |   | \ _ _ _/ |   |   |    |   |             ||")
    print("||                 |__|_ _ _ _ _ _||  \_ _\ _|_ _|          |_ _|_ _|    |_ _|             ||")
    print("||                     _ _   _ __ _ _ __ __  _ _ _ _ _ _ _ _       _ _                     ||")
    print("||                    |   | /   /   _ _    |/     _ _ _||   |     |   |                    ||")
    print("||                    |   |/   /   /_ _\   |\    /  |   |   |_ _ _|   |                    ||")
    print("||                    |       /    _ __    | \   \  |   |             |                    ||")
    print("||                    |       \   |    |   |  \   \ |   |    _ _ _    |                    ||")
    print("||                    |   |\   \  |    |   |_ _\   \|   |   |     |   |                    ||")
    print("||                    |_ _| \_ _\_|    |_ _|_ _ _ _/|_ _|_ _|     |_ _|                    ||")
    print("||                                                                                         ||")
    print("[]=========================================================================================[]")

def MainProgram():
    printlogo()
    print()
    print("---------------------------------------------------------------------------------------------")
    print()
    print("[]========================================= Menu ==========================================[]")
    print("||                                                                                         ||")
    print("||                              Berikut Dataset yang tersedia :                            ||")
    print("||                                 1. Dataset Iris                                         ||")
    print("||                                 2. Dataset Wine                                         ||")
    print("||                                 3. Dataset Breast_Cancer                                ||")
    print("||                                 4. Dataset Diabetes                                     ||")
    print("||                                 5. Dataset Digits                                       ||")
    print("||                                                                                         ||")
    print("[]=========================================================================================[]")
    print("||                           >> Pilih 0 jika ingin keluar program                          ||")
    print("[]=========================================================================================[]")
    command = int(input("Masukkan Command yang diinginkan : "))
    while command != 0:
        if command == 1 or command == 2 or command == 3 or command == 4 or command == 5:
            df, data = load_datasets(command)
            tampilkan_tabel_dataset(df)
            tampilkan_plot_grafik(df, data)
        else:
            print("Maaf masukkan tidak dikenali")
        print("---------------------------------------------------------------------------------------------")
        command = int(input("Masukkan Kembali Command Anda : "))
    logo_penutup()
    exit()
if __name__ == "__main__":
    MainProgram()
