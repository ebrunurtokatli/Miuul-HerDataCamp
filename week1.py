###############################################
# Python Alıştırmalar
###############################################

###############################################
# GÖREV 1: Veri yapılarının tipleriniz inceleyiniz.
###############################################

x = 8
type(x)

y = 3.2
type(y)

z = 8j + 18
type(z)

a = "Hello World"
type(a)

# SORGU İFADESİ
b = True
type(b)

# SORGU İFADESİ
c = 23 < 22
type(c)


l = [1, 2, 3, 4,"String",3.2, False]
type(l)

# Sıralıdır
# Kapsayıcıdır
# Değiştirilebilir


d = {"Name" :"Jake",
     "Age": [27,56],
     "Adress": "Downtown"}
type(d)

# Değiştirilebilir
# Kapsayıcı
# Sırasız
# Key değerleri farklı olacak


t = ("Machine Learning", "Data Science")
type(t)

# Değiştirilemez
# Kapsayıcı
# Sıralı


s = {"Python", "Machine Learning", "Data Science","Python"}
type(s)

# Küme
# Değiştirilebilir
# Sırasız + Eşsiz
# Kapsayıcı



###############################################
# GÖREV 2: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz,
# kelime kelime ayırınız.
###############################################

text = "The goal is to turn data into information, and information into insight."
text.upper().replace(","," ").replace("."," ").split()


#Chat sorusu?
text.split(".")
text.replace(" ",".")

#Chat cevap :)
text = "The goal is to turn data into information, and information into insight."
words = text.replace(",", "").replace(".", "").split()
son = [word.upper() for word in words]
print(son)


# NOT: split() sonuç olarak bize bir liste veriyor.


###############################################
# GÖREV 3: Verilen liste için aşağıdaki görevleri yapınız.
###############################################

lst = ["D","A","T","A","S","C","I","E","N","C","E"]

# Adım 1: Verilen listenin eleman sayısına bakın.
len(lst)

# Adım 2: Sıfırıncı ve onuncu index'teki elemanları çağırın.
lst[0]
lst[10]

# Chat soru?: Aynı anda sıfır ve onuncu indeksi print edebilir miyiz?
print(lst[0],lst[10])

# NOT: İndex numarasını [] kullanarak yazıyoruz.

# Adım 3: Verilen liste üzerinden ["D","A","T","A"] listesi oluşturun.

data_list = lst[0:4]
data_list

# [0:4] - Sol taraf dahil, sağ taraf dahil değil. 4' e kadar olan kısmı al.

# Adım 4: Sekizinci index'teki elemanı silin.

lst.pop(8)
lst

# Adım 5: Yeni bir eleman ekleyin.

lst.append(101)
lst


# Adım 6: Sekizinci index'e  "N" elemanını tekrar ekleyin.

lst.insert(8, "N")
lst


###############################################
# GÖREV 4: Verilen sözlük yapısına aşağıdaki adımları uygulayınız.
###############################################

dict = {'Christian': ["America",18],
        'Daisy':["England",12],
        'Antonio':["Spain",22],
        'Dante':["Italy",25]}


# Adım 1: Key değerlerine erişiniz.

dict.keys()

# Adım 2: Value'lara erişiniz.

dict.values()

# Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.

# 1.YÖNTEM
dict.update({"Daisy": ["England",13]})
dict

# dict.append({"Miuul": ["Turkey",13]})  #append metodu yok :(

# 2.YÖNTEM
dict["Daisy"][1] = 14
dict
dir(dict)
#dict["Daisy"][0]

# BONUS :)  get metodu ile sadece value değerini getirebilirz.
dict.get("Daisy")

dict.get("Daisy")[1]= 15
dict

# Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.

dict.update({"Ahmet": ["Turkey", 24]})
dict

# Adım 5: Antonio'yu dictionary'den siliniz.

dict.pop("Antonio")
dict

# belirli bir indexe nasıl koyarız?
# Sözlükler sırasız olduğu için Listeler gibi belirli bir indexe değer ekleyemeyiz !!

###############################################
# GÖREV 5: Arguman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atıyan ve
# bu listeleri return eden fonskiyon yazınız.
###############################################

l = [2,13,18,93,22]

def func(list):

    çift_list = []
    tek_list = []

    for i in list:
        if i % 2 == 0:
            çift_list.append(i)
        else:
            tek_list.append(i)

    return çift_list, tek_list
çift,tek = func(l)

### Global
çift_list = []
tek_list = []

def func(list):

    for i in list:
        if i % 2 == 0:
            çift_list.append(i)
        else:
            tek_list.append(i)
    return çift_list, tek_list

çift,tek = func(l)

# BONUS :) List comp. çözümü
l = [2,13,18,93,22]

def func(list):
    çift_list = [x for x in list if x % 2 == 0]
    tek_list = [x for x in list if x % 2 != 0]
    return çift_list, tek_list

çift,tek = func(l)

###############################################
# GÖREV 6: Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri bulunmaktadır.
# Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de tıp fakültesi
# öğrenci sırasına aittir.
# Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.
###############################################

