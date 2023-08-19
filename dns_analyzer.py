import csv
import socket

def analyze_dns(website):
    try:
        ip_addresses = socket.gethostbyname_ex(website)[2]
        return ip_addresses
    except Exception as e:
        print(f"Error analyzing DNS for {website}: {e}")
        return []

def main():
    input_csv = "website_list.csv"
    output_csv = "dns_analysis.csv"

    # Read website URLs from CSV
    websites = []
    with open(input_csv, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            websites.append(row["Website"])

    # Analyze DNS for websites and store results
    results = []
    for website in websites:
        ip_addresses = analyze_dns(website)
        results.append({"Website": website, "IP Addresses": ", ".join(ip_addresses)})

    # Write results to CSV
    with open(output_csv, "w", newline="") as csv_file:
        fieldnames = ["Website", "IP Addresses"]
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(results)

    print(f"DNS analysis results saved to {output_csv}")

if __name__ == "__main__":
    main()
