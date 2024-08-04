from django.shortcuts import redirect

def explorer_redirect(request):
    return redirect(
        "/explorer"
    )
