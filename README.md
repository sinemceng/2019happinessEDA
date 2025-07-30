# 📊 2019 Dünya Mutluluk Raporu: Kapsamlı Keşifçi Veri Analizi (EDA)

Bu proje, [2019 Dünya Mutluluk Raporu](https://www.kaggle.com/datasets/unsdsn/world-happiness) veri setini kullanarak kapsamlı bir Keşifçi Veri Analizi (EDA) gerçekleştirmeyi amaçlamaktadır. Amaç; veri setinin temel yapısını anlamak, değişkenlerin dağılımlarını görselleştirmek, eksik ve aykırı değerleri tespit etmek ve değişkenler arası ilişkileri analiz etmektir. Bu analizde Python’un popüler kütüphaneleri olan **Pandas**, **NumPy**, **Matplotlib** ve **Seaborn** kullanılmıştır.

## 🌟 Proje Hedefleri

- Veri setini yüklemek ve genel bir ön inceleme yapmak  
- Veri tiplerini ve eksik verileri kontrol etmek  
- Sayısal değişkenler için temel istatistiksel özetleri sunmak  
- Değişken dağılımlarını görselleştirmek (histogram, KDE, çubuk grafik)  
- Aykırı değerleri tespit etmek (box plotlar)  
- Korelasyon analizi yapmak (ısı haritası)

## 🚀 Kullanılan Kütüphaneler

- `pandas`
- `numpy`
- `matplotlib.pyplot`
- `seaborn`


## 📝 Analiz Adımları ve İçgörüler

1. **`load_veri()`**: Veri setini yükler ve `info()` ile `describe()` çıktıları sunar.  
2. **`null_control()` & `heatmap()`**: Eksik değerleri sayısal ve görsel olarak gösterir. (Veri setinde eksik veri bulunmamıştır.) <img width="2205" height="1377" alt="heatmap" src="https://github.com/user-attachments/assets/74e1b50b-5721-4ba2-b52e-adfd4e1334fe" />

3. **`types()`**: Sütun veri tiplerini listeler.  
4. **`std_var()`**: Seçili sütunların standart sapma ve varyansını hesaplar.  
5. **`string_dagilim()`**: Kategorik verilerin dağılımını inceler. ('Country or region' benzersizdir.)  <img width="3974" height="978" alt="string" src="https://github.com/user-attachments/assets/0d00f369-e192-4f1c-b99f-093669279da2" />

6. **`hist()`**: Tüm sayısal sütunlar için KDE içeren histogramlar oluşturur. `histplot.png` olarak kaydedilir.  <img width="2380" height="1409" alt="histplot" src="https://github.com/user-attachments/assets/48d80fd7-3354-4339-b49a-912ad532c78d" />

   - **İçgörü**: "Generosity" ve "Perceptions of corruption" sağa çarpık; "GDP per capita" ve "Social support" sola çarpıktır.  
7. **`plot_()`**: Temel histogramları çizer. `plot.png` olarak kaydedilir.  <img width="2380" height="1410" alt="plot" src="https://github.com/user-attachments/assets/6eb94e5c-a05b-4e32-a9ab-4b77fae201d0" />

8. **`box()`**: Sayısal değişkenler için box plotlar oluşturur. `box.png` olarak kaydedilir.  <img width="2380" height="1409" alt="box" src="https://github.com/user-attachments/assets/b463e5f0-42b6-41bb-a9ba-876a8dbffc15" />

   - **İçgörü**: Bazı değişkenlerde yüksek/düşük uçta aykırı değerler gözlemlenmiştir.  
9. **`heat()`**: Sayısal değişkenlerin korelasyon matrisini ısı haritası ile görselleştirir.<img width="1976" height="2902" alt="heat" src="https://github.com/user-attachments/assets/2d2da9bc-941d-4953-9883-84b3702454f8" />


## 💡 Sonuçlar ve Gelecek Adımlar

Bu EDA çalışması, veri setinin yapısı, dağılımlar ve aykırı değerler hakkında önemli bilgiler sağlamıştır. Bulgular, veri ön işleme ve modelleme süreci için yol gösterici olabilir.  
Gelecek adımlar:  
- Çarpık dağılımlar için logaritmik dönüşüm  
- Aykırı değerleri ele almak için robust ölçekleme  
- Özellik mühendisliği ve makine öğrenimi uygulamaları

## 📂 Veri Kümesi Bilgisi

- **Kaynak:** [Kaggle - World Happiness Report 2019](https://www.kaggle.com/datasets/unsdsn/world-happiness)  
- **Lisans:** CC0: Public Domain  
- **Açıklama:** Bu projede kullanılan veri seti, ülkelerin mutluluk düzeylerini etkileyen çeşitli faktörlere (GDP, sosyal destek, yaşam süresi vb.) dair 2019 yılına ait verileri içermektedir. Veri seti, Birleşmiş Milletler Sürdürülebilir Kalkınma Çözümleri Ağı tarafından derlenmiştir ve halka açık bir şekilde paylaşılmıştır.
