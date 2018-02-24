from typing import List
from etk.extractor import Extractor
from etk.etk_extraction import Extraction, Extractable


class HTMLMetadataExtractor(Extractor):
    """
    Extracts META, microdata, JSON-LD and RDFa from HTML pages.

    Uses https://stackoverflow.com/questions/36768068/get-meta-tag-content-property-with-beautifulsoup-and-python to
    extract the META tags

    Uses https://github.com/scrapinghub/extruct to extract metadata from HTML pages
    """

    def __init__(self):
        pass

    @property
    def input_type(self):
        """
        The type of input that an extractor wants
        Returns: HTML text
        """
        return self.InputType.HTML

    # @property
    def name(self):
        return "HTML metadata extractor"

    # @property
    def category(self):
        return "HTML extractor"

    def extract(self, extractables: List[Extractable],
                extract_meta: bool = True,
                extract_microdata: bool = True,
                extract_json_ld: bool = True,
                extract_rdfa: bool = True) \
            -> List[Extraction]:
        """

        Args:
            extractables ():
            extract_meta ():
            extract_microdata ():
            extract_json_ld ():
            extract_rdfa ():

        Returns: List[Extraction], where each extraction contains a dict with each type of metadata.

        """
        pass
