from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Country_Data, City_Data
# Create your views here.
def data_page(request):
    model = Country_Data
    object_name = "Country"
    queryset = Country_Data.objects.all()
    context = {'latest_question_list': queryset}
    return render(
        request,
        'masterdata/data.html',
        context
    )

class Country_Create(ListView):
    model = Country_Data
    template_name = 'masterdata/country_data.html'
    queryset = Country_Data.objects.all()
    context_object_name =  "Country_list"
    
    def get_context_data(self, **kwargs):
        context = super(Country_Create, self).get_context_data(**kwargs)
        context['City_list'] = City_Data.objects.all()
        context['Country_list'] = self.queryset
        return context


    