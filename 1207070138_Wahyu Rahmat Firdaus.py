import numpy as np
import cv2
import matplotlib.pyplot as plt
#Import

img = cv2.imread(r"C:\Users\Wahyu\Downloads\Compressed\Prak 34\Praktikum 3 dan 4\image\orange.jpg")
#Lokasi File

img_height = img.shape[0]
img_width = img.shape[1]
img_channel = img.shape[2]
img_type = img.dtype
#Memvariabelkan tinggi, lebar, channel dan tipe gambar

img_flip_horizontal = np.zeros(img.shape, img_type)
img_flip_vertical = np.zeros(img.shape, img_type)
#Membuat variabel dengan resolusi dan tipe yang sama seperti gambar

for y in range(0, img_height):
    for x in range(0, img_width):
        for c in range(0, img_channel):
            img_flip_horizontal[y][x][c] = img[y][img_width-1-x][c]
#Membalik gambar secara horizontal
            
for y in range(0, img_height):
    for x in range(0, img_width):
        for c in range(0, img_channel):
            img_flip_vertical[y][x][c] = img[img_height-1-y][x][c]
#Membalik gambar secara vertical

fig, axes = plt.subplots(2, 2, figsize=(12, 12))
ax = axes.ravel()
ax[0].imshow(img)
ax[0].set_title("Original")
ax[1].imshow(img_flip_horizontal)
ax[1].set_title("Flip Horizontal")
ax[2].imshow(img_flip_vertical)
ax[2].set_title("Flip Vertical")            
plt.show()
#Menampilkan hasil balik gambar

img_grayscale = np.zeros(img.shape, dtype=np.uint8)

for y in range(0, img_height):
    for x in range(0, img_width):
        red = img[y][x][0]
        green = img[y][x][1]
        blue = img[y][x][2]
        gray = (int(red) + int(green) + int(blue)) / 3
        img_grayscale[y][x] = (gray, gray, gray)
#Mengubah gambar menjadi grayscale
        
plt.imshow(img_grayscale)
plt.title("Grayscale")
plt.show()
#Menampilkan Gambar grayscale

hg = np.zeros((256))
#Membuat variabel untuk menyimpan data gambar

for x in range(0, 256):
    hg[x] = 0
#Mengisi setiap nilai dalam array hg dengan 0
for y in range(0, img_height):
    for x in range(0, img_width):
        gray = img_grayscale[y][x][0]
        hg[gray] += 1
#Mengisi setiap nilai dalam array hg dengan 0
       
bins = np.linspace(0, 256, 100)
plt.hist(hg, bins, color="black", alpha=0.5)
plt.title("Histogram")
plt.show()
#Menampilkan Histogram

hgr = np.zeros((256))
hgg = np.zeros((256))
hgb = np.zeros((256))
hgrgb = np.zeros((768))
#Membuat variabel untuk menyimpan data gambar

for x in range(0, 256):
    hgr[x] = 0
    hgg[x] = 0
    hgb[x] = 0
#Mengisi setiap nilai dalam array hg dengan 0
   
for x in range(0, 768):
    hgrgb[x] = 0
    
for x in range(0, 256):
    hgr[x] = 0
    hgg[x] = 0
    hgb[x] = 0
    
for x in range(0, 768):
    hgrgb[x] = 0

# th = int(256/64)
temp = [0]
for y in range(0, img.shape[0]):
    for x in range(0, img.shape[1]):
        red = int(img[y][x][0])
        green = int(img[y][x][1])
        blue = int(img[y][x][2])
        green = green + 256
        blue = blue + 512
#         temp.append(green)
        hgrgb[red] += 1
        hgrgb[green] += 1
        hgrgb[blue] += 1

binsrgb = np.linspace(0, 768, 100)
plt.hist(hgrgb, binsrgb, color="black", alpha=0.5)
# plt.plot(hgrgb)
plt.title("Histogram Red Green Blue")
plt.show()
#Menghitung nilai dari gambar dan emanmpilkan histogram dari RGB

for y in range(0, img_height):
    for x in range(0, img_width):
        red = img[y][x][0]
        green = img[y][x][1]
        blue = img[y][x][2]
        hgr[red] += 1
        hgg[green] += 1
        hgb[blue] += 1

bins = np.linspace(0, 256, 100)
plt.hist(hgr, bins, color="red", alpha=0.5)
plt.title("Histogram Red")
plt.show()

plt.hist(hgg, bins, color="green", alpha=0.5)
plt.title("Histogram Green")
plt.show()

plt.hist(hgb, bins, color="blue", alpha=0.5)
plt.title("Histogram Blue")
plt.show()
#Menampilkan Histogram dan RGB secara terpisah

hgk = np.zeros((256))
c = np.zeros((256))

for x in range(0, 256):
    hgk[x] = 0
    c[x] = 0

