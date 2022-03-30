
from django.shortcuts import render
from django.views import View

from paintapp.forms import ColorPickerForm

# Create your views here.


class ColorPickerView(View):
    def get(self, request):
        '''Display color picker form and the color to the user'''
        form = ColorPickerForm()

        context = {
            'form': form,
            'red': 255,
            'green': 255,
            'blue': 255,
            'font': 'dark'
        }

        return render(request=request, template_name='color_picker.html', context=context)

    def post(self, request):
        '''display users selected color'''
        form = ColorPickerForm(request.POST)

        red = int(request.POST['red_amount'])
        green = int(request.POST['green_amount'])
        blue = int(request.POST['blue_amount'])
        font = 'dark'
        color_threshold = 120

    # Changes font color to light if background is too dark
        if (red < color_threshold) or (green < color_threshold) or (blue < color_threshold):
            font = 'light'

        context = {
            'form': form,
            'red': red,
            'green': green,
            'blue': blue,
            'font': font
        }

        return render(request=request, template_name='color_picker.html', context=context)
