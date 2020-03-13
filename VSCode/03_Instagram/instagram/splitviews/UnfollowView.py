from .common import *

'''
[Instagram] 언팔로우 뷰
: 사용자가 언팔로우 버튼이 클릭된 계정을 언팔로우 할 수 있는 뷰
- UnfollowView post_list.html에 있는 팔로잉 버튼과 연결되어있다.

1. 현재 사용자와 언팔로우 대상 계정의 아이디를 이용해 following 테이블에서 DELETE
2. post_list.html의 팔로우 수 변경을 위한 팔로우 수 SELECT
3. 팔로우 수 return
'''

@login_required
def UnfollowView(request, following_id):
    user = request.user

    try:
        cursor = connection.cursor()

        strSql = "DELETE FROM following"
        strSql += " WHERE user_id = (%s)"
        strSql += " AND following_id = (%s)"
        result = cursor.execute(strSql, (user.username, following_id))

        # 팔로워 수
        strSql = "SELECT COUNT(user_id)"
        strSql += " FROM following"
        strSql += " WHERE following_id = (%s)"

        result = cursor.execute(strSql, (following_id,))
        data = cursor.fetchall()
        followerCount = data[0][0]

        # responseData = {
        #     'followerCount': followerCount,
        # }

        # return JsonResponse(responseData)
        return HttpResponse(json.dumps({'result': '200', 'followerCount': followerCount}), content_type='application/json')

    except:
        connection.rollback()
        print("Failed deleting in UnfollowView")

    finally:
        connection.close()