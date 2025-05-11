import os
import shutil

def get_xampp_path():
    return input('กรุณากรอกที่อยู่ของ XAMPP (เช่น C:\\xampp): ').strip()

def get_data_folder(xampp_path):
    return os.path.join(xampp_path, 'mysql', 'data')

def rename_data_folder(data_dir):
    index = 1
    while True:
        new_data_dir = f'{data_dir}_df{index}'
        if not os.path.exists(new_data_dir):
            shutil.move(data_dir, new_data_dir)
            print(f'เปลี่ยนชื่อ {data_dir} เป็น {new_data_dir}')
            return new_data_dir
        index += 1

def copy_backup_to_data(xampp_path):
    backup_dir = os.path.join(xampp_path, 'mysql', 'backup')
    data_dir = get_data_folder(xampp_path)
    new_data_dir = data_dir

    # เปลี่ยนชื่อ backup เป็น data
    if os.path.exists(backup_dir):
        shutil.copytree(backup_dir, data_dir)
        print(f'คัดลอก {backup_dir} ไปยัง {data_dir}')
    else:
        print(f'ไม่พบโฟลเดอร์ backup: {backup_dir}')

def move_databases_to_data(new_data_dir, data_dir):
    exclude_dirs = ['mysql', 'performance_schema', 'phpmyadmin']
    for item in os.listdir(new_data_dir):
        if item not in exclude_dirs:
            src_path = os.path.join(new_data_dir, item)
            dst_path = os.path.join(data_dir, item)
            if os.path.exists(dst_path):
                print(f'ข้ามฐานข้อมูลที่มีอยู่แล้ว: {dst_path}')
            else:
                if os.path.isdir(src_path):
                    shutil.copytree(src_path, dst_path)
                else:
                    shutil.copy2(src_path, dst_path)
                print(f'คัดลอก {src_path} ไปยัง {dst_path}')

def copy_ibdata1(new_data_dir, data_dir):
    ibdata1_src = os.path.join(new_data_dir, 'ibdata1')
    ibdata1_dst = os.path.join(data_dir, 'ibdata1')
    if os.path.exists(ibdata1_src):
        shutil.copy2(ibdata1_src, ibdata1_dst)
        print(f'คัดลอก {ibdata1_src} ไปยัง {ibdata1_dst}')

def main():
    xampp_path = get_xampp_path()
    data_dir = get_data_folder(xampp_path)

    # ขั้นตอนที่ 1: เปลี่ยนชื่อโฟลเดอร์ data
    new_data_dir = rename_data_folder(data_dir)

    # ขั้นตอนที่ 2: คัดลอก backup ไปยัง data
    copy_backup_to_data(xampp_path)

    # ขั้นตอนที่ 3: ย้ายฐานข้อมูล (ยกเว้นที่ต้องข้าม) ไปยัง data
    move_databases_to_data(new_data_dir, data_dir)

    # ขั้นตอนที่ 4: คัดลอก ibdata1
    copy_ibdata1(new_data_dir, data_dir)

    print('กระบวนการเสร็จสิ้นเรียบร้อยแล้ว')

if __name__ == '__main__':
    main()