for y in range(0, img_height):
    for x in range(0, img_width):
        gray = img_grayscale[y][x][0]
        hgk[gray] += 1
                
c[0] = hgk[0]
for x in range(1, 256):
     c[x] = c[x-1] + hgk[x]

hmaxk = c[255]

for x in range(0, 256):
    c[x] = 190 * c[x] / hmaxk

plt.hist(c, bins, color="black", alpha=0.5)
plt.title("Histogram Grayscale Kumulatif")
plt.show()
#Menampilkan Histogram Kumulatif

hgh = np.zeros((256))
h = np.zeros((256))
c = np.zeros((256))

for x in range(0, 256):
    hgh[x] = 0
    h[x] = 0
    c[x] = 0

for y in range(0, img_height):
    for x in range(0, img_width):
        gray = img_grayscale[y][x][0]
        hgh[gray] += 1
                
h[0] = hgh[0]
for x in range(1, 256):
     h[x] = h[x-1] + hgh[x]

for x in range(0, 256):
     h[x] = h[x] / img_height / img_width

for x in range(0, 256):
    hgh[x] = 0
    
for y in range(0, img_height):
    for x in range(0, img_width):
        gray = img_grayscale[y][x][0]
        gray = h[gray] * 255
        hgh[int(gray)] += 1

c[0] = hgh[0]
for x in range(1, 256):
     c[x] = c[x-1] + hgh[x]

hmaxk = c[255]

for x in range(0, 256):
    c[x] = 190 * c[x] / hmaxk

plt.hist(c, bins, color="black", alpha=0.5)
plt.title("Histogram Grayscale Hequalisasi")
plt.show()
#Menampilkan Histogram Hequalisasi

img_inversi = np.zeros(img.shape, dtype=np.uint8)
#Membuat variabel img_inversi

def inversi_grayscale(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            gray = nilai - gray
            img_inversi[y][x] = (gray, gray, gray)
#Membuat variabel img_inversi
  
def inversi_rgb(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            red = nilai - red
            green = img[y][x][1]
            green = nilai - green
            blue = img[y][x][2]
            blue = nilai - blue
            img_inversi[y][x] = (red, green, blue)
#Membuat fungsi untuk inversi rgb

inversi_grayscale(255)
plt.imshow(img_inversi)
plt.title("Inversi Grayscale")
plt.show()
#Menampilkan hasil inversi Grayscale

inversi_rgb(255)
plt.imshow(img_inversi)
plt.title("Inversi RGB")
plt.show()
#Menampilkan hasil inversi RGB

img_log = np.zeros(img.shape, dtype=np.uint8)
##Menampilkan hasil inversi Grayscale

def log(c):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            gray = int(c * np.log(gray + 1))
            if gray > 255:
                gray = 255
            if gray < 0:
                gray = 0
            img_log[y][x] = (gray, gray, gray)
##Menampilkan hasil inversi Grayscale
           
log(30)
plt.imshow(img_log)
plt.title("Log")
plt.show()
#Menampilkan hasil log¶

img_inlog = np.zeros(img.shape, dtype=np.uint8)
#img_inlog = np.zeros(img.shape, dtype=np.uint8)

def inlog(c):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            gray = int(c * np.log(255 - gray + 1))
            if gray > 255:
                gray = 255
            if gray < 0:
                gray = 0
            img_inlog[y][x] = (gray, gray, gray)
#img_inlog = np.zeros(img.shape, dtype=np.uint8)
            
inlog(30)
plt.imshow(img_inlog)
plt.title("Inversi & Log")
plt.show()
#img_inlog = np.zeros(img.shape, dtype=np.uint8)

img_nthpower = np.zeros(img.shape, dtype=np.uint8)
#Membuat variabel img_nthpower untuk menampung hasil

def nthpower(c, y):
    thc = c / 100
    thy = y / 100
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            gray = int(thc * pow(gray, thy))
            if gray > 255:
                gray = 255
            if gray < 0:
                gray = 0
            img_nthpower[y][x] = (gray, gray, gray)
#Membuat variabel img_nthpower untuk menampung hasil
            
nthpower(50, 100)
plt.imshow(img_nthpower)
plt.title("Nth Power")
plt.show()
#Menampilkan hasil

img_nthrootpower = np.zeros(img.shape, dtype=np.uint8)
#Membuat variabel img_nthrootpower

def nthrootpower(c, y):
    thc = c / 100
    thy = y / 100
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            gray = int(thc * pow(gray, 1./thy))
            if gray > 255:
                gray = 255
            if gray < 0:
                gray = 0
            img_nthpower[y][x] = (gray, gray, gray)
#Membuat fungsi untuk nth root power
           
nthrootpower(50, 100)
plt.imshow(img_nthrootpower)
plt.title("Nth Root Power")
plt.show()
#Menampilkan hasil