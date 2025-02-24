def format_linter_error(error: dict) -> dict:

    return {
        "line" if key == "line_number" else
        "column" if key == "column_number" else
        "message" if key == "text" else
        "name" if key == "code" else key:value
        for key, value in error.items()
        if key in ["column_number", "line_number", "text", "code",]
    } | {"source": "flake8"}



def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [
            {
                "line" if key == "line_number" else
                "column" if key == "column_number" else
                "message" if key == "text" else
                "name" if key == "code" else key: value
                for key, value in error.items()
                if key in ["column_number", "line_number", "text", "code"]
            } | {"source": "flake8"}
            for error in errors
        ],
        "path": file_path,
        "status": "failed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        {
            "errors": [
                {
                    "line": error["line_number"],
                    "column": error["column_number"],
                    "message": error["text"],
                    "name": error["code"],
                    "source": "flake8"
                }
                for error in errors
            ],
            "path": file_path,
            "status": "failed" if errors else "passed"
        }
        for file_path, errors in linter_report.items()
    ]
