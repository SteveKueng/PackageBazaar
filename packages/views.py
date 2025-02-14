import base64
from django.shortcuts import render
from .models import MunkiRepo

from django.conf import settings

def package_list_view(request):
    """Get all catalogs and packages from the Munki repo"""

    app_name = getattr(settings, "APP_NAME", "PackageBazaar")

    catalog = []
    catalogs_to_display = settings.CATALOGS_TO_DISPLAY
    for catalog_to_display in catalogs_to_display:
        catalog += MunkiRepo.read('catalogs', catalog_to_display)

        itemlist = []
    package_dict = {}  # Dictionary for quick lookup of package names

    for item in catalog:
        package_name = item['name']

        if package_name in package_dict:
            # If the package already exists, update the version in catalogs
            existing_package = package_dict[package_name]
            catalogs = item.get('catalogs', [])

            for catalog in catalogs:
                if catalog not in catalogs_to_display:
                    continue

                catalog_version = {
                    'name': catalog,
                    'version': item['version']
                }
                
                # Check if the catalog already exists, then overwrite the version
                for existing_catalog in existing_package['catalogs']:
                    if existing_catalog['name'] == catalog:
                        existing_catalog['version'] = item['version']
                        break
                else:
                    # If the catalog does not exist, add it
                    existing_package['catalogs'].append(catalog_version)

        else:
            # Create a new package entry
            package_item = {
                'name': item['name'],
                'display_name': item.get('display_name', item['name']),
                'version': item['version'],
                'developer': item.get('developer', None),
                'categorie': item.get('categorie', None),
                'catalogs': [],
                'description': item.get('description', ''),
                'icon': 'data:image/png;base64,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'  # Default value for the icon
            }

            # Add catalogs and ensure only one version per catalog exists
            catalogs = item.get('catalogs', [])
            for catalog in catalogs:
                if catalog not in catalogs_to_display:
                    continue
                
                catalog_version = {
                    'name': catalog,
                    'version': item['version']
                }
                package_item['catalogs'].append(catalog_version)

            # Load the icon as a Base64-encoded string
            icon_name = item.get('icon_name', item['name'] + '.png')
            icon_list = MunkiRepo.list('icons')

            if icon_name in icon_list:
                icon_path = MunkiRepo.get('icons', icon_name)
                
                # Check if `MunkiRepo.get()` returns a file path or bytes
                if isinstance(icon_path, str):  # If it's a file path, open the file
                    try:
                        with open(icon_path, "rb") as icon_file:
                            encoded_icon = base64.b64encode(icon_file.read()).decode("utf-8")
                            package_item['icon'] = f"data:image/png;base64,{encoded_icon}"
                    except FileNotFoundError:
                        package_item['icon'] = None
                else:
                    # If MunkiRepo.get() directly returns bytes
                    package_item['icon'] = f"data:image/png;base64,{base64.b64encode(icon_path).decode('utf-8')}"

            # Store the package in the dictionary and add it to the list
            package_dict[package_name] = package_item
            itemlist.append(package_item)

    return render(request, "packages/package_list.html", {
        "packages": itemlist,
        "app_name": app_name
    })