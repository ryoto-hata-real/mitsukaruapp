from django.contrib.auth.models import User
from django.core import paginator
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from product.models import LanguageTagMaster, Product, LevelTagMaster, ContentTagMaster, Review
from mainapp.forms import ChangeUserNameForm, UserCreationForm
from django.core.mail import send_mail
import os

from django.core.paginator import Paginator

def index(request):
    level_tag = ''
    language_tag = ''
    content_tag = ''
    if 'level_tag' in request.GET or 'language_tag' in request.GET or 'content_tag' in request.GET:
        
        if 'level_tag' in request.GET:
            level_tag = request.GET['level_tag']
        if 'language_tag' in request.GET:
            language_tag = request.GET['language_tag']
        if 'content_tag' in request.GET:
            content_tag = request.GET['content_tag']

        products = Product.objects.filter(level_tags__icontains=level_tag,language_tags__icontains=language_tag,content_tags__icontains=content_tag).order_by('score').reverse()
        product_count = products.count()
    else:
        products = Product.objects.all().order_by('score').reverse()
        product_count = products.count()
    
    level_tag_list = LevelTagMaster.objects.all()
    language_tag_list = LanguageTagMaster.objects.all()
    content_tag_list = ContentTagMaster.objects.all()

    paginator = Paginator(products,50)
    page_number = request.GET.get('page')

    context = {
        'level_tag' : level_tag,
        'language_tag' : language_tag,
        'content_tag' : content_tag,
        'level_tag_list':level_tag_list,
        'language_tag_list':language_tag_list,
        'content_tag_list':content_tag_list,
        'page_obj' : paginator.get_page(page_number),
        'page_number' : page_number,
        'count' : product_count
    }
    return render(request,'mainapp/index.html',context)


class Login(LoginView):
    template_name = 'mainapp/auth.html'
    def post(self, request, *args, **kwargs):
        return redirect('/')


def signup(request):
    context = {}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('/')
    return render(request, 'mainapp/auth.html', context)


def contact(request):
    context={}
    #------Email--------------
    if request.method == "POST":
            subject = 'MITSUMARU：お問合せがありました。'
            message = """名前：{}
メールアドレス：{}
内容：""".format(
                request.POST.get('name'), 
                request.POST.get('email'),
                request.POST.get('contact')
            )
            email_from = os.environ['EMAIL_HOST_USER']
            email_to = [
                os.environ['EMAIL_HOST_USER']
            ]
            send_mail(subject, message, email_from, email_to)
            return redirect('/contact-done')
    #------Email---------

    return render(request, 'mainapp/contact.html', context)

def contactDone(request):
    context={
        "message":"お問い合わせが完了いたしました。引き続き、MITSUKARUをよろしくお願いいたします。",
    }
    return render(request, 'mainapp/contact.html', context)

def term(request):
    context={}
    return render(request, 'mainapp/term.html', context)


def privacy(request):
    context={}
    return render(request, 'mainapp/privacy.html', context)

def profile(request):
    user = request.user
    if request.method == 'POST':
        form = ChangeUserNameForm(request.POST)
        if form.is_valid():
            user.name = request.POST['name']
            user.save()
            return redirect('/')
        else:
            return redirect('/profile')
    context = {
        'user' : user,
    }

    return render(request, 'mainapp/profile.html', context)