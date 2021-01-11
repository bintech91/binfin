class BootCampTask(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2017, 6, 1)
        self.SetEndDate(2017, 6, 15)

        #1,2. Select IWM minute resolution data and set it to Raw normalization mode
        self.iwm = self.AddEquity("IWM", Resolution.Minute)
        self.iwm.SetDataNormalizationMode(DataNormalizationMode.Raw)

    def OnData(self, data):

        #3. Place an order for 100 shares of IWM and print the average fill price
        #4. Debug the AveragePrice of IWM
        self.MarketOrder("IWM", 100)
        if self.Portfolio["IWM"].Invested:
            self.Debug(self.Portfolio["IWM"].AveragePrice)
