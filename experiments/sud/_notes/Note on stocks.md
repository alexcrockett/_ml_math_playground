# Notes on stocks included in training

The following set of stocks was compiled to create as well-rounded and robust a training set as possible. The assumption being that by using funds that either; have exposure to the stock market as a whole, or that have exposure to areas of the market that, broadly speaking, reflect financial behavior, a model would be trained on a realistic perspective of markets.

Each of the stocks/funds listed below will each have 500 entries entered to train the model in batches of 100. That means there will be 20,000 total rows processed over the course of the first round of training. From the original import of 5 years, an additional 3 years worth of data will remain unused and available for further training epochs. 

1. **Broad Market Exposure**:
    - **SPY** (S&P 500 ETF) and 
    - **QQQ** (NASDAQ-100 ETF) offer exposure to a large segment of the U.S. stock market, including the largest companies.
    - **DJIA** (Dow Jones Industrial Average) captures 30 significant U.S. stocks, providing insights into blue-chip performance.
    - **VTI** (Vanguard Total Stock Market ETF): Covers the entire U.S. stock market, providing exposure to small-, mid-, and large-cap stocks.
   - **ITOT** (iShares Core S&P Total U.S. Stock Market ETF): Similar to VTI, offering comprehensive coverage of the U.S. market.

2. **Sector-Specific ETFs**:
    - **XLF** (Financial Select Sector SPDR Fund), 
    - **VFH** (Vanguard Financials ETF), and 
    - **KRE** (SPDR S&P Regional Banking ETF) cover the financial sector.
    - **XLE** (Energy Select Sector SPDR Fund) provides exposure to the energy sector.
    - **IYK** (iShares U.S. Consumer Goods ETF) reflects the consumer goods sector.
    - **XLK** (Technology Select Sector SPDR Fund): Focused on the technology sector, capturing major tech companies.
   - **XLY** (Consumer Discretionary Select Sector SPDR Fund): Covers companies in the consumer discretionary sector.
   - **XLV** (Health Care Select Sector SPDR Fund): Provides exposure to the healthcare sector.

3. **Dividend and Income Focus**:
    - **NOBL** (ProShares S&P 500 Dividend Aristocrats ETF) and 
    - **VYM** (Vanguard High Dividend Yield ETF) focus on dividend-paying stocks.
    - **JNK** (SPDR Bloomberg Barclays High Yield Bond ETF) and 
    - **HYG** (iShares iBoxx $ High Yield Corporate Bond ETF) include high-yield bonds.

4. **International Exposure**:
    - **IXUS** (iShares Core MSCI Total International Stock ETF) and 
    - **HEFA** (iShares Currency Hedged MSCI EAFE ETF) offer exposure to international markets.
    - **VYMI** (Vanguard International High Dividend Yield ETF) focuses on international dividend stocks.
    - **EEM** (iShares MSCI Emerging Markets ETF): Offers exposure to emerging market economies.
   - **VEU** (Vanguard FTSE All-World ex-US ETF): Covers all world markets outside of the U.S., providing broader international exposure.

5. **Specialty and Niche Areas**:
    - **LIT** (Global X Lithium & Battery Tech ETF) and 
    - **USOI** (UBS ETRACS Crude Oil Shares Covered Call)

6. **Broad ETFs**:
    - **HDV** (iShares Core High Dividend ETF), 
    - **SCHD** (Schwab U.S. Dividend Equity ETF), and 
    - **DGRO** (iShares Core Dividend Growth ETF) are broadly focused on high dividend and growth stocks.

7. **Small-Cap Focus**:
   - **VB** (Vanguard Small-Cap ETF): Focuses on small-cap stocks in the U.S., which can behave differently from large-cap stocks.