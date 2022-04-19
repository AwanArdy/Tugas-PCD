from PIL import Image
from PIL import ImageFilter

def applyMaximumFilter(image):
    return image.filter(ImageFilter.MaxFilter);

imagePath   = "fiony.jpg";
imageObject = Image.open(imagePath);

filterApplied = imageObject;
for i in range(0, 10):
    print(i);
    filterApplied = applyMaximumFilter(filterApplied);

imageObject.show();
filterApplied.show();