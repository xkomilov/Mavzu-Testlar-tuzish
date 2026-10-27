# Yakuniy hisobot — 291 mavzu bo'yicha test jadvallari

## Natija
- Fayllar: **291 ta** (`Тест2/001.xlsx … 291.xlsx`), hammasi `shablon.xlsx` asosida (sarlavha: `Question | A | B | C | D | E | Correct | Comment (Faqat to'g'ri javob uchun)`, Correct ustunida A–E ro'yxat tekshiruvi saqlangan, mavzu nomi jadvalga yozilmagan).
- Savollar: **2974 ta** (243 faylda 10 tadan, 48 faylda 11–13 tadan; hech bir faylda 10 dan kam emas).
- Har savolda 1 to'g'ri + 4 noto'g'ri javob, Correct va Comment to'ldirilgan. Comment shakli: `To'g'ri javob: <matn>. <izoh>. Manba: …`.
- Tekshiruvlar: `tools/build_tests.py check` — muammolar 0; `tools/verify_xlsx.py` — 291 faylning hammasi OK; `291.xlsx` qayta o'qilib format ko'zdan kechirildi.

## To'g'ri javob harflari (jami)
A = 595, B = 595, C = 600, D = 590, E = 594 (har fayl ichida ham deyarli teng, bir harf ketma-ket 3 marta kelmaydi).

## To'g'ri javob uzunligi
- To'g'ri javob eng uzun noto'g'ri javobdan **>10 % uzun** bo'lgan savollar: **168 ta (5,6 %)**.
- Ularning hammasi 30 % (foydalanuvchi belgilagan zaxira chegarasi) dan past; eng yuqori nisbat 1,28; 1,25 dan yuqorisi 2 ta, 1,20 dan yuqorisi 40 ta.
- 001–197-mavzularda qat'iy ≤10 % saqlangan (0 ta); 198-mavzudan keyin 10–30 % oraliq faqat ogohlantirish sifatida qoldirilgan, sababi — "mavzu materiali" qisqa va aniq iboralardan iborat bo'lgani uchun noto'g'ri variantlarni ma'noli va bir xil uzunlikda yozish qiyin bo'ldi.

## Rad etilgan/qo'llanmagan yo'llar
- Noto'g'ri javoblarni shablon qo'shimchalar bilan sun'iy cho'zish rad etildi.
- xayrullokomilov.uz kutubxonasi sandboxdan ochilmadi (403), shuning uchun u saytdagi sahifa raqamlari **tekshirilmagan**.
- Eski `Тест2/001–070.xlsx` (zip ichida) tegilmagan; yangilari alohida yozilgan.

## Material rasmiy manbalardan farq qilgan joylar (raqam bilan)
- **001** — [4]-havola (Komilov) tekshirilmagan.
- **002/003** — Levenguk: material "XVII asr oxiri" va "70-yillar" deydi; kattalashtirish "200×" deyilgan (manbalarda 100–200, eng yaxshisi >260×); [3] WHO qo'llanmasi tarix manbai emas.
- **005** — mezosoma haqidagi da'vo; **006** — "korteks suvni kam tutadi", *C. botulinum* toksini "sporaga yaqin davrda"; **008** — gram-musbatda bazal tana halqalari (MS va C).
- **017** — gemoliz patogenlikni ko'rsatadi deyilgan; **022** — streptokokklar gemolizga ko'ra, Lansfild bo'yicha emas.
- **024** — psixrofil optimumi 20–25 °C (darslikda ≤15 °C); **025** — "10000 atmosfera", quritish shkafi 180–200 °C; **029** — "70–30 %".
- **030/031** — toza suvda 100–200 /ml, ifloslangan suvda 100 000–300 000 /ml; cho'kish 75 %; **034** — "aralash simmetriya, boshi kubsimon" (bosh ikosaedr), faglar 65–70 °C da o'ladi; **036** — fagodiagnostika eski sovet ma'nosida; **037** — sefalosporinlar "tor spektrli"; **041** — MIK matni chalkash; **028** — tuproqda saqlanish ro'yxatlari.
- **181/182** — material "bo'g'ma" nomi ostida *Bordetella pertussis* ni tasvirlaydi; "bo'g'ma" aslida difteriya (*C. diphtheriae*), ko'kyo'tal 187–191-mavzularda. Savollar darslik bo'yicha difteriya faktlari bilan tuzilgan.
- **223/224** — material endemik toshmali tifning tashuvchisi sifatida "pashsha"ni yozadi; to'g'risi — burga (*Xenopsylla cheopis*), buni 221-mavzu ham tasdiqlaydi. Savollarda burga ishlatilgan.
- **253/255/265/270/277** — koli-titr/koli-indeks ta'riflari eski sovet ma'nosida (gramm/millilitr/litr birliklarida); xalqaro amaliyotda MPN/KHB. "EES" va "EHS" qisqartmalari mavzular orasida turlicha.
- **237/243** — quruq issiqlik 160–180 °C, CDC bo'yicha 170 °C da 60 daq yoki 160 °C da 120 daq; **241** — 121 °C da 15–20 daq (CDC: 15–30 daq), 134 °C — CDC bo'yicha 132–135 °C.
- **246** — soda qo'shilganda qaynash harorati "biroz oshadi" (ta'sir juda kichik).
- **250** — biologik usul (aerob + anaerob ikki qatlam) ommabop amaliyotdan ko'ra o'quv tajribasi sifatida bayon etilgan.

## Faqat mavzu materialiga tayangan, tashqi manba bilan tasdiqlanmagan faktlar
- **001** — uch bosqichli tekshiruv; shtammlarni sanitar-epidemiologik xizmat bilan almashish.
- **025** — quritishga sezgir patogenlar ro'yxati; **097** — streptokokk "enterotoksin" atamasi (materialning o'zi ma'lumot kam deydi); **137** — *S. aureus* kapsula turlari 5/8; **156** — brutsellyozning kasbiy ro'yxati.
- **234** — Ojeshko usulining maqsadi materialda tasdiqlanmagan; savol faqat "qo'llashdan oldin ko'rsatmani o'qish" haqida.
- **226–227, 258–263, 274–275, 280–281** — amaliy tartiblar (masalan 1,5 m balandlik, ekspozitsiya vaqti, 0–20 sm tuproq chuqurligi, 20–30 sm suv chuqurligi va idishning 3/4 qismi to'ldirilishi, 100 sm² maydon, 75–80 °C qizdirish) materialdan olingan; SanPiN/MU me'yoriy raqamlari materialda berilmagani uchun savollarga **kiritilmagan**.
- **244** — UB lampa o'chgach xonaga darhol kirmaslik sababi ("zaharli moddalar") materialdan.

## Tavsiya
Noto'g'ri variantlarni (distraktorlarni) soha mutaxassisi tomonidan tanlab ko'zdan kechirish tavsiya etiladi, ayniqsa yuqoridagi "farq qilgan" mavzularda.
