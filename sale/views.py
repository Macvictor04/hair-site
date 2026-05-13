from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Feedback
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import RegistrationForm, LoginForm, FeedbackForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request,"sale/register.html",{"form":form})
    form = RegistrationForm()
    return render(request,"sale/register.html",{"form":form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                form.add_error(None, "Invalid username or password")
                return render(request, "sale/login.html", {"form": form})
    form = LoginForm()
    return render(request, 'sale/login.html', {"form":form})
def logout_view(request):
    logout(request)
    return redirect('login')

def home(request):
    featured_product = Product.objects.filter(featured=True).order_by('-created_at')[:10]
    feedbacks = Feedback.objects.all().order_by('-created_at')[:7]
    form = FeedbackForm()

    return render(request, "sale/home.html", {
        "featured_product": featured_product,
        "feedbacks": feedbacks,
        "form": form
    })

def list_product(request):
    query = request.GET.get('q')
    category = Category.objects.all()
    if query:
        product_list = Product.objects.filter(
            Q(name__icontains=query)|Q(discription__icontains=query)
        )
    else:
        product_list = Product.objects.all()
    category_id = request.GET.get('category')
    if category_id:
        product_list = Product.objects.filter(categories_id=category_id)
    paginator = Paginator(product_list,5)
    page_num = request.GET.get('page')
    product = paginator.get_page(page_num)
    return render(request, "sale/list_product.html", {"category":category,"product":product, "query":query})

def product_detail(request,id):
    product = get_object_or_404(Product, id=id)
    return render(request, "sale/detail.html",{"product":product})

def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback=form.save(commit=False)
            feedback.user = request.user
            feedback.save()
            return redirect('home')