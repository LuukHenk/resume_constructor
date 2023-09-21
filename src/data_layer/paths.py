from pathlib import Path

ROOT = Path(__file__).parent.parent.parent
RESUME_DATA_PATH = ROOT / "resume_data"
EXPORT_PATH = ROOT / "export"
RESUME_HTML_EXPORT_PATH = EXPORT_PATH / "resume.html"

WEB_APP_PATH = Path(__file__).parent.parent / "web_application"
RESUME_TEMPLATE_PATH = WEB_APP_PATH / "templates/resume.html"

STATIC_PATH = Path("static")
IMAGES_PATH = STATIC_PATH / "images"
CSS_PATH = STATIC_PATH / "css"
JS_PATH = STATIC_PATH / "js"
