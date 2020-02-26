from .common import *

def UserInfoModifyView(request):
    if request.method == 'GET':
        user = request.user

        context = {
            'user' : user,
        }

        return render(request,'accounts/user_info_modify.html', context)
    
    else:
        profile_img_file = request.FILES.get('profile_img_file')
        profile_msg = request.POST.get('profile_msg')
        email = request.POST.get('email')
        name = request.POST.get('name')
        user_pw = request.POST.get('user_pw')
        
        try:
            user = User.objects.get(username=user.username)

            user.profile_img_src = profile_img_src
            user.profile_msg = profile_msg
            user.email = email
            user.firstname = name
            user.set_password(user.pw) # 비밀번호 변경

            user.save()

            return redirect('instagram:post_list', user.username)

        except:
            messages.error('사용자가 정보를 수정하는 과정에서 에러가 발생했습니다.')
            return redirect('instagram:userinfomodify')
