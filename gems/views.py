from django.shortcuts import render, redirect
from .models import *
from .forms import ProfileForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


def Contact_us(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        query = request.POST.get('query')
        contact.name = name
        contact.phone = phone
        contact.query = query
        contact.save()
        messages.success(request, 'Thanks for Contact us !')
        return redirect('contact')

    return render(request, 'main/contact.html')


@login_required(login_url='login')
def Profile(request):
    return render(request, 'user/profile_page.html')


@login_required(login_url='login')
def Profile_Update(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES,
                           instance=request.user.profile)
        if form.is_valid():
            form.save()
            username = request.user.username
            messages.success(request, f'{username} , Your Profile is updated!')
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    context = {'form': form}
    return render(request, 'user/profile.html', context)


def Review_Page(request):
    reviews = Review.objects.all()
    context = {'reviews': reviews}
    return render(request, 'review/review.html', context)


@login_required(login_url='login')
def create_review(request):
    reviews = Review.objects.all()
    context = {'reviews': reviews}
    return render(request, 'review/create_review.html', context)


@login_required(login_url='login')
def add_review(request):
    if request.method == 'POST':
        re = Review()
        re.name = request.POST.get('name')
        re.email = request.POST.get('email')
        re.city = request.POST.get('city')
        re.review = request.POST.get('review')

        if len(request.FILES) != 0:
            re.product_image = request.FILES['productimage']
        re.save()
        messages.success(request, 'Thanks for your Review !')
        return redirect('review')

    return render(request, "review/review.html")
