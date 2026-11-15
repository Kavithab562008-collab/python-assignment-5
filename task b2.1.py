import csv
 
def read_station_csv(path):
    try:
        with open(path, "r", newline="", encoding="utf-8-sig") as f:
            sample = f.read(2048)
            if not sample.strip():
                raise ValueError("File is empty")
            f.seek(0)
            try:
                dialect = csv.Sniffer().sniff(sample, delimiters=",;\t")
            except csv.Error:
                dialect = csv.excel
            reader = csv.DictReader(f, dialect=dialect)
            required = {"station", "date", "pm25"}
            if not reader.fieldnames or not required.issubset(reader.fieldnames):
                raise ValueError("Missing required CSV columns")
            return list(reader)
    except UnicodeDecodeError as exc:
        raise ValueError("Unsupported text encoding") from exc
    except FileNotFoundError:
        raise ValueError("Input file does not exist")
