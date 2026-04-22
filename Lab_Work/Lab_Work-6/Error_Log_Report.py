'''Error Log Reporter

Read error logs:

Group by error type
Count occurrences
Write summary file
'''

# ---------------- ERROR LOG REPORTER ----------------

def process_logs(input_file, output_file):

    error_counts = {}   # dictionary to store error type counts

    try:
        # ----------- READ LOG FILE -----------
        with open(input_file, 'r') as file:
            for line in file:
                
                # remove extra spaces and newline characters
                line = line.strip()

                # skip empty lines
                if not line:
                    continue

                try:
                    # ----------- EXTRACT ERROR TYPE -----------
                    # assuming format: TYPE: message
                    error_type = line.split(":")[0]

                    # count occurrences
                    if error_type in error_counts:
                        error_counts[error_type] += 1
                    else:
                        error_counts[error_type] = 1

                except Exception:
                    print(f"Invalid log format → Skipped: {line}")

        # ----------- WRITE SUMMARY FILE -----------
        with open(output_file, 'w') as outfile:
            outfile.write("Error Summary Report\n")
            outfile.write("----------------------\n")

            for err, count in error_counts.items():
                outfile.write(f"{err}: {count}\n")

        print("\nReport generated successfully!")
        print(f"Saved to: {output_file}")

    except FileNotFoundError:
        print("Log file not found!")


# ---------------- RUN PROGRAM ----------------
process_logs("error_log.txt", "summary.txt")