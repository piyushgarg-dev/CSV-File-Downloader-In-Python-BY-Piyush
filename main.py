from urllib import request
import sys


print("CSV DOWNLOADER BY PIYUSH GARG")

downloadurl=input("Enter the URL of csv : ")
#downloadurl="http://samplecsvs.s3.amazonaws.com/SalesJan2009.csv"

downloadurl.strip()

if downloadurl.find("https") or downloadurl.find("http"):
    pass
else:
    print("Invalid URL")
    sys.exit()



def download(csv_url):
    response=request.urlopen(csv_url)
    csv=response.read()
    csv_str=str(csv)
    lines =csv_str.split("\\n")
    dest_url=r"Piyush.csv"
    fx=open(dest_url,"w")
    for line in lines:
        fx.write(line+"\n")
    fx.close()


download(downloadurl)
print("Download Successfull, Please Check the Program Directory \"Piyush.csv\" , Thankyou")