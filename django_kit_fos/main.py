from django.http import HttpResponse
from django.urls import resolve, reverse, NoReverseMatch, path


def triggerable(view_func):
    """
    Wrap a view function to be used with djapified feature.
    :param view_func:
    :return:
    """
    setattr(view_func, 'triggerable__', True)
    return view_func


@triggerable
def trigger_request_via_url_name(request, url_name: str):
    try:
        view_func = resolve(reverse(url_name)).func
    except NoReverseMatch:
        return HttpResponse(f"URL name '{url_name}' does not exist.", status=404)
    if not getattr(view_func, 'triggerable__', False):
        raise ValueError('This view function is not wrapped for djapified feature.')
    return view_func(request)


trigger_pattern = [
    path('trvun/', trigger_request_via_url_name, name='trigger_request_via_url_name'),
]
