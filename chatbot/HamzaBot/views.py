from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

import os
import openai

openai.api_key =" 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"


# Create your views here.
def HamzaBot(request):
        return render(request, "index.html")
def about(request):
        return render(request, "about.html")

def chatAPI(request):
    if request.method == "POST":
        prompt = request.POST.get("prompt")
        if prompt:
            # Create a message object with the user's prompt
            messages = [{"role": "user", "content": prompt}]

            # Make the API call with the 'messages' property
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=1,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            
            )

            # Extract the generated response from the API response
            if response and 'choices' in response:
                generated_response = response['choices'][0]['message']['content']
                return JsonResponse({"choices": [{"message": {"content": generated_response}}]})
            else:
                return JsonResponse({"error": "Invalid API response"})
        else:
            return JsonResponse({"error": "No prompt provided in the request"})
    return JsonResponse({"error": "Bad Request"})
