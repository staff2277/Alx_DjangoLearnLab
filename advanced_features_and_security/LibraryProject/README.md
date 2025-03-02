## Security Features Implemented

1. **Django Security Settings**

   - Disabled `DEBUG` in production.
   - Enforced secure cookies and HTTPS redirection.
   - Added protection against XSS, CSRF, and Clickjacking.
   - Configured HTTP Strict Transport Security (HSTS).

2. **CSRF Protection**

   - All forms include `{% csrf_token %}`.

3. **SQL Injection Prevention**

   - User input is validated via Django Forms (`BookSearchForm`).
   - ORM is used to prevent raw SQL execution.

4. **Content Security Policy (CSP)**
   - Middleware added to restrict external script execution.
