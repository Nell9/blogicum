import html
from django import template

register = template.Library()


@register.filter(is_save=True)
def original_text_format(value):
    value = html.escape(value)
    # Если мы хотим сохранить полностью оригинальное форматирование,
    # то стоит добавить строку:
    # value = value.replace(' ', '&nbsp;'),
    # но в таком случае не проходит pytest.
    value = value.replace('\t', '&nbsp;&nbsp;&nbsp;&nbsp;')
    value = value.replace('\n', '<br>')
    return value
