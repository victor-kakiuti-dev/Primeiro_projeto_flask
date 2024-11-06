from flask.views import MethodView
from flask import request, render_template, redirect
from src.db import pymysql

mysql = pymysql.connect(
    host='localhost',
    user='root',
    password='Loop@654',
    db='db_flask'
)


class IndexController(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM produto")
            data = cur.fetchall()

        #     cur.execute("SELECT * FROM categories")
        #     categories = cur.fetchall()
        return render_template('public/index.html', data=data)

    def post(self):
        code = request.form['code']
        name = request.form['name']
        stock = request.form['stock']
        value = request.form['value']

        with mysql.cursor()as cur:
            cur.execute("INSERT INTO produto VALUES (%s, %s, %s, %s)",(code, name, stock, value))
            cur.connection.commit()
            return redirect('/')


class DeleteProdutoController(MethodView):
    def post(self, code):
        with mysql.cursor()as cur:
            cur.execute("DELETE FROM produto WHERE code =%s", (code,))
            cur.connection.commit()
            return redirect('/')


class UpdateProdutoController(MethodView):
    def get(self, code):
        with mysql.cursor()as cur:
            cur.execute("SELECT * FROM produto WHERE code =%s", (code))
            product = cur.fetchone()
            return render_template('public/update.html', product=product)

    def post(self, code):
        productCode = request.form['code']
        name = request.form['name']
        stock = request.form['stock']
        value = request.form['value']
        with mysql.cursor()as cur:
            cur.execute("UPDATE produto SET code =%s,name =%s,stock =%s, value =%s WHERE code = %s", (productCode, name, stock, value, code))
            cur.connection.commit()
            return redirect('/')


