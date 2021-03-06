from .common import *

'''
[Instagram] 포스트 리스트 페이지
: 사용자가 작성한 포스트만을 볼 수 있는 페이지
1. 아이디가 클릭된 유저의 포스트 리스트를 SELECT
2. [200302] 아이디가 클릭된 유저의 게시물 수, 팔로우 수, 팔로잉 수 SELECT
3. [200310] 팔로잉 리스트 모달에 띄울 팔로잉 유저 데이터 SELECT
4. [200319] 현재 유저가 컬렉션(북마크)한 포스트 리스트 데이터 SELECT
5. 가져온 포스트를 post_list.html에 rendering
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

        # 게시글 수
        strSql = "SELECT COUNT(post_id)"
        strSql += " FROM post"
        strSql += " WHERE user_id = (%s)"

        result = cursor.execute(strSql, (user_id,))
        data = cursor.fetchall()
        postCount = data[0][0]

        # 팔로잉 수
        strSql = "SELECT COUNT(following_id)"
        strSql += " FROM following"
        strSql += " WHERE user_id = (%s)"

        result = cursor.execute(strSql, (user_id,))
        data = cursor.fetchall()
        followingCount = data[0][0]

        # 팔로워 수
        strSql = "SELECT COUNT(user_id)"
        strSql += " FROM following"
        strSql += " WHERE following_id = (%s)"

        result = cursor.execute(strSql, (user_id,))
        data = cursor.fetchall()
        followerCount = data[0][0]

        # 현재 로그인한 사용자의 클릭 된 사용자에 대한 팔로우 여부
        strSql = "SELECT COUNT(following_id)"
        strSql += " FROM following"
        strSql += " WHERE user_id = (%s)"
        strSql += " AND following_id = (%s)"

        result = cursor.execute(strSql, (user.username, postListUser.username))
        data = cursor.fetchall()
        follow = data[0][0]

        # 아이디가 클릭 된 유저의 팔로잉 리스트
        strSql = "SELECT username, profile_img_src, profile_msg"
        strSql += " FROM accounts_user as AU"
        strSql += " JOIN following as F ON AU.username = F.following_id"
        strSql += " WHERE F.user_id = (%s)"
        result = cursor.execute(strSql, (user_id,))
        datas = cursor.fetchall()

        followingUsers = []
        for data in datas:
            raw_data = {
                'username': data[0],
                'profile_img_src': data[1],
                'profile_msg': data[2],
            }    
        
            # 현재 유저의 팔로잉 리스트에 대한 팔로우 여부
            strSql = "SELECT COUNT(following_id)"
            strSql += " FROM following"
            strSql += " WHERE user_id = (%s)"
            strSql += " AND following_id = (%s)"

            result = cursor.execute(strSql, (user.username, raw_data['username']))
            data = cursor.fetchall()
            raw_data['follow'] = data[0][0]

            followingUsers.append(raw_data)

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

        # 컬렉션 포스트 리스트
        collection = []
        if postListUser == user:
            strSql = "SELECT P.post_id, P.post_img_url"
            strSql += " FROM post as P"
            strSql += " JOIN collection as C ON P.post_id = C.post_id"
            strSql += " WHERE C.user_id = (%s)"
            strSql += " ORDER BY C.time DESC"
            result = cursor.execute(strSql, (user_id,))
            datas = cursor.fetchall()

            for data in datas:
                raw_data = {
                    'post_id': data[0],
                    'post_img_url': data[1],
                }
                collection.append(raw_data)

        context = {
            'postListUser' : postListUser,
            'postCount' : postCount,
            'followingCount' : followingCount,
            'followerCount' : followerCount,
            'follow' : follow,
            'followingUsers' : followingUsers,
            'posts': posts,
            'collection' : collection,
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
