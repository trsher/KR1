from django.shortcuts import render
import sqlite3
# Create your views here.
def first_page(request):
    c = sqlite3.connect('create.db')
    cur = c.cursor()
    cur.execute("SELECT type, description from type_of_building")
    test = cur.fetchall()
    cur.execute("SELECT Type, Square from building")
    build = cur.fetchall()
    return render(request, 'Page.html', {'test': test, 'build': build})