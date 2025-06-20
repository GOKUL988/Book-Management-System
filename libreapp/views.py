from lib2to3.fixes.fix_input import context
from django.shortcuts import render,redirect, get_object_or_404
from .models import purchase,supplier,stock,issue,member,sales,saledt
import json
from django.contrib import messages
from datetime import date, datetime
from django.db.models import Q

# Create your views here.
def home(request):
    return render(request, 'home.html')
def base(request):
    return render(request, 'base.html')
def sto_book(request):
    sea_qt = request.GET.get('search1')
    if sea_qt:
       book_inf= stock.objects.filter(
            Q(booktitle__icontains=sea_qt) | Q(isbn__icontains=sea_qt)
        )
    else:
        book_inf = stock.objects.all().order_by("-purc_id__date")
    return render(request, 'sto_book.html',{'book_inf': book_inf})
def bookdt(request,acceno):
    book1=get_object_or_404(stock, acceno=acceno)
    purchasedt=book1.purc_id
    supplierdt=book1.suppl_id
    issu_dt=issue.objects.filter(book_id=book1)
    context={
        'a':book1,
        'b':purchasedt,
        'c':supplierdt,
        'd':issu_dt,
    }
    return render(request, "bookdt.html", context)

def memdt(request,mem_id):
    mem=member.objects.get(member_id=mem_id)
    sto_iss=issue.objects.filter(mem_id=mem)
    return render(request, "member/memdt.html",locals())

def sto_entry(request):
    supp = supplier.objects.all()
    purr = purchase.objects.all().order_by("-pk")[:1]
    context={
        'supp': supp,
        'purr': purr
    }
    if request.method == "POST":
        form_type = request.POST.get('form_type')

        if form_type == 'purchase':
            supplier_obj = supplier.objects.get(sup_id=request.POST.get('supp_id'))
            purchasedt = purchase(
                supp_id=supplier_obj,
                billno=request.POST.get('billno'),
                date=request.POST.get('date'),
                bill=request.FILES.get('bill')
            )
            purchasedt.save()

        elif form_type == 'stock':
            obj1=purchase.objects.get(purch_id=request.POST.get('purch_id'))
            stockdt = stock(
                suppl_id=obj1.supp_id,
                purc_id=obj1,
                booktitle=request.POST.get('booktitle'),
                authorname=request.POST.get('authorname'),
                edition=request.POST.get('edition'),
                yearofpub=request.POST.get('yearofpub'),
                rate=request.POST.get('rate'),
                ava=request.POST.get('ava'),
                qun=request.POST.get('qun'),
                classfic=request.POST.get('classfic'),
                rack=request.POST.get('rack'),

            )
            stockdt.save()
            messages.success(request, "Stock Entry has been Successfully !")
            return redirect('sto_book.html')

    return render(request, 'sto_entry.html', context)

def sup_entry(request):
    if request.method=="POST":
        supp_dt=supplier(
            sup_name=request.POST.get('sup_name'),
            email=request.POST.get('email'),
            mobile=request.POST.get('mobile'),
            doorno=request.POST.get('doorno'),
            street=request.POST.get('street'),
            dist=request.POST.get('dist'),
            stat=request.POST.get('stat'),
            pin=request.POST.get('pin'),
        )
        supp_dt.save()
        messages.success(request, "Supplier Entry has been saved Successfully !")
        return redirect('sup_list.html')
    else:
        messages.warning(request, "Supplier Entry not been saved")
    return render(request, 'supplier/sup_entry.html')

def sup_list(request):
    sup_flt=request.GET.get('search_supp')
    if sup_flt:
        suplist=supplier.objects.filter(
            Q(supp_id__icontains=sup_flt) | Q(sup_name__icontains=sup_flt)
        )
    else:
        suplist=supplier.objects.all()
    return render(request, "supplier/sup_list.html",locals())
def sup_dt(request,sup_id):
    supp=get_object_or_404(supplier,sup_id=sup_id)
    purdt=stock.objects.filter(suppl_id=supp)
    context={
        'supp':supp,
        'purdt':purdt
    }
    return render(request, "supplier/sup_dt.html",context)

def mem_entry(request):
    if request.method=="POST":
        mement=member(
            memname=request.POST.get('memname'),
            dob=request.POST.get('dob'),
            gender=request.POST.get('gender'),
            doorno=request.POST.get('doorno'),
            strnme=request.POST.get('strnme'),
            dist=request.POST.get('dist'),
            state=request.POST.get('state'),
            pincode=request.POST.get('pincode'),
            memtype=request.POST.get('memtype')
        )
        mement.save()
        messages.success(request, "Member Entry has been saved Successfully !")
        return redirect('mem_list.html')
    return render(request, "member/mem_entry.html")
def mem_list(request):
    memlist = member.objects.all()
    mem_flt=request.GET.get("search_mem")
    no_res=False
    if mem_flt:
        memlist=member.objects.filter(
            Q(member_id__icontains=mem_flt) | Q(memname__icontains=mem_flt)
        )
        if not memlist.exists():
            no_res=True

    context={
        'memlist':memlist,
        'non':no_res
    }
    return render(request,"member/mem_list.html",context)

