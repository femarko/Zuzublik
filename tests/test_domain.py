from src.app.domain import models


def test_create_zuzublik():
    result = models.create_zuzublik(title="test_title", url="test_url", xpath="test_xpath")
    assert isinstance(result, models.Zuzublik)
    assert result.title == "test_title"
    assert result.url == "test_url"
    assert result.xpath == "test_xpath"
