import csv
import matplotlib.pyplot as plt


# Voltage checking function
def check_voltage(voltage, lower_limit=11.5, upper_limit=12.5):
    if lower_limit <= voltage <= upper_limit:
        return "PASS"
    else:
        return "FAIL"


# Main application
def main():

    print("AUTOMATED ENGINEERING TEST SYSTEM")
    print("=================================")

    lower_limit = 11.5
    upper_limit = 12.5

    passed = 0
    failed = 0
    voltages = []

    print("\nReading engineering test data...\n")

    try:
        with open("test_data.csv", "r", newline="") as file:

            reader = csv.DictReader(file)

            if not {"test_id", "voltage"}.issubset(reader.fieldnames or []):
                raise ValueError(
                    "CSV must contain test_id and voltage columns."
                )

            with open("results.csv", "w", newline="") as output_file:

                fieldnames = ["test_id", "voltage", "result"]
                writer = csv.DictWriter(
                    output_file, fieldnames=fieldnames
                )

                writer.writeheader()

                for row in reader:

                    test_id = row["test_id"]

                    try:
                        voltage = float(row["voltage"])
                    except (ValueError, TypeError):
                        raise ValueError(
                            f"Invalid voltage for test ID {test_id}"
                        )

                    voltages.append(voltage)

                    result = check_voltage(
                        voltage, lower_limit, upper_limit
                    )

                    if result == "PASS":
                        passed += 1
                    else:
                        failed += 1

                    print("Test:", test_id)
                    print("Measured voltage:", voltage, "V")
                    print("Result:", result, "\n")

                    writer.writerow({
                        "test_id": test_id,
                        "voltage": voltage,
                        "result": result
                    })

    except FileNotFoundError:
        print("ERROR: test_data.csv was not found.")
        return

    except ValueError as error:
        print("ERROR:", error)
        return

    # Check whether measurements are available
    if not voltages:
        print("No valid test measurements found.")
        return

    # Test summary
    print("========== TEST SUMMARY ==========")
    print("Total tests:", passed + failed)
    print("Passed:", passed)
    print("Failed:", failed)
    print("\nResults saved to results.csv")

    # Engineering analysis
    print("\n========== ENGINEERING ANALYSIS ==========")

    average_voltage = sum(voltages) / len(voltages)
    maximum_voltage = max(voltages)
    minimum_voltage = min(voltages)
    pass_percentage = (passed / len(voltages)) * 100

    print("Average voltage:", round(average_voltage, 2), "V")
    print("Maximum voltage:", maximum_voltage, "V")
    print("Minimum voltage:", minimum_voltage, "V")
    print("Pass percentage:", round(pass_percentage, 2), "%")

    # Create voltage performance graph
    test_ids = list(range(1, len(voltages) + 1))

    plt.figure(figsize=(10, 5))

    plt.plot(
        test_ids,
        voltages,
        marker="o",
        label="Measured Voltage"
    )

    plt.axhline(
        y=upper_limit,
        linestyle="--",
        label="Upper Limit (12.5 V)"
    )

    plt.axhline(
        y=lower_limit,
        linestyle="--",
        label="Lower Limit (11.5 V)"
    )

    plt.xlabel("Test ID")
    plt.ylabel("Voltage (V)")
    plt.title("Automated Voltage Test Results")

    plt.xticks(test_ids)
    plt.grid(True)
    plt.legend()

    plt.savefig("voltage_analysis.png")
    plt.show()


# Execute application only when run directly
if __name__ == "__main__":
    main()