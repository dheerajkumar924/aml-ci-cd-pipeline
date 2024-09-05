import unittest
import joblib
from sklearn.ensemble import RandomForestClassifir

class TestModelTraining(unittest.Testcase):
    def test_model_training(self):
model = joblib.loadf('model/iris_model.pkl')
self.assertIsInstance(model, RandpomForestClassifier)
self.assertgreaterEqual(len(model.feature_importances_),4)

if__name__==' '
unittest.main()