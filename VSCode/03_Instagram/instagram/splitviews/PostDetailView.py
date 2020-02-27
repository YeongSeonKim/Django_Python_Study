from .common import *

def PostDetailView(request, post_id):
    user = request.user

    try:
        cursor = connection.cursor()

        strSql = "SELECT post_id, user_id, post_img_url, content, time"
        strSql += " FROM post"
        strSql += " WHERE post_id = (%s)"
        result = cursor.execute(strSql, (post_id,))
        data = cursor.fetchall()

        post = {'post_id': data[0][0],
                'user_id': data[0][1],
                'post_img_url': data[0][2],
                'content': data[0][3],
                'time': data[0][4]}

        context = {
            'user_id' : user.username,
            'post_id' : post.post_id,
            'post' : post,
        }
        
        return render(request, 'instagram/post_detail.html', context)

    except:
        connection.rollback()
        print("Failed selecting in PostDetailView")

        messages.error(request, '포스트를 가져오는데 에러가 발생했습니다.')

        return render(request,'instagram/post_detail.html')

    finally:
        connection.close()        