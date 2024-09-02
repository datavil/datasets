from pathlib import Path

import polars as pl


def convert(path: Path, overwrite: bool = False)->None:
    """
    Convert a dataset from csv to feather format. 

    Parameters
    ----------
    path : Path
        Path to the dataset csv file.
    
    Returns
    -------
    None
    """
    feather_path = path.parent.parent / "feather" / path.name.replace(".csv", ".feather")
    if feather_path.exists() and not overwrite:
        return
    else:
        pl.read_csv(path, infer_schema_length=10_000).write_ipc(feather_path, compression='zstd')
        print(f"{path.name:>20} --> {feather_path.name}") 
    return


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

def main() -> None:

    full_path = Path("csv").resolve() # for absoulte path
    for path in get_paths(full_path):

        convert(path,overwrite=True)

    return

if __name__ == "__main__":
    main()