import os
os.system('clear')
total = 0
banyak1 = 0#
banyak2 = 0#
banyak3 = 0#
banyak4 = 0#
rego1 = 0#
rego2 = 0#
rego3 = 0#
rego4 = 0#
ai = ['','',''], ['','',''], ['','',''], ['','','']##
print ('	##########################################')
print ('	#    Program Perhitungan Harga Barang    #')
print ('	##########################################\n')

name = str(raw_input('Masukan Jenis Pelanggan (t = Tetap)/(u = Umum) : '))
os.system('clear')
if name == ('u'):
	print ('Pembeli adalah Pelanggan Umum\n')
if name == ('t'):
	print ('Pembeli adalah Pelanggan Tetap\n')
print ('Kode barang :\n 1 = Motor Servo\n 2 = Arduino\n 3 = Sensor Jarak\n 4 = Sensor Suara')

def tabel():
	print '\n----------------------------------------------------------------------------------------------'
	print '|    Barang    |  Unit  |  Harga  | Diskon | Besar Diskon |   Harga Awal   |   Harga Akhir   |'
	print '----------------------------------------------------------------------------------------------'

while (True) :
	kode = int(input('Masukan kode barang : '))
	if kode == 1:
		nama1 = ('Motor Servo')##
		harga = 35000
		jumlah = int(input('jumlah yang ingin di beli : '))
		banyak1 += jumlah##
		if name == ('t'):
			sisa = jumlah % 5
			d_item = jumlah - sisa
			h_awal = d_item * harga
			diskon = d_item * harga * 10/100
			h_akhir = h_awal - diskon
			s_item = sisa * harga
			dibayar = s_item + h_akhir
			total = total + dibayar
			tabel()
			rego1 += dibayar#
			ai[0][0] = nama1##
			ai[0][1] = banyak1##
			ai[0][2] = rego1##
			if jumlah > 5 and sisa > 0 :	
				for line in [['Motor Servo', d_item , harga,  '10%', diskon, h_awal, h_akhir], [' Motor Servo', sisa, harga, 0, 0, s_item, s_item]]:
					print('{:>13} {:>8} {:>9} {:>9} {:>14} {:>14} {:>17} '.format(*line))
			if jumlah < 5 :
				for line in [[' Motor Servo', sisa, harga, 0, 0, s_item, s_item]]:
					print('{:>13} {:>8} {:>9} {:>9} {:>14} {:>14} {:>17} '.format(*line))
			if jumlah >= 5 and sisa == 0 :
				for line in [['Motor Servo', d_item , harga,  '10%', diskon, h_awal, h_akhir]]:
					print('{:>13} {:>8} {:>9} {:>9} {:>14} {:>14} {:>17} '.format(*line))
			print '---------------------------------------------------------------------------------------------+'
			for line in [['total            ', ' ', dibayar]]:
				print('{:>1} {:>50} {:21}'.format(*line))
		
		if name == ('u'):
			sisa = jumlah % 5
			d_item = jumlah - sisa
			h_awal = d_item * harga
			diskon = d_item * harga * 5/100
			h_akhir = h_awal - diskon
			s_item = sisa * harga
			dibayar = s_item + h_akhir
			total = total + dibayar
			tabel()
			rego1 += dibayar#
			ai[0][0] = nama1##
			ai[0][1] = banyak1##
			ai[0][2] = rego1##
			if jumlah > 5 and sisa > 0 :	
				for line in [['Motor Servo', d_item , harga,  '5%', diskon, h_awal, h_akhir], [' Motor Servo', sisa, harga, 0, 0, s_item, s_item]]:
					print('{:>13} {:>8} {:>9} {:>9} {:>14} {:>14} {:>17} '.format(*line))
			if jumlah < 5 :
				for line in [[' Motor Servo', sisa, harga, 0, 0, s_item, s_item]]:
					print('{:>13} {:>8} {:>9} {:>9} {:>14} {:>14} {:>17} '.format(*line))
			if jumlah >= 5 and sisa == 0 :
				for line in [['Motor Servo', d_item , harga,  '5%', diskon, h_awal, h_akhir]]:
					print('{:>13} {:>8} {:>9} {:>9} {:>14} {:>14} {:>17} '.format(*line))
			print '---------------------------------------------------------------------------------------------+'
			for line in [['total            ', ' ', dibayar]]:
				print('{:>1} {:>50} {:21}'.format(*line))
