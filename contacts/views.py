#These views connect the templates to the model. Displays objects in model and adds new objects to model

from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from .forms import PostForm

# takes request and will return the value it gets from calling another function render that will render (put together)
# the contact list template
def post_list(request): # Request takes information recieved from the user via internet.
    contacts = Contact.objects.order_by('first_name') # Order objects by their first_name field
    return render(request, 'contacts/contact_list.html', {'contacts': contacts}) #Template uses objects named contacts


def contact_detail(request, pk): # Catches pk integer 
    contact = get_object_or_404(Contact, pk=pk) # Request for one object or returns error if object not valid in model
    return render(request, 'contacts/contact_detail.html', {'contact': contact}) # Displays object's fields with detail template


def create_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('contact_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'contacts/contact_edit.html', {'form': form})
