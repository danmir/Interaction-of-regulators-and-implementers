from django.db import models
from django.contrib.auth.models import User


class LVDiffEqSolution (models.Model):
    user = models.ForeignKey(User)
    init_condition_x = models.FloatField()
    init_condition_y = models.FloatField()
    init_param_a = models.FloatField()
    init_param_b = models.FloatField()
    init_param_c = models.FloatField()
    init_param_d = models.FloatField()

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return "/lotka_volterra/calc_result/{}".format(self.id)
