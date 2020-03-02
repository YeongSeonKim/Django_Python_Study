from .common import *

'''
[Istagram] 메인 페이지
: 사용자의 포스트, 사용자가 팔로우한 계정의 포스트를 볼 수 있는 페이지
1. 현재 접속하고 있는 유저와 현재 유저가 팔로잉하고 있는 유저들의
   포스트 리스트를 SELECT
2. 가져온 포스트를 main.html에 rendering
'''

# 메인페이지
@login_required
def MainView(request):
    user = request.user

    try:
        cursor = connection.cursor()

        strSql = "SELECT post_id, user_id, post_img_url, content, time"
        strSql += " FROM post"
        strSql += " WHERE user_id IN (SELECT following_id FROM following WHERE user_id = (%s))"
        strSql += " OR user_id = (%s)"
        strSql += " ORDER BY time DESC"

        result = cursor.execute(strSql, (user.username, user.username))
        datas = cursor.fetchall()

        # 파일 업로드 시간
        upload_time = datetime.datetime.today()

        posts = []
        for data in datas:
            raw_data = {
                'post_id' : data[0],
                'user_id' : data[1],
                'post_img_url' : data[2],
                'content' : data[3],
                'time' : data[4],
                'postUser' : User.objects.get(username=data[1]),
            }
            posts.append(raw_data)
            print(raw_data)

            context = {
                'posts' : posts,
            }

            return render(request,'instagram/main.html', context)

    except:
        connection.rollback()
        print("Failed selecting in MainView")

        messages.error(request, '포스트를 가져오는데 에러가 발생했습니다.')

        return render(request,'instagram/main.html')

    finally:
        connection.close()