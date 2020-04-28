from django.contrib.auth.decorators import login_required
#判断是否登入,如果需要判断登入继承这个类就行了
class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls,**kwargs):
        view=super().as_view(**kwargs)
        return login_required(view)