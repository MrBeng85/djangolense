from django.shortcuts import redirect, render, get_object_or_404
from .models import Article, CustomUser
from .forms import ArticleForm, ProfileImageForm
from itertools import chain

articles = Article.objects.all()

def acceuil(request):
    return render(request, 'app/acceuil.html')

def home(request):
    articles = Article.objects.all()
    if request.method == 'GET':
        name = request.GET.get('recherche')
        if name != None:
            name = name.lower()

            articles_by_title = Article.objects.filter(title__icontains=name)

            users = CustomUser.objects.filter(username__icontains=name)

            articles_by_user = Article.objects.filter(user__in=users)

            articles = list(chain(articles_by_title, articles_by_user))

    context = {'articles': articles}

    return render(request, 'app/home.html', context=context)

def article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'app/article.html', context={'article': article})

def profile(request, user_id):
    try:
        user = CustomUser.objects.get(pk=user_id)
    except:
        return redirect('account_login')
    if '/image' in request.path:
        if request.user.id != user_id:
            return redirect('account_login')
        if request.method == 'POST':
            form = ProfileImageForm(request.POST, request.FILES, instance=user)
            if form.is_valid():
                form.save()
                return redirect('app-profile', user_id=user.pk)
        else:
            form = ProfileImageForm(instance=request.user)
        return render(request, 'app/image_profile.html', context={'user' : user, 'form': form})
    else:
        self_articles = Article.objects.filter(user=CustomUser.objects.get(pk=user_id))
        return render(request, 'app/profile.html', context={'user' : user, 'articles': self_articles})

def edit(request, slug):
    user = request.user
    if user.__str__() == "AnonymousUser":
        return redirect('account_login')
    
    if slug == 'append_article':
        initial = {'user': user, 'title': 'Inserez un titre ici', 'content': 'Inserez votre contenu ici'}
        form = ArticleForm(initial=initial)
        if request.method == 'POST':
            print( 'ArticleForm(request.POST).data -------------------------->' ,ArticleForm(request.POST).data)
            if ArticleForm(request.POST).data.get('title') != initial.get('title') or ArticleForm(request.POST).data.get('content') != initial.get('content'):
                article = ArticleForm(request.POST).save(commit=False)
                article.user = user
                article.save()
                return redirect('app-profile', user_id=user.id)
            else:
                return redirect('app-profile', user_id=user.id)
            
    else:
        article = get_object_or_404(Article, slug=slug)
        if article.user.username != user.username and not user.is_superuser:
            return redirect('account_login')
        
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('app-profile', user_id=user.id)
        else:
            form = ArticleForm(instance=article)
    
    context = {'form': form}
    return render(request, 'app/edit.html', context=context)

def delete(request, pk):
    user = request.user
    article = get_object_or_404(Article, pk=pk)
    if user.__str__() == "AnonymousUser" or article.user != user:
        return redirect('account_login')    
    if request.method == 'POST':
        article.delete()
        return redirect('app-profile', user_id=user.id)
    return render(request, 'app/delete.html', context={'article': article})