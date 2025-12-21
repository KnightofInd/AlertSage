# tests/test_preprocess.py

import pytest

from triage.preprocess import clean_description


def test_clean_description_basic_lowercasing_and_strip():
    text = "  User CLICKED A Suspicious LINK   "
    cleaned = clean_description(text)
    assert isinstance(cleaned, str)
    # loose expectations so we don't overfit to implementation details
    assert "user" in cleaned
    assert "clicked" in cleaned
    assert "suspicious" in cleaned
    assert cleaned == cleaned.strip()
    assert cleaned.lower() == cleaned  # expect lowercased


def test_clean_description_removes_urls():
    text = "User clicked http://malicious.example.com in an email"
    cleaned = clean_description(text)
    # URL should not survive literally
    assert "http" not in cleaned
    assert "example.com" not in cleaned


def test_clean_description_handles_empty_string():
    cleaned = clean_description("")
    assert cleaned == ""


def test_clean_description_handles_whitespace_only():
    cleaned = clean_description("   \n\t   ")
    # Either empty string or something very small; just ensure no error
    assert isinstance(cleaned, str)
    assert cleaned.strip() == ""


def test_clean_description_is_idempotent():
    text = "User clicked a suspicious link."
    once = clean_description(text)
    twice = clean_description(once)
    assert once == twice