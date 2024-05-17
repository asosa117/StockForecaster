Introduction
	As technology continues to improve and various ideas come to light, the average American becomes exposed to more knowledge at the click of a button. With the shape of our current smartphones and desktops/laptops, anyone can perform tasks with relative ease that 20 years ago would have required specialized knowledge; one such task is stock management. There have been multiple apps in the financial sector such as Robinhood, Charles Schwab, and Fidelity, that are now allowing anyone with access to a smartphone the opportunity to trade stocks online. According to Gallup, based on a 2023 April Economy and Personal Finance survey, 61% of Americans report they own stock, which is up 6% from 2020’s 55% ownership percentage (Jones, 2023). More people are beginning to learn about the opportunities stock trading offers, but that can come at risk for an individual who isn’t as knowledgeable in the concepts of trading. A new trader can become more susceptible to emotional trading, lack of risk management, and overtrading due to a lack of education and knowledge of the stock market (Burns, 2023). The stock market, without a strategy, can be compared to placing a bet on a sports team, you think they’re going to do well but they end up having their star player injured and you lose your bet because you didn’t do research. Having an AI for stock market simulation is important because it will give this new wave of stock traders a source of information they can use to base their trading rather than going in with no research. 
In early 2021, GameStop and AMC stock were reaching a tipping point which hedge funds decided would be an optimal time to place short bets on them. Social media users became aware of this and began buying GameStop and AMC stock as a way to increase their stock prices and go against the short sellers. The stock rose significantly as more individuals decided to join the movement and short sellers bought shares to cover their losses (Osman, 2023). Having an AI simulate GameStop and AMC stock during the movement would have allowed traders to understand if they should continue to buy or bet on the short. Cryptocurrency jumped in popularity during the covid pandemic lockdown as well with notable currencies such as Bitcoin, Ethereum, and Dogecoin being in the spotlight. Cryptocurrency to the general public was something new that was different from regular stocks which created a gray zone in trading knowledge. People began building around crypto and followed them without fully understanding how crypto worked. This led to company/crypto collapses with billions of dollars in losses from average traders. The Luna Cryptocurrency and FTX are some examples of crashes that led to $60 billion being wiped out of the digital currency space and $8.9 billion in customer assets missing, respectively (Rooney, 2023). Cryptocurrencies being a new way to trade require more sources that will help traders understand when to buy and sell. An AI to simulate the future values of stocks and cryptocurrencies would be a major asset in making stock management decisions.
From the start of COVID-19 and the volatility of the market as of late, people have been finding it harder and harder to trust the stock market. Especially the younger generations such as Millennials and Generation Z. These two groups of people aren’t investing in the stock market as much and it can start to affect the buying and selling of company stock (Merkoulova & Veld, 2022). The stock market is important because it “works as a platform through which savings and investments of individuals are efficiently channeled into productive investment opportunities and add to the capital formation and economic growth of the country” (What Is the Stock Market, What Does It Do, and How Does It Work?, n.d.). This can cause even more volatility in the stock market and create even more havoc. This general problem is what we hope to attempt to tackle, we hope to ease the minds of future stock market investors and help predict some of the future for these stocks. 
Many already existing applications use AI to predict future stock prices. One such app is Danelfin, which uses AI to rate stocks on a scale from 1 to 10, where 10 is a strong buy and 1 is a strong sell. The AI uses an algorithm that analyzes and rates stock fundamentals, technicals, sentiment, and risk. What makes Danelfin stand out relative to other stock predictors is its transparency in how it calculates its ratings, showing details of each factor such as current value, sub-rankings from 1 to 10, signal importance, and calculated odds to beat the market (Dave, 2023).
Danelfin’s main disadvantages are missing features that consumers would likely use; it does not display fundamental analysis tools such as earnings per share, price-to-earnings ratio, return on equity, etc., nor does it display technical analysis tools such as relative strength index, moving average, on-balance volume, etc. It also doesn’t have a stock screener function for choosing stocks based on search criteria (Dave, 2023).
Another app is AltIndex, which uses AI and alternative data to create ratings for user-selected stocks, ranging from 1 (low) to 100 (high). Essentially, the AI extracts data from non-traditional sources, such as social media sites like Twitter, Facebook, and Reddit. More specifically, it looks for and analyzes public sentiment about companies and related stocks using follows, likes, and shares. More positive sentiment leads the AI to give a high rating, and more negative sentiments lead to lower ratings (Pepi, 2023). This use of alternative data is a strong advantage for this app relative to other stock predictors because most others use only conventional data sources such as financial news, quarterly earnings reports, annual statements, etc., meaning that most stock predictors use the same data and thus come up with similar results. Alternative data adds other perspectives from the mass public, which may factor into a better result (Pepi, 2023).
AltIndex does not seem to have any major disadvantages compared to other stock predictors besides requiring a paid subscription to access all features and not covering commodities (Pepi, 2023). However, although AltIndex is an excellent example of an existing app that uses AI to power a stock predictor, it does not do it (or at least it does not visualize it) in the way we plan to. We want to create an app that is more visual with its predictions; instead of just giving stock ratings on whether to buy them or not, we want to create a graph that shows AI-predicted prices, like a standard stock graph with the addition of future dates to the right of the current date.
Our program is similar to another LTSM model being developed by our other classmates and they had trouble with the time series forecasting by using the LSTM model and their model not being able to predict the spikes. We encountered this same problem since our model exists to replicate a "normal" trading environment without the interference of extreme outside events. It's a simulation of the majority of time when trading: pretty boring trends, not exciting spikes. This is helpful for nonserious and more recreational investors and people we hope to target are those people starting in the stock market and who are investing in more “safe” and “easier” options such as the S&P 500 or Apple, these things tend not to fluctuate as much as smaller and more volatile investments. If we did have a corner on this “spike” prediction we would be able to make millions of dollars because then it would be a more “true” stock market prediction but this simply is not possible due to a variety of variables.
Our Application
Our AI application is going to be an AI-assisted simulation of stocks and the stock market. We hope to target the population of people who hope to see how their choices are going to play out before they make their choices of stocks, ETFs, or any other form of the stock market they hope to corner. The main functionalities of our AI application are going to be actively showing the current stock market as well as a way to select certain stocks to highlight or “favorite.” To predict their future values, there will be a function to select certain stocks and a length of time to predict; most other stock market apps have increments of 1 Day, 5 Days, 1 Month, and 1 Year, which we also plan to use. Much like the other applications that exist, we will draw data from financial news, earnings reports, and other annual reports coming from the stocks themselves. If possible, we also want to use stock data from social media and third-party reporting sites to supplement our data, similar to apps such as AltIndex. We want to draw from as many sources as possible to create the best-informed predictions we can.
We hope to implement some of the features that other applications lack, like displaying fundamental analysis tools and technical tools, such as earnings per share, price-to-earnings ratio, return on equity, relative strength index, moving average, on-balance volume, etc. The immediate benefits of our application also help the lack of knowledge that some of the population have about the stock market. In a study assessing the reasons why most people don’t invest in the stock market, 22% of all people who responded to the survey don’t have the knowledge to invest and feel it is too risky (Merkoulova & Veld, 2022). Our application can help ease the minds of people investing money for long terms in the stock market by representing what would possibly happen to their money. While our application can’t predict exactly what will happen, it can help show the possible progression or decline of investments.

