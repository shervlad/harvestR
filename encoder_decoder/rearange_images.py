import os

path = "../Fruit Picker Unity/observations/camera/depth/"
for filename in os.listdir(path):
    os.remove(os.path.join(path , filename))

path = "../Fruit Picker Unity/observations/camera/img/"
for filename in os.listdir(path):
    os.remove(os.path.join(path , filename))

path = "../Fruit Picker Unity/observations/camera/layer/"
for filename in os.listdir(path):
    os.remove(os.path.join(path , filename))


path = "../Fruit Picker Unity/observations/camera/"
for filename in os.listdir(path):
    if(os.path.isfile(os.path.join(path, filename))):
        if 'depth' in filename:
            os.rename(os.path.join(path,filename),os.path.join(path,'depth',filename))
        elif 'img' in filename:
            os.rename(os.path.join(path,filename),os.path.join(path,'img',filename))
        elif 'layer' in filename:
            os.rename(os.path.join(path,filename),os.path.join(path,'layer',filename))
        else:
            os.remove(os.path.join(path,filename))

