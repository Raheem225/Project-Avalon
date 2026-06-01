Markdown

##Task 1: Transform CoinGecko's public API about digital assets into an insightful dashboard. Incorporate features such as alerts etc into the grafana dashboard.

Data source: CoinGecko API {https://docs.coingecko.com/v3.0.1/reference/trending-search}
Data storage (Mainly for trend graph): Elasticsearch
Data transformation: Python
Data visualization: Grafana Cloud
Environment: AWS (EC2 - Debian)

1. Create a table panel showing the top 15 trending coins according to user search.
2. Create a bar chat showing top 7 trending NFTs according to % change in price.
3. Create a table showing top categories of digital assets capturing the coins count and market cap.
4. Create a time series graph showing a trend of the fluctuations in rank of the coins in 1 above.





##Task 2: Build a prometheus dashboard to monitor the AWS EC2 infrastructure running task 1.

1. Create a stat panel showing system up time.
2. Create a stat and segmented gauge panel showing CPU cores and the active time.
3. Create a stat and a rounded arc gauge panel showing memory size and consumption.
4. Create a stat and a rounded arc gauge panel showing swap size and utilization.
5. Create a stat and a flat arc gauge panel showing disk size and utilization of the system.
6. Create a timeseries graph panel showing the memory state of the system.
7. Create a timeseries graph panel showing the disk utilization of the system.
8. Create a timeseries graph panel showing the memory consumption of the node expoerter process on the node.
9. Create a timeseries graph panel showing the CPU utilization of the node expoerter process on the node.