IMPLEMENTED FEATURES
DESCRIPTION
Stock market viewer
Shows the user the current state of the stock market
Prediction maker/Forecaster
Gives the user the ability to choose stocks that they want to predict and for the duration of their choosing
Favorites
Ability to favorite stocks they want to keep an eye on


The inputs of our application are as follows: data from financial news, earnings reports, and other annual reports coming from the stocks themselves. We may also try to gather data from social media and third-party reporting sites on stocks to supplement our predictions. All these potential sources of data will then go through our AI, and as an output, we will have visual graphs and charts of stock prices and their fluctuations on the web UI. We will also have different time stamps for certain days to show what the price was on a given day.

Link to the Python File of our AI
The specific AI algorithm/model we plan to use is a long short-term memory (LSMT) machine learning model. It is a specialized type of recurrent neural network (RNN), which is a neural network designed for processing sequential data by remembering information from previous inputs, which they then use to process the current input (Saxena, 2021). Unlike traditional RNNs, LSTM incorporates memory cells and three gates—forget, input, and output gates—to regulate the flow of information within the network, which allows it to work with long-term dependencies. These gates enable the model to selectively keep or discard information, allowing them to learn patterns in time-series data (Saxena, 2021). LSTMs are widely used in various applications, including time series predictions, which is exactly what we need.
	To train our LSTM model, we also need to determine optimal epochs and batch sizes. Epoch is the number of times the LSTM is run through the data, and batch size is the number of values processed before being passed through the model. A higher epoch number makes the model fit the input data better, while a higher batch size decreases training time. However, these values should not go too high, as a high epoch may lead to overfitting, while a high batch size will decrease accuracy. Overfitting is where the model becomes too accustomed to the training data, and thus predicts very well on the training data, but performs poorly with any other data. However, having too low epoch numbers will lead to underfitting, which just makes the model rather vague and inaccurate for any data input. The key to having a good model depends on a balance of fit and training time, adjusted using epochs and batch number

