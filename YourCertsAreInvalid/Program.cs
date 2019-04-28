using Newtonsoft.Json.Linq;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace YourCertsAreInvalid
{
    class Program
    {
        // gets the last occurrence of a datetime
        static DateTime GetLastOccurrence(DateTime dateTime, JArray linesArray, string otherId, int i, int j, DateTime otherThisDateTime)
        {
            List<DateTime> otherDateTimes = new List<DateTime>();

            for (int k = 0; k < linesArray.Count; k++)
            {
                if (k != j && k != i && (string)linesArray[k]["id"] == otherId)
                {
                    otherDateTimes.Add(DateTime.Parse((string)linesArray[k]["ts"]));
                }
            }
            DateTime otherHighestDateTime = otherThisDateTime;
            foreach (DateTime otherDateTime in otherDateTimes)
            {
                if (otherDateTime.CompareTo(otherThisDateTime) > 0)
                {
                    // if the other date time is more recent
                    otherHighestDateTime = otherDateTime;
                }
            }

            return otherHighestDateTime;
        }

        static void Main(string[] args)
        {
            string[] lines = File.ReadAllLines("x509_1.log");

            JArray linesArray = new JArray();

            // convert txt file to json array
            foreach (string line in lines)
            {
                JObject obj = JObject.Parse(line);
                linesArray.Add(obj);
            }

            for (int i = 0; i < linesArray.Count; i++)
            {
                string id = (string)linesArray[i]["id"];
                string name = ((string)linesArray[i]["certificate.subject"]);
                double ts = (double)linesArray[i]["ts"];
                DateTime thisDateTime = DateTime.

                for (int j = 0; j < linesArray.Count; j++)
                {
                    string otherId = (string)linesArray[j]["id"];

                    // if this line has same ID as another line
                    if (j != i && otherId == id)
                    {
                        string otherName = ((string)linesArray[i]["certificate.subject"]);

                        DateTime otherThisDateTime = DateTime.Parse((string)linesArray[i]["ts"]);

                        // get last occurrence of site
                        DateTime highestDateTime = GetLastOccurrence(thisDateTime, linesArray, id, i, j, thisDateTime);

                        // get last occurrence of other site
                        DateTime otherHighestDateTime = GetLastOccurrence(otherThisDateTime, linesArray, otherId, i, j, otherThisDateTime);

                        // invalidate both
                        Console.WriteLine("Request: " + name.Substring(name.IndexOf("CN=") + "CN=".Count()) + Environment.NewLine + "First: " + thisDateTime.ToString() + Environment.NewLine + "Last: " + highestDateTime.ToString() + Environment.NewLine +
                            "Request: " + otherName.Substring(otherName.IndexOf("CN=") + "CN=".Count()) + Environment.NewLine + "First: " + otherThisDateTime.ToString() + Environment.NewLine + "Last: " + otherHighestDateTime.ToString() + Environment.NewLine);
                    }
                }
            }
        }
    }
}
