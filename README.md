# Expert System Rekomendasi Minuman

Sistem pakar sederhana berbasis Python yang merekomendasikan minuman berdasarkan kondisi cuaca dan suasana hati pengguna.

## Cara Kerja

Program menggunakan pendekatan **forward chaining**: fakta dari pengguna (cuaca + suasana hati) dicocokkan dengan aturan yang tersimpan di `aturan.json`. Jika semua syarat suatu aturan terpenuhi, minuman tersebut direkomendasikan.

## Struktur File

```
es-minuman/
├── expert_system.py      # Versi ringkas menggunakan all()
├── expert_system01.py    # Versi verbose dengan penjelasan tiap langkah
└── aturan.json           # Basis pengetahuan (aturan IF-THEN)
```

## Basis Pengetahuan

| Cuaca  | Suasana Hati | Rekomendasi      |
|--------|--------------|------------------|
| Panas  | Santai       | Cola Dingin      |
| Panas  | Lelah        | Es Teh Manis     |
| Dingin | Sedih        | Cokelat Panas    |
| Dingin | Lelah        | Kopi Hitam       |
| Hujan  | Sedih        | Teh Hangat Madu  |
| Hujan  | Santai       | Wedang Jahe      |

## Cara Menjalankan

```bash
python expert_system01.py
```

Ikuti pertanyaan yang muncul:

```
=== Expert System Rekomendasi Minuman ===

Bagaimana cuaca saat ini?
  1. panas
  2. dingin
  3. hujan
Pilih nomor: 1

Bagaimana suasana hati Anda?
  1. santai
  2. lelah
  3. sedih
Pilih nomor: 2

--- HASIL ---

Rekomendasi: Es Teh Manis
Alasan     : Es teh manis memberi kesegaran dan tambahan gula untuk mengembalikan energi saat lelah di cuaca panas.
```

## Menambah Aturan Baru

Tambahkan entri baru di `aturan.json` tanpa mengubah kode Python:

```json
{
  "nama": "Nama Minuman",
  "syarat": {
    "cuaca": "panas",
    "suasana_hati": "santai"
  },
  "alasan": "Alasan rekomendasi."
}
```

## Persyaratan

- Python 3.x
