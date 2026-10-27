# Mavzu-Testlar-tuzish

`олий тоифа laborant.zip` ichidagi 291 ta mavzu (`Мавзу2/NNN.docx`) uchun test jadvallari.

## Tuzilishi
- `Тест2/NNN.xlsx` — tayyor jadvallar (shablon.xlsx asosida; hozircha 001–176).
- `savollar/*.txt` — savollar matn ko'rinishida (`? savol`, `+ to'g'ri`, `- noto'g'ri ×4`, `! izoh`, `@ manba kalitlari`).
- `tools/build_tests.py` — sifat tekshiruvi (`check`) va `.xlsx` ga yig'ish (`build`). Aralashtirish mavzu raqamidan olingan seed bilan, natija qayta qurilganda o'zgarmaydi.
- `tools/verify_xlsx.py` — tayyor faylni qayta o'qib format tekshiradi (sarlavha, dimension, A–E ro'yxat tekshiruvi, Correct ↔ Comment mosligi).
- `tools/extract_docx.py` — `.docx` dan matn ajratish (pandoc kerak emas).
- `tools/make_all.sh` — hamma partiyani birlashtirib tekshiradi va yig'adi.

## Qoidalar (avtomatik tekshiriladi)
Har mavzuda ≥10 savol; 1 to'g'ri + 4 noto'g'ri; to'g'ri javob eng uzun noto'g'ri javobdan ≤10 % uzun;
"Faqat/Hech/Umuman/Barcha" bilan boshlanuvchi noto'g'ri javob ≤1 ta; 3+ javob bir xil so'z bilan boshlanmaydi;
harflar muvozanatli, bir harf ketma-ket 3 marta kelmaydi.
