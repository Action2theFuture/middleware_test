class JSONMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.my_json_object = {
            "name" : "Doge",
            "age" : 5
        }
    
    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_template_response(self, _, response):
        response.context_data['my_json_object'] = self.my_json_object
        return response