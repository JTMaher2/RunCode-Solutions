using Newtonsoft.Json.Linq;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace SSH_I_Am_Pawsing_Bwo
{
    class SSH_I_Am_Pawsing_Bwo
    {
        // compare segments from two IP addresses
        static int CompareSegs(string ipAddr, string otherIpAddr, int seg)
        {
            string[] ipAddrSegs = ipAddr.Split('.'),
                otherIpAddrSegs = otherIpAddr.Split('.');

            // start the comparison with the final segment
            ipAddrSegs = ipAddrSegs.Reverse().ToArray();
            otherIpAddrSegs = otherIpAddrSegs.Reverse().ToArray();

            int ipAddrSeg = int.Parse(ipAddrSegs[seg]),
                otherIpAddrSeg = int.Parse(otherIpAddrSegs[seg]);

            if (ipAddrSeg >= otherIpAddrSeg)
            {
                return 1; // this IP address is lower than the other IP address
            }

            if (seg < ipAddrSegs.Length - 1)
            {
                // go to next segment
                CompareSegs(ipAddr, otherIpAddr, seg + 1);
            }

            // either both IP addresses are same, or first IP address is less than second IP address
            return 0;
        }

        static void Main(string[] args)
        {
            string[] lines = File.ReadAllLines(args[0]);

            JArray linesArray = new JArray();

            // convert txt file to json array
            foreach (string line in lines)
            {
                JObject obj = JObject.Parse(line);
                linesArray.Add(obj);
            }

            Dictionary<string, int> potentialHacks = new Dictionary<string, int>();

            // get # of potential hacks for each IP
            for (int i = 0; i < linesArray.Count; i++)
            {
                string id = (string)linesArray[i]["id.resp_h"];

                if (potentialHacks.ContainsKey(id))
                { // has already occurred before
                    potentialHacks[id]++;
                } else
                { // 1st occurrence
                    potentialHacks[id] = 1; // assume that there is always at least 1 potential hack
                }
            }

            // get length of longest potentially hacked IP
            string[] potentialHacksArray = potentialHacks.Keys.ToArray();

            string longestIp = potentialHacksArray[0];
            for (int i = 0; i < potentialHacksArray.Count(); i++)
            {
                if (potentialHacksArray[i].Count() > longestIp.Count())
                {
                    longestIp = potentialHacksArray[i];
                }
            }

            // sort the IP addresses in ascending order
            int lowCompIdx = 0,
                highCompIdx = 1;

            while (true)
            {
                int comparison = CompareSegs(potentialHacksArray[lowCompIdx], potentialHacksArray[highCompIdx], 0);
                if (comparison == 1)
                {
                    // if a higher IP address was found to be lower than the previously-thought lowest,
                    // make the lowest IP address this new IP address
                    string temp = potentialHacksArray[lowCompIdx];
                    potentialHacksArray[lowCompIdx] = potentialHacksArray[highCompIdx];
                    potentialHacksArray[highCompIdx] = temp;

                    // start comparison over from beginning
                    lowCompIdx = 0;
                    highCompIdx = 1;
                } else
                { // the lower IP address was not higher than the higher IP address

                    if (highCompIdx == potentialHacksArray.Count() - 1)
                    { // there's no more room to increment high index,
                        // so increment low index, and set high index to one above low index
                        lowCompIdx++;
                        if (lowCompIdx + 1 < potentialHacksArray.Length)
                        {
                            highCompIdx = lowCompIdx + 1;
                        } else
                        {
                            // all possible permutations have been checked
                            break;
                        }
                    } else
                    { // there's still room to increment the high index
                        highCompIdx++;
                    }
                }
            }

            // print potential # of hacks for each IP
            for (int i = 0; i < potentialHacks.Count; i++)
            {
                Console.Write(potentialHacksArray[i]);

                // add # of placeholder spaces that is difference between longest potentially hacked IP and this one
                for (int placeholderSpace = 0; placeholderSpace < longestIp.Count() - potentialHacksArray[i].Count(); placeholderSpace++)
                {
                    Console.Write(" ");
                }

                Console.WriteLine(" --> " + potentialHacks[potentialHacksArray[i]] + " potential hax");
            }
        }
    }
}