##########################################################
	if kode == 2:
		harga = 50000
		nama2 = ('Mktr Arduino')##
		jumlah = int(input('jumlah yang ingin di beli : '))
		banyak2 += jumlah##
		if name == ('t'):
			sisa = jumlah % 10
			d_item = jumlah - sisa
			h_awal = d_item * harga
			diskon = d_item * harga * 10/100
			h_akhir = h_awal - diskon
			s_item = sisa * harga
			dibayar = s_item + h_akhir
			total = total + dibayar
			tabel()
			rego2 += dibayar#
			ai[1][0] = nama2##
			ai[1][1] = banyak2##
			ai[1][2] = rego2##
			if jumlah > 10 and sisa > 0 :	
				for line in [['Mktr Arduino', d_item , harga,  '10%', diskon, h_awal, h_akhir], ['Mktr Arduino', sisa, harga, 0, 0, s_item, s_item]]:
					print('{:>13} {:>8} {:>9} {:>9} {:>14} {:>14} {:>17} '.format(*line))
			if jumlah < 10 :
				for line in [['Mktr Arduino', sisa, harga, 0, 0, s_item, s_item]]:
					print('{:>13} {:>8} {:>9} {:>9} {:>14} {:>14} {:>17} '.format(*line))
			if jumlah >= 10 and sisa == 0 :
				for line in [['Mktr Arduino', d_item , harga,  '10%', diskon, h_awal, h_akhir]]:
					print('{:>13} {:>8} {:>9} {:>9} {:>14} {:>14} {:>17} '.format(*line))
			print '---------------------------------------------------------------------------------------------+'
			for line in [['total            ', ' ', dibayar]]:
				print('{:>1} {:>50} {:21}'.format(*line))
		if name == ('u'):
			sisa = jumlah % 15
			d_item = jumlah - sisa
			h_awal = d_item * harga
			diskon = d_item * harga * 10/100
			h_akhir = h_awal - diskon
			s_item = sisa * harga
			dibayar = s_item + h_akhir
			total = total + dibayar
			tabel()
			rego2 += dibayar#
			ai[1][0] = nama2##
			ai[1][1] = banyak2##
			ai[1][2] = rego2##
			if jumlah > 15 and sisa > 0 :	
				for line in [['Mktr Arduino', d_item , harga,  '10%', diskon, h_awal, h_akhir], ['Mktr Arduino', sisa, harga, 0, 0, s_item, s_item]]:
					print('{:>13} {:>8} {:>9} {:>9} {:>14} {:>14} {:>17} '.format(*line))
			if jumlah < 15 :
				for line in [['Mktr Arduino', sisa, harga, 0, 0, s_item, s_item]]:
					print('{:>13} {:>8} {:>9} {:>9} {:>14} {:>14} {:>17} '.format(*line))
			if jumlah >= 15 and sisa == 0 :
				for line in [['Mktr Arduino', d_item , harga,  '10%', diskon, h_awal, h_akhir]]:
					print('{:>13} {:>8} {:>9} {:>9} {:>14} {:>14} {:>17} '.format(*line))
			print '---------------------------------------------------------------------------------------------+'
			for line in [['total            ', ' ', dibayar]]:
				print('{:>1} {:>50} {:21}'.format(*line))
##########################################################
	if kode == 3:
		harga = 30000
		nama3 = ('Sensor Jarak')
		jumlah = int(input('jumlah yang ingin di beli : '))
		banyak3 += jumlah##
		if name == ('t'):
			sisa = jumlah % 5
			d_item = jumlah - sisa
			h_awal = d_item * harga
			diskon = d_item * harga * 10/100
			h_akhir = h_awal - diskon
			s_item = sisa * harga
			dibayar = s_item + h_akhir
			total = total + dibayar
			tabel()
			rego3 += dibayar#
			ai[2][0] = nama3##
			ai[2][1] = banyak3##
			ai[2][2] = rego3##
			if jumlah > 5 and sisa > 0 :	
				for line in [['Sensor Jarak', d_item , harga,  '10%', diskon, h_awal, h_akhir], ['Sensor Jarak', sisa, harga, 0, 0, s_item, s_item]]:
					print('{:>13} {:>8} {:>9} {:>9} {:>14} {:>14} {:>17} '.format(*line))
			if jumlah < 5 :
				for line in [['Sensor Jarak', sisa, harga, 0, 0, s_item, s_item]]:
					print('{:>13} {:>8} {:>9} {:>9} {:>14} {:>14} {:>17} '.format(*line))
			if jumlah >= 5 and sisa == 0 :
				for line in [['Sensor Jarak', d_item , harga,  '10%', diskon, h_awal, h_akhir]]:
					print('{:>13} {:>8} {:>9} {:>9} {:>14} {:>14} {:>17} '.format(*line))
			print '---------------------------------------------------------------------------------------------+'
			for line in [['total            ', ' ', dibayar]]:
				print('{:>1} {:>50} {:21}'.format(*line))
		if name == ('u'):
			sisa = jumlah % 10
			d_item = jumlah - sisa
			h_awal = d_item * harga
			diskon = d_item * harga * 5/100
			h_akhir = h_awal - diskon
			s_item = sisa * harga
			dibayar = s_item + h_akhir
			total = total + dibayar
			tabel()
			rego3 += dibayar#
			ai[2][0] = nama3##
			ai[2][1] = banyak3##
			ai[2][2] = rego3##
			if jumlah > 10 and sisa > 0 :	
				for line in [['Sensor Jarak', d_item , harga,  '5%', diskon, h_awal, h_akhir], ['Sensor Jarak', sisa, harga, 0, 0, s_item, s_item]]:
					print('{:>13} {:>8} {:>9} {:>9} {:>14} {:>14} {:>17} '.format(*line))
			if jumlah < 10 :
				for line in [['Sensor Jarak', sisa, harga, 0, 0, s_item, s_item]]:
					print('{:>13} {:>8} {:>9} {:>9} {:>14} {:>14} {:>17} '.format(*line))
			if jumlah >= 10 and sisa == 0 :
				for line in [['Sensor Jarak', d_item , harga,  '5%', diskon, h_awal, h_akhir]]:
					print('{:>13} {:>8} {:>9} {:>9} {:>14} {:>14} {:>17} '.format(*line))
			print '---------------------------------------------------------------------------------------------+'
			for line in [['total            ', ' ', dibayar]]:
				print('{:>1} {:>50} {:21}'.format(*line))
