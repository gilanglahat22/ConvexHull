from myConvexHull import *
from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt
import random

# Buat Visualisasi

#inisialisasi variabel global
convex_hull = myConvexHull()

# Fungsi untuk pewarnaan
def Warna(n):
    warna = ['m', 'g', 'y', 'k', 'b', 'c', 'w', 'r']
    if n > len(warna):
        for i in (range(n-len(warna))):
            r = random.random()
            g = random.random()
            b = random.random()
            warna.append((r, g, b))
    return warna

# Fungsi untuk memilih dataset
def load_datasets(nomor_dataset):
    if nomor_dataset == 1:
        data = datasets.load_iris()
    elif nomor_dataset == 2:
        data = datasets.load_wine()
    elif nomor_dataset == 3:
        data = datasets.load_breast_cancer()
    elif nomor_dataset == 4:
        data = datasets.load_diabetes()
    elif nomor_dataset == 5:
        data = datasets.load_digits()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['target'] = pd.DataFrame(data.target)
    return df, data

# Fungsi untuk menampilkan tabel dataset
def tampilkan_tabel_dataset(df):
    print(df.shape)
    print(df.head)

# Fungsi untuk menampilkan plot grafik
def tampilkan_plot_grafik(df, data):
    selesai = 0
    sumbu_x = int(input("Masukkan Kolom untuk sumbu-x : "))
    sumbu_y = int(input("Masukkan Kolom untuk sumbu-y : "))
    savefile = input("Masukkan nama file yang ingin disave : ")
    plt.figure(figsize = (10, 6))
    UkuranLabel = len(df['target'].unique())
    colors = Warna(UkuranLabel)
    plt.title(str(data.feature_names[sumbu_x])+" vs "+str(data.feature_names[sumbu_y]))
    plt.xlabel(data.feature_names[sumbu_x])
    plt.ylabel(data.feature_names[sumbu_y])
    print("Vertex dari convex hull adalah : ")
    for i in range(UkuranLabel):
        bucket = df[df['target'] == i]
        bucket = bucket.iloc[:,[sumbu_x,sumbu_y]].values
        convexhull = convex_hull(bucket)
        if convexhull is not None:
            plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i], color=colors[i])
            print(convexhull)
            convexhull = np.vstack([convexhull, convexhull[0]])
            plt.plot(convexhull[:,0], convexhull[:,1], colors[i])
            selesai += 1
    if selesai > 0:
        plt.legend()
        plt.savefig('output/' + savefile)
        plt.show()
