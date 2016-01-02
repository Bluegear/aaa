from mcweb.models import Merchant
from rest_framework import serializers


class MerchantSerializer(serializers.Serializer):
    display_name = serializers.CharField(
            max_length=Merchant._meta.get_field('display_name').max_length,
            required=True,
    )

    def create(self, validated_data):
        return Merchant.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.display_name = validated_data.get('display_name', instance.display_name)
        instance.save()
        return instance
