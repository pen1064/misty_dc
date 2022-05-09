from pickle import FALSE
from apps.endpoints.models import Endpoints, MLAlgorithm, MLAlgorithm_Status

class MLRegistry:
    def __init__(self):
        self.endpoints={}
        self.alg_created = FALSE

    def add_algorithm(self, endpoint_name, alg_obj, alg_name, alg_status, alg_ver, alg_owner, alg_description, alg_code):
        endpoint, _ = Endpoints.objects.get_or_create(name=endpoint_name, owner=alg_owner)

        db_obj, alg_created = MLAlgorithm.objects.get_or_create(name=alg_name, code = alg_code, description=alg_description, version = alg_ver, parent_endpoint = endpoint)
        self.alg_created = alg_created
        print(alg_created)
        if alg_created:
            status = MLAlgorithm_Status(status = alg_status, user = alg_owner, parent_mlalgorithm = db_obj, active=True)
            status.save()
            print(status.active)
        self.endpoints[db_obj.id] = alg_obj
