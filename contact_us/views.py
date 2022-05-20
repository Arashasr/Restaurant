from django.shortcuts import render, redirect
from .forms import ContactForm



def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('foods:food_list')
    else:
        form = ContactForm()

    context = {
        'form': form,
    }

    return render(request, 'contact_us/contact.html', context)