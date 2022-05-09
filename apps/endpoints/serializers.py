from rest_framework import serializers
from apps.endpoints.models import Endpoints, MLAlgorithm, MLAlgorithm_Status, MLRequest

class EndpointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endpoints
        read_only_fields = ('id', 'name', 'owner', 'created_date')
        fields = read_only_fields

class MLAlgorithmSerializer(serializers.ModelSerializer):
    #current_status = serializers.SerializerMethodField(read_only=True)

    def get_current_status(self, mlalgorithm):
        return MLAlgorithm_Status.objects.filter(parent_mlalgorithm = mlalgorithm).latest('created_date').status

    class Meta:
        model = MLAlgorithm
        read_only_fields=('id', 'name', 'code','description', 'version', 'created_date', 'parent_endpoint')
        fields = read_only_fields

class MLAlgorithm_StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MLAlgorithm_Status
        read_only_data = ('id', 'active')
        fields = ('id', 'active', 'status', 'created_date', 'parent_mlalgorithm')
    
class MLRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MLRequest
        read_only_fields = ("id","input_data","response","full_response",
        "created_date", "parent_mlalgorithm")

        fields =  ("id","input_data","response","full_response",
        "created_date", "parent_mlalgorithm")