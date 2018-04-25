import sys
import datetime
import json
from time import mktime
import vulnSearch
import argparse

class vulnSearchDate:

    def convertDate2Epoch(self, days, month, year, debug):
        self.debug = debug

        try:
            date_obj = datetime.date(int(year), int(month), int(days))
            timestamp = mktime(date_obj.timetuple())

        except Exception as e:
            if self.debug:
                print('Error: date info below')
                print(days, month, year)
                print(timestamp)
                print(datetime.datetime.fromtimestamp(timestamp))
                print()

            return e

        return timestamp

    def betweenDates(self, vulns, beginYear, endYear, debug):

        day = 1
        month = 1
        start = self.convertDate2Epoch(day, month, beginYear, debug)
        end = self.convertDate2Epoch(day, month, endYear, debug)
        out = ''

        for item in vulns:

            if ( vulns[item].datePublic < start or vulns[item].datePublic > end):
                continue

            else:
                if debug:
                    print(str(vulns[item]))

                out = out + json.dumps(vulns[item], default=lambda o: o.__dict__)

        return out


    def run(self, debug, vendor, product, searchMax, beginYear, endYear):
        vulns = vulnSearch.Search().run(debug, vendor, product, searchMax)

        if debug:
            print(vulns)

        results = self.betweenDates(vulns, beginYear, endYear, debug)
        #out = ''

        #for item in results:
            #out = out + json.dumps(results[item], default=lambda o: o.__dict__)

        if debug:
            print('Results:\n{}'.format(results))

        return results


if __name__ == "__main__":
    #Parsing the command line for arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--debug', help='turn on script debugging', action='store_true', default=False)
    parser.add_argument('vendor', help='Vendor of product',type=str)
    parser.add_argument('product', help='Product to search for',type=str)
    parser.add_argument('searchMax', help='Input number of results to return. Default is all', nargs='?', type=str, default='all')
    parser.add_argument('beginYear', help='input year to start search',type=int)
    parser.add_argument('endYear', help='input year to end search',type=int)

    args = parser.parse_args()

    vulnSearchDate().run(args.debug, args.vendor, args.product, args.searchMax, args.beginYear, args.endYear)


