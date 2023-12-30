from django.shortcuts import render

posts = [
                {
                        'author': 'Alex Mwaniki',
                        'title': 'Full Stack Developer Roadmap',
                        'content': 'First post content',
                        'date_posted': 'August 27, 2021'
                },
                {
                        'author': 'Jane Doe',
                        'title': 'Blog Post 2',
                        'content': 'Second post content',
                        'date_posted': 'August 28, 2021'
                }
]

def home(request):
        context = {
                'posts': posts
        }
        return render(request, 'blog/home.html', context)

def about(request):
        return render(request, 'blog/about.html')