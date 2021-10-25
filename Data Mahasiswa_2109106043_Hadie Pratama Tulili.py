import os
import sys

class Mahasiswa:
        Nim=''
        Nama=''

pilih = 0
dataMahasiswa = []

def menu():
	os.system('cls')
	print("============================\nMenu Program Data Mahasiswa\n============================")
	print("1. Input Data Mahasiswa")
	print("2. Tampilkan Data Mahasiswa")
	print("3. Update Data Mahasiswa")
	print("4. Hapus Data Mahasiswa")
	print("5. Keluar dari program")
	pilih = int(input("Masukkan pilihan anda : "))
	if pilih == 1 :
		pilih1()
		menu()
	elif pilih == 2:
		tampil()
		input("Kembali ke menu utama")
		menu()
	elif pilih == 3:
		index_update=-1
		tampil()
		id_edit = int(input("Input Nim yang akan di update ")) 
		for a in range(0, len(dataMahasiswa)): 
			if id_edit == dataMahasiswa[a].nim: 
					index_update = a 
					break 
		if(index_update > -1): 
			print("INPUT DATA YANG INGIN DI UPDATE ") 
			mahasiswa = Mahasiswa() 
			mahasiswa.nim = (int(input("Masukkan Nim : "))) 
			mahasiswa.nama = (input("masukkan Nama Mahasiswa : "))
			mahasiswa.fakultas = (str(input("Masukkan Nama fakultas Mahasiswa : ")))
			mahasiswa.prodi = (str(input("Masukkan Nama prodi Mahasiswa : ")))
			mahasiswa.ip = (input("Masukan Ip Mahasiswa : "))
			dataMahasiswa[index_update] = mahasiswa 
			print("Berhasil update data mahasiswa") 
		else : print("Nim tidak ditemukan") 
		input("Kembali menu utama") 
		menu()
	elif pilih == 4:
                os.system('cls')
                tampil()
                id_hapus = int(input("Input Nim yang akan di hapus : "))
                for data in dataMahasiswa:
                    if data.nim == id_hapus:
                         dataMahasiswa.remove(data)
                    else :
                         print("Data tidak di temukan")
                print("DATA MAHASISWA ")
                for data in dataMahasiswa:
                    print("Nim : "+str(data.nim))
                    print("Nama  : "+str(data.nama))
                input("kembali menu utama")
                menu()
	elif pilih == 5 :
		os.system('cls')
		print("================================================\nTerimakasih telah menggunakan program ini :)\nSemoga harimu menyenangkan!\n================================================")
		sys.exit()

def tampil():
	os.system('cls');
	print("DATA MAHASISWA")
	for data in dataMahasiswa:
		print("Nim : "+str(data.nim)) 
		print("Nama : "+str(data.nama)) 
		print("Fakultas : "+str(data.fakultas))
		print("Prodi : " +str(data.prodi))
		print("Ip : " +str(data.ip))
		print("===================")

def pilih1():
	ulang = 'Y'
	while ulang in('y', 'Y'):
		os.system('cls')
		mahasiswaBaru = Mahasiswa() 
		print("INPUT DATA MAHASISWA ") 
		mahasiswaBaru.nim = (int(input("Masukkan Nim Mahasiswa : "))) 
		mahasiswaBaru.nama = (str(input("Masukkan Nama Mahasiswa : ")))
		mahasiswaBaru.fakultas = (str(input("Masukkan Nama fakultas Mahasiswa : ")))
		mahasiswaBaru.prodi = (str(input("Masukkan Nama prodi Mahasiswa : ")))
		mahasiswaBaru.ip = (input("Masukkan Ip mahasiswa : "))
		dataMahasiswa.append(mahasiswaBaru) 
		ulang = input("Data Mahasiswa telah berhasil disimpan!\nApakah Anda Ingin Mengulang (Y/ T)?")		

menu()