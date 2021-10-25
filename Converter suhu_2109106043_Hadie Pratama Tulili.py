import os

def konversiSuhu(suhu):
   derajat = int(suhu[:- 1])
   inputan = suhu[-1]
         
   if inputan.upper() == "F":
     hasil1 = float((derajat - 32) * 5 / 9)
     hasil2 = float(((derajat - 32) * 5 / 9) + 273.15)
     hasil3 = float(4/9 * (derajat-32))
     jenis0 = "Fahrenheit"
     jenis1 = "Celsius"
     jenis2 = "Kelvin"
     jenis3 = "Reamur"
     print(derajat,jenis0,"=","{:.1f}".format(hasil1),jenis1)
     print(derajat,jenis0,"=","{:.1f}".format(hasil2),jenis2)
     print(derajat,jenis0,"=","{:.1f}".format(hasil3),jenis3)

   elif inputan.upper() == "K":
     hasil1 = float(derajat - 273.15)
     hasil2 = float(((derajat - 273.15) * 9 / 5)+32)
     hasil3 = float(4/5 * (derajat-273))
     jenis0 = "Kelvin"
     jenis1 = "Celcius"
     jenis2 = "Fahrenheit"
     jenis3 = "Reamur"
     print(derajat,jenis0,"=","{:.1f}".format(hasil1),jenis1)
     print(derajat,jenis0,"=","{:.1f}".format(hasil2),jenis2)
     print(derajat,jenis0,"=","{:.1f}".format(hasil3),jenis3)
     
   elif inputan.upper() == "R":
     hasil1 = float((5/4) * derajat)
     hasil2 = float((9/4 * derajat) + 32)
     hasil3 = float((5/4 * derajat) + 273)
     jenis0 = "Reamur"
     jenis1 = "Celcius"
     jenis2 = "Fahrenheit"
     jenis3 = "Kelvin"
     print(derajat,jenis0,"=","{:.1f}".format(hasil1),jenis1)
     print(derajat,jenis0,"=","{:.1f}".format(hasil2),jenis2)
     print(derajat,jenis0,"=","{:.1f}".format(hasil3),jenis3)
     
   else:
      print("\nInputan tidak sesuai!! Perhatikan Penulisan Input (Pada program ini tidak memakai inputan Celcius)\n")


i=0
os.system('cls')
print("=======================================\nProgram Konversi Satuan Suhu ke Celcius\n=======================================")
while i==0:
   temp = input("\nSilahkan masukan suhu (Misal: 37F, 45R, 76K) -> ")
   konversiSuhu(temp)

   lagi=int(input("Mau menghitung kembali ? (1=ya & 0=tidak) -> "))
   if(lagi==1):
      i=0
   elif(lagi!=1):
      os.system('cls')
      print("================================================\nTerimakasih telah menggunakan program ini :)\nSemoga harimu menyenangkan!\n================================================")
      i=1