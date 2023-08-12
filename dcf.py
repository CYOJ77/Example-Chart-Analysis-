# Importing necessary libraries
import numpy as np

# Assumptions
discount_rate = 0.1  # Discount rate (required rate of return)
terminal_growth_rate = 0.03  # Terminal growth rate
forecast_period = 5  # Number of forecast periods

# Financial Data (in billions)
free_cash_flows = [50, 60, 70, 80, 90]  # Projected free cash flows for the forecast period
terminal_cash_flow = free_cash_flows[-1] * (1 + terminal_growth_rate) / (discount_rate - terminal_growth_rate)  # Terminal cash flow

# Calculate present value of cash flows
present_values = [cf / (1 + discount_rate) ** (i + 1) for i, cf in enumerate(free_cash_flows)]
terminal_value = terminal_cash_flow / (1 + discount_rate) ** forecast_period
total_present_value = np.sum(present_values) + terminal_value

# Print the results
print(f"Present Value of Free Cash Flows: {present_values}")
print(f"Present Value of Terminal Cash Flow: {terminal_value}")
print(f"Total Present Value: {total_present_value}")