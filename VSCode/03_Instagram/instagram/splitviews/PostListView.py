from .common import *

'''
[Instagram] 포스트 리스트 페이지
: 사용자가 작성한 포스트만을 볼 수 있는 페이지
1. 아이디가 클릭된 유저의 포스트 리스트를 SELECT
2. 가져온 포스트를 post_list.html에 rendering
'''

def PostListView(request, user_id):
    user = request.user

    try:
        postListUser = User.objects.get(username=user_id)
    
    except ObjectDoesNotExist:
        messages.error(request, '존재하지 않는 계정입니다.')
        return render(request, 'instagram/post_list.html')

    try:
        cursor = connection.cursor()

        # # 게시글 수
        # strSql = "SELECT COUNT(post_id)"
        # strSql += " FROM post"
        # strSql += " WHERE user_id = (%s)"

        # result = cursor.execute(strSql, (user_id,))
        # data = cursor.fetchall()
        # postCount = data[0][0]

        # # 팔로잉 수
        # strSql = "SELECT COUNT(following_id)"
        # strSql += " FROM follwing"
        # strSql += " WHERE user_id = (%s)"

        # result = cursor.execute(strSql, (user_id,))
        # data = cursor.fetchall()
        # followingCount = data[0][0]

        # # 팔로워 수
        # strSql = "SELECT COUNT(user_id)"
        # strSql += " FROM follwing"
        # strSql += " WHERE following_id = (%s)"

        # result = cursor.execute(strSql, (user_id,))
        # data = cursor.fetchall()
        # followerCount = data[0][0]

        # # 현재 로그인한 사용자의 클릭 된 사용자에 대한 팔로우 여부
        # strSql = "SELECT COUNT(following_id)"
        # strSql += " FROM following"
        # strSql += " WHERE user_id = (%s)"
        # strSql += " AND following_id = (%s)"

        # result = cursor.execute(strSql, (user.username, postListUser.username))
        # data = cursor.fetchall()
        # follow = data[0][0]

        # 포스트 리스트
        strSql = "SELECT post_id, post_img_url"
        strSql += " FROM post"
        strSql += " WHERE user_id = (%s)"
        strSql += " ORDER BY time DESC"

        result = cursor.execute(strSql, (user_id,))
        datas = cursor.fetchall()

        posts = []
        for data in datas:
            raw_data = {
                'post_id': data[0],
                'post_img_url': data[1],
            }
            posts.append(raw_data)
            print(raw_data)

        context = {
            'postListUser' : postListUser,
            # 'postCount' : postCount,
            # 'followingCount' : followingCount,
            # 'followerCount' : followerCount,
            # 'follow' : follow,
            'posts': posts,
            }

        return render(request, 'instagram/post_list.html', context)


    except:
        connection.rollback()
        print("Failed selecting in PostListView")

        messages.error(request, '포스트를 가져오는데 에러가 발생하였습니다.')

        context = {
            'user_id' : user_id,
        }
        return render(request, 'instagram/post_list.html', context)

    finally:
        connection.close()
