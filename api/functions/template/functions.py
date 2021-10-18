import re
import os
from io import BytesIO
from typing import List
from zipfile import ZipFile
from urllib.request import urlopen
from subprocess import Popen
import subprocess


MAIN_XML_FILE_NAME = "word/document.xml"


def _get_key(hole: str) -> str:
    key = re.sub(r"<.*?>", "", hole)
    return key


def _get_docx_zip_buffer(docx_file_url: str) -> BytesIO:
    # response_docx_file = urlopen(docx_file_url)
    # return BytesIO(response_docx_file.read())

    return docx_file_url


def get_holes_and_keys(docx_file_url: str):
    with ZipFile(_get_docx_zip_buffer(docx_file_url)) as template_docx_zip_file:
        # get main text of docx file
        xml_data = template_docx_zip_file.read(MAIN_XML_FILE_NAME).decode("utf-8")

    holes = re.findall(r"«(.*?)»", xml_data)

    keys = [_get_key(hole) for hole in holes]

    unique_keys = list(set(keys))

    return holes, keys, unique_keys


def fill_holes_by_keys(docx_file_url: str, need_to_fill_data: dict, holes: List[str], keys: List[str]) -> BytesIO:
    template_docx_zip_file = ZipFile(_get_docx_zip_buffer(docx_file_url))
    xml_data = template_docx_zip_file.read(MAIN_XML_FILE_NAME).decode("utf-8")

    zip_buffer = BytesIO()
    docx_zip_file = ZipFile(zip_buffer, mode="w")

    # add all child files in template docx.zip to new document file (file need to fill holes)
    child_file_names = template_docx_zip_file.namelist()
    child_file_names.remove(MAIN_XML_FILE_NAME)
    for child_file_name in child_file_names:
        docx_zip_file.writestr(child_file_name, template_docx_zip_file.read(child_file_name))

    for key, value in need_to_fill_data.items():
        index_keys = [i for i, x in enumerate(keys) if x == key]
        if not index_keys:
            raise ValueError

        # xml_data = xml_data.replace(f'<w:instrText xml:space="preserve"> MERGEFIELD  {key} </w:instrText>', "")
        # xml_data = xml_data.replace(f'<w:instrText xml:space="preserve"> MERGEFIELD  {key}  </w:instrText>', "")
        # xml_data = xml_data.replace(
        #     f'<w:instrText xml:space="preserve"> MERGEFIELD  {key}  \* MERGEFORMAT </w:instrText>', ""
        # )

        for index_key in index_keys:
            xml_data = xml_data.replace(f"«{holes[index_key]}»", value)
            # xml_data = xml_data.replace(f'<w:t>«{holes[index_key]}»</w:t>',
            #                             f'<w:rPr><w:i /><w:iCs/></w:rPr><w:t>{value}</w:t>')
            # xml_data = xml_data.replace(f'<w:t>«{holes[index_key]}»</w:t>', f'<w:rPr><w:b /><w:i /><w:iCs/></w:rPr><w:t>{value}</w:t>')

        # print(xml_data)

    docx_zip_file.writestr(MAIN_XML_FILE_NAME, xml_data)

    return zip_buffer


def docx_to_pdf(input_docx_path, output_folder_path):
    process = Popen(
        ["libreoffice", "--headless", "--convert-to", "pdf", "--outdir", output_folder_path, input_docx_path]
    )
    process.communicate()


def docx_to_pdf_window(input_docx_path, output_folder_path):
    process = f'start /wait soffice --headless --convert-to pdf --outdir "{output_folder_path}" "{input_docx_path}"'
    subprocess.call(process, shell=True)


# if __name__ == '__main__':
#     docx_file_url = 'http://192.168.157.193:9199/dms-dev/198402/7e05e2976837476ea3962f2a7a99ed7a?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=dms-admin%2F20210526%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210526T033555Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=d8e3a40de5a17dbaaec3ea9546ce785f3a9cac1da12a74139c4a0cf8ae2d83e8'
#
#     holes, keys, unique_keys = get_holes_and_keys(docx_file_url=docx_file_url)
#     if holes and keys:
#         for i in range(len(holes)):
#             print(i)
#             print(holes[i])
#             print(keys[i])
#             print()
#
#     print(len(keys), len(holes), len(unique_keys))
#
#     zip_buffer = fill_holes_by_keys(
#         docx_file_url=docx_file_url,
#         need_to_fill_data={
#             'BC_trangthaiTS': 'ầdfadfadf',
#             'BC_chinhanh': 'Võ Văn Dương',
#             'BC_MaTS': '12345',
#             'landglai': 'werew',
#             'BC_nhanvien': 'Minh Anh',
#             'BC_CMNDCSH': '212810695',
#         },
#         holes=holes,
#         keys=keys
#     )
#     with open('xyz.docx', 'wb') as out:
#         out.write(zip_buffer.getbuffer())
#
#     docx_to_pdf('xyz.docx', '')
#     # os.remove('xyz.docx')
