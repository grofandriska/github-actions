# csk-gha-demo

A tiny web app, one test, and two GitHub Actions workflows.

| file | what it is |
|---|---|
| `app.py` | the app: answers every request with `greeting()` on port 8080 |
| `test_app.py` | the test: checks what `greeting()` returns |
| `Dockerfile` | packs the app into an image |
| `.github/workflows/pr.yml` | on every **pull request** to `main`: run the test |
| `.github/workflows/main.yml` | on every **push** to `main`: run the test, then build the image and push it to GHCR, tagged with the commit SHA |

Run it locally:

```bash
python3 -m unittest -v
python3 app.py          # then: curl localhost:8080
```
