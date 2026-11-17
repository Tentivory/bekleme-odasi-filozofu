#!/usr/bin/env python3
# Bekleme Odası Filozofu - Hiçbir şey beklemiyor, her şeyi düşünüyor.

import time
import random
import sys

FELSEFELER = [
    "Beklemek, zamanın kendisiyle yüzleşmektir... ama sandalyeler rahatsız.",
    "Bu odada oturmak bir sanat, beklemek ise bir bilimdir.",
    "Randevu saatim geldi mi diye sormak, evrenin düzenini bozar.",
    "Evraklarım eksik değil, eksik olan benim sabrım.",
    "Beklerken düşünmek, düşünürken beklemek... hangisi önce?",
    "Kapı açılacak, ama ne zaman? İşte asıl sır bu.",
    # Gizli not: bazen sistemin kendisi bekleten olur, vatandas degil.
]

def bekle(saatler=1):
    print("Bekleme odasına hoş geldiniz. Lütfen oturun ve düşünün.")
    print("(Program sonsuza kadar bekleyecek, Ctrl+C ile kurtulun)\n")
    
    sayac = 0
    while True:
        print(f"Bekleme süresi: {sayac} saniye | {random.choice(FELSEFELER)}")
        time.sleep(random.uniform(2, 5))
        sayac += 1
        if sayac > 1000000:
            print("Hala bekliyorsunuz. Tebrikler, artık bir filozofsunuz.")

if __name__ == "__main__":
    try:
        bekle()
    except KeyboardInterrupt:
        print("\n\nBekleme sona erdi. Özgürlüğünüzü kazandınız. Ya da sadece sıkıldınız.")
        sys.exit(0)
