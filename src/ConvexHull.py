# NAMA  : Muhammad Gilang Ramadhan
# NIM   : 13520137
# TUCIL 2 IF2211 Strategi Algoritma
# SOLVE CONVEX HULL PROBLEM WITH DIVIDE AND CONQUER STRATEGY

import numpy as np

# Fungsi yang mengembalikan cross product dari koordinat ke segmen garis
# Sekaligus menghitung jarak dari koordinat ke garis   
def Menghitung_jarak(mulai, selesai, koordinat, eps=1e-8):
    jarak = np.cross(selesai-mulai,koordinat-mulai)/(np.linalg.norm(selesai-mulai)+eps)
    return jarak

# Fungsi untuk membagi dua set of koordinat menjadi dua daerah
def partisi_setOfkoordinat_manjadiDua(mulai, selesai, array_of_koordinat):
    # Jika koordinat is None atau < 1
    if array_of_koordinat is None or array_of_koordinat.shape[0] < 1:
        return None, None
    
    # Jika tidak kosong atau < 1
    temp1 = [] 
    temp2 = []
    for koordinat in array_of_koordinat:
        jarak = Menghitung_jarak(mulai, selesai, koordinat)
        if jarak > 0:
            temp1.append(koordinat)
        else:
            temp2.append(koordinat) 
            
    # Mengubah dari bentuk koordinat dari temp1 dan temp2 menjadi bentuk array of numpy
    if len(temp1):
        temp1 = np.vstack(temp1) 
    else: 
        temp1 = None
    if len(temp2):
        temp2 = np.vstack(temp2)
    else:
        temp2 = None
    return temp1, temp2

# Fungsi untuk mempartisi satu set of koordinat menjadi 2 set of koordinat yang berbentuk segitiga 
def Partisi_Segitiga(Array_of_koordinat, Vertex1, Vertex2, Vertex3):
    # Jika array of koordinat is None
    if Array_of_koordinat is None:
        return None, None
    
    # Mencari di sisi mana titik tersebut berada dengan cross product
    temp1 = []
    temp2 = []
    for koordinat in Array_of_koordinat:
        jarakPC = Menghitung_jarak(Vertex1, Vertex2, koordinat)
        jarakCQ = Menghitung_jarak(Vertex2, Vertex3, koordinat)
        if jarakPC > 0 and jarakCQ < 0:
            temp1.append(koordinat)
        elif jarakPC < 0 and jarakCQ > 0:
            temp2.append(koordinat)
    
    # Mengubah dari bentuk koordinat dari temp1 dan temp2 menjadi bentuk array of numpy
    if len(temp1):
        temp1 = np.vstack(temp1) 
    else: 
        temp1 = None
    if len(temp2):
        temp2 = np.vstack(temp2)
    else:
        temp2 = None
    return temp1, temp2  

# Fungsi untuk mensorting vertices pada clockwise dengan berdasarkan sudutnya
# Yaitu antara sumbu x dan vektor yang menuju center dari koordinat
def CLOCK_SORT(koordinat):
    absis = koordinat[:,0].mean() 
    ordinat = koordinat[:,1].mean()
    theta = np.arctan2(koordinat[:,1] - ordinat, koordinat[:,0] - absis)
    indeks = np.argsort(theta)
    koordinat = koordinat[indeks]
    return koordinat

