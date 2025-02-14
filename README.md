from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import google.generativeai as genai
import os


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyDY032c8BGyN-TfqazVu3br6WnuudKzZV0")
genai.configure(api_key=GEMINI_API_KEY)

@csrf_exempt  
def ai_chat(request):
    if request.method == "POST":
        user_message = request.POST.get('message', '').strip()

        if not user_message:
            return JsonResponse({'reply': "Error: No message received."}, status=400)

        try:
            model = genai.GenerativeModel("gemini-pro") 
            response = model.generate_content(user_message)
            
            ai_response = response.text if response else "Error: No response from AI"
            return JsonResponse({'reply': ai_response})

        except Exception as e:
            return JsonResponse({'reply': f"Error: {str(e)}"}, status=500)

    return render(request, "chat.html") 


