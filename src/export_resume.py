import re
from pathlib import Path
from shutil import copyfile
from typing import List

from data_layer.paths import (
    WEB_APP_PATH,
    CSS_PATH,
    JS_PATH,
    IMAGES_PATH,
    EXPORT_PATH,
    RESUME_TEMPLATE_PATH,
    RESUME_HTML_EXPORT_PATH,
    STATIC_PATH,
)

STATIC_PATHS = [
    str(CSS_PATH),
    str(JS_PATH),
    str(IMAGES_PATH),
]


def __copy_resume_template_to_export_folder():
    with open(RESUME_TEMPLATE_PATH) as resume_template_file:
        resume_template_data = resume_template_file.readlines()

    resume_template_data = __replace_paths(resume_template_data)

    with open(RESUME_HTML_EXPORT_PATH, "w") as resume_template_export_file:
        resume_template_export_file.writelines(resume_template_data)


def __replace_paths(resume_template_data: List[str]) -> List[str]:
    for i, line in enumerate(resume_template_data):
        for path in STATIC_PATHS:
            if path in line:
                resume_template_data[i] = re.sub(path + "/", "", line)
    return resume_template_data


def __create_export_folder():
    EXPORT_PATH.mkdir(parents=True, exist_ok=True)


def __copy_static_files_to_export_folder():
    files_to_copy = [f for f in Path(WEB_APP_PATH / IMAGES_PATH).iterdir() if f.is_file()]
    files_to_copy.append(WEB_APP_PATH / CSS_PATH / "resume.css")
    files_to_copy.append(WEB_APP_PATH / JS_PATH / "pdf.js")
    for file in files_to_copy:
        copyfile(file, EXPORT_PATH / file.name)


def main():
    __create_export_folder()
    __copy_static_files_to_export_folder()
    __copy_resume_template_to_export_folder()
    print(f"Exported data to '{EXPORT_PATH}'")


if __name__ == "__main__":
    main()
