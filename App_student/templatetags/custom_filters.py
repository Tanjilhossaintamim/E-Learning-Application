from django import template
from App_teacher.models import QuizAnswar,Quiz


register = template.Library()

@register.filter
def range_filter(value):
    if len(value)<300:
        return value
    return value[0:300]+'   - - - - - - - - - - - -- - - - -'

@register.filter
def mark_count(user):
    return QuizAnswar.objects.filter(user=user).count()



