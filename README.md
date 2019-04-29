# PHBS_BlockChain_2018
Effectiveness of Quantitative Investment Strategies on Bitcoin
===
Cryptocurrency is a kind of electronic currency based on cryptography. In 2008, with the concept of Bitcoin proposed by Nakamoto, the cryptocurrency began to attract more and more attention from mainstream society. Because cryptocurrency such as Bitcoin is currently available for trading on many public exchanges, which is like stocks, it’s reasonable to think that the quantitative investment method which has been proved effective in stocks market may also be effective in cryptocurrency. The core idea of this paper is to test whether the quantitative investment strategy that has been successfully applied to the stock market is still valid for cryptocurrency such as Bitcoin. This paper mainly constructs the timing strategy based on the technical indicators derived from the stock price such as ADX, HMA, and judges the effectiveness of the investment strategy according to the final result of the strategy.

# 1 Introduction
## 1.1	Introduction to quantitative investment
Quantitative investment refers to the way of trading for obtaining stable income through quantitative methods and computer programmatically issuing trading orders. Currently, it is mainly used in stocks, futures and some financial derivatives. There are two main branches of quantitative investment: quantitative stock selection strategies and quantitative timing strategies. Quantitative stock selection is to use some criteria to determine a portfolio from a large pool of investment targets to obtain excess returns. Quantitative timing is to determine the trading time for the same target and earn the profit based on the difference between the bid-ask spread on the same target.
Because the current type of cryptocurrency is relatively small in compared with stocks (the Chinese stock market has more than 3,000 stocks), the quantitative stock selection strategy is basically not applicable to cryptocurrency. Considering that the quantitative timing strategy operates on the same target, we can try to apply the quantitative timing strategy to the cryptocurrency.
There are many types of quantitative timing strategies. Considering the lack of fundamental data in cryptocurrency, we adapt technical indicators to construct quantitative timing strategies for cryptocurrency.

## 1.2 Strategic core idea
The core idea of this paper's strategy is to judge the current price trend according to the technical indicators, to buy the target when rising trends appear and earn the profit by following the trend. And if there are downward trends, we just sell out the portfolio to stop loss.
This paper mainly uses four technical indicators including ADX, HMA, FRAMA, and KAMA. These four technical indicators are all from the research reports of [*Liangxin Investment Corporation*](http://www.liang-xin.com/website/w/h?). According to the research report of the company, the timing strategy based on these four indicators can obtain significant excess returns on the Shanghai Composite Index. This article will re-implements these four indicators and tests their effectiveness in digital currency.

## 1.3 Why can we use timing strategy on cryptocurrency?
The timing strategy is used on the same target, earning profit by choosing the buying and selling time and following the rising trend. Therefore, the target applied by the timing strategy should meet two major conditions: First, the target has certain volatility, because if the price of the target is too stable, the price difference cannot be obtained; Second, the target price has a certain rising trend, because if the target price does not have a trend and is always oscillating, it is impossible to earn excess returns by following the trend.
The bitcoin price perfectly meets the above two conditions. Bitcoin prices have some volatility, and they also have some obvious rising trend, and this trend lasts relatively long. The chart below shows the trend of bitcoin prices from 2017.10 to 2018.10. The circled part shows a clear rising trend.
![BTC price from 2017.10 to 2018.10](https://github.com/Simon9511/PHBS_BlockChain_2018/blob/master/picture/BTC_price.jpg "BTC price from 2017.10 to 2018.10")

## 1.4 Data source
All data used in this article is obtained from [*cryptodatadownload.com*](www.cryptodatadownload.com). cryptodatadownload.com is a website that collects information on various cryptocurrency prices. The website provides data download service. We download the cryptocurrency price locally and then use python for data analysis.
cryptodatadownload.com provides daily, hourly quote data for cryptocurrency on multiple cryptocurrency trading platforms. To facilitate uniform comparison, we quote the quotation data of the [*Bitstamp*](https://www.bitstamp.net/) trading platform here (in US dollars). Founded in 2011, Bitstamp is one of the world's oldest cryptocurrency exchange platform. Therefore, using data from Bitstamp is very reliable.

1. Calculate<a href="https://www.codecogs.com/eqnedit.php?latex=upmove_{t}=high_{t}-high_{t-1}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?upmove_{t}=high_{t}-high_{t-1}" title="upmove_{t}=high_{t}-high_{t-1}" /></a>

$$
x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}
$$
