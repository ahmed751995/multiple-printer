import frappe
from frappe.utils.print_format import print_by_server

def send_to_printers(doc, method=None):
    
    
    printer = ['pdf', 'raw']
    print_by_server(doc, 'all_items', printer[0])
    
    items = doc.items
    items_group = {}
    for item in items:
        if item.item_group not in items_group.keys():
            items_group[item.item_group] = [item]
        else:
            items_group[item['item_group']].append(item)
    # print(f'\n\n\n\n\n\n\n{items_group}\n\n\n\n')
    
    # print(f"\n\n\n\n\n{items_group}\n\n\n\n")
    for group in items_group.keys():
        # new_doc = dict(doc.as_dict())
        # new_doc['items'] = items_group[group]
        doc.items = items_group[group]
        # print(f"\n\n\n\n\n\n{doc.items}\n\n\n\n")
        print_by_server(doc, group, printer[0])
