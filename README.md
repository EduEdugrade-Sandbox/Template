# Template

Minimal template repo for the GitHub assignment integration spike.

It contains a small Python function, pytest tests and a workflow that uploads the JUnit XML result as an artifact.

## Run locally

```bash
pip install -r requirements.txt
pytest --junitxml=test-results.xml
```
