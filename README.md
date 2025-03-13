# PDFTitleSync
A simple Python tool to update the metadata title of PDF files to match their filenames.

## Description
This script processes all PDF files in a specified folder and updates their metadata `/Title` field to match the file name (without the `.pdf` extension). Useful for ensuring consistency between file names and the titles displayed in web browsers or PDF viewers.

## Features
- Updates PDF metadata titles based on filenames.
- Processes multiple PDF files in a folder.
- Overwrites original files with updated metadata (optional backup recommended).

## Requirements
- Python 3.x
- `pypdf` library (`pip install pypdf`)

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/[YourUsername]/PDFTitleSync.git


#### Türkçe Versiyon
# PDFTitleSync
PDF dosyalarının metadata başlığını dosya adlarıyla eşleştiren basit bir Python aracı.

## Açıklama
Bu betik, belirtilen bir klasördeki tüm PDF dosyalarını işler ve metadata’daki `/Title` alanını dosya adıyla (`.pdf` uzantısı olmadan) günceller. Dosya adları ile web tarayıcılarında veya PDF görüntüleyicilerde görünen başlıklar arasında tutarlılık sağlamak için kullanışlıdır.

## Özellikler
- PDF metadata başlıklarını dosya adlarına göre günceller.
- Bir klasördeki birden fazla PDF dosyasını işler.
- Orijinal dosyaları güncellenmiş metadata ile üzerine yazar (yedekleme önerilir).

## Gereksinimler
- Python 3.x
- `pypdf` kütüphanesi (`pip install pypdf`)

## Kurulum
1. Bu depoyu klonlayın:
   ```bash
   git clone https://github.com/[KullanıcıAdınız]/PDFTitleSync.git
