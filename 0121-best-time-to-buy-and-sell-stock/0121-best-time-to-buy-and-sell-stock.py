class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left_pointer = 0 # Buy 
        right_pointer = 1 # Sell
        max_profit = 0 # Maximum Profit
        
        while(right_pointer < len(prices)):
            current_profit = prices[right_pointer] - prices[left_pointer]
            if current_profit > max_profit:
                max_profit = current_profit
            if prices[right_pointer] < prices[left_pointer]:
                left_pointer = right_pointer
            right_pointer += 1 
        
        return max_profit