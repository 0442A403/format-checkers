import lxml.etree as etree

from checkers.checker import Checker


class XmlChecker(Checker):
    need_schema = True

    def __init__(self, schema: str):
        schema_root = etree.XMLSchema(etree.XML(schema))
        self.parser = etree.XMLParser(schema=schema_root)

    def validate_data(self, data: bytes) -> bool:
        try:
            etree.fromstring(data.decode('UTF-8'), parser=self.parser)
            return True
        except etree.XMLSyntaxError as e:
            return False
