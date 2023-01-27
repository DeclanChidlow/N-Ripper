import pyscreenshot;
import time;
import shutil;
import os;
from pynput.keyboard import Key, Controller;
import img2pdf;
kb = Controller();

print("Tool to rip books from websites where downloads are not supported. \nPlease do NOT use for illegal purposes.");

#Collect information about book
title = input("What is the title of the book? ");
pages = int(input("How many pages is the book? "));

x1 = int(input("What is the top x location? "));
x2 = int(input("What is the top y location? "));
y1 = int(input("What is the bottom x location? "));
y2 = int(input("What is the bottom y location? "));

#Print information about user inputs
print("----------");
print(("Info:"), title);
print(("Pages:"), pages);
print("From X" + str(x1) + ",Y" + str(x2) + " to X" + str(y1) + ",Y" + str(y2) + " will be downloaded");
print("----------");

shutil.rmtree("output");
os.makedirs("output");

#Screenshot and save
while (pages >= 0):
    print("Downloading page", pages);
    time.sleep(5);
    image = pyscreenshot.grab(bbox=(x1, x2, y1, y2));
    image.save("output/" + "Page" + str( pages) + ".png");
    pages -= 1;
    kb.press(Key.right);
    kb.release(Key.right);

else:
    print("Book downloaded.");

#Convert to .pdf
if input("Would you like to convert it to a .pdf? (y/n) ") != "y":
    exit();

imgs = [];
for r, _, f in os.walk("output/"):
    for fname in f:
        if not fname.endswith(".png"):
            continue
        imgs.append(os.path.join(r, fname));
with open(title + ".pdf","wb") as f:
    f.write(img2pdf.convert(imgs));

print("Book converted to .pdf.");
