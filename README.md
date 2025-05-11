# xampp-mysql-utils

สำหรับแก้ไขปัญหา MySQL ใน XAMPP โดยการเปลี่ยนชื่อโฟลเดอร์ `data`, คัดลอก `backup` และกู้คืนไฟล์ฐานข้อมูล

## ✅ คุณสมบัติ
- เปลี่ยนชื่อโฟลเดอร์ `data` เป็น `data_dfX` (X คือตัวเลขลำดับ)
- คัดลอก `backup` เปลี่ยนชื่อเป็น `data`
- ย้ายโฟลเดอร์ฐานข้อมูล (ยกเว้น `mysql`, `performance_schema`, `phpmyadmin`) จาก `data_dfX` ไปยัง `data`
- คัดลอก `ibdata1` จาก `data_dfX` ไปยัง `data`

## 📦 ความต้องการ
- Python 
- XAMPP Mysql ใช่ไม่ได้

## 🚀 การติดตั้ง
1. โคลนโปรเจกต์:
   ```bash
   git clone https://github.com/petchdiamonddev/xampp-mysql-utils
   cd xampp-mysql-utils
   ```

2. รันสคริปต์:
   ```bash
   python main.py
   ```

## 🛠️ วิธีการใช้งาน
- กรอก path ของ XAMPP เมื่อมีการถาม (เช่น `C:\xampp`).
- สคริปต์จะทำตามขั้นตอนดังนี้:
  1. เปลี่ยนชื่อ `data` เป็น `data_dfX`
  2. คัดลอก `backup` ไปยัง `data`
  3. ย้ายโฟลเดอร์ฐานข้อมูลไปยัง `data`
  4. คัดลอก `ibdata1` ไปยัง `data`

## ⚠️ คำเตือน
- ตรวจสอบให้แน่ใจว่าได้ **ปิด XAMPP** ก่อนรันสคริปต์
- สำรองข้อมูลสำคัญก่อนดำเนินการ

## 🧑‍💻 นักพัฒนา
**เพชร** – [GitHub](https://github.com/petchdiamonddev)
