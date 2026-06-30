# greetlib — GitHub Packages Demo

A minimal Python package published to **GitHub Packages** and consumed from another project.

## Publish

```yaml
# .github/workflows/publish.yml — runs on every tag push
```

On each `git tag v*` push, GitHub Actions builds the package and uploads it to GitHub Packages.

## Consume

```bash
pip install --extra-index-url https://pypi.pkg.github.com/YOUR_USERNAME/simple/ greetlib
```

Or add to `requirements.txt`:
```
--extra-index-url https://pypi.pkg.github.com/YOUR_USERNAME/simple/
greetlib
```

## How it works

| Step | What happens |
|------|-------------|
| Build | `python -m build` creates `.tar.gz` + `.whl` |
| Publish | `twine` uploads to GitHub Packages PyPI registry |
| Auth | `GITHUB_TOKEN` from Actions workflow (no secrets needed) |
| Install | `pip` fetches from GitHub Packages index instead of PyPI |
