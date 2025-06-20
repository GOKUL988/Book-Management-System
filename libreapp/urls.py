from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path("",views.home, name='home.html'),
    path("base",views.base, name='base.html'),
    path("sto_entry", views.sto_entry, name='sto_entry.html'),
    path("bookdt/<uuid:acceno>", views.bookdt, name='bookdt.html'),
    path("memdt/<mem_id>",views.memdt, name="memdt.html"),
    path("sto_book", views.sto_book, name='sto_book.html'),
    path("sup_entry", views.sup_entry, name='sup_entry.html'),
    path("sup_list", views.sup_list, name='sup_list.html'),
    path("sup_dt/<sup_id>", views.sup_dt, name='sup_dt.html'),
    path("mem_entry", views.mem_entry, name='mem_entry.html'),
    path("mem_list", views.mem_list, name='mem_list.html'),
    path("issu_lt", views.issu_lt , name='issu_lt.html'),
    path("issu_dt/<issu_id>", views.issu_dt, name='issu_dt.html'),
    path('issu_entry',views.issu_entry, name='issu_entry.html'),
    path("issu_ret/<issu_id>", views.issu_ret, name='issu_ret.html'),
    path("tot_sup", views.tot_sup, name= 'tot_sup.html'),
    path("issu_retdt", views.issu_retdt, name='issu_retdt.html'),
    path("sale_nw", views.sale_nw, name='sale_nw.html'),
    path("sale_list", views.sale_list, name="sale_list.html"),
    path("vw_bill/<invcno>", views.vw_bill, name="vw_bill.html"),
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)