### About this template

This template is used to show to use the Elastic APM library, for Python in this example, to send performance data, about our example web API, to an Elastic APM server and view that information in Kibana.

---

### To use this template clone it with cookiecutter:

1. Install the `cookiecutter` library if it isn't already installed:
   `pip3 install cookiecutter`

   - Optionally, setup pre-commit hooks:
     - `pip3 install pre-commit`

2. Use this cookiecutter template: `cookiecutter gh:andrewguest/cookiecutter-elastic-apm-python`

3. Answer the questions when prompted (example below):

| Prompt                    | Explanation                                                                                  | Defaults        |
| ------------------------- | -------------------------------------------------------------------------------------------- | --------------- |
| `project_name []`         | Name for this project.                                                                       | fastapi-elastic |
| `project_slug []`         | Automatically formatted version of `project_name`.                                           | N/A             |
| `fastapi_service_name []` | Name for the FastAPI service. This is how the API will be referenced within the Elastic APM. | fastapi-01      |

---

### Services:

| Service            | Port |
| ------------------ | ---- |
| Elastic APM server | 8200 |
| Elasticsearch      | 9200 |
| Kibana             | 5601 |
| FastAPI            | 7000 |

---

### Routes

| Route        | Explainattion                                                     |
| ------------ | ----------------------------------------------------------------- |
| /            | A normal, 200-OK route                                            |
| /elastic-apm | A route with a manually caught error (try/except)                 |
| /5xx         | A route with an automcatically caught internal server error (500) |