Pipeline for Application Development and Implementation From Phase 1










Updated Pipeline for Application Development and Implementation

The way we plan to develop our app is through a continuous development and implementation pipeline. In general, we would first develop the app by coding, testing, and creating the core functions as well as the UI before going through more rigorous testing. We would repeat this process as many times as we would need until the app is ready for a final deployment.
We were not able to complete things such as unit testing, user acceptance testing, and load testing. These were added to our initial pipeline as goals for us to achieve and potentially do but it wasn’t feasible within the scope of our application. We were able to do functional tests making sure that the forecast graph depicts something that looks right anecdotally. We can’t exactly do something like user acceptance testing, the closest we have done is functional testing. But we have done that same functional testing repeatedly to make sure our final product is the best it can be. The other forms of testing were there as a guideline for what we could potentially do but the only form of testing that was applicable here was functional testing.

Initial UI Design

Link to Figma UI.
	Our initial UI design was made using Figma. It’s currently comprised of four main tabs (which can be expanded if needed): a stocks searcher, favorited stocks, future graph simulator, and settings. The Figma link above displays a fundamental layout with a sidebar on the left to navigate to the four tabs, and each tab shows some basic UIs that we will develop more at a later date. Although barebones for now, we have a lot of features that we can implement later.


Final Web UI
Link to GitHub Repository
	For our final app, the UI has become much more refined, and the stock forecasting AI has been integrated. The final app has two pages, both of which have links at the top of the page. The app starts on the general page upon running app.py. On it are instructions on how to use the forecaster, definitions for the necessary input values, the input values entry boxes, and the graph. The necessary inputs include a ticker symbol, price history for actual values, lookback range for training the AI, and forecast range for prediction. If a user ever inputs an invalid input, an error message will show up above the graph.



	The favorites page includes a list of the user's favorited tickers with their price respectively. The page is formatted with an input box and a button that allows the user to input their favorite ticker and then click the “Save” button to save it to their list. Once saved, the program will display a table with the user’s current list of favorites tickers along with the ticker’s current price which was retrieved using the yfinance library.






UML Class Diagram



	Our initial UML class diagram includes 4 classes: stock, market, AI, and user. A user can have zero to many stocks saved/favorited, the market holds many stocks, and the AI predicts the future values of one or more stocks. The stock class includes important data about each stock such as their history of values + dates, uniquely identified by their ticker number. The market class simply holds all the stocks by ticker ID. The AI class is what we will use to predict and graph the future values of a selected stock. The user class is mainly for information such as saved stocks.

Languages and libraries