ogrenciler = ["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]

for i,x in enumerate(ogrenciler):
    if i<3:
        i += 1
        print("Mühendislik Fakültesi",i,". öğrenci: ",x)
    else:
        i -= 2
        print("Tıp Fakültesi",i,". öğrenci: ",x)

# 2. yol:
ogrenciler = ["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]

for i,x in enumerate(ogrenciler,1):
    if i<4:
        print("Mühendislik Fakültesi",i,". öğrenci: ",x)
        i += 1
    else:
        i -= 3
        print("Tıp Fakültesi",i,". öğrenci: ",x)

# 3.yol:
[print("Mühendislik Fakültesi{}. öğrenci: {}".format(index,value)) if index<4
 else print("Tıp Fakültesi{}. öğrenci: {}".format((index-3),value)) for index,value in enumerate(ogrenciler,1)]



###############################################
# GÖREV 7: Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri
# yer almaktadır. Zip kullanarak ders bilgilerini bastırınız.
###############################################

ders_kodu = ["CMP1005","PSY1001","HUK1005","SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]

for ders_kodu, kredi, kontenjan in zip(ders_kodu, kredi, kontenjan):
  print(f"Kredisi {kredi} olan {ders_kodu} kodlu dersin kontenjanı {kontenjan} kişidir.")


###############################################
# GÖREV 8: Aşağıda 2 adet set verilmiştir.
# Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını eğer kapsamıyor ise 2. kümenin 1. kümeden
# farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.
###############################################

# Kümenin Üst Küme Olup Olmadığını Kontrol Etmek için : issuperset
# Kesişme(): intersection

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

def kume(set1,set2):
    if set1.issuperset(set2):
        print(set1.intersection(set2))
    else:
        print(set2.difference(set1))

kume(kume1,kume2)

kume(kume2,kume1)






##################################################
# List Comprehensions
##################################################

# ###############################################
# # GÖREV 1: List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük harfe çeviriniz
# ve başına NUM ekleyiniz.
# ###############################################
#
# # Beklenen Çıktı
#
# # ['NUM_TOTAL',
# #  'NUM_SPEEDING',
# #  'NUM_ALCOHOL',
# #  'NUM_NOT_DISTRACTED',
# #  'NUM_NO_PREVIOUS',
# #  'NUM_INS_PREMIUM',
# #  'NUM_INS_LOSSES',
# #  'ABBREV']
#
# # Notlar:
# # Numerik olmayanların da isimleri büyümeli.
# # Tek bir list comp yapısı ile yapılmalı.


import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = sns.load_dataset("car_crashes")
df.columns
df.info()


["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns]


# ###############################################
# # GÖREV 2: List Comprehension yapısı kullanarak car_crashes verisindeki isminde "no" barındırmayan değişkenlerin isimlerininin
# sonuna "FLAG" yazınız.
# ###############################################
#
# # Notlar:
# # Tüm değişken isimleri büyük olmalı.
# # Tek bir list comp ile yapılmalı.
#
# # Beklenen çıktı:
#
# # ['TOTAL_FLAG',
# #  'SPEEDING_FLAG',
# #  'ALCOHOL_FLAG',
# #  'NOT_DISTRACTED',
# #  'NO_PREVIOUS',
# #  'INS_PREMIUM_FLAG',
# #  'INS_LOSSES_FLAG',
# #  'ABBREV_FLAG']


[col.upper() + "_FLAG" if "no" not in col else col.upper() for col in df.columns]


kolon=["abbrev", "no_previous"]
list_kolon = [kolon.upper() if "no" in kolon else kolon.upper() + "_FLAG" for kolon in df.columns]

# ###############################################
# # Görev 3: List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan değişkenlerin isimlerini
# seçiniz ve yeni bir dataframe oluşturunuz.
# ###############################################
#
og_list = ["abbrev", "no_previous"]
#
# # Notlar:
# # Önce yukarıdaki listeye göre list comprehension kullanarak new_cols adında yeni liste oluşturunuz.
# # Sonra df[new_cols] ile bu değişkenleri seçerek yeni bir df oluşturunuz adını new_df olarak isimlendiriniz.
#
# # Beklenen çıktı:
#
# #    total  speeding  alcohol  not_distracted  ins_premium  ins_losses
# # 0 18.800     7.332    5.640          18.048      784.550     145.080
# # 1 18.100     7.421    4.525          16.290     1053.480     133.930
# # 2 18.600     6.510    5.208          15.624      899.470     110.350
# # 3 22.400     4.032    5.824          21.056      827.340     142.390
# # 4 12.000     4.200    3.360          10.920      878.410     165.630
#

og_list = ["abbrev", "no_previous"]
new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]
new_df.head()


##################################################################
#BONUS-1
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

# COMP.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]
print(newlist)

##################################################################
# BONUS-2
sentence = "Miuul herdatacamp first day"
words = sentence.split()
word_lengths = []

for word in words:
      if word != "day":
          word_lengths.append(len(word))
print(words)
print(word_lengths)

# Comp.
sentence = "Miuul herdatacamp first day"
words = sentence.split()

word_lengths = [len(word) for word in words if word != "day"]

print(words)
print(word_lengths)


# Chat soru?:Comprehension'da elif kullanilma durumu soz konusu mudur?
l = [1, 2, 3, 4, 5]

for values in l:
    if values == 1:
        print('yes')
    elif values == 2:
        print('no')
    else:
        print('idle')

#cozum
l = [1, 2, 3, 4, 5]
result=['yes' if v == 1 else ('no' if v == 2 else 'idle') for v in l]
result