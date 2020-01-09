from django.shortcuts import render, get_object_or_404

# Create your views here.
def Shoppingmall_main(request):
    return render(request,'shoppingmall/shoppingmall_main.html')

def Shoppingmall_menu_detail(request):
    return render(request,'shoppingmall/shoppingmall_menu_detail.html')

def Shoppingmall_sub_menu_detail(request):
    return render(request,'shoppingmall/shoppingmall_sub_menu_detail.html')