def issu_lt(request):
    isslist=issue.objects.all()
    iss_flt=request.GET.get("search_issu")
    no_rec=False
    if iss_flt:
        isslist= issue.objects.filter(
            Q(book_id__booktitle__icontains=iss_flt) | Q(mem_id__member_id=iss_flt) | Q(mem_id__memname=iss_flt)
        )
        if not isslist.exists():
            no_rec=True

    context={
         'isslist':isslist,
         'no_rec':no_rec
    }
    return render(request, "issue/issu_lt.html",context)
def issu_dt(request, issu_id):
    issdt=issue.objects.filter(issu_id=issu_id)
    context={
        'a': issdt,
    }
    return render(request, "issue/issu_dt.html", context)

def issu_entry(request):
    sto=stock.objects.all()
    mem=member.objects.all()
    sto_finish = False
    saved = False
    if request.method=="POST":
        sel_book=stock.objects.get(acceno=request.POST.get('book_id'))
        sel_mem=get_object_or_404(member, member_id=request.POST.get('mem_id'))
        if sel_book.ava.lower() == "yes" and sel_book.qun >=1 :
            issnew = issue(
                book_id=sel_book,
                mem_id=sel_mem,
                iss_date= request.POST.get('iss_date'),
                ret_date= request.POST.get('ret_date')
            )
            issnew.save()
            messages.success(request, "Issue has been successfully saved!")
            return redirect('issu_lt.html')
        else:
            messages.error(request, "Book is not available to issue.")
            return redirect('issu_lt.html')

    context = {
            'sto': sto,
            'mem': mem,
    }
    return render(request, "issue/issu_entry.html",context)

def issu_ret(request, issu_id):
    iss_obj1 = issue.objects.filter(issu_id=issu_id, actual_date__isnull=True)
    if request.method == "POST":
        form_type = request.POST.get('form_type')
        if form_type == "actualdate":
            iss_obj = issue.objects.get(issu_id= issu_id, actual_date__isnull=True)
            print(iss_obj)
            actual_date = request.POST.get('actual_date')
            if iss_obj and actual_date:
                actual_date1 = datetime.strptime(actual_date, "%Y-%m-%d").date()
                iss_obj.actual_date = actual_date1
                iss_obj.save()
                messages.success(request, "Return entry has been recorded.")
                if iss_obj.fine == 0:
                    return redirect("issu_lt.html")
            else:
                messages.warning(request, "No book found to return.")

        elif form_type == "billing":
            iss_obj = issue.objects.get(issu_id=issu_id, paymth__isnull=True)
            paymth1 = request.POST.get('paymth')
            if iss_obj and paymth1:
                iss_obj.paymth = paymth1
                iss_obj.save()
                messages.success(request, "Payment method saved successfully.")
                return redirect("issu_lt.html")
            else:
                messages.warning(request, "No return entry found for payment.")

        else:
            messages.warning(request, "Invalid form submission.")

    return render(request, "issue/issu_ret.html", locals())

def tot_sup(request):
    amount=0
    quan1=0
    sup_en=0
    count_mem=0
    tot_fine=0
    book_obj=stock.objects.all()
    for i in book_obj:
        # book count and total amount
        amu=i.rate
        quan=i.qun
        res=amu*quan
        quan1=quan1 + quan
        amount=amount+res
    # total supplier entry
    for j in book_obj:
        supp=j.suppl_id.sup_name
        sup_en=sup_en+1
    #member count
    mem_dt=member.objects.all()
    for a in mem_dt:
        mem=a.member_id
        count_mem=count_mem+1
   # total fine calculate
    iss_tot=issue.objects.all()
    for b in iss_tot:
        fines=b.fine
        tot_fine=tot_fine+fines
    return render(request, 'more/tot_sup.html',locals())

def issu_retdt(request):
    isslist=issue.objects.filter(actual_date__isnull=True)
    return render(request, 'issue/issu_retdt.html',locals())
def sale_nw(request):
    mem_lst=member.objects.all()
    sto_lst=stock.objects.all()
    if request.method== "POST":
        memid=request.POST.get("memdt")
        tot=request.POST.get("total")
        print(memid)
        print(tot)
        invo_inf= sales.objects.create(
            mem_dt=request.POST.get("memdt"),
            dat = request.POST.get("dat"),
            tot= request.POST.get("total")
        )
        isbn_list=request.POST.getlist("isbn_dt[]")
        book_list = request.POST.getlist("book_dt[]")
        rate_list=request.POST.getlist("perunt[]")
        qun_list=request.POST.getlist("qunt[]")
        amt_list=request.POST.getlist("amount[]")
        print(isbn_list,book_list,rate_list,qun_list,amt_list)
        for bkisbn_dt, bktit_dt, perunt, qunt, amount in zip(isbn_list, book_list, rate_list, qun_list, amt_list):
            saledt.objects.create(
                invoice = invo_inf,
                bkisbn_dt=bkisbn_dt,
                bktit_dt=bktit_dt,
                perunt=perunt,
                qunt=qunt,
                amount=amount,
            )
    return render(request,'sales/sale_nw.html',locals())


def sale_list(request):
    inv_id= sales.objects.all()
    return render(request, "sales/sale_list.html",locals())
def vw_bill(request,invcno):
    inv_dt= get_object_or_404(sales, invcno=invcno)
    memdt= inv_dt.mem_dt
    memdt_obj = member.objects.get(member_id = memdt)
    saled = saledt.objects.filter(invoice = inv_dt)
    context = {
            'a': inv_dt,
            'b': memdt_obj,
            'c': saled,
    }

    return render(request, "sales/vw_bill.html", context)