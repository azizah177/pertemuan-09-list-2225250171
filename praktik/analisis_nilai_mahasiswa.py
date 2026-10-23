
# Praktik: Analisis Nilai Mahasiswa

def rata_rata(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)


def nilai_lulus(data, batas=60):
    lulus = []
    for x in data:
        if x >= batas:
            lulus.append(x)
    return lulus


nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]

banyak = len(nilai)
total = sum(nilai)
rata = rata_rata(nilai)
minimum = min(nilai)
maksimum = max(nilai)

lulus = nilai_lulus(nilai)
jumlah_lulus = len(lulus)
jumlah_belum_lulus = banyak - jumlah_lulus

print("=== ANALISIS NILAI MAHASISWA ===")
print(f"Data nilai          = {nilai}")
print(f"Banyak data         = {banyak}")
print(f"Total nilai         = {total}")
print(f"Rata-rata           = {rata:.2f}")
print(f"Nilai minimum       = {minimum}")
print(f"Nilai maksimum      = {maksimum}")
print(f"Nilai lulus         = {lulus}")
print(f"Jumlah mahasiswa lulus = {jumlah_lulus}")
print(f"Jumlah belum lulus  = {jumlah_belum_lulus}")
