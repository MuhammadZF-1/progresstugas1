import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler


datatrain=pd.read_csv('kendaraan_train.csv')
#print(datatrain.info()) #untuk mengecek info dalam file yang berisi kolom dan tipenya
#print(datatrain.describe()) #untuk cek mean,mode, min, max dalam data
#print(datatrain.iloc[:5,:6]) #melihat isi baris 0-4 dengan 6 kolom dari kiri
#print(datatrain.iloc[:5,5:]) #melihat isi baris 0-4 dengan kolom ke-6 sampai akhir

datatrain.drop(['id','Tertarik'],axis=1,inplace=True) # kolom id dan tertarik tidak dibutuhkan 
#print(datatrain)

datatrain=datatrain.drop_duplicates() #drop data duplikasi karena bisa mengganggu proses

def encoding(dataenc): #mengubah data menjadi numerik agar perhitungan menjadi lebih mudah
    dataenc['Jenis_Kelamin']=dataenc['Jenis_Kelamin'].replace(['Pria','Wanita'],[1,0])
    dataenc['Umur_Kendaraan']=dataenc['Umur_Kendaraan'].replace(['< 1 Tahun','1-2 Tahun','> 2 Tahun'],[0,1,2])
    dataenc['Kendaraan_Rusak']=dataenc['Kendaraan_Rusak'].replace(['Tidak','Pernah'],[0,1])   
encoding(datatrain)
# print(datatrain.isnull().sum()) #cek ada berapa data yang null
# print(datatrain.skew()) #cek skewness 

datatrain['SIM']=datatrain['SIM'].fillna(datatrain['SIM'].median())
datatrain=datatrain.fillna(datatrain.mean())
#print(data.isna().sum())       #cek untuk memastikan data tidak ada yang null

# fig,ax= plt.subplots(ncols=3,figsize=(7,7))
# sns.boxplot(y='Premi',data=datatrain,ax=ax[0])
# sns.boxplot(y='Kanal_Penjualan',data=datatrain,ax=ax[1])
# sns.boxplot(y='Lama_Berlangganan',data=datatrain,ax=ax[2])
# plt.show()

q1=datatrain['Premi'].quantile(0.25)
q3=datatrain['Premi'].quantile(0.75)
iqr=q3-q1

batasbawah=q1-(1.5*iqr)
batasatas=q3+(1.5*iqr)

datatrain=datatrain[~( (datatrain['Premi']< batasbawah ) | (datatrain['Premi']>batasatas))]#data selain
# dalam range batas bawah dan atas tidak akan dimasukkan 

# fig,ax= plt.subplots(ncols=3,figsize=(7,7))
# sns.boxplot(y='Premi',data=datatrain,ax=ax[0])
# sns.boxplot(y='Lama_Berlangganan',data=datatrain,ax=ax[1])
# sns.boxplot(y='Kanal_Penjualan',data=datatrain,ax=ax[2])
# plt.show()

allkolom=['Jenis_Kelamin','Umur','SIM','Kode_Daerah','Sudah_Asuransi'
,'Umur_Kendaraan','Kendaraan_Rusak','Premi','Kanal_Penjualan','Lama_Berlangganan']# semua kolom dimasukkan 
# untuk di normalisasi 
normalisasi = StandardScaler() #panggil fungsi standardscaler untuk z score
datatrain[allkolom]=normalisasi.fit_transform(datatrain[allkolom].values) #proses normalisasi data
print(datatrain)
# datatrain.to_csv('hasilprogress1.csv',index=False) # export hasil data ke csv
