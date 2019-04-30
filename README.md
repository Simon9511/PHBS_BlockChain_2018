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

# 2 ADX strategy
The ADX strategy is based on the investment strategy of the technical indicator ADX. The ADX indicator is a composite technical indicator calculated by the opening price, closing price, highest price and lowest price of the target, which can be used to quantify the current market trend strength. According to the ADX indicator, we first judge whether there is a trend in the current market. If there is a trend, then compare with the recent increase and other data to determine whether it is an upward trend, if it is determined to be an upward trend, then follow the trend to buy to earn excess returns.

## 2.1 ADX calculation method
1. Calculate $UpMove$ and $DownMove$:
$$
UpMove_{t}=high_{t}-high_{t-1}
$$
$$
DownMove_{t}=low_{t-1}-low_{t}
$$
2. Calculate $DMplus$ and $DMminus$:<br>
When $UpMove > max(DownMove, 0)$, $DMplus=UpMove$; else, $DMplus=0$<br>
When $DownMove > max(UpMove, 0)$, $DMminus=DownMove$; else, $DMminus=0$<br>

3. Calculate the true volatility of the day (denoted as $TR$), which is equal to the maximum of the following three values: the difference between $high_t$ and $low_t$, the absolute value of difference between $high_t$ and $close_{t-1}$ and the absolute value of the difference between $low_t$ and $close_{t-1}$.

4. For $DMplus$, $DMminus$, and $TR$, we use the smooth motion algorithm to calculate the sum of n periods, denoted as $DMplusN$, $DMminusN$, and $TRN$ respectively. Take $TRN$ as an example, its calculation method is:<br>
- The first value of $TRN$ is the sum of $TR$ for the past n days (including the current day);<br>
- Starting from the second value, the $TRN_t = TRN_{t-1} × (n - 1) / n + TR_t$

5. Calculate $DIplusN$ and $DIminusN$:
$$
DIplusN = 100 * DMplusN / TRN
$$
$$
DIminusN = 100 * DMminusN / TRN
$$

6. Calculate the direction motion index $DX$:
$$
DX = 100 * |(DIplusN – DIminusN) / (DIplusN + DIminusN)|
$$

7. Calculate $ADX$. It is the n-period smooth moving average of $DX$. Its calculation method is:<br>
- The first value of $ADX$ is the mean of $DX$ over the past n days (including the current day);<br>
- Starting from the second value, $ADX_t = (ADX_{t-1} * (n-1) + DX_t) / n$<br>

## 2.1 Meaning of ADX indicators
Although the process of calculating ADX is cumbersome, during which we use a lot of auxiliary variables, the meaning behind ADX is very clear. $DIplusN$ and $DIminusN$ describe recent ups and downs respectively. Whether it is rising or falling, as long as the trend is significant, there will always be a larger one among $DIplusN$ and $DIminusN$. So the value of $DX = 100 × abs((DIplusN – DIminusN) / (DIplusN + DIminusN))$ will range from 0 to 100. The more significant the trend is, the bigger the $DX$ is.Since $ADX$ is the smoothed mean of $DX$, $ADX$ can describe the strength of recent trends. Because the absolute value is taken when calculating $DX$, this results in $ADX$ values ranging from 0 to 100, so $ADX$ itself only describes the strength of the trend and does not indicate the direction of the trend. However, the direction of the trend can still be judged by the size of $DIplusN$ and $DIminusN$ (or other methods).
The blue curve in the figure below is the ADX value of the weekly frequency data of the Shanghai Composite Index over the past 12 years (n = 8 when calculating the smoothing mean). It is not difficult to see that there is significant rising trend in the circled area. And at the same time the ADX value in these area is also significantly high, which means ADX indicators can indicate the strength of the trend of stock price.
![000001.XSHG ADX](https://github.com/Simon9511/PHBS_BlockChain_2018/blob/master/picture/ADX_000001.png)
We use the same parameters to calculate the ADX indicator of BTC. And we can see from the picture below that ADX can also indicates significant trend in BTC price (in the circled area, there is a significant rising trend in BTC with a relatively high ADX value).
![BTC ADX](https://github.com/Simon9511/PHBS_BlockChain_2018/blob/master/picture/ADX_BTC.png)
From the graph above, you may notice that even when there is strong downward trend in the market, the ADX value is still very high, and think ADX may have some mistake in these situations. Actually, as we said earlier, the ADX indicator is only used to judge the strength of the trend, not to judge the direction of the trend. Therefore, when constructing a strategy, we will first judge the strength of the trend according to the ADX indicator. If the trend is strong, we will judge the direction of the trend based on other criterion. Therefore, the fact that the ADX index is high when the market falls does not affect the construction of our strategy.















