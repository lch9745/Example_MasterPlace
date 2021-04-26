from django.shortcuts import render

# Create your views here.
def data_page(request):
    return render(
        request,
        'masterdata/data.html',
    )