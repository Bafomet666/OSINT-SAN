import nmap
import json


def default_ports_scan(host, port):
    print()
    print("Starting port scan with range 22-443")
    nm = nmap.PortScanner()
    scan_result = nm.scan(host, '22-443')
    display(scan_result)  # noqa


def custom_range_ports_scan(host, Yport):
        print()
        port_range = input("Enter the range : ")
        print()
        print(f"Starting port scan with range {port_range}")
        nm = nmap.PortScanner()
        scan_result = nm.scan(host, port_range)
        display(scan_result)  # noqa


def display(result):
    new = next(iter(result['scan'].values()))
    ip_add = new['addresses']
    print()
    print("IP Address : %s" % ip_add['ipv4'])
    hosting = new['hostnames']
    hostname0 = hosting[0]
    hostname1 = hosting[1]
    print()
    print("Hostname 1  : %s" % hostname0['name'])
    print("Hostname 2  : %s" % hostname1['name'])
    print()
    print("Open Ports  : ")
    print()
    ports = new['tcp']
    json_scan = json.dumps(ports)
    parsed = json.loads(json_scan)
    print(json.dumps(parsed, indent=4, sort_keys=True))
