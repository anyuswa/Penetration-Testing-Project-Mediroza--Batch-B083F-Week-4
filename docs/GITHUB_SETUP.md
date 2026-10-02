# Publish this portfolio to GitHub

## Which folder to upload

Extract the delivery ZIP. Upload only `mediroza-pentest-portfolio`. Keep `CONFIDENTIAL_REFERENCE_DO_NOT_UPLOAD` and `START_HERE.md` outside the repository. Do not upload the delivery ZIP itself.

The confidential folder preserves every original source file and the complete client PDF. It contains medical and employee information plus access material. `.gitignore` does not prevent browser uploads.

## Browser upload

1. Sign in to GitHub and create a repository named `mediroza-pentest-portfolio`.
2. Suggested description: **Authorised educational hospital web assessment: evidence-based findings, risk ratings and remediation.**
3. Choose visibility according to your publication permission. This package provides a sanitised public portfolio; the assignment's testing permission does not automatically grant publication permission.
4. Avoid creating a second README, licence or `.gitignore` during setup; these are included.
5. Select **uploading an existing file** and upload the contents of the portfolio folder so `README.md` is at repository root. Include the `.github` directory and `.gitignore` if your file picker supports them; using Git is more reliable for these paths.
6. Commit the files. Read the rendered README and verify the report/finding links.
7. Suggested topics: `cybersecurity`, `penetration-testing`, `security-assessment`, `burp-suite`, `technical-report`, `portfolio`.

## Git upload

The ZIP omits `.git` history for portable upload. Run the following inside the extracted portfolio directory, replacing `YOUR_USERNAME` with your GitHub account name:

```bash
git init -b main
git add .
git status --short
python scripts/check_repository.py
git commit -m "Add sanitised Mediroza assessment portfolio"
git remote add origin https://github.com/YOUR_USERNAME/mediroza-pentest-portfolio.git
git push -u origin main
```

If Git requests an author identity, set your own name and email using your normal Git configuration. Authenticate using your usual GitHub flow; do not place credentials in the remote URL or project files.

## Before publishing changes

Check the staged files and the complete commit history for sensitive material. Do not copy the confidential PDF or original screenshots into the public folder. The offline checks are guardrails, not a guarantee that every kind of sensitive information will be detected.

## Official reference

[GitHub Docs: Adding locally hosted code to GitHub](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github).
