import os
import shutil
import argparse


def copy_and_sort(source_dir, destination_dir):
    try:
        for item in os.listdir(source_dir):
            item_path = os.path.join(source_dir, item)
            if os.path.isdir(item_path):
                copy_and_sort(item_path, destination_dir)
            else:
                file_extension = os.path.splitext(item)[1][1:]
                destination_subdir = os.path.join(destination_dir, file_extension)
                os.makedirs(destination_subdir, exist_ok=True)
                shutil.copy(item_path, destination_subdir)
    except Exception as e:
        print(f"Error: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Copy files recursively and sort them by extension."
    )
    parser.add_argument("source_dir", type=str, help="Path to the source directory")
    parser.add_argument(
        "destination_dir",
        type=str,
        nargs="?",
        default="dist",
        help="Path to the destination directory (default: dist)",
    )
    args = parser.parse_args()

    source_dir = args.source_dir
    destination_dir = args.destination_dir

    if not os.path.exists(source_dir):
        print("Source directory does not exist.")
        return

    copy_and_sort(source_dir, destination_dir)
    print("Files have been copied and sorted successfully.")


if __name__ == "__main__":
    main()


