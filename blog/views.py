from django.shortcuts import render

posts = [
        {
                'author': 'Alex Mwaniki',
                'title': 'BackEnd Web Development',
                'content': 'What is BackEnd Web Development? Back-end web development is the server side of web programming. It consists of everything that the user can not see in the browser, like databases and servers. Back-end developers are responsible for building and maintaining technology that powers those components which, together, enable the user-facing side of the website to even exist in the first place.',
                'date_posted': 'December 31, 2023'
        },
        {
                'author': 'Alex Mwaniki',
                'title': 'FrontEnd Web Development',
                'content': 'What is FrontEnd Web Development? Front-end web development, also known as client-side development is the practice of producing HTML, CSS and JavaScript for a website or Web Application so that a user can see and interact with them directly.',
                'date_posted': 'December 31, 2023'
        },
        {
                'author': 'Alex Mwaniki',
                'title': 'FullStack Web Development',
                'content': 'What is FullStack Web Development? Full stack web development is the practice of developing both front and back end of a website. It is a combination of both programming and designing. It is a combination of both programming and designing.',
                'date_posted': 'December 31, 2023'
        },
        {
                'author': 'Alex Mwaniki',
                'title': 'Web Development',
                'content': 'What is Web Development? Web development is the work involved in developing a Web site for the Internet or an intranet. Web development can range from developing a simple single static page of plain text to complex web applications, electronic businesses, and social network services.',
                'date_posted': 'December 31, 2023'
        },
        {
                'author': 'Alex Mwaniki',
                'title': 'Web Design',
                'content': 'What is Web Design? Web design refers to the design of websites that are displayed on the internet. It usually refers to the user experience aspects of website development rather than software development. Web design used to be focused on designing websites for desktop browsers; however, since the mid-2010s, design for mobile and tablet browsers has become ever-increasingly important.',
                'date_posted': 'December 31, 2023'
        }
]

def home(request):
        context = {
                'posts': posts
        }
        return render(request, 'blog/home.html', context)

def about(request):
        return render(request, 'blog/about.html' , {'title': 'About'})