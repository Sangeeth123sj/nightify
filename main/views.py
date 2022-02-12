from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .models import Picture
from .forms import UploadForm
from PIL import Image, ImageOps
from django.http import JsonResponse

# Create your views here.

def home(request):
    return render(request, 'contact.html')

def converter(request):
    context = {}
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data.get('upload')
            user = request.user
            obj = Picture.objects.create(upload = image, user = user)
            
            print("obj upload "+str(obj.upload))
            context['upload_status'] = 'Image uploaded!'
            context['image'] = obj.upload
            image_to_convert = Image.open(obj.upload)
            converted_image = ImageOps.grayscale(image_to_convert)
            filename = filename_generator(str(obj.upload))
            converted_image.save('./media/uploads/grey_'+filename)
            obj.converted_picture = 'uploads/grey_'+filename
            context['converted_picture'] = obj.converted_picture
            obj.save()
            print("obj.converted_picture"+str(obj.converted_picture))
        form = UploadForm()
    context['form'] = UploadForm()
    return render(request, 'converter.html', context)

def filename_generator(s):
    file = s.split("/")
    print('file_name: '+file[1])
    return file[1]
    
@login_required
def gallery(request):
    pictures = Picture.objects.all()
    context = {}
    context['pictures'] = pictures
    return render(request, 'gallery.html', context )

def download_ajax(request):
    picture_upload = request.GET['picture_upload']
    #converted_picture = request.GET['converted_picture']
    print(picture_upload)
    #print(converted_picture)
    if picture_upload:
        request.session['picture_upload'] = picture_upload
    #elif converted_picture:
    #    request.session['converted_picture'] = converted_picture 
    data = {
        'picture_type': "picture",
    }
    return JsonResponse(data)


@login_required
def download(request):
    picture = request.session['picture_upload']
    context = {}
    context['picture_url'] = picture
    print ("url "+'picture')
    return render(request, 'download.html', context)

@login_required
def my_pictures(request):
    pictures = Picture.objects.filter(user = request.user)
    context = {}
    context['pictures'] = pictures
    return render(request, 'my_pictures.html', context)