import java.util.*;
import java.io.*;

public class TwentyOnetoThirty 
{

	public static void main(String[] args) throws Exception 
	{
		Scanner scan = new Scanner(new File("names.txt"));
		String[] names = scan.next().split(",");
		System.out.println(nameScores(names));
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
	
}
