# Contributing to NXOpen Python Tutorials

First off, thanks for taking the time to contribute!

The following is a set of guidelines for contributing to the NXOpen Python Tutorials repository. These are mostly guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

## How Can I Contribute?

### Reporting Bugs

This section guides you through submitting a bug report for the NXOpen Python Tutorials. Following these guidelines helps maintainers and the community understand your report, reproduce the behavior, and find related reports.

- **Use a clear and descriptive title** for the issue to identify the problem.
- **Describe the exact steps to reproduce the problem** in as many details as possible.
- **Provide specific examples** to demonstrate the steps.

### Suggesting Enhancements

This section guides you through submitting an enhancement suggestion for the NXOpen Python Tutorials, including completely new features and minor improvements to existing functionality.

- **Use a clear and descriptive title** for the issue to identify the suggestion.
- **Provide a step-by-step description of the suggested enhancement** in as much detail as possible.
- **Explain why this enhancement would be useful** to most users.

### Contributing Examples

We welcome new NXOpen Python examples! If you have code snippets or full scripts that demonstrate how to automate tasks in Siemens NX using Python, please share them.

1.  **Fork the repository** on GitHub.
2.  **Clone your fork** locally:
    ```bash
    git clone https://github.com/YOUR_USERNAME/NXOpen_Python_tutorials.git
    cd NXOpen_Python_tutorials
    ```
3.  **Create a new branch** for your contribution:
    ```bash
    git checkout -b meaningful-branch-name
    ```
4.  **Add your example** to the `Examples/` folder. Please use a naming convention consistent with existing files (e.g., `ex000X.py`) if applicable, or a descriptive name.
5.  **Update the README** to include documentation for your new example.
6.  **Commit your changes** with a clear commit message:
    ```bash
    git commit -m "Add example for creating a block feature"
    ```
7.  **Push to your fork**:
    ```bash
    git push origin meaningful-branch-name
    ```
8.  **Submit a Pull Request** on GitHub to the main repository.

## Styleguides

### Python Styleguide

- We follow [PEP 8](https://www.python.org/dev/peps/pep-0008/).
- Please ensure your code is readable and well-commented.
- Use meaningful variable and function names.

### Documentation Styleguide

- Use Markdown for documentation.
- When adding an example, please update the main `README.md` with a brief description and, if possible, a screenshot in the `Pictures/` directory.

## License

By contributing, you agree that your contributions will be licensed under the [CC0 1.0 Universal](LICENSE) (Public Domain) license.
