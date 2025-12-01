import os
from django.conf import settings
from .forms import QRCodeForm
import qrcode
from django.shortcuts import render

def generate_qr(request):
    if request.method == "POST":
        form = QRCodeForm(request.POST)
        if form.is_valid():
            res_name = form.cleaned_data['restaurant_name']
            url = form.cleaned_data['url']

            qr = qrcode.make(url)
            file_name = res_name.replace(" ", "_").lower() + '_Menu.png'

            os.makedirs(settings.MEDIA_ROOT, exist_ok=True)

            file_path = os.path.join(settings.MEDIA_ROOT, file_name)
            qr.save(file_path)

            media_url = settings.MEDIA_URL
            if not media_url.endswith('/'):
                media_url += '/'
            qr_url = media_url + file_name

            if not os.path.exists(file_path):
                return render(request, 'Download_Qr.html', {
                    'res': res_name,
                    'qr_url': '',
                    'file_name': file_name,
                    'error': f'File not found on disk at {file_path}'
                })

            return render(request, 'Download_Qr.html', {'res': res_name, 'qr_url': qr_url, 'file_name': file_name})
    else:
        form = QRCodeForm()
    return render(request, "qr_code.html", {'form': form})
