# SSH-BRUTE-FORCE Aracı  

**SSH-BRUTE-FORCE**, web uygulamalarına yönelik `GET`, `POST` ve `COOKIE` istek yöntemlerini kullanarak brute-force saldırıları gerçekleştirmek için geliştirilmiş, Python tabanlı bir betiktir.  

⚠ **Yasal Uyarı:**  
Bu araç yalnızca **yetkili testler** için tasarlanmıştır. Aracı kullanmadan önce hedefin sahibinden açık izin almanız gerekmektedir. İzinsiz kullanım, yasalara aykırıdır ve ciddi sonuçlara yol açabilir.

---

## Özellikler  
- `GET`, `POST` ve `COOKIE` saldırı vektörlerini destekler.  
- Hedef URL üzerindeki parametre veya çerez değerlerini brute-force yöntemiyle test eder.  
- Başarı mesajına dayalı otomatik sonuç doğrulaması.  
- Kullanıcı dostu bir arayüz ile etkileşimli kullanım.  

---

## Gereksinimler  
- Python 3.x  
- `urllib` (Python ile birlikte gelir)  

---

## Kurulum  
1. Bu projeyi klonlayın:  
   ```bash
   git clone https://github.com/enesdq/ssh-brute-force
   python ssh-brute-force.py
 ## örenek çalışma

 
 |-------------------------------------------------------|
|          SSH-BRUTE-FORCE   A R A C I N A   H O Ş G E L D İ N İ Z          |
|                 yapın: ENESCDQ                  |
|-------------------------------------------------------|

Lütfen URL'yi girin (gerekliyse bir eğik çizgiyle bitirin): http://hedef-sunucu.com
Lütfen başarı mesajını girin: Giriş Başarılı
Lütfen bir saldırı vektörü seçin (GET, POST, COOKIE): GET

[+] Saldırı başlatıldı!
[+] Deneniyor parametre = 0
[+] Deneniyor parametre = 1
[+] Deneniyor parametre = 42
[+] Saldırı başarılı! Başarı mesajı parametre = 42 olduğunda bulundu.

Cevabı burada yazdıralım mı? (Evet / Hayır): evet

## CEVAP ##

Giriş Başarılı! Hoş geldiniz.
