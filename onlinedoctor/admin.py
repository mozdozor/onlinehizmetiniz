from django.contrib import admin
from .models import TimeScheduleModel, appointmentModel, bannerModel,alanModel,alanYazilarModel,CustomUserModel,CommentModel, deletedAppointmentModel
# Register your models here.


admin.site.register(bannerModel)
admin.site.register(alanModel)
admin.site.register(alanYazilarModel)
admin.site.register(CustomUserModel)
admin.site.register(CommentModel)
admin.site.register(TimeScheduleModel)
admin.site.register(appointmentModel)
admin.site.register(deletedAppointmentModel)