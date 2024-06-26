columns = ['bed',
 'bath',
 'carport',
 'surface_area',
 'building_area',
 'listing-location_Banguntapan, Bantul',
 'listing-location_Bantul, Bantul',
 'listing-location_Bantul, Yogyakarta',
 'listing-location_Berbah, Sleman',
 'listing-location_Caturtunggal, Sleman',
 'listing-location_Caturtunggal, Yogyakarta',
 'listing-location_Cebongan, Sleman',
 'listing-location_Cebongan, Yogyakarta',
 'listing-location_Condong Catur, Sleman',
 'listing-location_Danurejan, Yogyakarta',
 'listing-location_Demangan, Yogyakarta',
 'listing-location_Depok, Sleman',
 'listing-location_Gamping, Sleman',
 'listing-location_Gedong Tengen, Yogyakarta',
 'listing-location_Godean, Sleman',
 'listing-location_Gondokusuman, Yogyakarta',
 'listing-location_Gondomanan, Yogyakarta',
 'listing-location_Imogiri , Bantul',
 'listing-location_Imogiri, Yogyakarta',
 'listing-location_Jetis, Bantul',
 'listing-location_Jetis, Yogyakarta',
 'listing-location_Jombor, Sleman',
 'listing-location_Kalasan, Sleman',
 'listing-location_Kaliurang, Sleman',
 'listing-location_Kaliurang, Yogyakarta',
 'listing-location_Karangmojo, Gunung Kidul',
 'listing-location_Kasihan, Bantul',
 'listing-location_Kotagede, Yogyakarta',
 'listing-location_Kraton, Yogyakarta',
 'listing-location_Kulonprogo, Kulon Progo',
 'listing-location_Kulonprogo, Yogyakarta',
 'listing-location_Maguwoharjo, Yogyakarta',
 'listing-location_Mantrijeron, Yogyakarta',
 'listing-location_Mergangsan, Yogyakarta',
 'listing-location_Minggir, Sleman',
 'listing-location_Mlati, Sleman',
 'listing-location_Moyudan, Sleman',
 'listing-location_Nanggulan, Kulon Progo',
 'listing-location_Ngaglik, Sleman',
 'listing-location_Ngemplak, Sleman',
 'listing-location_Nologaten, Yogyakarta',
 'listing-location_Pajangan, Bantul',
 'listing-location_Pakem, Sleman',
 'listing-location_Pakualaman, Yogyakarta',
 'listing-location_Pandak, Bantul',
 'listing-location_Piyungan, Bantul',
 'listing-location_Playen, Gunung Kidul',
 'listing-location_Plered, Bantul',
 'listing-location_Pogung, Yogyakarta',
 'listing-location_Prambanan, Sleman',
 'listing-location_Purwomartani , Sleman',
 'listing-location_Purwomartani, Yogyakarta',
 'listing-location_Sayegan, Sleman',
 'listing-location_Sedayu, Bantul',
 'listing-location_Sekip, Yogyakarta',
 'listing-location_Sentolo, Kulon Progo',
 'listing-location_Seturan, Yogyakarta',
 'listing-location_Sewon, Bantul',
 'listing-location_Sidoarum , Sleman',
 'listing-location_Sleman, Sleman',
 'listing-location_Sleman, Yogyakarta',
 'listing-location_Tegalrejo, Yogyakarta',
 'listing-location_Tempel, Sleman',
 'listing-location_Turi, Sleman',
 'listing-location_Umbulharjo, Yogyakarta',
 'listing-location_Wates, Kulon Progo',
 'listing-location_Wirobrajan, Yogyakarta',
 'listing-location_Wonosari, Gunung Kidul']

def transform(data):
    data = data.get_dummies(data, columns=['listing-location'])
    data = data.reindex(columns=columns, fill_value=0)
    return data