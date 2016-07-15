
public class EasyQuestions
{
	public static void main(String[] args)
	{
		System.out.println(mult3and5(1000));
	}
	
	public static int mult3and5(int cap)
	{
		int total = 0;
		for(int i = 1; i < cap; i++)
		{
			if(i % 3 == 0 || i % 5 == 0)
				total += i;
		}
		
		return total;
	}

}
