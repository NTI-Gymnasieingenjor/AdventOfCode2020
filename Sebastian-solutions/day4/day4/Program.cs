using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace day4
{
    class Program
    {
        static void Main(string[] args)
        {
            StreamReader streamReader = new StreamReader(@"C:\Users\sebastian.landen1\Documents\GitHub\AdventOfCode2020\solutions\day4\passports.txt");

            string passports = streamReader.ReadToEnd();
            Console.WriteLine(streamReader.ReadToEnd());
            Console.ReadLine();
            passports.Split(new string[] { "\n\n" }, StringSplitOptions.None);
            //Console.WriteLine(passports);
            //Console.ReadLine();
        }
    }
}
