# tests/test_model_artifacts.py

import joblib
import numpy as np
import os

from triage.preprocess import clean_description


MODELS_DIR = os.path.join(os.path.dirname(__file__), "..", "models")


def test_model_artifacts_exist():
    vectorizer_path = os.path.join(MODELS_DIR, "vectorizer.joblib")
    model_path = os.path.join(MODELS_DIR, "baseline_logreg.joblib")

    assert os.path.exists(vectorizer_path), "vectorizer.joblib is missing"
    assert os.path.exists(model_path), "baseline_logreg.joblib is missing"


def test_model_can_predict_single_text():
    vectorizer = joblib.load(os.path.join(MODELS_DIR, "vectorizer.joblib"))
    clf = joblib.load(os.path.join(MODELS_DIR, "baseline_logreg.joblib"))

    text = "User received an email with a fake VPN login link."
    cleaned = clean_description(text)
    X = vectorizer.transform([cleaned])

    assert X.shape[0] == 1
    y_pred = clf.predict(X)
    assert len(y_pred) == 1
    assert isinstance(y_pred[0], str)

    # If classifier has probabilities, check they make sense
    if hasattr(clf, "predict_proba"):
        proba = clf.predict_proba(X)[0]
        assert isinstance(proba, np.ndarray)
        assert np.isclose(proba.sum(), 1.0, atol=1e-6)
        assert proba.shape[0] == len(clf.classes_)


def test_expected_classes_present():
    clf = joblib.load(os.path.join(MODELS_DIR, "baseline_logreg.joblib"))
    classes = set(clf.classes_)

    expected = {
        "phishing",
        "malware",
        "access_abuse",
        "data_exfiltration",
        "policy_violation",
        "web_attack",
        "benign_activity",
    }

    missing = expected - classes
    assert not missing, f"Missing expected classes: {missing}"