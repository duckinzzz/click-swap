from django.shortcuts import render


# Create your views here.
def lobby(request):
    return render(request, 'btn_img_app/button_page.html')


def image_page(request):
    return render(request, 'btn_img_app/image_page.html')
