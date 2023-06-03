from django.db import models


class machine_info(models.Model):
    objects = models.Manager()
    machine_id = models.CharField(max_length=20)
    machine_name = models.CharField(max_length=50)
    machine_url = models.CharField(max_length=50)
    machine_image = models.CharField(max_length=150)
    machine_model = models.CharField(max_length=20)
    location = models.CharField(max_length=50)
    set_points = models.TextField()
    sensor = models.TextField()
    compressor = models.TextField()
    pressure = models.TextField()
    water = models.TextField()
    dosing = models.TextField()
    pump = models.TextField()
    pp3 = models.TextField()
    subzero = models.TextField(default=[])

    def __str__(self):
        return self.machine_name


class machine_data(models.Model):
    objects = models.Manager()
    time_stamp = models.CharField(max_length=180, blank=True, default=None, null=True)
    machine_id = models.CharField(max_length=20, blank=True, default=None, null=True)
    location = models.CharField(max_length=50, blank=True, default=None, null=True)
    Default_Temperature = models.IntegerField( blank=True, default=None, null=True)
    Default_Humidity = models.IntegerField( blank=True, default=None, null=True)
    Set_Temperature_H = models.IntegerField(blank=True, default=None, null=True)
    Set_Temperature_L = models.IntegerField( blank=True, default=None, null=True)
    Set_Humidity_H = models.IntegerField(blank=True, default=None, null=True)
    Set_Humidity_L = models.IntegerField( blank=True, default=None, null=True)
    Temperature = models.IntegerField(blank=True, default=None, null=True)
    Humidity = models.IntegerField(blank=True, default=None, null=True)
    Compressor_1 = models.CharField(max_length=10, blank=True, default=None, null=True)
    Compressor_2 = models.CharField(max_length=10, blank=True, default=None, null=True)
    LP_1 = models.CharField(max_length=10, blank=True, default=None, null=True)
    LP_2 = models.CharField(max_length=10, blank=True, default=None, null=True)
    HP_1 = models.CharField(max_length=10, blank=True, default=None, null=True)
    HP_2 = models.CharField(max_length=10, blank=True, default=None, null=True)
    Water_Level = models.CharField(max_length=10, blank=True, default=None, null=True)
    Upper_Tank_Level = models.CharField(max_length=10, blank=True, default=None, null=True)
    Water_State = models.CharField(max_length=20, blank=True, default=None, null=True)
    Dosing_Level = models.CharField(max_length=10, blank=True, default=None, null=True)
    Flow = models.FloatField(blank=True, default=None, null=True)
    Pump1Status = models.CharField(max_length=10, blank=True, default=None, null=True)
    Pump2Status = models.CharField(max_length=10, blank=True, default=None, null=True)
    Pump3Status = models.CharField(max_length=10, blank=True, default=None, null=True)
    ThreePhasePreventer = models.CharField(max_length=10, blank=True, default=None, null=True)
    th_sensor_status = models.CharField(max_length=10, blank=True, default=None, null=True)
    temp_subzero = models.CharField(max_length=10, blank=True, default=None, null=True)
    hum_subzero = models.CharField(max_length=10, blank=True, default=None, null=True)

    def __str__(self):
        return self.machine_id