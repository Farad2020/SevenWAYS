from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

# Create your views here.
from MainApp.models import *

"""
try:
    ...
except:
    raise Http404("Page not found")
return (return regular statement)


# object = get_object_or_404(object, statement) 
"""

# Maybe use smaller list, that could be loaded by the press of a button, or going to the next page
def index(request):
    places = Place.objects.all()
    place_and_comments = {}
    for place in places:
        place_and_comments[place] = find_bad_comments_num(place)

    place_and_comments = {k: v for k, v in sorted(place_and_comments.items(), key=lambda item: item[1], reverse=True)}
    places_sorted_by_negative = place_and_comments.keys()
    print(places_sorted_by_negative)
    # articles = Article.objects.all().exclude(is_active=False).order_by('article_date')[:4]
    return render(request, 'MainApp/homepage.html', {'places': places,
                                                     'places_sorted_by_negative': places_sorted_by_negative,
                                                     })


def find_bad_comments_num(place):
    comments = Review.objects.filter(place_id=place.id)
    good_comments = []
    tolerable_comments = []
    impossible_comments = []
    for comm in comments:
        if "Good" in comm.reviewers_attitude:
            good_comments.append(comm)
        elif "Impossible" in comm.reviewers_attitude:
            impossible_comments.append(comm)
        else:
            tolerable_comments.append(comm)
    return impossible_comments.__len__()


def get_all_places(request):
    """
    places = Place.objects.filter().order_by('game_name')
    week_days = ["Monday", "Tuesday", "Wednesday", "Thursday",
                  "Friday", "Saturday", "Sunday", ]
    return render(request, "game_pages/games_page.html", {'games': games,
                                                          'week_days': week_days})
"""


def place_details(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    place.save()
    work_time = WorkTime.objects.filter(place_id=place_id)
    comments = Review.objects.filter(place_id=place_id)
    place_image = PlaceImages.objects.filter(place_id=place_id)
    #good_comments1 = Review.objects.filter(place_id=place_id, )
    good_comments = []
    tolerable_comments = []
    impossible_comments = []
    for comm in comments:
        if "Good" in comm.reviewers_attitude:
            good_comments.append(comm)
        elif "Impossible" in comm.reviewers_attitude:
            impossible_comments.append(comm)
        else:
            tolerable_comments.append(comm)
    return render(request, "MainApp/place_page.html", {'place': place,
                                                       'work_time': work_time,
                                                       'comments': comments,
                                                       'place_image': place_image,
                                                       'good_comments': good_comments.__len__(),
                                                       'tolerable_comments': tolerable_comments.__len__(),
                                                       'impossible_comments': impossible_comments.__len__(),
                                                       })
