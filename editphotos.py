from PIL import Image, ImageOps, ImageEnhance, ImageFilter
import os

path = './imgs'
pathOut = './editedImgs'

if not os.path.exists(path):
  print(f"{path} does not exist.")
  
else:

    for filename in os.listdir(path):
      
      img = Image.open(f'{path}/{filename}')
      
      edit = img.filter(ImageFilter.SHARPEN).convert('L')
      edit = ImageOps.exif_transpose(edit) #apply the rotation from EXIF data
         
      clean_name = os.path.splitext(filename)[0]
        
      if not os.path.exists(pathOut):
        os.makedirs(pathOut)
        
      edit.save(f'{pathOut}/{clean_name}_edited.jpg')
    