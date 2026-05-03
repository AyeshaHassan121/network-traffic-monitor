from flask import Flask, render_template, jsonify, request
import csv
import os

app = Flask(__name__)

packets_log = []
is_loaded = False

def load_dataset():
    global packets_log
    packets_log = []
   
    dataset_path = os.path.join(os.path.dirname(__file__), 'dataset.csv')
    with open(dataset_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            packets_log.append({
                "time":     row["Time"],
                "src_ip":   row["Source IP"],
                "dst_ip":   row["Destination IP"],
                "protocol": row["Protocol"],
                "src_port": row["Src Port"],
                "dst_port": row["Dst Port"],
                "service":  row["Service"],
                "size":     int(row["Size"])
            })

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/start", methods=["POST"])
def start():
    global is_loaded
    load_dataset()
    is_loaded = True
    return jsonify({"status": "started"})

@app.route("/stop", methods=["POST"])
def stop():
    global is_loaded, packets_log
    is_loaded = False
    packets_log = []
    return jsonify({"status": "stopped"})

@app.route("/packets")
def get_packets():
    protocol = request.args.get("protocol", "")
    src_ip   = request.args.get("src_ip", "")
    dst_ip   = request.args.get("dst_ip", "")

    filtered = packets_log

    if protocol:
        filtered = [p for p in filtered if p["protocol"] == protocol]
    if src_ip:
        filtered = [p for p in filtered if src_ip in p["src_ip"]]
    if dst_ip:
        filtered = [p for p in filtered if dst_ip in p["dst_ip"]]

    return jsonify(filtered)

@app.route("/stats")
def stats():
    total = len(packets_log)
    tcp   = sum(1 for p in packets_log if p["protocol"] == "TCP")
    udp   = sum(1 for p in packets_log if p["protocol"] == "UDP")
    icmp  = sum(1 for p in packets_log if p["protocol"] == "ICMP")
    avg   = round(sum(p["size"] for p in packets_log) / total, 2) if total > 0 else 0
    return jsonify({"total": total, "tcp": tcp, "udp": udp, "icmp": icmp, "avg_size": avg})

if __name__ == "__main__":
    app.run(debug=True)