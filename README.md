# PHBS_BlockChain_2018
Effectiveness of Quantitative Investment Strategies on Cryptocurrency
===
Cryptocurrency is a kind of electronic currency based on cryptography. In 2008, with the concept of Bitcoin proposed by Nakamoto, the cryptocurrency began to attract more and more attention from mainstream society. Because cryptocurrency such as Bitcoin is currently available for trading on many public exchanges, which is like stocks, it’s reasonable to think that the quantitative investment method which has been proved effective in stocks market may also be effective in cryptocurrency. The core idea of this paper is to test whether the quantitative investment strategy that has been successfully applied to the stock market is still valid for cryptocurrency such as Bitcoin. This paper mainly constructs the timing strategy based on the technical indicators derived from the stock price such as ADX, MA, and judges the effectiveness of the investment strategy according to the final result of the strategy.

# 1 Introduction
## 1.1	Introduction to quantitative investment
Quantitative investment refers to the way of trading for obtaining stable income through quantitative methods and computer programmatically issuing trading orders. Currently, it is mainly used in stocks, futures and some financial derivatives. There are two main branches of quantitative investment: quantitative stock selection strategies and quantitative timing strategies. Quantitative stock selection is to use some criteria to determine a portfolio from a large pool of investment targets to obtain excess returns. Quantitative timing is to determine the trading time for the same target and earn the profit based on the difference between the bid-ask spread on the same target.
Because the current type of cryptocurrency is relatively small in compared with stocks (the Chinese stock market has more than 3,000 stocks), the quantitative stock selection strategy is basically not applicable to cryptocurrency. Considering that the quantitative timing strategy operates on the same target, we can try to apply the quantitative timing strategy to the cryptocurrency.
There are many types of quantitative timing strategies. Considering the lack of fundamental data in cryptocurrency, we adapt technical indicators to construct quantitative timing strategies for cryptocurrency.

## 1.2 Strategic core idea
The core idea of this paper's strategy is to judge the current price trend according to the technical indicators, to buy the target when rising trends appear and earn the profit by following the trend. And if there are downward trends, we just sell out the portfolio to stop loss.
This paper mainly uses two technical indicators (MA and ADX). These two technical indicators are both calculated from price data of the target and indicate the trend of the target price. Based on the value of these indicators, we can determine the present trend and make our investment decision.

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

