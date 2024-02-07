from django.shortcuts import render ,redirect
from django.http import HttpResponse
from.models import Blog_Category , contact_info , blog_posts , comment


from.form import Blog_Form , BlogPost_Form
from django.shortcuts import redirect , get_object_or_404
from django.http import HttpResponseRedirect

from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    # return HttpResponse('This is home page')
    #fetch the data from db
    x=Blog_Category.objects.all()
    print (x)
    # mail=request.user.email
    # print(mail)
    return render(request,'myblogs/home.html',{"category":x})




@login_required(login_url='loginuser')
def contact(request):
    # return HttpResponse('<h1>This is contact page</h1>')
        if request.method == 'GET':
            return render(request, 'myblogs/contact.html')
        elif request.method == 'POST':
            email = request.POST.get('user_email')
            message = request.POST.get('message')
            x = contact_info(u_email=email, u_message=message)
            x.save()
            print(email)
            print(message)
            return render(request,'myblogs/contact.html',{'feedback':'Your message has been recorded'})


@login_required(login_url='loginuser')
def blog(request):
        x = Blog_Form()  
        if request.method == "GET":
            return render(request,'myblogs/blog.html',{"x":x})
        else:
            print("hi")
            form = Blog_Form(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                print("hi")
                return redirect('home')
            else:
                return render(request,'myblogs/blog.html',{"x":x})
            

@login_required(login_url='loginuser')
def ck(request):
    x = BlogPost_Form()
    return render(request,'myblogs/ck.html',{"x":x})




@login_required(login_url='loginuser')
def allblogs(request):
    x = blog_posts.objects.all()
    var = request.GET.get('category')
    print(var)
    if(var):
        x=blog_posts.objects.filter(blog_cat__blog_cat=var)
        print(x)
    else:
        x=blog_posts.objects.all()
        print(x)

    p = Paginator(x, 3)
    page_number = request.GET.get("page")
    page_obj = p.get_page(page_number)
    return render(request,'myblogs/allblogs.html',{"y":x})



@login_required(login_url='loginuser')
def blog_details(request, blog_id):
    obj = get_object_or_404(blog_posts, pk=blog_id)
    z=obj.views_count
    z=z+1
    obj.views_count=z
    obj.save()
    
    # if request.method == 'GET':
    #     return render(request,"{% url 'add_comment' obj.blog_name%}?blog_id={{obj.id}}", {"obj":obj})

    return render(request,'myblogs/blog_details.html',{"obj":obj})
    # print(obj)
    # print(blog_id)
# return render(request,'myblogs/blog_details.html',{"obj":obj})


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'myblogs/loginuser.html', {'form':AuthenticationForm()})
    else:
        a= request.POST.get('username') 
        b= request.POST.get('password') 
        user =authenticate(request,username=a,password=b)
        if user is None:
            return render(request,'myblogs/loginuser.html',{'form':AuthenticationForm(), 'error':'Invalid  Credentials'})
        else :
            login(request, user)
            return redirect('home')


def signupuser(request):
    if request.method =='GET':
        return render(request,'myblogs/signupuser.html',{'form':UserCreationForm()})
    else:
        a= request.POST.get('username') 
        b= request.POST.get('password1') 
        c= request.POST.get('password2') 
        if b==c:
            # check whether user name is unique
            if (User.objects.filter(username =a)):
                return render(request,'myblogs/signupuser.html',{'form':UserCreationForm(),'error': 'User Name  Already exists Try Again'})
            else :
                user =User.objects.create_user(username =a , password=b)
                user.save()
                login(request,user)
                return redirect('home')
        else:
            return render(request,'myblogs/signupuser.html',{'form':UserCreationForm(),'error': 'password Mismatch Try Again'})

def logoutuser(request):
    if request.method =='GET':
        logout(request)
        return redirect('home')
    


def blog(request):
    # Extract the category from the request parameters
    category_name = request.GET.get('category')

    # If a category is provided, filter blog posts by that category, otherwise, get all blog posts
    if category_name:
        blogs = blog_posts.objects.filter(blog_cat__blog_cat=category_name)
    else:
        blogs = blog_posts.objects.all()

    return render(request, 'myblogs/allblogs.html', {"blogs": blogs, "category": category_name})

def add_like(request, blog_id):
    obj = get_object_or_404(blog_posts, pk=blog_id)
    print (obj.like_count)
    y=obj.like_count
    y=y+1
    obj.like_count=y
    obj.save()
    return redirect('blog_details', obj.id)



def add_comment(request,blog_title):
    Blog_id=request.GET.get('blog_id')
    print(Blog_id)
    obj=get_object_or_404(blog_posts, pk=Blog_id)
    if(request.method == 'GET'):
        redirect('home')
        return render(request,'myblogs/blog_details.html', {"obj":obj})
    elif(request.method == 'POST'):
        x = request.POST.get('comment')
        print(x)
        # obj2=comment
        # obj2.comment_info=x
        # obj2.comment_email=request.user.email
        # obj2.comment_id=blog_title
        # title= str(blog_title)
        mail=request.user.email
        obj2 = comment(comment_email=str(request.user.email), comment_info=str(x),comment_id=obj)
        print(obj2.comment_email)
        obj2.save()
        print(obj2.comment_info)
        print(mail)
        print(obj2.comment_id)
        return render(request,'myblogs/blog_details.html', {"obj":obj})
    




