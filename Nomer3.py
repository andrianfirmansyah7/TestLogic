def countLetter(word):
    #Inisialisasi Variabel untuk Dictionary
    data = {}
    finaldata = {}
    
    #Melakukan Perulangan untuk Menghitung Jumlah Huruf dan Memasukkannya pada sebuah Dictionary
    for i in word:
        if i == " ":
            continue
        else:
            if i in data.keys():
                data[i] = data[i]+1
            else:
                data[i] = 1
    
    #Mengubah key pada dictionary menjadi 
    keyAlphabet = list(data.keys())
    x = len(keyAlphabet)
    
    #MMengurutkan huruf sesuai huruf Besar dan Kecil
    sortedKey = sorted(keyAlphabet, key=lambda a: (a.lower(), a))
    
    #Melakukan Input Value dari Dictionary yang Belum Berurutan Ke Dalam Dictionary Baru yang Telah Berurutan
    for key in sortedKey:
        finaldata[key] = data[key]
        
    return finaldata

print("Contoh Output")
print("Hello World :",countLetter("Hello World"))
print("Bismillah :",countLetter("Bismillah"))
print("MasyaAllah :",countLetter("MasyaAllah"))
print("Selamat Hari Selasa :",countLetter("Selamat Hari Selasa"))