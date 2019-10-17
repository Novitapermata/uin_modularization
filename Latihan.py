nama = 'Novita Permata Sari'
program = 'usaha'

print(f'program {program} oleh {nama}')

def hitung_usaha(gaya, jarak):
    usaha = gaya * jarak
    print(f'gaya = {gaya * 10}newton menempuh jarak = {jarak * 100}meter')
    print(f'sehingga usaha = {usaha} joule')
    return usaha

# gaya = 10
# jarak = 100
usaha = hitung_usaha(10, 100)
usaha = hitung_usaha(15, 150)