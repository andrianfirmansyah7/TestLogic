def pattern_count(word, pattern):
    #Menghitung Panjang Dari Setiap Variabel dan inisialisasi variabel count
    a = len(word)
    b = len(pattern)
    count = 0
    
    #Jika panjang data lebih dari  100
    if a and b > 100:
        return "Kata melebihi 100 karakter"
    #Jika panjang data kurang dari sama dengan 00    
    else:
        #jika panjang b lebih dari 0
        if b > 0:
            for i in range(a):
                #Jika nilai i+b-1 lebih kecil dari a
                if(i+b-1 < a):
                    if word[i:i+b] == pattern:
                        count +=1
                else:
                    break
        
    return count

print("Test Case")
print("Palindrom, ind :",pattern_count("Palindrom","ind"))
print("abakadabra, ab :",pattern_count("abakadabra","ab"))
print("hello, '' :",pattern_count("hello",""))
print("ababab, aba :",pattern_count("ababab","aba"))
print("aaaaaa, aa :",pattern_count("aaaaaa","aa"))
print("hell, hello :",pattern_count("hell","hello"))