from typing import Union
from pathlib import Path
from pypdf import PdfFileReader, PdfFileWriter
import logging

LOG = logging.getLogger("main")


def fill_in_pdf(template_filename, field_values, filepath: Union[Path, str]):
    LOG.debug(f"PDF template_filename = {template_filename} => filename = {filepath}")
    template_pdf = PdfFileReader(open(template_filename, "rb"), strict=False)
    with PdfFileWriter(str(filepath)) as output:
        output.have_viewer_render_fields()
        for page_no in range(template_pdf.numPages):
            template_page = template_pdf.getPage(page_no)
            output.addPage(template_page)
            page = output.getPage(page_no)
            output.updatePageFormFieldValues(page, field_values, read_only=True)
        output.write()

