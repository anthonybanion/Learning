package introduction.programing;
/* Descrition: This program contains methods to calculate the average price of a stock, find the maximum price,
 * File name: StockAnalysis.java
 * Creation date: 17/03/2025
 * Last update: 17/03/2025
*/

import java.util.ArrayList;

public class StockAnalysis {

    // Method to calculate the average price from an array
    public static double calculateAveragePrice(int[] prices) {
        int sum = 0;
        for (int price : prices) {
            sum += price;
        }
        return (double) sum / prices.length;    // Cast sum to double to get a double result
    }

    // Method to calculate the average price from an ArrayList
    public static double calculateAveragePrice(ArrayList<Integer> prices) {
        int sum = 0;
        for (int price : prices) {
            sum += price;
        }
        return (double) sum / prices.size();    // Cast sum to double to get a double result
    }

    // Method to find the maximum price in an array
    public static int findMaximumPrice(int[] prices) {
        int maxPrice = prices[0];
        for (int price : prices) {
            if (price > maxPrice) {
                maxPrice = price;
            }
        }
        return maxPrice;
    }

    // Method to find the maximum price in an ArrayList
    public static int findMaximumPrice(ArrayList<Integer> prices) {
        int maxPrice = prices.get(0);
        for (int price : prices) {
            if (price > maxPrice) {
                maxPrice = price;
            }
        }
        return maxPrice;
    }

    // Method to count occurrences of a specific price in an array
    public static int countOccurrences(int[] prices, int targetPrice) {
        int count = 0;
        for (int price : prices) {
            if (price == targetPrice) {
                count++;
            }
        }
        return count;
    }

    // Method to compute the cumulative sum of stock prices in an ArrayList
    public static ArrayList<Integer> computeCumulativeSum(ArrayList<Integer> prices) {
        ArrayList<Integer> cumulativeSum = new ArrayList<>();
        int sum = 0;
        for (int price : prices) {
            sum += price;
            cumulativeSum.add(sum);
        }
        return cumulativeSum;
    }

    public static void main(String[] args) {
        int[] stockPricesArray = {100, 102, 98, 105, 101, 97, 103, 100, 99, 104};
        ArrayList<Integer> stockPricesList = new ArrayList<>();
        for (int price : stockPricesArray) {
            stockPricesList.add(price);
        }

        System.out.println("Average price (Array): " + calculateAveragePrice(stockPricesArray));
        System.out.println("Average price (ArrayList): " + calculateAveragePrice(stockPricesList));
        System.out.println("Maximum price (Array): " + findMaximumPrice(stockPricesArray));
        System.out.println("Maximum price (ArrayList): " + findMaximumPrice(stockPricesList));
        System.out.println("Occurrences of price 100 (Array): " + countOccurrences(stockPricesArray, 100));
        System.out.println("Cumulative sum (ArrayList): " + computeCumulativeSum(stockPricesList));
    }
}