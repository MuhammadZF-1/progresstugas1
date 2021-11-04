import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler


datatrain=pd.read_csv('kendaraan_train.csv')
#print(data.info())
# data.drop(['id','Tertarik'],axis=1,inplace=True)
#print(datatrain.iloc[:5,5:12])
# # print("total dataset ",len(data))
# # data.sample(5)

# #print(data.info())
a=datatrain.isnull().sum()
print(a)
# data=data.drop_duplicates() #drop data duplikasi karena bisa mengganggu proses
# #print(data)
# def encoding(dataenc):
#     dataenc['Jenis_Kelamin']=dataenc['Jenis_Kelamin'].replace(['Pria','Wanita'],[1,0])
#     dataenc['Umur_Kendaraan']=dataenc['Umur_Kendaraan'].replace(['< 1 Tahun','1-2 Tahun','> 2 Tahun'],[0,1,2])
#     dataenc['Kendaraan_Rusak']=dataenc['Kendaraan_Rusak'].replace(['Tidak','Pernah'],[0,1])   
# encoding(data)
# #print(data.isna().sum())       #cek ada berapa data yang null
# #print(data.skew())             #cek skewness masing2 kolom
# data['SIM']=data['SIM'].fillna(data['SIM'].median())
# data=data.fillna(data.mean())
# #print(data.isna().sum())       #cek ada berapa data yang null

# # fig,ax= plt.subplots(ncols=3,figsize=(16,4))
# # sns.boxplot(y='Premi',data3=data,ax=ax[0])
# # sns.boxplot(y='Lama_Berlangganan',data3=data,ax=ax[1])
# # sns.boxplot(y='Kanal_Penjualan',data3=data,ax=ax[2])
# # plt.show()

# q1=data['Premi'].quantile(0.25)
# q3=data['Premi'].quantile(0.75)
# iqr=q3-q1

# bb=q1-(1.5*iqr)
# ba=q3+(1.5*iqr)

# print("ba: ",ba)
# print("bb: ",bb)

# data=data[~( (data['Premi']< bb ) | (data['Premi']>ba))]
# fig,ax= plt.subplots(ncols=3,figsize=(16,4))
# sns.boxplot(y='Premi',data=data,ax=ax[0])
# sns.boxplot(y='Lama_Berlangganan',data=data,ax=ax[1])
# sns.boxplot(y='Kanal_Penjualan',data=data,ax=ax[2])
# plt.show()

# numeric=['Jenis_Kelamin','Umur','SIM','Kode_Daerah','Sudah_Asuransi'
# ,'Umur_Kendaraan','Kendaraan_Rusak','Premi','Kanal_Penjualan','Lama_Berlangganan']
# scaler= StandardScaler()
# data[numeric]=scaler.fit_transform(data[numeric].values)

# # data.to_csv('cobakuy.csv',index=False)


