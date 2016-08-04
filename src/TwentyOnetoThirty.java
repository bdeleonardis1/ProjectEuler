import java.util.*;
import java.io.*;
import java.math.BigDecimal;
import java.math.BigInteger;

public class TwentyOnetoThirty 
{

	public static void main(String[] args) throws Exception 
	{
		System.out.println(recipCycles());
	}
	
	//------------
	//Problem 21
	//------------
	public static int amicable_numbers(int cap)
	{
		HashSet<Integer> amicables = new HashSet<Integer>();
		for(int i = 2; i < cap; i++)
		{
			if(amicables.contains(i))
				continue;
			
			int sum = sumFactors(i);
			if(i == sumFactors(sum) && i != sum)
			{
				amicables.add(i);
				amicables.add(sum);
			}
		}
		
		int sum = 0;
		for(Integer i: amicables)
			sum += i;
		
		return sum;
	}
	
	//Helper for 21
	public static int sumFactors(double num)
	{
		int sum = 1;
		for(int i = 2; i <= Math.sqrt(num); i++)
		{
			if(num / i == (int)(num / i))
			{
				sum += i;
				sum += (int)(num / i);
			}
		}
		if(Math.sqrt(num) == (int)Math.sqrt(num))
			sum -= Math.sqrt(num);
		
		return sum;
	}
	
	//-------------
	//Problem 22
	//-------------
	public static long nameScores(String[] names)
	{
		Arrays.sort(names);
		long sum = 0;
		for(int i = 0; i < names.length; i++)
		{
			String n = names[i];
			int curr = 0;
			
			for(int j = 0; j < n.length(); j++)
				curr += (int)n.charAt(j) - 64;
			
			sum += curr * (i + 1);
		}
		return sum;
	}
	
	//-------------
	//Problem 23
	//-------------
	public static long nonAbundantSums()
	{
		ArrayList<Integer> abundants = new ArrayList<Integer>();
		for(int i = 12; i < 28112; i++)
			if(sumFactors(i) > i)
				abundants.add(i);
		
		HashSet<Integer> sums = new HashSet<Integer>();
		for(int i = 0; i < abundants.size(); i++)
			for(int j = 0; j < abundants.size(); j++)
				sums.add(abundants.get(i) + abundants.get(j));
		
		long sum = 0;
		for(int i = 0; i < 28124; i++)
			if(!sums.contains(i))
				sum += i;
		
		return sum;
	}
	
	//------------
	//Problem 24
	//------------
	public static int[] lexiPermutations(int[] nums)
	{
		for(int i = 1; i < 1000000; i++)
		{
			int j = nums.length - 1;
			while(j > 0 && nums[j] <= nums[j - 1])
				j--;
			
			if(j == 0)
				break;
			
			int pivot = j - 1;
			int k = nums.length - 1;
			
			while(nums[k] <= nums[pivot])
				k--;
			
			int temp = nums[pivot];
			nums[pivot] = nums[k];
			nums[k] = temp;	
			
			int l = nums.length - 1;
			while(j < l)
			{
				temp = nums[j];
				nums[j] = nums[l];
				nums[l] = temp;
				
				j++;
				l--;
			}
		}
		return nums;
	}
	
	//---------------
	//Problem 25
	//---------------
	public static long thousDigitFib()
	{
		BigInteger first = new BigInteger("1");
		BigInteger second = new BigInteger("1");
		BigInteger curr;
		long count = 2;
		while(true)
		{
			curr = first.add(second);
			count++;
			
			if(curr.toString().length() >= 1000)
				return count;
			
			if(first.compareTo(second) < 0)
				first = curr;
			else
				second = curr;
		}
	}
	
	//--------------
	//Problem 26
	//--------------
	public static int recipCycles()
	{
		int d = 0, len = 0;
		
		for(int i = 1000; i > 1; i--)
		{
			if(len >= i)
				break;
			
			int remainders[] = new int[i];
			int val = 1, poss = 0;
			
			while(remainders[val] == 0 && val != 0)
			{
				remainders[val] = poss;
				val *= 10;
				val %= i;
				poss++;
			}
			
			if(poss - remainders[val] > len)
			{
				d = i;
				len = poss - remainders[val];
			}
		}
		
		return d;
	}
	
	
	
	//Random method to generate all the subsets
	public static void subsets(Object[] items)
	{
		ArrayList<ArrayList<Object>> sets = new ArrayList<ArrayList<Object>>();
		sets.add(new ArrayList<Object>());
		
		for(int i = 0; i < items.length; i++)
		{
			int size = sets.size();
			for(int j = 0; j < size; j++)
			{
				System.out.println("i: " + i + " j: " + j + " sets.size " + sets.size());
				ArrayList<Object> curr = new ArrayList<Object>();
				for(int k = 0; k < sets.get(j).size(); k++)
					curr.add(sets.get(j).get(k));
				curr.add(i);
				sets.add(curr);
			}
		}
	}
}
