from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render,redirect,reverse
import time,datetime
from leaveapp import models
from user import models as umodels


class Judge_Add_Personal(MiddlewareMixin):

    def process_request(self, request):
        try:
            user = request.user
            umodel = umodels.Message.objects.get(user=user.id)
            model = models.Ratify.objects.get(name=umodel.name)
            x = model.due_date
            date2 = time.strftime('%Y-%m-%d', time.localtime(time.time()))
            b_date = datetime.date(*map(int, date2.split('-')))
            c = x - b_date
            if c <= 0:
                model.is_delete=1
                model.save()
        except Exception:
            pass


