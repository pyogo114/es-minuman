import json

# 1. BACA basis pengetahuan dari file JSON (bukan hard code di program)
with open("aturan.json", "r", encoding="utf-8") as f:
    basis_pengetahuan = json.load(f)


# 2. MESIN INFERENSI: fungsi umum yang mencocokkan fakta dengan aturan
def cari_rekomendasi(fakta, basis):
    """
    fakta: dict berisi input pengguna, contoh {"cuaca": "panas", "suasana_hati": "santai"}
    basis: data aturan dari JSON
    """
    hasil = []

    # Loop pertama: periksa setiap minuman satu per satu
    for minuman in basis["minuman"]:
        syarat = minuman["syarat"]

        # Anggap semua syarat cocok dulu, sampai terbukti ada yang tidak cocok
        cocok = True

        # Loop kedua: periksa setiap syarat dari minuman ini
        # Contoh syarat = {"cuaca": "panas", "suasana_hati": "santai"}
        for kunci, nilai_syarat in syarat.items():
            # kunci      = "cuaca"   (lalu di iterasi berikutnya "suasana_hati")
            # nilai_syarat = "panas" (lalu "santai")

            # Ambil fakta dari pengguna untuk kunci ini
            nilai_fakta = fakta.get(kunci)

            # Bandingkan: apakah fakta pengguna sama dengan syarat?
            if nilai_fakta != nilai_syarat:
                # Ada satu syarat yang tidak cocok, berarti aturan ini gagal
                cocok = False
                break  # tidak perlu cek syarat lain, langsung keluar dari loop

        # Setelah semua syarat diperiksa, baru ambil keputusan
        if cocok:
            hasil.append(minuman)

    return hasil


# 3. ANTARMUKA PENGGUNA: tanya jawab sederhana
def tanya(pertanyaan, pilihan):
    print(f"\n{pertanyaan}")
    for i, p in enumerate(pilihan, 1):
        print(f"  {i}. {p}")
    while True:
        jawab = input("Pilih nomor: ").strip()
        if jawab.isdigit() and 1 <= int(jawab) <= len(pilihan):
            return pilihan[int(jawab) - 1]
        print("Input tidak valid, coba lagi.")


def main():
    print("=== Expert System Rekomendasi Minuman ===")

    cuaca = tanya("Bagaimana cuaca saat ini?", ["panas", "dingin", "hujan"])
    suasana = tanya("Bagaimana suasana hati Anda?", ["santai", "lelah", "sedih"])

    fakta = {"cuaca": cuaca, "suasana_hati": suasana}

    rekomendasi = cari_rekomendasi(fakta, basis_pengetahuan)

    print("\n--- HASIL ---")
    if rekomendasi:
        for r in rekomendasi:
            print(f"\nRekomendasi: {r['nama']}")
            print(f"Alasan     : {r['alasan']}")
    else:
        print("Maaf, belum ada rekomendasi untuk kombinasi tersebut.")


if __name__ == "__main__":
    main()