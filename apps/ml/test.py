# add at the beginning of the file:
from django.test import TestCase
import inspect
from apps.ml.registry import MLRegistry
from apps.ml.classifier.xgb_model import XGBClassifier

class Add(TestCase):
# add below method to MLTests class:
    def test_registry(self):
        registry = MLRegistry()
        self.assertEqual(len(registry.endpoints), 0)
        endpoint_name = "classifier"
        algorithm_object = XGBClassifier()
        algorithm_name = "xgb"
        algorithm_status = "production"
        algorithm_version = "0.0.1"
        algorithm_owner = "Pusheen"
        algorithm_description = "xgbwith simple pre- and post-processing"
        algorithm_code = inspect.getsource(XGBClassifier)
        # add to registry
        registry.add_algorithm(endpoint_name, algorithm_object, algorithm_name,
                    algorithm_status, algorithm_version, algorithm_owner,
                    algorithm_description, algorithm_code)
        # there should be one endpoint available
        self.assertEqual(len(registry.endpoints), 1)
        self.assertEqual(registry.alg_created, True)