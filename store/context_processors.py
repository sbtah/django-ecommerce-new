from store.models import Category


# This output categories objects to all templates via context manager in settings.
def categories(request):

    return {
        'categories': Category.objects.all(),
        'categories_number': Category.objects.all().count()
    }
