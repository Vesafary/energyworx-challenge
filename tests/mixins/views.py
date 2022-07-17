from application.core.views import CreateView


class ViewsMixin:
    def create_url(self):
        body = {
            "url": "http://www.energyworx.com",
            "shortcode": "abc_12"
        }

        self.client.post("/shorten", body, content_type='application/json')

    def retrieve_url(self):
        self.client.get("/abc_12")