# Fungsi yang menghasilkan array of koordinat yang merupakan convex hull yang dihasilkan menggunakan quick hull
# Quick hull merupakan salah satu cara untuk mencari convex hull dengan pendekatan divide and conquer strategy
class ConvexHull:
    def __init__(self):
        self.array_of_koordinat = None
        self.convext_hull = []

    def reset(self):
        self.array_of_koordinat = None
        self.convext_hull = []

    def forward(self, koordinat_set):
        if koordinat_set is None or len(koordinat_set) < 3:
            print("Convex Hull yang ditemukan tidak valid! Mohon sediakan lebih dari 3 array of koordinat yang unik")
            return None
        self.reset()          
        # Menghilangkan elemen yang duplicate
        self.array_of_koordinat = np.unique(koordinat_set, axis=0)
        return self._QuickHull()
    
    def __call__(self, koordinat_set):
        return self.forward(koordinat_set)
    
    def isInside(self, array_of_koordinat):
        if len(self.convext_hull) == 0:
            print("Mohon setidaknya build 1 Convex Hull")
            return None
        Hasil = []   
        for koordinat in array_of_koordinat:
            Hasil.append(self._isDidalam(koordinat))
        Hasil = np.asarray(Hasil)
        return Hasil

    def _QuickHull(self):        
        # sort the data by x-axis, then by y-axis
        self.array_of_koordinat = self.array_of_koordinat[np.lexsort(np.transpose(self.array_of_koordinat)[::-1])]
        # Mencari left-most of koordinat dan right-most of koordinat
        left_most, right_most = self.array_of_koordinat[0], self.array_of_koordinat[-1]
        # Mendapatkan rest of array_of_koordinat 
        self.array_of_koordinat = self.array_of_koordinat[1:-1]
        #Menambahkan left-most koordinat ke dalam output 
        self.convext_hull.append(left_most) 
        #Menambahkan right-most koordinat ke dalam output
        self.convext_hull.append(right_most)

        self.right_array_of_koordinat, self.left_array_of_koordinat = partisi_setOfkoordinat_manjadiDua(left_most, right_most, self.array_of_koordinat)

        self._Mencarihull(self.right_array_of_koordinat, left_most, right_most)
        self._Mencarihull(self.left_array_of_koordinat, right_most, left_most)

        self.convext_hull = np.stack(self.convext_hull)
        self.convext_hull = CLOCK_SORT(self.convext_hull)
        if self.convext_hull.shape[0] >= 3:
            return self.convext_hull
        else:
            try:
                raise Exception("Array of koordinat yang ditemukan tidak cukup untuk convex hull. Mohon cek lagi input anda!")
            except Exception as tipe:
                print(type(tipe))
                print(tipe.args) 

    def _Mencarihull(self, array_of_koordinat, Vertex1, Vertex2):
        if array_of_koordinat is None:
            return None
        jarak = 0.0
        koordinat_sekarang = None 
        indeks = None
        for i, koordinat in enumerate(array_of_koordinat):
            jarak_sekarang = abs(Menghitung_jarak(Vertex1, Vertex2, koordinat))
            # Mencari jarak yang berjarak maksimum dari PQ yang berasal dari array_of_koordinat
            if jarak_sekarang > jarak:
                koordinat_sekarang = koordinat
                indeks = i
                jarak = jarak_sekarang
        if koordinat_sekarang is None:
            try:
                raise Exception("input array of koordinat berada di line yang sama. Tidak ada convex hull yang ditemukan!")
            except Exception as inst:
                print(type(inst))
                print(inst.args) 
                return None
        else:
            self.convext_hull.append(koordinat_sekarang)
            # Delete koordinat sekarang dari array of koordinat yang original
            array_of_koordinat = np.delete(array_of_koordinat, indeks, axis=0)
        
        # mereturn hasil partisi segitiga ke temp1 dan temp2   
        temp1, temp2 = Partisi_Segitiga(array_of_koordinat, Vertex1, koordinat_sekarang, Vertex2)
        self._Mencarihull(temp1, Vertex1, koordinat_sekarang)
        self._Mencarihull(temp2, koordinat_sekarang, Vertex2)
    
    def _isDidalam(self, koordinat):
        for i in range(self.convext_hull.shape[0]-1):
            mulai = self.convext_hull[i] 
            selesai = self.convext_hull[i+1]
            if Menghitung_jarak(mulai, selesai, koordinat) < 0:
                return False
        return True