from django.db import models


class Reading(models.Model):
    sensor = models.ForeignKey('Sensor')
    value = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        get_latest_by = 'id'

    def __unicode__(self):
        return u' %s ' % self.sensor + u' -> %s ' % self.value

    def get_fields(self):
        try:
            return [(field.name, field.value_to_string(self)) for field in Reading._meta.fields]
        except ValueError:
            return None


class Sensor(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    serial = models.CharField(max_length=255)
    sensor_type = models.ForeignKey('SensorType', blank=True, null=True)

    def __unicode__(self):
        return unicode(self.sensor_type) + ' - ' + unicode(self.title)

    def readings(self):
        return Reading.objects.filter(sensor=self)

    def latest_reading(self):
        return Reading.objects.filter(sensor=self).latest().value

    def get_fields(self):
        try:
            return [(field.name, field.value_to_string(self)) for field in Sensor._meta.fields]
        except ValueError:
            return None


class SensorType(models.Model):
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return unicode(self.title)

    def sensors(self):
        return Sensor.objects.filter(sensor_type=self)

    def get_fields(self):
        try:
            return [(field.name, field.value_to_string(self)) for field in SensorType._meta.fields]
        except ValueError:
            return None
