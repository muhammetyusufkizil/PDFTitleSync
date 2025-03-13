from pypdf import PdfReader, PdfWriter
import os

# PDF dosyalarının bulunduğu klasör
klasor_yolu = ""  # Kendi yolunuzu kontrol edin

# Tüm PDF dosyalarını tarayın
for dosya in os.listdir(klasor_yolu):
    if dosya.endswith(".pdf"):
        dosya_yolu = os.path.join(klasor_yolu, dosya)
        
        # PDF'yi oku
        pdf = PdfReader(dosya_yolu)
        
        # Mevcut metadata’yı kontrol et
        mevcut_metadata = pdf.metadata or {}
        mevcut_baslik = mevcut_metadata.get('/Title', 'Başlık yok')
        print(f"{dosya} - Mevcut başlık: {mevcut_baslik}")
        
        # Yeni PDF yazıcı oluştur
        pdf_yazici = PdfWriter()
        
        # Mevcut sayfaları ekle
        for sayfa in pdf.pages:
            pdf_yazici.add_page(sayfa)
        
        # Yeni başlığı dosya adıyla güncelle
        yeni_baslik = dosya.replace(".pdf", "")  # Uzantıyı kaldır
        pdf_yazici.add_metadata({"/Title": yeni_baslik})
        
        # Orijinal dosyayı güncelle (yedek almak isterseniz bu satırı değiştirin)
        with open(dosya_yolu, "wb") as cikti:
            pdf_yazici.write(cikti)
        
        print(f"{dosya} - Yeni başlık: {yeni_baslik}")

print("Tüm PDF başlıkları güncellendi!")
