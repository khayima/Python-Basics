#!/usr/bin/env python
# coding: utf-8

# # Python Basic (Function and IF-ELSE)

# # Number 1
# 

# In[35]:


hasil = []

def bilangan_prima(awal,akhir):
    for i in range (awal,akhir): #range nilai dari 1-100

        if i>1: #syarat ketentuan bilangan prima di atas 1 
            for j in range(2, i): #range nilai angka yang digunakan untuk menguji 'n' bilangan dari range 1 sampai bilangan itu sendiri.
                if i%j==0: #Formula menentukan apakah saat bilangan itu sendiri dibagi dengan angka-angka lain di bawah bilangan tersebut hingga dirinya sendiri akan habis terbagi?
                    break #Untuk menghentikan fungsi program saat ditemukan kondisi bilangan bisa habis dibagi selain dengan bilangan itu sendiri

            else:
                hasil.append(i) #menambahkan i yang termasuk bilangan prima ke dalam list 'hasil'
    print('List dari bilangan prima (1-100) : ', hasil) #Menampilkan bilangan prima (bilangan yang habis terbagi hanya dengan dirinya sendiri)

#Input nilai yang akan ditambahkan ke dalam fungsi
bilangan_prima(1,100)


# # Number 2

# In[2]:


faktor_nilai=[] #menyediakan list kosong untuk menampilkan faktor-faktor dari nilai input yang bukan bilangan prima

def angka_nonprima(nilai): #fungsi untuk angka nonprima
    for j in range (2, nilai): #range nilai angka yang digunakan untuk menguji 'n' bilangan dari range 1 sampai bilangan itu sendiri.
        if nilai%j==0: #Formula menentukan apakah saat bilangan itu sendiri dibagi dengan angka-angka lain di bawah bilangan tersebut hingga dirinya sendiri akan habis terbagi?
            faktor_nilai.append(j) #Menambahkan angka yang termasuk faktor dari nilai input ke dalam list faktor_nilai
    print('Faktor dari angka input: ' ,faktor_nilai) #print isi dari list faktor_nilai
            
angka_nonprima(int(input('Masukkan Angka: '))) #input nilai untuk suatu fungsi dan mengkonversi input tersebut dalam bentuk integer


# # Number 3
# 

# In[36]:


def lesser_of_two_evens(awal,akhir): #Fungsi untuk memasukkan 2 nilai
    
    if awal%2==0 and akhir%2==0: #Logika statement untuk menentukan apakah kedua bilangan tersebut termasuk even numbers
        if awal>akhir: #logika statement untuk memilih bilangan yang terbesar
            print(awal)
        else:
            print(akhir)
    else:              #logika statement untuk memilih bilangan yang terkecil
        if awal<akhir:
            print(awal)
        else:
            print(akhir)
            
#Masukkan 2 bilangan input sebagai awal dan akhir
lesser_of_two_evens(int(input('Masukkan nilai awal : ')), int(input('Masukkan nilai akhir: ')))


# # Number 4

# In[37]:


def animal_crackers(words): #Fungsi yang berisi susunan 2 kata
    
    hasil = words.split(' ')[0][0] #variabel yang berisi split huruf pertama kata pertama dari 2 suku kata input 
    print('Huruf pertama kata pertama: ',hasil)
    hasil1 = words.split(' ')[1][0] #variabel yang berisi split huruf pertama kata kedua dari 2 suku kata input
    print('Huruf pertama kata kedua: ',hasil1)
    if hasil == hasil1:             #Logika statement untuk check apakah antara (huruf pertama kata pertama) sama dengan (huruf pertama kata kedua)
        print('Output:',True)       #output nilai apabila statement benar
    else:
        print('Output: ', False)    #output nilai apabila statement salah
    
#Masukkan 2 kata
animal_crackers(str(input("Masukkan kata: ")))


# # Number 5

# In[31]:


def master_yoda(sentences):  #fungsi yang berisi kalimat (bebas tersusun dari beberapa suu kata)
    
    new_sentences = sentences.split(' ') #proses spliting untuk memisahkan kalimat ke beberapa suku kata ke dalam list
    new_sentences = list(reversed(new_sentences)) #proses untuk membalik masing-masing index dari list
    print(' '.join(new_sentences)) #Menggabungkan kata dalam reverse list menjadi kalimat
    
#input kalimat
master_yoda(input("Kalimat yang akan dibalik: ")) 


# In[ ]:





# In[ ]:




