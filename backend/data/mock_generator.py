import numpy as np
import pandas as pd

class MockDataGenerator:
    def __init__(self, initial_price, mu, sigma, num_steps, num_simulations):
        self.initial_price = initial_price  # Starting price
        self.mu = mu  # Expected return
        self.sigma = sigma  # Volatility
        self.num_steps = num_steps  # Number of time steps
        self.num_simulations = num_simulations  # Number of simulations

    def generate_data(self):
        dt = 1  # Time step (can be adjusted based on frequency)
        prices = np.zeros((self.num_steps, self.num_simulations))
        prices[0] = self.initial_price

        for t in range(1, self.num_steps):
            z = np.random.normal(0, 1, self.num_simulations)  # Generate random samples
            prices[t] = prices[t-1] * np.exp((self.mu - 0.5 * self.sigma ** 2) * dt + self.sigma * z * np.sqrt(dt))

        return prices

    def get_ohlcv(self):
        prices = self.generate_data()
        timestamps = pd.date_range(start=pd.Timestamp('2026-04-15 10:34:50'), periods=self.num_steps, freq='T')
        data = {
            'timestamp': timestamps,
            'open': prices[0],
            'high': np.max(prices, axis=0),
            'low': np.min(prices, axis=0),
            'close': prices[-1],
            'volume': np.random.randint(1, 1000, size=self.num_simulations)
        }
        return pd.DataFrame(data)