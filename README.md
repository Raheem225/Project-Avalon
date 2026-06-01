# Project-Avalon

####Overview####
CoinGecko is a popular crypto data platform that helps users track prices, market trends, and the latest updates across the cryptocurrency world. Upon coming across CoinGecko's Trending Search List API (https://docs.coingecko.com/v3.0.1/reference/trending-search) which essentially allows you to query trending search coins, NFTs and categories. It seems the API directly powers this section (https://www.coingecko.com/en/highlights/trending-crypto) of the CoinGecko platform. While the first dashboard in this project essentially transforms the aforementioned API into insights, it also addresses a small gap. Generally cryptocurrency analysis and charts focus heavily on price changes, however there are times when it may be useful to do some additional analysis using the search trend data (particularly, that of a coin). This is where Grafana's powerful alerting features and timeseries graph on this project come in. In fact, user search trends are not only helpful when monitoring newly launched coins, finding opportunities before major listings or tracking market narrative; they can assist in proactively detecting early retail interest before significant price changes and broad market reaction. Also, pairing (upward) search trend insights with other factors like increase in price and volume gives a better picture of the overall market momentum which could otherwise be heavily skewed by a few large traders.

The second dashboard simply uses a prometheus node exporter to monitor the AWS EC2 instance on which the entire setup is running. In order to manage free credits on AWS, I am using a small instance and this comes with its own challenges related to resource utilization. Consequently, I also setup alerts related to consumption of resources such as memory, CPU, disk etcetera.


Lastly, I also added a very simple python grader at the end which programmatically verifies certain elements of the task. Think of it loosely like a unit test.



####Architecture####

     (Python transformation)
API -------------------------> Elasticsearch --------------> Grafana
                              (Hosted on AWS)
