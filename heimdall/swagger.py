from drf_spectacular.views import SpectacularSwaggerView
from collections import defaultdict

class CustomSwaggerView(SpectacularSwaggerView):
    def get_swagger_ui_settings(self):
        urls = self.get_urls()
        return {'urls': self.group_urls_by_app(urls)}

    def get_urls(self):
        return self.generator.get_schema().get('paths', {})

    def group_urls_by_app(self, urls):
        grouped_urls = defaultdict(dict)

        for path, path_data in urls.items():
            app_label = self.get_app_label_from_path(path)
            if app_label:
                grouped_urls[app_label][path] = path_data

        return grouped_urls

    def get_app_label_from_path(self, path):
        parts = path.strip('/').split('/')
        if len(parts) >= 2:
            return parts[0]  # Assuming the app name is the first part of the URL
        return None