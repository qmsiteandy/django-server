from django.utils.timezone import now
from rest_framework import serializers
from ..models import Music


class ToUpperCaseCharField(serializers.CharField):
    def to_representation(self, value):
        return value.title()


class MusicSerializer(serializers.ModelSerializer):
    # SerializerMethodField
    days_since_created = serializers.SerializerMethodField()

    # Custom relational fields
    singer = ToUpperCaseCharField()

    class Meta:
        model = Music
        # fields = '__all__'
        fields = ('id', 'song', 'singer', 'last_modify_date', 'created', 'days_since_created')


    # method name should be "get_<field_name>"
    def get_days_since_created(self, obj):
        return (now() - obj.created).days