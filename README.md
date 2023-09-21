# Resume generator

Version 0.1.0

## Generating the resume

The `resume_data` folder contains all the data displayed on the resume.
<br>To add an education, extracurricular activity, or working experience, just copy one of the existing
toml files in one of the folders folder and create your own.
<br>To add/change the hobbies or languages, just change the list in the designated toml files.
<br>Finally, the header file contains the data that is displayed on top. Note that profile image needs to
be saved in the `src/web_application/static/images` folder.
<br><br>After running `$ python3 src/construct_resume.py`, your new activity will be displayed on the webpage.


## Viewing the resume

After creating the resume, it can be viewed using the [flask application](https://flask.palletsprojects.com/en/2.3.x/).
```
$ export FLASK_APP=src/web_application/web_application
$ flask run --reload
```

The resume can be tweaked using the css file in the static folder.

## Exporting to [GitHub pages](https://pages.github.com/)

When you are satisfied with the styling of the webpage,
the resume can be exported to the GitHub pages format using the export script.
<br>`$ python3 src/export_resume.py`




