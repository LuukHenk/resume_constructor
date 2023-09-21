from pathlib import Path

from dominate import document, tags, util

from resume_data_reader.resume_data_reader import ResumeDataReader
from resume_constructor.activities_constructor import construct_activities
from resume_constructor.page_header_constructor import construct_resume_page_header
from data_layer.paths import CSS_PATH, IMAGES_PATH, JS_PATH
from data_layer import html_class_keys


class HtmlResumeConstructor:
    def __init__(self):
        self.__input_data_reader = ResumeDataReader()

    def write(self, path: Path) -> None:
        # TODO Im not sure if this function belongs in this class ....
        resume_str = self.__construct_resume().render()
        with open(path, "w") as resume_file:
            resume_file.write(resume_str)

    def __construct_resume(self) -> document:
        resume = document(title="Resume Luuk Perdaems", cls=html_class_keys.RESUME_PAGE)
        self.__set_head_data(resume.head)
        resume.body["id"] = html_class_keys.HTML_BODY_ID
        resume.add(self.__get_page_header())
        resume.add(self.__get_page_body())
        return resume

    @staticmethod
    def __set_head_data(resume_header: tags.head) -> None:
        with resume_header:
            tags.link(rel="stylesheet", type="text/css", href=CSS_PATH / "resume.css")
            tags.link(rel="shortcut icon", href=IMAGES_PATH / "favicon.ico")
            js_src = tags.script(src=JS_PATH / "pdf.js")
            js_src.set_attribute("defer", "defer")

    def __get_page_header(self) -> tags.div:
        header_data = self.__input_data_reader.get_header()
        resume_header = construct_resume_page_header(header_data)
        return resume_header

    def __get_page_body(self) -> tags.div:
        page_body = tags.div(cls=html_class_keys.PAGE_BODY)

        page_body.add(self.__get_working_experiences())
        page_body.add(self.__get_educations())

        page_body.add(self.__get_extra_curricular_activities())
        smaller_subsection = tags.div(cls=html_class_keys.SMALLER_SUBSECTION)
        smaller_subsection.add(self.__get_languages())
        smaller_subsection.add(self.__get_hobbies())
        page_body.add(smaller_subsection)
        return page_body

    def __get_working_experiences(self) -> tags.div:
        return construct_activities(
            title="Working Experiences",
            activities_data=self.__input_data_reader.get_working_experiences(),
        )

    def __get_educations(self) -> tags.div:
        return construct_activities(
            title="Educations",
            activities_data=self.__input_data_reader.get_educations(),
        )

    def __get_languages(self) -> tags.div:
        languages = tags.div(cls=html_class_keys.ACTIVITIES)
        languages.add(tags.h2("Languages", cls=html_class_keys.ACTIVITIES_TITLE))
        for language in self.__input_data_reader.get_languages():
            languages.add(tags.div(language, cls=html_class_keys.SKILL))
        return languages

    def __get_extra_curricular_activities(self) -> tags.div:
        extra_activities = tags.div(cls=html_class_keys.ACTIVITIES)
        extra_activities.add(tags.h2("Extra-curricular activities", cls=html_class_keys.ACTIVITIES_TITLE))
        for activity in self.__input_data_reader.get_extra_curricular_activities():
            activity_text = tags.div()
            activity_text.add(tags.b(f"{activity.title} - "))
            activity_text.add(activity.description)
            extra_activities.add(activity_text)
        return extra_activities

    def __get_hobbies(self) -> tags.div:
        hobbies = tags.div(cls=html_class_keys.ACTIVITIES)
        hobbies.add(tags.h2("Hobbies", cls=html_class_keys.ACTIVITIES_TITLE))
        for hobby in self.__input_data_reader.get_hobbies():
            hobbies.add(tags.div(hobby, cls=html_class_keys.SKILL))
        return hobbies
