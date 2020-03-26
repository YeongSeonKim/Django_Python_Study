from .common import *

'''
[Instagram] 포스트 삭제 뷰
: 사용자의 포스트를 삭제하는 뷰
- PostDeleteView는 post_detail.html에 있는 포스트 삭제 버튼과 연결되어있다.

1. URL의 parameter 값으로 사용자가 클릭한 포스트의 post_id 값을 받는다.
2. 받아온 post_id를 조건하여 bookmark 테이블에서 데이터 DELETE
3. 받아온 post_id를 조건하여 post_hashtag 테이블에서 데이터 DELETE
4. 받아온 post_id를 조건하여 post 테이블에서 데이터 DELETE
'''

@login_required
def PostDeleteView(request, post_id):
    user = request.user

    try:
        cursor = connection.cursor()

        # 포스트 삭제
        strSql = "DELETE FROM post"
        strSql += " WHERE post_id = (%s)"
        result = cursor.execute(strSql, (post_id,))
        
        # 북마크 삭제
        strSql = "DELETE FROM collection"
        strSql += " WHERE post_id = (%s)"
        result = cursor.execute(strSql, (post_id,))
        
        # 해시태그 삭제
        strSql = "DELETE FROM post_hashtag"
        strSql += " WHERE post_id = (%s)"
        result = cursor.execute(strSql, (post_id,))
        
        return redirect('instagram:post_list', user.username)

    except:
        connection.rollback()
        print('Failed deleting in PostDeleteView')

        messages.error(request, '포스트를 삭제하는데 에러가 발생했습니다.')
        return redirect('instagram:post_detail', post_id)
    
    finally:
        connection.close()