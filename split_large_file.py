from sys import argv


def split_jsonl_file(input_file, max_size=40 * 1024 * 1024):
    assert input_file.endswith(".jsonl")
    prefix = input_file[:-6]
    with open(input_file, "r") as file:
        lines = file.readlines()

    part_number = 0
    current_size = 0
    current_lines = []

    for line in lines:
        line_size = len(line.encode("utf-8"))

        if current_size + line_size > max_size:
            output_file = f"{prefix}_{part_number}.jsonl"
            with open(output_file, "w") as file:
                file.writelines(current_lines)
            print(f"Wrote {output_file}, {current_size} bytes")

            part_number += 1
            current_size = 0
            current_lines = []

        current_lines.append(line)
        current_size += line_size

    if current_lines:
        output_file = f"{prefix}_{part_number}.jsonl"
        with open(output_file, "w") as file:
            file.writelines(current_lines)
        print(f"Wrote {output_file}, {current_size} bytes")


if __name__ == "__main__":
    input_file = argv[1]
    split_jsonl_file(input_file)
