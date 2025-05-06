# views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .automation import (
    get_linkedin_url_from_page,
    scrape_employees_with_arc,
    get_email_with_skrapp,
    testLinkedinScraper
)


@csrf_exempt
def extract_linkedin_link(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        page_url = data.get('url')

        if not page_url:
            return JsonResponse({'error': 'URL manquante'}, status=400)

        linkedin_url = get_linkedin_url_from_page(page_url)

        if linkedin_url:
            return JsonResponse({'linkedin_url': linkedin_url})
        else:
            return JsonResponse({'error': 'Lien LinkedIn introuvable'}, status=404)


@csrf_exempt
def extract_employees_from_linkedin(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        linkedin_url = data.get('linkedin_url')

        if not linkedin_url:
            return JsonResponse({'error': 'Lien LinkedIn manquant'}, status=400)

        success = scrape_employees_with_arc(linkedin_url)

        return JsonResponse({'status': 'ok' if success else 'fail'})


@csrf_exempt
def extract_email_from_linkedin(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        linkedin_url = data.get('linkedin_url')

        if not linkedin_url:
            return JsonResponse({'error': 'Lien LinkedIn manquant'}, status=400)

        email = get_email_with_skrapp(linkedin_url)

        if email:
            return JsonResponse({'email': email})
        else:
            return JsonResponse({'error': 'Email introuvable'}, status=404)
@csrf_exempt
def testLinkedin(request):
    if request.method == 'GET':
        success = testLinkedinScraper()
        return JsonResponse({'status': 'ok' if success else 'fail'})
