product_db = {
    "P001": {
        "name": "นมสด",
        "lot": "L20260601",
        "temp": "4°C",
        "expiry": "2026-06-10",
        "price": 45,
        "nutrition": "โปรตีน 8g, แคลเซียมสูง"
    }
}

def scan_and_login():
    # 1. แสกนหรือใส่รหัสสินค้าก่อน
    qr_code = input("สแกน 2D Barcode: ")
    product_id = qr_code[:4]
    
    if product_id not in product_db:
        print("ไม่พบสินค้าในระบบ")
        return

    item = product_db[product_id]

    # 2. ให้เลือกว่าใครเป็นคนใช้งาน
    print("\nกรุณาเลือกบทบาทผู้ใช้งาน:")
    print("1. ลูกค้า")
    print("2. พนักงานคลัง")
    print("3. พนักงานแคชเชียร์")
    
    choice = input("เลือกหมายเลข (1-3): ")
    
    print("\n--- ผลการแสดงผล ---")
    if choice == "1":
        print(f"สินค้า: {item['name']}")
        print(f"คุณค่าทางโภชนาการ: {item['nutrition']}")
        
    elif choice == "2":
        print(f"เข้าสู่ระบบสำหรับพนักงานคลังสำเร็จ")
        print(f"สินค้า: {item['name']}")
        print(f"เลขล็อต: {item['lot']}")
        print(f"อุณหภูมิ: {item['temp']}")
        
    elif choice == "3":
        print(f"เข้าสู่ระบบสำหรับพนักงานแคชเชียร์สำเร็จ")
        print(f"สินค้า: {item['name']}")
        print(f"ราคา: {item['price']} บาท")
        print(f"วันหมดอายุ: {item['expiry']}")
        
    else:
        print("ตัวเลือกไม่ถูกต้อง")

# รันระบบ
scan_and_login()