The AI will be a web application using Dash for its front-end construction and a variety of other Python libraries for its back-end implementation. This will allow the consumer to view the results of the AI in a user-friendly way while the app runs more complex classes in the Python background. Dash is a Python framework for building web applications, and it is built on top of other frameworks such as Flask, Plotly.js, React, and React Js. It allows building dashboards using purely Python (“Dash for Beginners”, 2018). The relevant libraries for the back-end include vfinance for obtaining all the necessary stock market data we need (Aroussi, 2023), sci-kit for parts of machine learning we can incorporate into our AI (“User Guide,” n.d.), and Keras, which has an already built LSTM model that we can use (Keras Team, n.d.).
Final Test Results and Discussions
Our AI stock application is showing progress, as it displays a simulation of a chosen stock with its graph of growth up to the current day and a prediction of how the stock may perform until a chosen date. From our first phase, we thought about using the S&P 500 but changed our mind to Apple stock instead. This change was purely a change of opinion and we wanted to clarify this in our last phase. Our application can take into account any stock that is currently being publicly traded so the type of stock we use for our example is not as important. We've been using Apple Inc. as our test ticker to see how the AI agent would manipulate the data and display it to the user. The AI correctly, albeit roughly, displays the stock’s current price and its growth from a date while also simulating how the stock would move throughout the years.
One way to check how accurate the AI agent is is by reading various articles about Apple stock to see what experts were predicting along with studying the trend of current Apple stock to see if it has been moving up, moving down, or fluctuating between both. Using the matplotlib library we’ve been able to visually graph the AI Agent’s predictions from the stock data obtained using the yfinance library. This has allowed us to test our application's performance by reading the created graph and conducting a test of correctness by personally studying the stock trends. Another way we can test the functionality of our AI is by using past data to predict past data, i.e. using data between 2015 and 2023 to forecast prices between 2023 and 2024. This way, we have both actual prices and predicted prices to compare to each other.


Apple Stock Prediction From AI Agent, 2024 - 2025

	Ultimately, there is no way to predict a company’s stock price accurately, but using data available from what has already occurred the AI agent can read the stock’s historical trends to report an approximate prediction of future values if there were no outside influences. Thus our final test results showed that our app was not perfect due to unpredictable factors such as future customer satisfaction, spontaneous decisions of companies, even just plain bad luck; obtaining a perfect forecast is practically impossible. However, it has created data for a time period that has not passed, and that data is generally in the right direction.
Lessons Learned
	Something that we have learned so far is that for what we’re making, there is no reliable way to do so: predicting exact future stock prices is practically impossible. Theoretically, if you knew about all upcoming events and factors that can change stock value, you could predict them reasonably well. However, the problem with that is that the future is inherently unpredictable. Sure, you could try to predict future prices by taking into account the past year or so trend of the price (which is what we currently have), and then factor in major announcements made by companies related to the stock, but that would still completely disregard everything else that has major holds on the price, ranging from customer satisfaction to spontaneous decisions to just plain bad luck. Those factors are disregarded because you cannot predict them. In other words, a true stock forecaster that accurately sees further than a day is more or less completely impossible, which makes sense since otherwise the stock market would stagnate or break from everyone knowing the futures of stock prices. We can only try our best to make something that predicts future stock prices further than a day.
	On a related note, most “stock predictor” examples that you can find online compare the “predictions” with actual data (i.e. using machine learning to predict prices in 2020, and comparing the predictions to the actual values), with each “prediction” line impressively close to the actual value. It’s significantly less impressive than you’d think, since each day’s prediction uses the past 30 or so days for training data, meaning every predicted day’s value is based on the past 30 days of actual values. So when they show a predicted line for a month, it’s just a bunch of single-day forecasts, all using actual data so that as long as the forecast value doesn’t vary too much from the most recent day, the forecast line will look impressively close to the actual line no matter what.

	Some new skills and knowledge we have had to work with include working with new Python libraries, such as yfinance, Keras, and matplotlib: yfinance for extracting stock data, Keras for machine learning models, and matplotlib for creating visual graphs. We also had to learn more about machine learning models, specifically LSTM, and how training works with machine learning models (epochs, batch sizes, underfitting, overfitting, etc.). We have also had to learn how to use Dash to create the front end of our web app.
Timeline Schedule for the Remaining Project Tasks

Conclusions and Future Work 
	This project is a functional stock predictor application that takes in real stocks and can predict the future of this stock. This is the application we set out to achieve and we as a team think created a useful and functional application. 

Phase 1 Goal Features

POTENTIAL FEATURES
DESCRIPTION
Stock market viewer
Shows the user the current state of the stock market
Prediction maker
Gives the user the ability to choose stocks that they want to predict and for the duration of their choosing
Favorites
Ability to favorite stocks they want to keep an eye on
StockChat
Ability to ask the AI questions about stocks and learn more about other questions related to stocks

	
Phase 3 Final Features

