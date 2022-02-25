distance = int(input("ป้อนระยะทาง(กิโลเมตร) : "))
price = 35
 
if distance == 1:
    price = 35
    
elif  distance > 1 and distance <= 10:
    distance = (distance - 1)
    price += distance * 5.50
    
elif  distance > 10 and distance <= 20:
    distance = (distance - 1)
    price += distance * 6.50
   
elif  distance > 20 and distance <= 40 :
    distance = (distance - 1)
    price += distance * 7.50
   
elif  distance > 40 :
    distance = (distance - 1)
    price += distance * 9
  
print("\nค่าแท็กซี่ทั้งหมด %.0f บาท"% price);

 

    