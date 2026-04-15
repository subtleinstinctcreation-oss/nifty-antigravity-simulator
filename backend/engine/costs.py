from dataclasses import dataclass

@dataclass
class CostBreakdown:
    brokerage: float
    stt: float  # Securities Transaction Tax
    sebi_charges: float
    exchange_charges: float
    slippage: float

    def calculate_total_cost(self) -> float:
        return (self.brokerage + self.stt + self.sebi_charges + self.exchange_charges + self.slippage)  
