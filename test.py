import urllib
import urllib2 
import os.path

save_path = "/Users/ryan/DevOps/python/project_2_stock_analytic/symbols/"

def stock_price_get(fname):
    with open('symbol_list.csv') as f:
        content = f.readlines()
    

urllib.urlretrieve ("http://real-chart.finance.yahoo.com/table.csv?s=5168.KL&d=7&e=18&f=2015&g=d&a=0&b=3&c=2000&ignore=.csv",os.path.join(save_path,"5168.csv"))
