from django.shortcuts import render

# dummy data
posts = [
	{
		'Author' : 'Martin G.',
		'Title' : 'Post 1',
		'Content' : 'My Blog Post',
		'Date' : 'October 7 2019',
	},

	{
		'Author' : 'Elizabeth G.',
		'Title' : 'Post 2',
		'Content' : 'Her Blog Post',
		'Date' : 'October 7 2019',
	},
]

def home(request):
	context = {
		'posts' : posts
	}

	return render(request, 'blog/blog.html', context)


def about(request):
	return render(request, 'blog/about.html', 
		{'title' : 'About this Page'})