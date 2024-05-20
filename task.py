# 1) Folder taski
import os
import shutil


example_dir = 'Example'
os.makedirs(example_dir, exist_ok=True)

subdirect_dir = os.path.join(example_dir, 'subdirect')
os.makedirs(subdirect_dir, exist_ok=True)

picture_src = 'image.jpg'  
picture_dest = os.path.join(subdirect_dir, picture_src)
if os.path.exists(picture_src):
    shutil.copy(picture_src, picture_dest)
else:
    print(f"Şəkil faylı ({picture_src}) tapılmadı. Lütfən faylı cari qovluğa əlavə edin.")

text_file = os.path.join(subdirect_dir, 'example.txt')
with open(text_file, 'w', encoding='utf-8') as file:
    file.write('Bu bir nümunə mətn faylıdır.')

for item in os.listdir(subdirect_dir):
    item_path = os.path.join(subdirect_dir, item)
    if os.path.isfile(item_path) and item_path.endswith('.txt'):
        dest_path = os.path.join(example_dir, item)
        if os.path.exists(dest_path):
            base, ext = os.path.splitext(item)
            count = 1
            new_name = f"{base}_{count}{ext}"
            new_dest_path = os.path.join(example_dir, new_name)
            while os.path.exists(new_dest_path):
                count += 1
                new_name = f"{base}_{count}{ext}"
                new_dest_path = os.path.join(example_dir, new_name)
            shutil.move(item_path, new_dest_path)
            print(f"Mətn faylı {item} yeni adla köçürüldü: {new_name}")
        else:
            shutil.move(item_path, dest_path)
            print(f"Mətn faylı {item} 'Example' qovluğuna köçürüldü.")



# #2) Alqoritmik task
# def yerləri_hesabla(xallar):

#     xallar_indekslərlə = list(enumerate(xallar))
    
#     sıralanmış_xallar = sorted(xallar_indekslərlə, key=lambda x: x[1], reverse=True)

#     yerlər = [0] * len(xallar)
    
#     for sıra, (indeks, xal) in enumerate(sıralanmış_xallar):
#         yerlər[indeks] = f'{sıra + 1}-ci'
    
#     return yerlər


# xallar = [5, 3, 4, 2, 1]
# yerlər = yerləri_hesabla(xallar)
# print(yerlər)  
