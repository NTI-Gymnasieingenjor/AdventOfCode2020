using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace day3
{
    class Program
    {
        static void Main(string[] args)
        {
            int currentPosX = 0;
            int treeCounter = 0;

            string line;

            // Read the file and display it line by line.  
            System.IO.StreamReader map =
                new System.IO.StreamReader(@"C:\Users\sebastian.landen1\Documents\GitHub\AdventOfCode2020\solutions\day3\map.txt");
            while ((line = map.ReadLine()) != null)
            {
                if (currentPosX <= 31)
                {
                    if (line[currentPosX] == '#')
                    {
                        treeCounter++;
                        Console.WriteLine(currentPosX);
                        //Console.ReadLine();
                    }
                    if (currentPosX <= 29 && line[currentPosX + 1] == '#')
                    {
                        treeCounter++;
                    }
                    if (currentPosX <= 28 && line[currentPosX + 2] == '#')
                    {
                        treeCounter++;
                    }
                    currentPosX += 3;
                }

                if (currentPosX >= 31)
                {
                    currentPosX = 0;
                }

            }

            map.Close();
            Console.WriteLine("There were {0} trees.", treeCounter);
            // Suspend the screen.  
            Console.ReadLine();

        }
    }
}
