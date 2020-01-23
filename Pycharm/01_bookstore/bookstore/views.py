from django.shortcuts import render, get_object_or_404
from django.db import connection
# connection : 어느 DB던 상관없이 연결시켜주는 모듈, 커넥션 객체를 만들어줌
# from .models import Book

# Create your views here.
def Bookstore_index(request):
    # context = {
    #     'book_list' : Book.objects.all(),
    # }
    try:
        cursor = connection.cursor()
        # cursor() : cursor 객체 생성, SQL문을 수행하고 결과를 얻는데 사용하는 객체

        strSql = "SELECT code, name, author FROM bookstore_book"
        result = cursor.execute(strSql)
        book_list = cursor.fetchall()

        books = []
        for book in book_list:
            row = {
                'code': book[0],
                'name': book[1],
                'author': book[2],
            }

            books.append(row)

        connection.commit()
        connection.close()

    except:
        connection.rollback() # 실패했는데 실행이되면안되니까 실행되기 전으로 돌아가는거
        print("Failed selecting in Bookstore_index") # 에러가 어디서 나는지 알려주기 위해서

    # return render(request, 'bookstore/bookstore_index.html', context)
    return render(request, 'bookstore/bookstore_index.html', {'book_list': books})

def Bookstore_detail(request, bookstore_code):
    # book = get_object_or_404(Book, code=bookstore_code)
    # context = {
    #     'book': book,
    # }
    try:
        cursor = connection.cursor()

        strSql = "SELECT code, name, author, price, url FROM bookstore_book WHERE code = (%s)"
        result = cursor.execute(strSql, (bookstore_code,))
        datas = cursor.fetchall()

        connection.commit()
        connection.close()

        book = {'code': datas[0][0],
                'name': datas[0][1],
                'author': datas[0][2],
                'price': datas[0][3],
                'url': datas[0][4]}

    except:
        connection.rollback()
        print("Failed selecting in BookListView")

    # return render(request, 'bookstore/bookstore_detail.html', context)
    return render(request, 'bookstore/bookstore_detail.html', {'book': book})