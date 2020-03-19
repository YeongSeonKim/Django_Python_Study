from .common import *

'''
[Instagram] 북마크 취소 뷰
: 사용자가 포스트의 컬렉션 버튼을 누르면 사용자의 컬렉션에 저장되는 뷰
- UncollectionView는 main.html, post_detail.html에 있는 컬렉션 버튼과 연결되어있다.
- Ajax
1. 현재 로그인된 유저가 컬렉션을 누른 포스트의 post_id와 현재 유저의 아이디로 collection에 데이터 DELETE
2. 성공 여부를 return
'''

@login_required
def UncollectionView(request, post_id):
    user = request.user

    try:
        cursor = connection.cursor()

        strSql = "DELETE FROM collection"
        strSql += " WHERE post_id = (%s)"
        strSql += " AND user_id = (%s)"

        result = cursor.execute(strSql, (post_id, user.username))

        return HttpResponse(json.dumps({'result': '200',}), content_type="application/json")

    except:
        connection.rollback()
        print("Failed deleting in UncollectionView")

    finally:
        connection.close()    
    