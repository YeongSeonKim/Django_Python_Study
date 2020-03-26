from .common import *

'''
[Instagram] 포스트 상세 페이지
: 사용자가 작성한 포스트만을 볼 수 있는 페이지
1. 클릭된 포스트를 SELECT
2. [200308] 클릭된 포스트 세부사항 데이터 SELECT
3. [200326] 각 포스트별 해시태그 데이터 SELECT
4. 가져온 포스트를 post_detail.html에 rendering
'''

def PostDetailView(request, post_id):
    user = request.user

    try:
        cursor = connection.cursor()

        strSql = "SELECT post_id, user_id, post_img_url, content, time"
        strSql += " FROM post"
        strSql += " WHERE post_id = (%s)"
        result = cursor.execute(strSql, (post_id,))
        data = cursor.fetchall()
        data = [list(x) for x in data]

        post = {'post_id': data[0][0],
                'user_id': data[0][1],
                'post_img_url': data[0][2],
                'content': data[0][3],
                'time': data[0][4]}
        
        # 각각의 포스트 좋아요 개수
        strSql = "SELECT COUNT(*)"
        strSql += " FROM like_post"
        strSql += " WHERE post_id = (%s)"

        result = cursor.execute(strSql, (post['post_id'],))
        data = cursor.fetchall()

        post['likeCount'] = data[0][0]

        # 로그인한 유저가 해당 포스트에 좋아요를 눌렀는지에 대한 여부
        strSql = "SELECT COUNT(*)"
        strSql += " FROM like_post"
        strSql += " WHERE post_id = (%s)"
        strSql += " AND user_id = (%s)"

        result = cursor.execute(strSql, (post['post_id'], user.username)) 
        data = cursor.fetchall()

        post['like'] = data[0][0]

        # 로그인한 유저가 해당 포스트를 컬렉션에 추가했는지에 대한 여부
        strSql = " SELECT COUNT(*)" 
        strSql += " FROM collection" 
        strSql += " WHERE post_id = (%s)"
        strSql += " AND user_id = (%s)"

        result = cursor.execute(strSql, (post['post_id'], user.username))
        data = cursor.fetchall() 

        post['collection'] = data[0][0]

        # 포스트 별 해시태그
        strSql = "SELECT H.keyword"
        strSql += " FROM post_hashtag as PH"
        strSql += " JOIN hashtag as H ON PH.hashtag_id = H.hashtag_id"
        strSql += " WHERE PH.post_id = (%s)"

        result = cursor.execute(strSql, (post['post_id'],))
        data = cursor.fetchall()
        hashtags = [x for row in data for x in row]

        post['hashtags'] = hashtags

        postDetailUser = User.objects.get(username=post['user_id'])

        context = {
            'postDetailUser' : postDetailUser,
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