##########################################################
	if kode == 4:
		harga = 45000
		nama4 = ('Sensor Suara')
		jumlah = int(input('jumlah yang ingin di beli : '))
		banyak4 += jumlah##
		if name == ('t'):
			sisa = jumlah % 10
			d_item = jumlah - sisa
			h_awal = d_item * harga
			diskon = d_item * harga * 20/100
			h_akhir = h_awal - diskon
			s_item = sisa * harga
			dibayar = s_item + h_akhir
			total = total + dibayar
			tabel()
			rego4 += dibayar#
			ai[3][0] = nama4##
			ai[3][1] = banyak4##
			ai[3][2] = rego4##
			if jumlah > 10 and sisa > 0 :	
				for line in [['Sensor Suara', d_item , harga,  '20%', diskon, h_awal, h_akhir], ['Sensor Suara', sisa, harga, 0, 0, s_item, s_item]]:
					print('{:>13} {:>8} {:>9} {:>9} {:>14} {:>14} {:>17} '.format(*line))
			if jumlah < 10 :
				for line in [['Sensor Suara', sisa, harga, 0, 0, s_item, s_item]]:
					print('{:>13} {:>8} {:>9} {:>9} {:>14} {:>14} {:>17} '.format(*line))
			if jumlah >= 10 and sisa == 0 :
				for line in [['Sensor Suara', d_item , harga,  '20%', diskon, h_awal, h_akhir]]:
					print('{:>13} {:>8} {:>9} {:>9} {:>14} {:>14} {:>17} '.format(*line))
			print '---------------------------------------------------------------------------------------------+'
			for line in [['total            ', ' ', dibayar]]:
				print('{:>1} {:>50} {:21}'.format(*line))
		if name == ('u'):
			sisa = jumlah % 10
			d_item = jumlah - sisa
			h_awal = d_item * harga
			diskon = d_item * harga * 10/100
			h_akhir = h_awal - diskon
			s_item = sisa * harga
			dibayar = s_item + h_akhir
			total = total + dibayar
			tabel()
			rego4 += dibayar#
			ai[3][0] = nama4##
			ai[3][1] = banyak4##
			ai[3][2] = rego4##
			if jumlah > 10 and sisa > 0 :	
				for line in [['Sensor Suara', d_item , harga,  '10%', diskon, h_awal, h_akhir], ['Sensor Suara', sisa, harga, 0, 0, s_item, s_item]]:
					print('{:>13} {:>8} {:>9} {:>9} {:>14} {:>14} {:>17} '.format(*line))
			if jumlah < 10 :
				for line in [['Sensor Suara', sisa, harga, 0, 0, s_item, s_item]]:
					print('{:>13} {:>8} {:>9} {:>9} {:>14} {:>14} {:>17} '.format(*line))
			if jumlah >= 10 and sisa == 0 :
				for line in [['Sensor Suara', d_item , harga,  '10%', diskon, h_awal, h_akhir]]:
					print('{:>13} {:>8} {:>9} {:>9} {:>14} {:>14} {:>17} '.format(*line))
			print '---------------------------------------------------------------------------------------------+'
			for line in [['total            ', ' ', dibayar]]:
				print('{:>1} {:>50} {:21}'.format(*line))
##########################################################
							
	ulang = str(raw_input('\nApakah ada transaksi berikutnya? (y = Ya)/(t = Tidak): '))
	if ulang == ('t'):
		print '\n				       -------------------------------------------------------'##
		print '				       |     Barang     |  Total Unit  |     Total Harga     |'##
		print '				       -------------------------------------------------------'## 
		for line in ai:##
			print('{:>54} {:>10} {:>24}'.format(*line))##
		print '---------------------------------------------------------------------------------------------++'
		for line in [['total keseluruhan', ' ', total]]:
			print('{:>1} {:>50} {:21}'.format(*line))
		bayar = int(input('Masukan uang yang dibayarkan 						   : '))
		kembalian = bayar-total
		print '----------------------------------------------------------------------------------------------'
		for line in [['Kembalian', ' ', kembalian]]:
			print('{:>1} {:>57} {:>22}'.format(*line))
		break
	if ulang == ('y'):
		continue
	else:
		break

