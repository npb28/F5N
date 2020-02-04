from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from .forms import PostForm


def post_list(request):
    contacts = Contact.objects.order_by('first_name')
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})


def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'contacts/contact_detail.html', {'contact': contact})


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