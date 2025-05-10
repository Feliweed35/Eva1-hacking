from rest_framework import serializers

class ScanRequestSerializer(serializers.Serializer):
    tool = serializers.ChoiceField(choices=['google_dorks', 'dns', 'whois', 'nmap'])
    target = serializers.CharField()

class ScanResponseSerializer(serializers.Serializer):
    tool = serializers.CharField()
    target = serializers.CharField()
    output = serializers.CharField()
    status = serializers.CharField()