IMPLEMENTED FEATURES
DESCRIPTION
Stock market viewer
Shows the user the current state of the stock market
Prediction maker/Forecaster
Gives the user the ability to choose stocks that they want to predict and for the duration of their choosing
Favorites
Ability to favorite stocks they want to keep an eye on

	
	The difference between the two tables is very little so we were able to implement most of the basic features we set out to implement. The only one that we decided not to go with was the StockChat feature which was too difficult to implement without using other proprietary AI applications such as ChatGPT and creating our version of a model similar to ChatGPT wasn’t in the scope of our project schedule nor the scope of our skills as a team. But all in all, we did very well implementing the features we sought to achieve.
	Some potential ideas for future work that would make our app better include a better/more user-friendly UI, a more productive favorites page (perhaps something to link the contents of the favorites page to the general page), and an account/login system.

Phase 1 Proposed Schedule


Phase 3 Followed Schedule


	Our team also did very well at sticking to the schedule that we proposed at the beginning of our project. It was difficult to coordinate four different schedules together through a very busy term but we were successful in doing so and producing an amazing application. We also didn’t have any parts of our project that weren’t accomplished by our efforts. 	
	If someone were to continue developing this application, some of the features we feel would make this more usable would be the StockChat feature that we nixed at the beginning of our project. 

Give potential tasks for future AI work to make your application into a really usable and practical system.

Background Materials/References:

Aroussi, R. (2023, October 4). yfinance: Download market data from Yahoo! Finance API [OS Independent]. Retrieved November 11, 2023, from https://pypi.org/project/yfinance/

Burns, S. (2023, March 10). Why 90% Of Traders Lose Money. MoneyShow. https://www.moneyshow.com/articles/tradingidea-60554/why-90-of-traders-lose-money/

Dajac, C. V. G. (2020). Time Series Analysis Handbook. Chapter 4: Granger Causality Test - Time Series Analysis Handbook. https://phdinds-aim.github.io/time_series_handbook/04_GrangerCausality/04_GrangerCausality.html

“Dash for Beginners.” DataCamp, Aug. 2018, https://www.datacamp.com/tutorial/learn-build-dash-python#.

Dave. (2023, August 3). Danelfin Review – AI-Powered Stock Picking Service. Day Trade Review. https://daytradereview.com/danelfin-review/

Jones, J. M. (2023, May 31). What percentage of Americans own stock?. Gallup.com. https://news.gallup.com/poll/266807/percentage-americans-owns-stock.aspx

Kenton, W. (2023, September 22). S&P 500 index: What It’s for and Why It’s Important in Investing. Investopedia. https://www.investopedia.com/terms/s/sp500.asp

Keras Team. “Keras Documentation: LSTM Layer.” Keras, https://keras.io/api/layers/recurrent_layers/lstm/.
Accessed 3 Dec. 2023.

Merkoulova, Y., & Veld, C. (2022). Why do individuals not participate in the stock market? International Review of Financial Analysis, 83, 102292. https://doi.org/10.1016/j.irfa.2022.102292

Osman, J. (2023, August 28). Why you’re almost guaranteed to lose money trading gamestop, AMC &amp; Other Meme Stocks. Forbes. http://www.forbes.com/sites/jimosman/2023/08/26/why-youre-almost-guaranteed-to-lose-money-trading-gamestop-amc--other-meme-stocks/?sh=28eae79034ca

Pepi, K. (2023, September 2). AltIndex Review 2023 – Pros & Cons Revealed. Technopedia. https://www.techopedia.com/investing/altindex-review.

Rooney, K. (2023, October 2). FTX customers who lost a fortune on the bankrupt exchange are doubling down on crypto. CNBC. http://www.cnbc.com/2023/10/02/ftx-customers-who-lost-fortune-are-doubling-down-on-crypto-.html

Saxena, Shipra. “What Is LSTM? Introduction to Long Short-Term Memory.” Analytics Vidhya, 16 Mar. 2021, https://www.analyticsvidhya.com/blog/2021/03/introduction-to-long-short-term-memory-lstm/.

User guide. (n.d.). Scikit-Learn. Retrieved November 11, 2023, from https://scikit-learn/stable/user_guide.html

What Is the Stock Market, What Does It Do, and How Does It Work? (n.d.). Investopedia. Retrieved December 2,
2023, from https://www.investopedia.com/terms/s/stockmarket.asp
