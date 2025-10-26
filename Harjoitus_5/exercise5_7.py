appliances = ("PHILIPS_Vedenkeitin_HD4646_2020_09_21_C_1",
"KENWOOD_Yleiskone_KVL8300S_2015_09_22_C_3",
"BOSCH_Tehosekoitin_MMB65G5M_2016_05_07_C_3",
"WHIRLPOOL_Mikroaaltouuni_MCP345WH_2019_01_15_C_1",
"ROSENLEW_Pakastin_RPP2330_2017_01_29_C_2",
"ELECTROLUX_Jääkaappi_ERF4114AOW_2017_11_07_C_2")
categories = ("Muut", "Pienlaitteet","Kylmälaitteet","Sekoittimet")

brand = [item.split('_')[0] for item in appliances]
model = [item.split('_')[1] for item in appliances]
modelNumber = [item.split('_')[2] for item in appliances]
year = [item.split('_')[3] for item in appliances]
month = [item.split('_')[4] for item in appliances]
day = [item.split('_')[5] for item in appliances]
category = [item.split('_')[7] for item in appliances]


for i in range(len(appliances)):
    print(f"Merkki: {brand[i]}")
    print(f"Malli: {model[i]} ({modelNumber[i]})")
    print(f"Kategoria: {categories[int(category[i])]}")
    print(f"Lisäyspäivämäärä: {day[i]}.{month[i]}.{year[i]}\n")
    