from sklearn.ensemble import RandomForestClassifier

import joblib


class Machine:

    def __init__(self, df):
        self.name = 'Random Forest Classifier'
        target = df['Rarity']
        features = df.drop(columns=['Rarity', '_id', 'Name',
                                    'Damage', 'Timestamp'], errors='ignore')
        features = features.fillna(0)
        self.features = features.columns.tolist()
        self.model = RandomForestClassifier()
        self.model.fit(features, target)

    def __call__(self, feature_basis):
        preds = self.model.predict(feature_basis[self.features])
        probs = self.model.predict_proba(feature_basis[self.features])
        pred_probs = [probs[i][list(self.model.classes_).index(pred)]
                      for i, pred in enumerate(preds)]
        return preds, pred_probs

    def save(self, filepath):
        data = {
            'model': self.model,
            'features': self.features,
            'name': self.name
        }

        joblib.dump(data, filepath)

    @staticmethod
    def open(filepath):
        data = joblib.load(filepath)
        machine = Machine.__new__(Machine)
        machine.model = data['model']
        machine.features = data['features']
        machine.name = data['name']
        return machine

    def info(self):
        return f"{self.name} trained with {len(self.features)} features."
