from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect
import requests
from requests.structures import CaseInsensitiveDict
import urllib3

# let data = {
#     'file': file,
#     'fileName': file.name,
# };
# // You have to download 3rd Cookies library
# // https://docs.djangoproject.com/en/dev/ref/csrf/#ajax
# let csrftoken = Cookies.get('csrftoken');
# let response = fetch("/upload/", {
#     method: 'POST',
#     body: JSON.stringify(data),
#     headers: { "X-CSRFToken": csrftoken },
# })
def list_standupCards(request):

    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    
    with requests.session() as requests_session:   
        # requests_session = requests.session()
        url = 'http://127.0.0.1:8000/'
        csrftoken =requests_session.get('http://127.0.0.1:8000/profile/').cookies['csrftoken']
        try:
            response = requests.get(url + 'api/standup-cards/', headers={'X-CSRFToken': csrftoken})
        except Exception as e:
            print(e)
        cards = response.json()

    return render(request, 'standup_card/list_standup_cards.html',{'cards':cards} )  
