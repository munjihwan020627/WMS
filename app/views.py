from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product
from django.contrib import messages
from django.shortcuts import get_object_or_404


def index(request):
    return render(request, "index.html")

def main(request):
    return render(request, "main.html")
def blog(request):
    return render(request,"blog.html")

def login(request):
    return render(request,"login.html")

def channel1(request):
    return render(request,"channel1.html")

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '상품이 성공적으로 추가되었습니다.')
            return redirect('product_list') # 상품 목록 페이지로 리다이렉트 (추후 정의)
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})



def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  # ✅ request.FILES 추가
        if form.is_valid():
            form.save()
            messages.success(request, '상품이 성공적으로 추가되었습니다.')
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})


def delete_product(request, pk):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        messages.success(request, '상품이 삭제되었습니다.')
    return redirect('product_list')