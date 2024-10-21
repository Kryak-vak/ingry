from django.template.defaultfilters import slugify as django_slugify
from django.db.models import Model

menu = [
    {'title': 'Главная', 'url_name': 'ingredients'},
    {'title': 'Ингридиенты', 'url_name': 'ingredients'},
    {'title': 'Добавить ингредиент', 'url_name': 'add_ingredient'},
]


alphabet = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
            'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
            'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'y', 'э': 'e', 'ю': 'yu',
            'я': 'ya'}

def slugify(text: str, pk: int, model: Model) -> str:
    slug = django_slugify(''.join(alphabet.get(w, w) for w in text.lower()))

    slug_queryset = model.objects.filter(slug=slug).exclude(pk=pk)
    suffix = '' if len(slug_queryset) == 0 else f'-{len(slug_queryset)}'
    
    return f'{slug}{suffix}'