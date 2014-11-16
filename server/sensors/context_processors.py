from sensors.settings import UPDATE


def expose_settings(request):
    return {
        'AJAX_SLEEP': UPDATE['AJAX']
    }
