from app.service_layer import app_manager
import pathlib

def test_add_zuzublik():
    test_file = pathlib.Path(__file__).parent.parent / "test_file.xls"
    fake_parser = lambda x: {"title": "title", "url": "url", "xpath": "xpath"}
    fake_validator = lambda x: {"title": "title", "url": "url", "xpath": "xpath"}
    fake_uow = lambda: None
    app_manager.add_zuzublik(file=test_file, parser=fake_parser, validator=fake_validator, uow=fake_uow)