from triage.cli import (
    predict_with_uncertainty,
    load_artifacts,
)


def test_cli_prediction_structure():
    vectorizer, clf, embedder, classes = load_artifacts()

    text = "User reported a suspicious email with a fake login page."
    result = predict_with_uncertainty(text, vectorizer, clf, embedder, classes)

    # Check core keys exist (aligned with actual result dict)
    for key in [
        "raw_text",
        "cleaned",  # NOTE: matches your current result dict
        "base_label",
        "final_label",
        "max_prob",
        "probs_sorted",
        "threshold",
    ]:
        assert key in result

    assert result["raw_text"] == text
    assert isinstance(result["cleaned"], str)
    assert 0.0 <= result["max_prob"] <= 1.0

    # probs_sorted: should be non-empty, sorted desc, labels valid
    probs = result["probs_sorted"]
    assert 0 < len(probs) <= len(classes)

    labels_from_probs = [lbl for lbl, _ in probs]
    assert all(lbl in classes for lbl in labels_from_probs)

    probs_only = [p for _, p in probs]
    assert probs_only == sorted(probs_only, reverse=True)
