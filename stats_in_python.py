import sys
import math

# You can set the filename and column index below at line 100 with the main function

def read_column_data(filename, column_index):
    numbers = []
    total_count = 0

    try:
        with open(filename, 'r') as infile:
            for line_number, line in enumerate(infile, start=1):
                total_count += 1
                try:
                    value = line.split("\t")[column_index].strip()
                    if value.lower() == "nan" or not value:
                        continue  # Skip nan or empty values and continues on instead

                    # Will attempt to convert to float, will ignore if it fails conversion
                    number = float(value)
                    numbers.append(number)

                except ValueError:
                    continue  # Non-numeric values are ignored
                except IndexError:
                    # Handle the case when the specified column doesn't exist
                    print(
                        f"Exiting: There is no valid 'list index' in column {column_index} in line {line_number} in file: {filename}")
                    sys.exit(1)

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

    # If no valid numbers were found within the file, this will instead print an error message and exit
    if not numbers:
        print(f"Error: There were no valid number(s) in column {column_index} in file: {filename}")
        sys.exit(1)

    return numbers, total_count


def calculate_sample_variance(numbers):
    count = len(numbers)
    if count < 2:
        return 0  # If there are fewer than two data points, sample variance returns as undefined (return 0 or handle error) since it needs at least 2 to be useful.

    mean = sum(numbers) / count
    squared_diffs = [(x - mean) ** 2 for x in numbers]
    sample_variance = sum(squared_diffs) / (count - 1)

    return sample_variance


def calculate_statistics(numbers):
    count = len(numbers)
    if count == 0:
        return None

    # Calculation of basic stats
    avg = sum(numbers) / count
    max_val = max(numbers)
    min_val = min(numbers)

    # Calculation for Sample Variance and Standard Deviation (lumped together as variance is needed for std_dev calculations)
    variance = calculate_sample_variance(numbers)
    std_dev = math.sqrt(variance)

    # Calculation for Median
    sort_numbers = sorted(numbers)
    mid = count // 2
    if count % 2 == 0:
        median = (sort_numbers[mid - 1] + sort_numbers[mid]) / 2 # median calc if count outputs as even, average of the two middle values is the median
    else:
        median = sort_numbers[mid] # median calc if count outputs as odd, middle value is the median

    return {
        "count": count,
        "average": avg,
        "maximum": max_val,
        "minimum": min_val,
        "variance": variance,
        "std_dev": std_dev,
        "median": median
    }


def print_statistics(stats, total_count, valid_count):
    print(f"        Count     =   {total_count:.3f}")
    print(f"        ValidNum  =   {valid_count:.3f}")
    print(f"        Average   =   {stats['average']:.3f}")
    print(f"        Maximum   =   {stats['maximum']:.3f}")
    print(f"        Minimum   =   {stats['minimum']:.3f}")
    print(f"        Variance  =   {stats['variance']:.3f}")
    print(f"        Std Dev   =   {stats['std_dev']:.3f}")
    print(f"        Median    =   {stats['median']:.3f}")
    print("--------------------------------------------------------------------------------------")


def main(): # Here you can set the filename and column index here for the script
    filename = 'data_file.txt' # Change this to swap the filename (examples: data_file.txt, data_file2.txt, data_file3.txt)
    column_index = 3 # Change this index if you need to check different columns of the file

    print(f"{filename}\nColumn: {column_index}")
    numbers, total_count = read_column_data(filename, column_index)
    stats = calculate_statistics(numbers)
    if stats:
        print_statistics(stats, total_count, len(numbers))


if __name__ == "__main__":
    main()
