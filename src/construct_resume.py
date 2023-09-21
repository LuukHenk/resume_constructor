from resume_constructor.html_resume_constructor import HtmlResumeConstructor
from data_layer.paths import RESUME_TEMPLATE_PATH


HtmlResumeConstructor().write(RESUME_TEMPLATE_PATH)
print(f"Saved the resume at {RESUME_TEMPLATE_PATH}.")
