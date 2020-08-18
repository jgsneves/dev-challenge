from rest_framework import serializers
from api.models import Employer, MedicalLicense, Member, MemberData

class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = [
            'employer_name',
            'employer_code',
            'member_count',
            'thumbnail',
            'register_date',
        ]

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = [
            'member_name',
            'member_code',
            'member_personal_data',
            'thumbnailHd',
            'birthday',
        ]

class MedicalLicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalLicense
        fields = [
            'initial_date',
            'final_date',
            'time',
            'member_code',
        ]