## 2.2 Meaning of ADX indicators
Although the process of calculating ADX is cumbersome, during which we use a lot of auxiliary variables, the meaning behind ADX is very clear. $DIplusN$ and $DIminusN$ describe recent ups and downs respectively. Whether it is rising or falling, as long as the trend is significant, there will always be a larger one among $DIplusN$ and $DIminusN$. So the value of $DX = 100 × abs((DIplusN – DIminusN) / (DIplusN + DIminusN))$ will range from 0 to 100. The more significant the trend is, the bigger the $DX$ is.Since $ADX$ is the smoothed mean of $DX$, $ADX$ can describe the strength of recent trends. Because the absolute value is taken when calculating $DX$, this results in $ADX$ values ranging from 0 to 100, so $ADX$ itself only describes the strength of the trend and does not indicate the direction of the trend. However, the direction of the trend can still be judged by the size of $DIplusN$ and $DIminusN$ (or other methods).
The blue curve in the figure below is the ADX value of the weekly frequency data of the Shanghai Composite Index over the past 12 years (n = 8 when calculating the smoothing mean). It is not difficult to see that there is significant rising trend in the circled area. And at the same time the ADX value in these area is also significantly high, which means ADX indicators can indicate the strength of the trend of stock price.
![000001.XSHG ADX](https://github.com/Simon9511/PHBS_BlockChain_2018/blob/master/picture/ADX_000001.png)
We use the same parameters to calculate the ADX indicator of BTC. And we can see from the picture below that ADX can also indicates significant trend in BTC price (in the circled area, there is a significant rising trend in BTC with a relatively high ADX value).
![BTC ADX](https://github.com/Simon9511/PHBS_BlockChain_2018/blob/master/picture/ADX_BTC.png)
From the graph above, you may notice that even when there is strong downward trend in the market, the ADX value is still very high, and think ADX may have some mistake in these situations. Actually, as we said earlier, the ADX indicator is only used to judge the strength of the trend, not to judge the direction of the trend. Therefore, when constructing a strategy, we will first judge the strength of the trend according to the ADX indicator. If the trend is strong, we will judge the direction of the trend based on other criterion. Therefore, the fact that the ADX index is high when the market falls does not affect the construction of our strategy.

## 2.3 ADX timing strategy construction
### 2.3.1 Strategy core idea
According to the above mentioned repeatedly, the ADX indicator can judge the significant trend very well. Therefore, when constructing an investment strategy, we first judge whether the current market is in a trend based on the value of the ADX. When ADX is greater than a certain threshold, we believe that it is currently in a trend situation and make the next decision. When the market is in a trend situation, we can judge whether the current stock price is in a rising trend or a downward trend based on the current stock price and the stock price comparison in the previous period.
### 2.3.2 Strategy details
In this strategy, we need to complete two judgments: buy judgment and sell judgment.
When the market conditions meet the buying criteria, we buy the target and continue to hold it. When the market conditions touch the selling criteria, we sell the portfolio and obtain the profit. The strategy is as follows:
- When the ADX value is greater than 35, and the stock price is greater than the stock price before 30 days, we buy the target.
- When the stock price decreased by 10% compared to the price of a month ago, or the max drawdown of recent one month is more than 15%, the sell out operation will be carried out. Otherwise we will always hold the position.<br>

The opening criteria of this strategy are very strict. When ADX is greater than 35 and the stock price is rising, we believe that the significant uptrend is already determined. It is precisely because our opening criteria are very strict, unless there are special circumstances, we will always keep the investment target. We only close the position when the net value of the stock falls below the stop loss line we set.
## 2.4 Strategy performance
### 2.4.1 Shanghai Composite Index
First, we perform back test on the Shanghai Composite Index. The time period for the backtesting is from 2005 to 2018. Because this time period includes various market conditions such as bear market, bull market and shock market, the back test results are more persuative.<br>
The strategy net value curve:<br>
![strategy netvalue on SCI](https://github.com/Simon9511/PHBS_BlockChain_2018/blob/master/picture/strategy_000001.png)
The strategy performance statistical indicators:

  Annual Profit  | Max Drawdown  | Sharpe Ratio
  :----: | :-----: | :------:  
  17.2%  | 26.2% | 2.27

From the net value curve of the strategy back test, we can see that this strategy can capture the market's rising trend (as shown in the black box), and this strategy will not trade when the market is volatile. After 10 years of investment, the net value of the strategy has more than 7 times, and the annualized rate of return has reached 17.2%, and the Sharp rate has reached 2.27, which is a good result. The maximum drawback of the strategy is 26.2%, which is relatively large, because in order not to miss the big uptrend, we set the stop loss line loosely. The advantage of this is that it will not miss the follow-up trend when the big trend comes, and the bad thing is that when the trend ends, the drawback is relatively large.

### 2.4.2 Bitcoin
Next, let us look at the application of this strategy on Bitcoin. In order to avoid overfitting problem, we don't choose a special parameter for Bitcoin and just use the same parameters as the above strategy for backtesting. The backtesting period was selected from 2005 to 2019. The strategy net value curve is shown below:
![strategy net value on btc](https://github.com/Simon9511/PHBS_BlockChain_2018/blob/master/picture/strategy_BTC.png)
The statistical indicators of strategic performance are as follows:

  Annual Profit  | Max Drawdown  | Sharpe Ratio
  :----: | :-----: | :------:  
  60.6%  | 59.9% | -2.18
  
From the results of the strategy backtesting, it is obvious that ADX strategy is not effective on Bitcoin, and the net value of the strategy does not catch up with the net value of the bitcoin price. Nonetheless, the annualized rate of return of the strategy has reached an astonishing 60%. The reason for this is that Bitcoin price has risen madly in the first few years of its existence, and the strategy of this strategy is very strict, which has led to the strategy missing many investment opportunities. After the bitcoin bubble burst, the price of Bitcoin fluctuated greatly, and this strategy could not capture a big upward trend.

### 2.4.3 Other cryptocurrency
Next, we apply our strategy to other cryptocurrency. Similarly, in order to avoid over-fitting, we have no intention of adjusting the strategy parameters, but applying the same parameters as the initial strategy. The strategy performances are as follows.
  - ETH
Strategy net value curve:
![strategy net value on eth](https://github.com/Simon9511/PHBS_BlockChain_2018/blob/master/picture/strategy_ETH.png)<br>

The statistical indicators of strategic performance are as follows:

  Annual Profit  | Max Drawdown  | Sharpe Ratio
  :----: | :-----: | :------:  
  32.5%  | 33.0% | 17.0
<br>  
 
  - LTC
Strategy net value curve:
![strategy net value on LTC](https://github.com/Simon9511/PHBS_BlockChain_2018/blob/master/picture/strategy_LTC.png)

The statistical indicators of strategic performance are as follows:

  Annual Profit  | Max Drawdown  | Sharpe Ratio
  :----: | :-----: | :------:  
  72.2%  | 77.6% | 5.62
<br>  
  
  - XRP
Strategy net value curve:
![strategy net value on btc](https://github.com/Simon9511/PHBS_BlockChain_2018/blob/master/picture/strategy_XRP.png)

The statistical indicators of strategic performance are as follows:

  Annual Profit  | Max Drawdown  | Sharpe Ratio
  :----: | :-----: | :------:  
  540.2%  | 55.4% | 11.0

Based on the net value curve and the strategy statistics, we can see that the application of this strategy in other cryptocurrency(such as Ethereum and Litecoin) is more effective than on Bitcoin. In these other cryptocurrency, the strategy can achieve excellent annual yields, while at the same time they have excess returns. This is mainly because the prices of these other digital currencies are not as frantic as the bitcoin, but the trend is more obvious, so the strategy can capture a large upward trend. In Bitcoin, bitcoin prices have risen too much because of the previous expansion and the strategy can not keep pace with the rise in bitcoin prices. That's why the strategy is significantly better on other cryptocurrency than on Bitcoin.

# 3 MA strategy
The MA strategy is another common strategy for quantitative investment. The strategy idea is very simple. It use the short-term moving average and the long-term moving average to judge the recent strength of the market, and then determine whether to buy or sell the target.

## 3.1 Strategy idea
Short-term trends in the market can be quantified using short-period moving averages, while long-term trends in the market can be quantified using longer-period moving averages. When the short-term moving average wears the long-term moving average, the two moving averages cross, and we call this cross a golden cross. Similarly, when the short-term moving average wears the long-term moving average, it is called the dead cross.

## 3.2 Strategy details
This strategy also requires two judgments: buy judgements and sell judgement. The criteria are as follows:
- When the target's 5-day moving average value is greater than the 30-day moving average value, it means the market's short-term uptrend is strong, so we need to carry out the buying operation.
- When the target 5-day moving average value is less than the 10-day moving average, it indicates that the short-term downtrend of the market is strong, and we should sell out the target.<br>

The reason why when making the buy-in judgment we use the 30-day moving average while the 10-day moving average is used when making selling judgement is because when we make the buying judgment, we hope to wait for the trend signal to be fully confirmed and then buy the position. Although using 30-day average value, the buying decision may be made a little later and we may lose some part of profit, it helps us to increase the accuracy of the judgement. When making selling decision, by using the 10-day moving average to judge, we can ensure that when the downtrend comes we can stop the loss timely.
In this strategy, we did not use many parameters, because when the numbers of parameters increase, the model has the risk of over-fitting. The simplest and straightforward idea helps us to test whether this investment logic is effective.

## 3.3 Strategy performance
We still tested our strategic thinking on four digital currencies. The results of the strategy are as follows:
- BTC
Strategy net value curve:
![strategy net value on BTC](https://github.com/Simon9511/PHBS_BlockChain_2018/blob/master/picture/strategy_MA_BTC.png)<br>

The statistical indicators of strategic performance are as follows:

  Annual Profit  | Max Drawdown  | Sharpe Ratio
  :----: | :-----: | :------:  
  86.1%  | 67.6% | 4.40
<br>  
 
- ETH
Strategy net value curve:
![strategy net value on eth](https://github.com/Simon9511/PHBS_BlockChain_2018/blob/master/picture/strategy_MA_ETH.png)<br>

The statistical indicators of strategic performance are as follows:

  Annual Profit  | Max Drawdown  | Sharpe Ratio
  :----: | :-----: | :------:  
  46.4%  | 51.4% | 27.79
<br>  
 
  - LTC
Strategy net value curve:
![strategy net value on LTC](https://github.com/Simon9511/PHBS_BlockChain_2018/blob/master/picture/strategy_MA_LTC.png)

The statistical indicators of strategic performance are as follows:

  Annual Profit  | Max Drawdown  | Sharpe Ratio
  :----: | :-----: | :------:  
  124%  | 53.8% | 30.79
<br>  
  
  - XRP
Strategy net value curve:
![strategy net value on btc](https://github.com/Simon9511/PHBS_BlockChain_2018/blob/master/picture/strategy_MA_XRP.png)

The statistical indicators of strategic performance are as follows:

  Annual Profit  | Max Drawdown  | Sharpe Ratio
  :----: | :-----: | :------:  
  718.9%  | 67.2% | 6.94
  
## 3.4 Results analysis
From the backtest results, the MA strategy can achieve excess returns on all four cryptocurrencies. Among them, the strategy performance is better on ETH and LTC. This is because the price trend of these two cryptocurrencies is more obvious. The MA strategy can effectively filter out the fluctuation period and obtain the benefits in the trend situation.

# 4 Summary
## 4.1 Strategy effectiveness
In general, the classic quantitative timing strategy can definitely obtain absolute profit on cryptocurrencies. For some targets, some strategies can also effectively obtain excess returns. This indicates that the cryptocurrency price is not valid. Among them, the ADX strategy can obtain excess returns on ETH, LTC and XRB; the MA strategy can obtain excess returns on all four digital currencies.

## 4.2 Analysis of bad performance on Bitcoin
From the backtest results we can see that the two quantitative strategies are not ideal for bitcoin, and even do not beat the benchmark price. This is because Bitcoin has a crazy rise period in the early stage. At this stage, it is very difficult for us to keep up with the price increase of Bitcoin, because every time we make a wrong judgment, we will lose a lot of profits. After the bitcoin price bubble burst, the volatility of bitcoin prices is very strong, and our strategy is difficult to make a correct judgment in this highly volatile market.

## 4.3 Best Investment Strategy for cryptocurrency
- When the price of digital money rises wildly (such as early bitcoin), any quantitative investment strategy is very difficult to work. In fact, just buying Bitcoin and holding it at this stage is the best investment strategy.
- When the digital currency price bubble bursts and the market tends to be rational, we can use quantitative timing strategies to obtain excess returns. As mentioned above, our strategy can achieve stable excess returns on both ETH and LTC.

# 5 Future prospects
Due to limited time, many strategy ideas have not been further verified in this paper. If there is an opportunity in the future, I hope to conduct further research on the basis of this article.
- 1. Test the application of more technical factors. This paper mainly tests the timing strategies derived from the two technical factors ADX and MA. In fact, in addition to these two factors, there are many technical factors (such as HMA, FRAMA, KAMA, etc.). Every indicator has different characrisitics. We can test the effectiveness of these technology factor timing strategies on cryptocurrency.
- 2. Multiple indicator resonance strategy. It is not accurate enough to use only one technical factor for timing. When the validity of more technical factors is tested, we can use multiple technical factors to judge at a time. When multiple factors indicate the buying signal at the same time, we carry out the buying operation. In this way, our winning rate will be further improved.

