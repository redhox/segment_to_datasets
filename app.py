import os
import random
from PIL import Image

dossier_principal = 'datasets'
dossier_train = os.path.join(dossier_principal, 'train')
dossier_test = os.path.join(dossier_principal, 'test')
dossier_val = os.path.join(dossier_principal, 'val')

# Création du dossier
if not os.path.exists(dossier_principal):
    os.makedirs(dossier_principal)
if not os.path.exists(dossier_train):
    os.makedirs(dossier_train)
if not os.path.exists(dossier_test):
    os.makedirs(dossier_test)
if not os.path.exists(dossier_val):
    os.makedirs(dossier_val)

for dossier in  os.listdir(dossier_principal):
    if dossier != "data.yaml":
        if not os.path.exists(f"{dossier_principal}/{dossier}/images"):
            os.makedirs(f"{dossier_principal}/{dossier}/images")
        if not os.path.exists(f"{dossier_principal}/{dossier}/labels"):
            os.makedirs(f"{dossier_principal}/{dossier}/labels")



images=[]
object_detecter=[]
path_images = "./image_debase/image/"
data_name = os.listdir(path_images)
i=0
for element in data_name:
    liste_image=os.listdir(f'{path_images}{element}')
    object_detecter.append([element,i])
    for image in liste_image:
        images.append([image,element,i])
    i=i+1
random.shuffle(images)
i = 0
j=0

#créé le data.yaml
f = open(f"datasets/data.yaml", 'w')
f.write(f"train: ../train/images\n")
f.write(f"val: ../valid/images\n")
f.write(f"test: ../test/images\n")
f.write(f"names:\n")
for element in object_detecter:
    if element != "data.yaml":
        f.write(f"  {element[1]}: {element[0]}\n")

f.close()


while j < len(images):
    data_yaml=[]
    image_principale = Image.open("./image_debase/imagep.jpg")
    image_p_l, image_p_h = image_principale.size
    space_l=image_p_l/40
    space_h=image_p_h/40
    x1, y1 = 0, 0
    max_size_image=0
    while y1 < image_p_h:
        while x1 < image_p_l:
            #position haut gauche de l'image
            x1 = x1 + space_l
            # colage de l'image
            try:
                image1 = Image.open(f"{path_images}{images[j][1]}/{images[j][0]}")
                image1_l, image1_h = image1.size
                if image1_h > max_size_image:
                    max_size_image = image1_h
                if (image1_l+ x1) < image_p_l and (image1_h+ y1) < image_p_h:
                    image_principale.paste(image1, (int(x1), int(y1)))
                    # recuperation des info pour train
                    y= (y1 + (image1_h / 2)) / image_p_h
                    x= (x1 + (image1_l / 2)) / image_p_l
                    height = image1_h/ image_p_h
                    width = image1_l / image_p_l
                    data_element=f"{images[j][2]} {x} {y} {width} {height} \n"
                    print(f"image:{i} objet:{j}/{len(images)} : {data_element}")
                    data_yaml.append(data_element)
                x1 = x1 + image1_l
            except:
                print("last image")
            j=j+1
        y1 = y1 + max_size_image + space_h
        x1=0
    i=i+1

    if j > len(images) * 0.9:
        path="val"
    elif j > len(images) * 0.7:
        path="test"
    else:
        path="train"

    image_principale.save(f"datasets/{path}/images/image{i}.png")
    f = open(f"datasets/{path}/labels/image{i}.txt", 'w')
    for ligne in data_yaml:
        f.write(f"{ligne}\n")
    f.close()
