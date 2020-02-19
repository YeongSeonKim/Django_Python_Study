from django.shortcuts import render, redirect

# Create your views here.
def MainView(request):
    # request가 session을 가지고 있는지 판단 session안에서 user_id 키 값을 가져오고 False로
    isSession = request.session.get('user_id',False)

    if isSession is not False:
        return render(request, 'instagram/main.html')
    else:
        return redirect('accounts:login')

def PostListView(request, user_id):
    return render(request, 'instagram/my_post_list.html')

def PostCreateView(request):
    return render(request, 'instagram/post_create.html')

def PostDetailView(request):
    return render(request, 'instagram/each_post_detail.html')