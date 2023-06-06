def sorting(data):
    length = len(data)
    
    for i in range(length-1):
        for j in range(length-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    
    return data

def sortData(data):
    #Inisialisasi List
    angka = []
    huruf = []
	
	#Perulangan untuk memisahkan data bertipe integer dan string
    for i in data:
        if type(i) is int:
            angka.append(i)
        else:
            huruf.append(i)
    
    #Melakukan Proses Sorting Data
    angka = sorting(angka)
    huruf = sorting(huruf)
    
    #Menggabungkan dua hasil Sorting dengan Mendahulukan Huruf
    sortedData = huruf + angka
    
    return sortedData

data = [12,9,30,"A","M",99,82,"J","N","B"]

print("Test Case")
print(data)
print(sortData(data))