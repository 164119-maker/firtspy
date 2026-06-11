print("Halo")
import math

def main():
    print("====================================")
    print("  โปรแกรมคำนวณพื้นที่รูปทรงเรขาคณิต  ")
    print("====================================")
    print("1. สี่เหลี่ยมมุมฉาก (Rectangle)")
    print("2. สามเหลี่ยม (Triangle)")
    print("3. วงกลม (Circle)")
    print("------------------------------------")
    
    # รับค่าเลือกรูปทรงจากผู้ใช้งาน (ตัดช่องว่างเซฟตี้ด้วย .strip())
    choice = input("เลือกรูปทรงที่ต้องการคำนวณ (พิมพ์ 1, 2 หรือ 3): ").strip()
    
    if choice == "1":
        print("\n[ คำนวณพื้นที่สี่เหลี่ยมมุมฉาก ]")
        width = float(input("กรอกความกว้าง: "))
        length = float(input("กรอกความยาว: "))
        area = width * length
        print(f"-> พื้นที่สี่เหลี่ยมคือ: {area:,.2f}")
        
    elif choice == "2":
        print("\n[ คำนวณพื้นที่สามเหลี่ยม ]")
        base = float(input("กรอกความยาวฐาน: "))
        height = float(input("กรอกความสูง: "))
        area = 0.5 * base * height
        print(f"-> พื้นที่สามเหลี่ยมคือ: {area:,.2f}")
        
    elif choice == "3":
        print("\n[ คำนวณพื้นที่วงกลม ]")
        radius = float(input("กรอกความยาวรัศมี (r): "))
        area = math.pi * (radius ** 2)
        print(f"-> พื้นที่วงกลมคือ: {area:,.2f}")
        
    else:
        print("\n❌ คุณกรอกเมนูไม่ถูกต้อง! กรุณารันโปรแกรมใหม่แล้วพิมพ์เฉพาะเลข 1-3 นะครับ")

if __name__ == "__main__":
    main()