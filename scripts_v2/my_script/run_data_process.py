# scripts_v2/my_script/run_data_process.py
import argparse

def process_data(input_file: str, output_file: str, upper_case: bool):
    """
    Reads data from input_file, optionally converts to uppercase,
    and writes to output_file.
    """
    try:
        with open(input_file, 'r') as infile:
            content = infile.read()
        
        if upper_case:
            content = content.upper()
        
        with open(output_file, 'w') as outfile:
            outfile.write(content)
        print(f"Data processed from {input_file} to {output_file} successfully.")
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process data from a file.")
    parser.add_argument("--input", "-i", required=True, help="Input file path.")
    parser.add_argument("--output", "-o", required=True, help="Output file path.")
    parser.add_argument("--upper-case", "-u", action="store_true", help="Convert content to upper case.")
    
    args = parser.parse_args()
    process_data(args.input, args.output, args.upper_case)