# Student Marks Calculator

A simple static web page that calculates each student's total, average, grade and result.
Runs fully in the browser (`index.html`), so it can be hosted free on GitHub Pages.

`student_calculator.py` is a separate, intentionally flawed Python file used to test static
analysis tools (Bandit, Ruff, Radon). It is not used by the web page. Do not use it in a real application.

## Deploy on GitHub Pages
1. Push `index.html` to the root of your repo (`main` branch).
2. Open the repo on GitHub: **Settings → Pages**.
3. Under **Build and deployment**, choose **Deploy from a branch**, pick `main` and `/ (root)`, then **Save**.
4. After a minute your site is live at `https://<your-username>.github.io/<repo-name>/`.
