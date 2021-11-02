from django.http import HttpResponse
from django.shortcuts import redirect

def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):
			if request.user.is_authenticated:
				
				group = None
				if request.user.groups.exists():
					group = request.user.groups.all()[0].name

				if group in allowed_roles:
					return view_func(request, *args, **kwargs)
				else:
					return HttpResponse("You are not allowed to view the content")
			else:
				return redirect("login")

		return wrapper_func
	return decorator
