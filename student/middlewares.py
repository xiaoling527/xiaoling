import time

from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin



class  TimeItMiddleware(MiddlewareMixin):
    def process_request(self,request):
        print("-----process_request------")
        self.start_time=time.time()
        return

    def process_view(self,request,func,*args,**kwargs):
        print("-----process_view------")
        if request.path != reverse('index'):
            return None

        start = time.time()
        response = func(request)
        costed = time.time()-start
        print('process view:{:.2f}s'.format(costed))
        return response

    def process_exception(self,request,exception):
        print("-----process_exception------")
        pass

    def process_template_response(self,request,response):
        print("-----process_template_response------")
        return response

    def process_response(self,request,response):
        print("-----process_response------")
        costed = time.time()-self.start_time
        print('request to response cose:{:.2f}s'.format(costed))
        return response
'''import time

from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse


class TimeItMiddleware(MiddlewareMixin):
    def process_request(self, request):
        return

    def process_view(self, request, func, *args, **kwargs):
        if request.path != reverse('index'):
            return None

        start = time.time()
        response = func(request)
        costed = time.time() - start
        print('{:.2f}s'.format(costed))
        return response

    def process_exception(self, request, exception):
        pass

    def process_template_response(self, request, response):
        return response

    def process_response(self, request, response):
        return response'''