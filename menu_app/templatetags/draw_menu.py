from django import template
from django.http import QueryDict
from menu_app.models import Menu, Item

register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu):
    items = Item.objects.filter(menu__name=menu).values()
    parents = items.filter(parent=None)

    try:
        selected_id = int(context['request'].GET['item_id'])
    except KeyError:
        return {'menu_items': parents}
    try:
        menu_items = get_tree(parents, items, selected_id)
    except:
        return {'menu_items': parents}

    return {
        'menu_items': menu_items
    }


def get_parent_id(items, item_id):
    item = items.get(id=item_id)

    if item['parent_id'] is not None:
        return get_parent_id(items, item['parent_id'])

    return item['id']


def get_tree(parents, items, selected_id):
    root_parent_id = get_parent_id(items, selected_id)
    selected_items = []
    for parent in parents:

        if parent['id'] == root_parent_id:

            parent = get_childes(items, root_parent_id , selected_id)
        selected_items.append(parent)

    return selected_items


def get_childes(items, root_parent_id, selected_item_id):
    childes = [child for child in items if child['parent_id'] == selected_item_id]

    parent_id = None
    for item in items:
        if item['id'] == selected_item_id:
            item['child_items'] = childes
            parent_id = item['parent_id']
            if root_parent_id == selected_item_id:
                return item
            else:
                return get_childes(items, root_parent_id, parent_id)
