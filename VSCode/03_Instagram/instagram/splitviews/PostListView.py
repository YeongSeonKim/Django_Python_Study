from .common import *

def PostListView(request, user_id):
    user = request.user

    try:
        cursor = connection.cursor()

        strSql = "SELECT post_id, post_img_url"
        strSql += " FROM post"
        strSql += " WHERE user_id = (%s)"
        strSql += " ORDER BY time DESC"

        result = cursor.execute(strSql, (user_id,))
        datas = cursor.fetchall()

        posts = []
        for data in datas:
            raw_data = {'post_id': data[0],
                        'post_img_url': data[1],}
            posts.append(raw_data)

            context = {
                'posts': posts,
                }

        return render(request, 'instagram/post_list.html', context)


    except:
        connection.rollback()
        print("Failed selecting in PostListView")

        messages.error(request, "포스트를 가져오는데 에러가 발생하였습니다.")
        
        context = {
            'user_id' : user_id,
        }

        return render(request, 'instagram/post_list.html', context)

    finally:
        connection.close()
