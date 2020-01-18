from django.shortcuts import render
from responseapp.forms import MyForm
from django.template import loader
from django.http import HttpResponse
from responseapp.models import Response


def responseform(request):
 #if form is submitted
     form_class = MyForm
     form = form_class(request.POST or None)
     if request.method == 'POST':
        myForm = MyForm(request.POST)

        if myForm.is_valid():
            name = myForm.cleaned_data['name']
            color = myForm.cleaned_data['color']
            pet = myForm.cleaned_data['pet']

            context = {
            'name': name,
            'color': color,
            'pet': pet
            }

            response, created = Response.objects.get_or_create(
                name = myForm.cleaned_data['name'],
                color = myForm.cleaned_data['color'],
                pet = myForm.cleaned_data['pet'],
            )

            if created:
                template = loader.get_template('thankyou.html')
                return HttpResponse(template.render(context, request))
            else:
                messages.error(request, "Error: name already exists")


     else:
         form = MyForm()

     return render(request, 'responseform.html', {'form':form});

