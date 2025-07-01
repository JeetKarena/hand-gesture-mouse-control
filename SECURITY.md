# Security Policy

Thank you for helping keep **Gesture Mouse Control** secure. This document outlines how to report security vulnerabilities and which versions of the project are supported for security updates.

## Supported Versions

As **Gesture Mouse Control** is a new project, we currently support only the latest code in the following branches for security updates:

| Branch | Supported          | Description                     |
|--------|--------------------|---------------------------------|
| main   | :white_check_mark: | Stable, production-ready code   |
| stag   | :white_check_mark: | Testing branch with CI/CD       |
| dev    | :white_check_mark: | Development branch for new code |

Since this is a new project, there are no legacy versions. Security updates will be applied to the `dev` branch and propagated to `stag` and `main` after testing.

## Reporting a Vulnerability

If you discover a security vulnerability in **Gesture Mouse Control**, please report it responsibly by following these steps:

1. **Do Not Open a Public Issue**: To protect users, do not disclose vulnerabilities in public GitHub issues or discussions.
2. **Contact Us Privately**:
   - Email the project maintainers at [your-email@example.com](mailto:your-email@example.com) with a detailed description of the vulnerability.
   - Alternatively, use GitHub's private vulnerability reporting feature (if enabled) by navigating to the "Security" tab in the repository and selecting "Report a vulnerability."
3. **Provide Details**:
   - Describe the vulnerability, including how it can be exploited.
   - Specify the affected branch (`main`, `stag`, or `dev`) or commit, if known.
   - Include steps to reproduce, potential impact, and any suggested fixes.
   - Attach logs, screenshots, or other relevant materials, if applicable.
4. **Response Expectations**:
   - We will acknowledge your report within 48 hours.
   - We will investigate and provide an update on the vulnerability's status within 7 days.
   - If the vulnerability is confirmed, we will work on a fix, test it on the `stag` branch, and release it to `main`.
   - If the vulnerability is declined (e.g., out of scope or not reproducible), we will explain the reason.
5. **Responsible Disclosure**:
   - Please allow us reasonable time to address the issue before disclosing it publicly.
   - We will credit you for the discovery (unless you prefer to remain anonymous) once the issue is resolved.

## Scope of Security Issues

We consider the following types of issues as security vulnerabilities:

- Code execution vulnerabilities in Python scripts or dependencies.
- Unauthorized access to user input (e.g., webcam data).
- Issues in gesture processing that could lead to unintended system actions.
- Vulnerabilities in dependencies listed in `requirements.txt`.

Issues not typically considered security vulnerabilities include:

- Bugs requiring physical access to the user's machine.
- Best practice recommendations without direct security impact.

## Security Practices

- We use SonarQube for code scanning on the `stag` branch to identify potential vulnerabilities.
- Dependencies are regularly updated to address known CVEs.
- All code changes undergo review and testing before merging into `main`.

## Contact

For questions about this policy, email [mail](gitops.excitable722@passinbox.com).

Thank you for helping us keep **Gesture Mouse Control** safe and secure!
