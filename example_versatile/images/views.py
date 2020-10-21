from django.forms import ModelForm
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from example_versatile.images.models import ExampleModel


class ExampleForm(ModelForm):
    class Meta:
        model = ExampleModel
        fields = ["image"]


@csrf_exempt
def form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return render(request, 'success.html')
    else:
        form = ExampleForm()
    return render(request, 'form.html', {'form': form})


def index_view(request):
    return render(request, 'index.html', {'objects': ExampleModel.objects.all()})
