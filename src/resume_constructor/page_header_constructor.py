from pathlib import Path

from dominate import tags

from data_models.header import Header
from data_layer.paths import IMAGES_PATH
from data_layer import html_class_keys


def construct_resume_page_header(header_data: Header) -> tags.div:
    page_header = tags.div(cls=html_class_keys.PAGE_HEADER)
    download_button = tags.button("Download PDF version", id=html_class_keys.DOWNLOAD_BUTTON_ID)
    # download_button.set_attribute("data-html2canvas-ignore", "true") # Set this to ignore the button when downloading pdf
    page_header.add(download_button)

    page_header.add(tags.img(cls=html_class_keys.PROFILE_IMAGE, src=header_data.image))
    page_header.add(tags.h1(header_data.name, cls=html_class_keys.PAGE_HEADER_NAME))

    page_header.add(
        __construct_linked_contact_method(
            link=header_data.github,
            image=IMAGES_PATH / "github.svg",
        )
    )
    page_header.add(
        __construct_linked_contact_method(
            link=header_data.linkedin,
            image=IMAGES_PATH / "linkedin.svg",
        )
    )

    return page_header


def __construct_linked_contact_method(link: str, image: Path) -> tags.div:
    linked_contact_method = __get_contact_method()
    linked_contact_method.add(tags.img(src=image))
    linked_contact_method.add(tags.a(link, href=f"https://www.{link}"))
    return linked_contact_method


def __get_contact_method() -> tags.div:
    return tags.div(cls=html_class_keys.CONTACTING_METHOD)
