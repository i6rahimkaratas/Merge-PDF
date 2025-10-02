"""
PDF Birleştirme Programı
Bu program iki veya daha fazla PDF dosyasını tek bir PDF'te birleştirir.
"""

from PyPDF2 import PdfMerger
import os

def pdf_birlestir(pdf_dosyalari, cikti_dosyasi="birlestirilmis.pdf"):
    """
    Birden fazla PDF dosyasını tek bir PDF'te birleştirir.
    
    Args:
        pdf_dosyalari (list): Birleştirilecek PDF dosyalarının yol listesi
        cikti_dosyasi (str): Çıktı PDF dosyasının adı
    
    Returns:
        bool: İşlem başarılı ise True, değilse False
    """
    try:
        # PDF birleştirici oluştur
        merger = PdfMerger()
        
        # Her PDF dosyasını kontrol et ve ekle
        for pdf in pdf_dosyalari:
            if not os.path.exists(pdf):
                print(f"Hata: '{pdf}' dosyası bulunamadı!")
                return False
            
            if not pdf.lower().endswith('.pdf'):
                print(f"Uyarı: '{pdf}' bir PDF dosyası olmayabilir!")
            
            print(f"Ekleniyor: {pdf}")
            merger.append(pdf)
        
        # Birleştirilmiş PDF'i kaydet
        merger.write(cikti_dosyasi)
        merger.close()
        
        print(f"\n✓ Başarılı! PDF'ler '{cikti_dosyasi}' dosyasında birleştirildi.")
        return True
        
    except Exception as e:
        print(f"\n✗ Hata oluştu: {str(e)}")
        return False


def main():
    """Ana program"""
    print("=" * 50)
    print("PDF BİRLEŞTİRME PROGRAMI")
    print("=" * 50)
    
    # Kullanıcıdan PDF dosya yollarını al
    pdf_dosyalari = []
    
    print("\nBirleştirilecek PDF dosyalarının yollarını girin.")
    print("(Her satıra bir dosya yolu, bitirmek için boş enter)\n")
    
    while True:
        dosya_yolu = input(f"PDF {len(pdf_dosyalari) + 1}: ").strip()
        
        if dosya_yolu == "":
            if len(pdf_dosyalari) < 2:
                print("En az 2 PDF dosyası girmelisiniz!")
                continue
            else:
                break
        
        pdf_dosyalari.append(dosya_yolu)
    
    # Çıktı dosya adını al
    print("\nBirleştirilmiş PDF'in adı nedir?")
    cikti = input("(Varsayılan: birlestirilmis.pdf): ").strip()
    
    if cikti == "":
        cikti = "birlestirilmis.pdf"
    elif not cikti.lower().endswith('.pdf'):
        cikti += ".pdf"
    
    # PDF'leri birleştir
    print("\n" + "=" * 50)
    pdf_birlestir(pdf_dosyalari, cikti)
    print("=" * 50)


# Alternatif kullanım: Doğrudan dosya yollarını belirterek
def hizli_birlestir():
    """Hızlı birleştirme - dosya yollarını kod içinde belirtin"""
    
    # Buraya dosya yollarınızı yazın
    dosyalar = [
        "dosya1.pdf",
        "dosya2.pdf"
    ]
    
    pdf_birlestir(dosyalar, "sonuc.pdf")


if __name__ == "__main__":
    # İnteraktif mod
    main()
    
    # Hızlı mod için şunu kullanabilirsiniz:
    # hizli_birlestir()
