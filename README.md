# Saeta

_(This README.md and repository is **under construction**)_

Capable of massively asynchronously scanning all Internet, detecting every host and its open ports, extracting banners to discover services and details (HTTP Servers, E-mail, etc.), later adding them to an ElasticSearch DB to search for vulnerable services or sensitive information.


## Installation

For the moment, just install Pipfile dependencies using pipenv on root folder

```bash
  pipenv update
```
    

## Deployment

To see a glimpse on what the frontend will look like, go into `saeta/frontend` and run main file with uvicorn

```bash
  cd saeta\frontend
  uvicorn main:app
```

Then open http://127.0.0.1:8000/search on your browser of choice
## Run Locally

**Frontend and backend are not yet connected**, but you can start saving data into your ElasticSearch database (although it only saves open ports in hosts, reason and TTL. **NOT GRABBING BANNERS YET**).

Go into `saeta/backend` and run `main.py` (make sure to have your ElasticSearch database properly installed and running, **replace lines 66 & 74 with your ElasticSearch port. You must have an index called `_saeta`**)

```bash
  cd saeta\backend
  python3 main.py
```

This will start scraping services and uploading data to Elastic, netblock by netblock. You can change port quantity by changing `self.tcpPortQuantityToScan` and `self.udpPortQuantityToScan` variables, or if you want to set a total of ports and keep the 67/33 TCP vs. UDP preferred ratio just change the `self.totalPortQuantityToScan` variable. Ports are ordered by most common used, enhancing usefulness. **Example:** Setting `self.totalPortQuantityToScan = 1200` will scan the 804 TCP & 396 UDP most common ports.

You can change socket throughput by changing `masscanMaxRate` variable. This is measured by open connections per second.


In my computer it scrapes ≈100.000 hosts with 1200 total ports (like Shodan) every 5:30 hours, via WiFi **(Macbook Pro 2017 13")**. On a single computer like mine, I calculated it would take roughly **3 months** non-stop to scan the **whole IPv4 range** (without banner grabbing), **setting this on multiple VPS' would lower this time dramatically.**

_Personal note: ... although I think 3 months isn't a crazy long time to scan every single IP address, but it would be mildly outdated by the time you finish._

**Warning:** Port scanning may be considered illegal in some countries, so **use this at your own risk.**


## Contributing

Contributions are always welcome! Feel free to send a PR and I will review it as soon as possible.
Also post an issue if you have ideas or you see anything that you think is wrong. Please remember previously mentioned info, this app is **under construction.**

If you want to collaborate and don't know where to start, please start writing tests/connecting frontend and backend.

**Please give this repo a star if you think it's useful :)**


## Tech Stack

This project is mainly based on **Masscan & Nmap**
