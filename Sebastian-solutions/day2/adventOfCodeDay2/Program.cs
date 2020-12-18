using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace adventOfCodeDay2
{
    class Program
    {
        static void Main(string[] args)
        {
            List<string> passwordList = System.IO.File.ReadLines(@"C:\Users\sebastian.landen1\Documents\GitHub\AdventOfCode2020\solutions\day2\passwordList.txt").ToList();

            int counter = 0;

            for (int i = 0; i < 1000; i++)
            {
                
                string min = passwordList[i].Split('-')[0].ToString();
                string maxTemp = passwordList[i].Split('-')[1].ToString();
                string max = maxTemp.Substring(0, 2);
                
                string letterTemp = passwordList[i].Split(':')[0].ToString();
                string letter = letterTemp.Split(' ')[1];

                string passwordTemp = passwordList[i].Split(':')[1].ToString();
                // Removes whitespace
                string password = passwordTemp.Split(' ')[1];
                
                int x = password.Split(letter.ToCharArray()).Length - 1;

                if (password.Contains(letter) && x >= int.Parse(min) && x <= int.Parse(max))
                {
                    counter++;
                }

            }
            Console.WriteLine(counter);
            Console.ReadLine();
        }
    }
}
