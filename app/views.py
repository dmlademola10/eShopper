from django.shortcuts import render


# Create your views here.
def signin(request):
    """
    This is the landing page for all users(Admins and Users alike). They are to input login details here,
    and they'll automatically get redirected to their respective destinations.
    """

    return render(request, "signin.html")
