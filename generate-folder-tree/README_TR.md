> 🇺🇸 **[Click for English Version / İngilizce Versiyon İçin Tıklayınız](README.md)**


# Dizin Ağacı Oluşturucu


## Araç Hakkında

Bu araç, klasör yapılarını haritalamak için tasarlanmış hafif bir Python otomasyon betiğidir. Bulunduğu dizini tarar ve tüm dosyaların ve alt klasörlerin, özyinelemeli bir dizin ağacı komutuna benzer şekilde, net ve görsel bir metin temsilini oluşturur. Proje yapılarını belgelemek, dosya hiyerarşilerini arşivlemek veya karmaşık dizin içeriklerini analiz etmek için idealdir.

## Temel Özellikler

* **Görsel Hiyerarşi:** Dalları ve iç içe geçmiş seviyeleri temsil etmek için standart ASCII karakterlerini kullanarak düzenli bir ağaç yapısı oluşturur.
* **Akıllı Filtreleme:** Gizli sistem dosyalarının ve nokta ile başlayan dosyaların sistem özniteliklerine göre dahil edilip edilmeyeceğini belirlemek için kullanıcı etkileşimli bir sorgu içerir.
* **Özyinelemeli Tarama:** Tam dosya mimarisini yakalamak için sınırsız derinlikteki alt dizinleri dolaşabilir.
* **Evrensel Uyumluluk:** Tüm dosya adlarının ve özel karakterlerin doğru şekilde işlenmesini sağlamak için UTF-8 kodlamasını kullanır.
* **Otomatik İsimlendirme:** Kolay tanımlama için çıktı metin dosyasını kök dizinin adına göre otomatik olarak adlandırır.

## Nasıl Çalışır

Çalıştırıldığında, betik mevcut çalışma dizinini kök olarak tanımlar. Terminal aracılığıyla kullanıcıya gizli dosyaların taramaya dahil edilip edilmeyeceğini sorar. Bu girişe dayanarak, her dosyayı ve klasörü dolaşır, bunları alfabetik olarak sıralar ve biçimlendirilmiş bir dize oluşturur. Son olarak, bu görsel haritayı aynı dizin içinde bir metin dosyasına kaydeder.

## Kurulum ve Kullanım

1.  **Dizin Kurulumu:**
    Sisteminizde Python'un yüklü olduğundan emin olun. Araç standart modülleri kullandığından harici bir kütüphane gerektirmez.

2.  **Etiketleri Ekle:**
    Hem Python betiğini hem de Batch dosyasını haritalamak istediğiniz belirli klasöre veya dizine kopyalayın.

3.  **Aracı Çalıştır:**
    * **Seçenek A (Otomatik):** Betiği bir terminal penceresinde otomatik olarak başlatmak için sağlanan Batch dosyasına çift tıklayın.
    * **Seçenek B (Manuel):** Hedef klasörde bir komut satırı arayüzü açın ve Python betiğini manuel olarak çalıştırın.

## Desteklenen Formatlar

Araç, işletim sistemi tarafından tanınan tüm dosya türlerini ve klasör yapılarını destekler. Standart belgeleri, sistem dizinlerini, geliştirme ortamlarını ve gizli yapılandırma dosyalarını kısıtlama olmaksızın doğru bir şekilde indeksler.