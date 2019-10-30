name=input("Enter Name:")
print("Welcome"+ name +"Hadi Adam Asmaca Oynayalım")


tahmin_metni=""

can=10
gizliKelime="Türkiye"

while can>0:

	char_left=0


	for char in gizliKelime:
		if char in tahmin_metni:
			print(char)
		else:
			print("*")
			char_left+=1

	if char_left==0:
		print("Kazandınız")
		break		



	tahmin=input("Bir Harf Tahmin Et : ")
	tahmin_metni+=tahmin

	if tahmin not in gizliKelime:
		can-=1
		print("Yanlış Tahmin")
		print(f" {can}'ınınız Kaldı")

		if can==0:
			print("Öldün ÇIK :D ")

 




