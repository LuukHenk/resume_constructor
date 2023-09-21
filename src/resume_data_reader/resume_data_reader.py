from datetime import date
from pathlib import Path
from tomllib import load
from typing import Any, List

from data_models.activity import Activity
from data_models.extra_curricular_activities import ExtraCurricularActivities
from data_models.header import Header
from data_layer.paths import IMAGES_PATH, RESUME_DATA_PATH


class ResumeDataReader:
    __HEADER_IMAGE_KEY = "image"

    __EDUCATIONS_PATH = RESUME_DATA_PATH / "educations"
    __HEADER_PATH = RESUME_DATA_PATH / "header.toml"
    __WORKING_EXPERIENCES_PATH = RESUME_DATA_PATH / "working_experiences"
    __EXTRA_CURRICULAR_ACTIVITIES_PATH = RESUME_DATA_PATH / "extra-curricular_activities"
    __HOBBIES_PATH = RESUME_DATA_PATH / "hobbies.toml"
    __LANGUAGES_PATH = RESUME_DATA_PATH / "languages.toml"

    def get_hobbies(self) -> List[str]:
        return self.__read_toml_file(self.__HOBBIES_PATH)["hobbies"]

    def get_languages(self) -> List[str]:
        return self.__read_toml_file(self.__LANGUAGES_PATH)["languages"]

    def get_educations(self) -> List[Activity]:
        educations = []
        for education_dict in self.__read_toml_files(self.__EDUCATIONS_PATH):
            educations.append(
                Activity(
                    title=education_dict["title"],
                    location=education_dict["location"],
                    city=education_dict["city"],
                    start_date=self.__create_date_stamp(education_dict["start_date"]),
                    end_date=self.__create_date_stamp(education_dict["end_date"]),
                    skills=education_dict["skills"],
                    description=education_dict["description"],
                )
            )
        return educations

    def get_working_experiences(self) -> List[Activity]:
        working_experiences = []
        for working_experience_dict in self.__read_toml_files(self.__WORKING_EXPERIENCES_PATH):
            working_experiences.append(
                Activity(
                    title=working_experience_dict["title"],
                    location=working_experience_dict["location"],
                    city=working_experience_dict["city"],
                    start_date=self.__create_date_stamp(working_experience_dict["start_date"]),
                    end_date=self.__create_date_stamp(working_experience_dict["end_date"]),
                    skills=working_experience_dict["skills"],
                    description=working_experience_dict["description"],
                )
            )
        return working_experiences

    def get_extra_curricular_activities(self) -> List[ExtraCurricularActivities]:
        extra_curricular_activities = []
        for activity_dict in self.__read_toml_files(self.__EXTRA_CURRICULAR_ACTIVITIES_PATH):
            extra_curricular_activities.append(
                ExtraCurricularActivities(
                    title=activity_dict["title"],
                    description=activity_dict["description"],
                )
            )
        return extra_curricular_activities

    def get_header(self) -> Header:
        header_dict = self.__read_toml_file(self.__HEADER_PATH)
        header_dict[self.__HEADER_IMAGE_KEY] = IMAGES_PATH / header_dict[self.__HEADER_IMAGE_KEY]
        header = Header(
            name=header_dict["name"],
            image=header_dict["image"],
            github=header_dict["github"],
            linkedin=header_dict["linkedin"],
        )
        return header

    def __read_toml_files(self, directory: Path) -> List[Any]:
        toml_file_paths = [x for x in directory.iterdir() if x.is_file() and x.match("*.toml")]
        return [self.__read_toml_file(toml_file_path) for toml_file_path in toml_file_paths]

    @staticmethod
    def __read_toml_file(toml_file_path: Path) -> Any:
        with open(toml_file_path, "rb") as toml_file:
            return load(toml_file)

    @staticmethod
    def __create_date_stamp(date_str: str) -> date:
        month_str, year_str = date_str.split("-")
        return date(year=int(year_str), month=int(month_str), day=1)
