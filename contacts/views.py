from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Contact
from .forms import ContactForm
# Create your views here.
def contact_list(request):
    contacts = Contact.objects.all()

    query = request.GET.get('q')
    if query is not None:
        contacts = contacts.filter(first_name__icontains = query) | contacts.filter(last_name__icontains = query)
    return render(request, 'home.html', {'contacts':contacts})

def contact_add(request):
    if request.method == 'POST':
        new_contact = ContactForm(request.POST)
        new_contact.save(commit=False)
        new_contact.user = request.user
        new_contact.save()
        return redirect('home')
    else:
        new_contact = ContactForm()
    return render(request, 'new_contact_form.html', {'new_contact':new_contact})

def contact_edit(request, pk):
    contact = get_object_or_404(Contact, pk=pk)

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'edit_contact.html', {'form': form})

def contact_details(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'contact_details.html', {'contact':contact})

def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('home')
    return render(request, 'delete_contact.html', {'contact':contact})