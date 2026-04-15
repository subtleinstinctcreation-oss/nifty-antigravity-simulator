from dataclasses import dataclass, field
from typing import List, Dict, Optional

@dataclass
class Position:
    symbol: str
    size: float
    entry_price: float
    current_price: Optional[float] = None

    def update_current_price(self, price: float):
        self.current_price = price

    def get_pnl(self) -> float:
        if self.current_price is not None:
            return (self.current_price - self.entry_price) * self.size
        return 0.0

@dataclass
class Trade:
    position: Position
    trade_type: str  # 'buy' or 'sell'
    quantity: float
    price: float

@dataclass
class Signal:
    symbol: str
    signal_type: str  # 'buy', 'sell', 'hold'
    strength: float  # Strength of the signal

@dataclass
class Portfolio:
    positions: Dict[str, Position] = field(default_factory=dict)
    cash: float = 100000.0  # Initial cash amount

    def execute_trade(self, trade: Trade):
        if trade.trade_type == 'buy':
            if self.cash >= trade.price * trade.quantity:
                self.cash -= trade.price * trade.quantity
                if trade.position.symbol in self.positions:
                    self.positions[trade.position.symbol].size += trade.quantity
                else:
                    self.positions[trade.position.symbol] = trade.position
            else:
                raise ValueError('Insufficient funds to execute trade.')
        elif trade.trade_type == 'sell':
            if trade.position.symbol in self.positions:
                if self.positions[trade.position.symbol].size >= trade.quantity:
                    self.positions[trade.position.symbol].size -= trade.quantity
                    self.cash += trade.price * trade.quantity
                else:
                    raise ValueError('Insufficient position size to execute trade.')
            else:
                raise ValueError('Position not found.')

    def get_total_pnl(self) -> float:
        total_pnl = 0.0
        for position in self.positions.values():
            total_pnl += position.get_pnl()
        return total_pnl
