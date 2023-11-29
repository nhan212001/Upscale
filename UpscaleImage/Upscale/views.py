from datetime import datetime
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UploadForm
from PIL import Image
import numpy as np
import cv2
from keras.models import load_model
from numpy.random import randint
import matplotlib.pyplot as plt

def main_view(request):
    if request.method == 'POST':
        generator = load_model('C:\PBL\PBL6\save_model\gen_e_8.h5', compile=False)

        file = request.FILES['img']
        img = Image.open(file)
        np_image = np.array(img)
        img = cv2.cvtColor(np_image,cv2.COLOR_BGR2RGB)
        img = img/255.
        img = cv2.resize(img,(32,32))
        
        vector = np.expand_dims(img, axis=0) 
        # print(vector.shape)
        result_img = generator.predict(vector)
        # result = np.reshape(result, result.shape[1:])
        result_img = result_img[0]
        # print(result_img)
        # print(np.array(result).shape)
        uploaded_img_path = "Upscale/image/" + datetime.now().isoformat().replace(":", ".") + "_" + file.name
        cv2.imwrite(uploaded_img_path,img*255)
        uploaded_rs_path = "Upscale/image/" + datetime.now().isoformat().replace(":", ".") + "_upscale_" + file.name
        cv2.imwrite(uploaded_rs_path,result_img*255)
        
        # plt.figure(figsize=(16, 8))
        # plt.subplot(231)
        # plt.title('LR Image')
        # plt.imshow(src_image[0,:,:,:])
        # plt.subplot(232)
        # plt.title('Superresolution')
        # plt.imshow(gen_image[0,:,:,:])


        # plt.show()

        context = {"path": uploaded_img_path,
                    "result": uploaded_rs_path}
        return render(request, 'home.html',context= context)
    return render(request, 'home.html')

# def dowload_image(request):
    


