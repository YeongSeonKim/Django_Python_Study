from .common import *

@login_required
def PostUploadView(request):
    user = request.user

    if request.method == 'GET':
        return render(request, 'instagram/post_create.html')

    else:
        content = request.POST.get('content')
        postImg = request.FILES.get('postImg')

        post_img_url = fileUpload(user, postImg)

        try:
            cursor = connection.cursor()

            strSql = "INSERT INTO post(user_id, post_img_url, content)"
            strSql += " VALUES(%s, %s, %s)"
            
            result = cursor.execute(strSql, (user.username, post_img_url, content))
            
            return redirect('instagrm:main')

        except:
            connection.rollback()
            print('Failed inserting in PostUploadView')

            messages.error('포스트를 업로드하는 과정에서 에러가 발생했습니다. 다시 시도해주세요.')

            return redirect('instagram:post_upload')

        finally:
            connection.close()    