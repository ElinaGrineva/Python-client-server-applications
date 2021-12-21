# Преобразовать слова «разработка», «администрирование», «protocol», «standard»
# из строкового представления в байтовое и выполнить обратное преобразование
# (используя методы encode и decode).

enc_str1 = 'разработка'
enc_str2 = 'администрирование'
enc_str3 = 'protocol'
enc_str4 = 'standard'

enc_str_bytes1 = enc_str1.encode('utf-8')
enc_str_bytes2 = enc_str2.encode('utf-8')
enc_str_bytes3 = enc_str3.encode('utf-8')
enc_str_bytes4 = enc_str4.encode('utf-8')

dec_str1 = enc_str_bytes1.decode('utf-8')
dec_str2 = enc_str_bytes2.decode('utf-8')
dec_str3 = enc_str_bytes3.decode('utf-8')
dec_str4 = enc_str_bytes4.decode('utf-8')

