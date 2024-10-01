from django.shortcuts import render

posts = [
    {
        'author': 'Deirbhile Larkin',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': '1st October 2024'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': '30th September 2024'
    },
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html',{'title':'About'})

