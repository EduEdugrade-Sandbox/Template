from src.release import is_semver


def test_release_tag_is_semver():
    assert is_semver("v1.2.3")


def test_release_tag_rejects_missing_v():
    assert not is_semver("1.2.3")
