from django import template
from django.template.defaultfilters import stringfilter
from datetime import datetime
from django.utils import timezone
# from dateutil.parser import parse
# from dateutil.utils

register = template.Library()


@register.filter("date_maker")
@stringfilter
def date_maker(value: str):
    return "-".join(reversed(value[:10].split("-")))


@register.filter("country_list")
def country_list(value: str):
    contry = [
                            'Cameroun',
                            'Algérie', 
                            'Angola',
                            'Bénin',
                            'Botswana',
                            'Burkina Faso',
                            'Burundi',
                            'Cabo Verde',
                            'République centrafricaine',
                            'Tchad',
                            'Comores',
                            'République du Congo',
                            'République démocratique du Congo',
                            'Côte d\'Ivoire',
                            'Djibouti',
                            'Égypte',
                            'Érythrée',
                            'Éthiopie',
                            'Gabon',
                            'Gambie',
                            'Ghana',
                            'Guinée',
                            'Guinée-Bissau',
                            'Guinée équatoriale',
                            'Kenya',
                            'Lesotho',
                            'Libéria',
                            'Libye',
                            'Madagascar',
                            'Malawi',
                            'Mali',
                            'Mauritanie',
                            'Maurice',
                            'Maroc',
                            'Mozambique',
                            'Namibie',
                            'Niger' ,
                            'Ouganda',
                            'Rwanda',
                            'Sao Tomé-et-Principe',
                            'Sénégal',
                            'Seychelles',
                            'Sierra Leone',
                            'Somalie',
                            'Afrique du Sud',
                            'Soudan',
                            'Soudan du Sud',
                            'Eswatini',
                            'Tanzanie',
                            'Togo',
                            'Tunisie',
                            'Ouganda',
                            'Zambie',
                            'Zimbabwe',
    ]
    return contry




@register.filter("wrap_content")
@stringfilter
def wrap_content(value, count):
    return value[:count] + "..."


@register.filter("filter_selected")
@stringfilter
def filter_selected(value, selected_type):

    return "" if selected_type != value else "selected"


@register.filter("value_in_list")
def value_in_list(lites: list[dict], value: str):
    print(lites)
    return [date_maker(val[value]) for val in lites]


@register.filter("dict_values")
def dict_values(value: dict):
    return value.values()

@register.filter("event_status")
@stringfilter
def event_status(startDate, endDate):
    startDate = datetime.strptime(str(startDate)[:-6], "%Y-%m-%d %H:%M:%S")
    endDate = datetime.strptime(str(endDate)[:-6], "%Y-%m-%d %H:%M:%S")

    startDate = timezone.make_aware(startDate, timezone.get_default_timezone())
    endDate = timezone.make_aware(endDate, timezone.get_default_timezone())
    now = timezone.now()
    if startDate < now and now < endDate:
        return "Évènement en cours"
    if startDate > now:
        return "Évènement à venir"
    else:
        return "Évènement passée" 
