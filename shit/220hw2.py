hist1=[5, 5, 8, 5, 7, 8, 12, 4, 5, 8, 1, 0]
gradepoints=[4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7,0.0]
ok=['4e','a8','2a','2c','d8']
ok1=['6c','a9','ba','3c','dc','ca','1c','fd','7d','1c']
al=0
ac={1:0,2:0,3:0,4:0}
topic=10
for i in ok1:
    z=(int(i,16))
    z=((z &240)>>4)
    print(z&topic)
    az=bin(z).replace('0b', '')
    while len(az)!=4:
        az='0'+az
    bz=(bin(topic).replace("0b",''))
    while len(bz) != 4:
        bz = '0' + bz
    print(az,bz)
    for i in range(len(az)):
        if az[i] == bz[i] and az[i]=='1':
            ac[i+1]+=1
print(ac)
maximum = max(ac, key=ac.get)
print(2**(4-maximum))