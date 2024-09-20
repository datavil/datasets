from pathlib import Path
from typing import Literal

import polars as pl


def ansii_red(text: str) -> str:
    return f"\033[31m{text}\033[0m"


def ansii_green(text: str) -> str:
    return f"\033[32m{text}\033[0m"


def ansii_blue(text: str) -> str:
    return f"\033[34m{text}\033[0m"


def convert(
    path: Path,
    format: Literal["parquet", "feather"] = "feather",
    overwrite: bool = False,
) -> str:
    """
    Convert a dataset from csv to feather or parquet.

    Parameters
    ----------
    path : Path
        Path to the dataset csv file.

    format : Literal["parquet", "feather"]
        Format to convert the dataset to.
        Default is "feather".

    overwrite : bool
        Whether to overwrite the feather file if it already exists.
    Returns
    -------
    str
        Message indicating the conversion process.
    """
    if not (path.parent.parent / format).exists():
        (path.parent.parent / format).mkdir()
    new_path = path.parent.parent / format / path.name.replace("csv", format)
    if new_path.exists() and not overwrite:
        return
    else:
        if format == "parquet":
            pl.read_csv(path, infer_schema_length=10_000).write_parquet(
                new_path, compression="zstd"
            )
            rate = new_path.stat().st_size / path.stat().st_size
            msg = f"{ansii_green(path.name):<30} -- {rate:.1%} --> {ansii_red(new_path.name)}"
            print(msg)
        elif format == "feather":
            pl.read_csv(path, infer_schema_length=10_000).write_ipc(
                new_path, compression="zstd"
            )
            rate = new_path.stat().st_size / path.stat().st_size
            msg = f"{ansii_green(path.name):<30} -- {rate:.1%} --> {ansii_blue(new_path.name)}"
            print(msg)
    return msg


def get_paths(dir: Path) -> list[Path]:
    """
    Get all csv files in a directory.

    Parameters
    ----------
    dir : Path
        Path to the directory.

    Returns
    -------
    list[Path]
        List of csv files in the directory.
    """
    return list(dir.glob("*.csv"))


def get_sizes(format: Literal["csv", "feather", "parquet"]) -> float:
    """
    Get the size of the feather files in the format.

    Parameters
    ----------
    format : Literal["csv","feather","parquet"]
        Format of the feather files.

    Returns
    -------
    float
        Size of the files in the given format.
    """
    return sum(f.stat().st_size for f in Path(f"./{format}").glob(f"*.{format}"))


def main() -> None:
    full_path = Path("csv").resolve()  # for absoulte path
    msgs = []
    # convert all csv files to feather and parquet
    msg = "\n{path:<25}{size}     {new_path}".format(
        path="FROM", size="Size%", new_path="TO"
    )
    print(msg)
    msgs.append(msg)

    for path in get_paths(full_path):
        msgs.append(convert(path, format="feather", overwrite=True))
        msgs.append(convert(path, format="parquet", overwrite=True))

    # dict comprehension for size of each format
    sizes = {format: get_sizes(format) for format in ["csv", "feather", "parquet"]}
    normalized_sizes = {
        format: f'{size/sizes["csv"]:.1%}' for format, size in sizes.items()
    }

    # print the sizes of each format

    msgs.append("\n{format:<10} {size}".format(format="FORMAT", size="SIZE%"))
    for format, size in normalized_sizes.items():
        msg = f"{format:<10} {size}"
        print(msg)
        msgs.append(msg)

    all_text = "\n".join(msgs)

    with open("log.html", "w") as html_file:
        from log2html import ansi_to_html_converter
        html = ansi_to_html_converter(all_text)
        html_file.write(html)

    return


if __name__ == "__main__":
    main()
