import subprocess
from django.shortcuts import render

def ghunt_email_lookup(request):
    result = None

    if request.method == "POST":
        email = request.POST.get('email')

        # Command to run GHunt via subprocess
        try:
            # Example GHunt command, assuming ghunt is installed and set up
            command = ["ghunt", "email", email]
            result  = subprocess.check_output(command, universal_newlines=True)
        except subprocess.CalledProcessError as e:
            result = f"Error: {str(e)}"
    
    return render(request, 'ghunt_form.html', {'result': result})
