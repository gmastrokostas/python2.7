#The script collects the IP addresses from the apache log file. It then uses the geoip2 database in order to find the geographical location of the IP. More information for the geoip2 database can be found at http://dev.maxmind.com/geoip/geoip2/downloadable/

#The module used to capture the IPs from the apache log file requires a CustomLog format. It needs to be specified in the apache config file and in the script. The string used is

#("%h <<%P>> %t %Dus \"%r\" %>s %b  \"%{Referer}i\" \"%{User-Agent}i\" %l %u"
import geoip2.database
import apache_log_parser
 
#specify the log file we will capture the IP from.
dir     = "/var/log/apache2/"
file    = "access.log"
apache_logfile = dir+file
 
 
#Create a connection to the mmdb file with all the IP geo-location data.
reader = geoip2.database.Reader("GeoLite2-City.mmdb")
 
#In case we cannot open the file throw an error message
try:
        f_open = open(apache_logfile, "rb")
except Exception as e:
        print e
 
#As required by the apache_log_parser module
line_parser = apache_log_parser.make_parser("%h <<%P>> %t %Dus \"%r\" %>s %b  \"%{Referer}i\" \"%{User-Agent}i\" %l %u")
 
#This is the list we will put in IPs.
ip_list = []
 
for loop in f_open:  #We are going through the file specified
    log_line_data = line_parser(loop) #We are using the apache parser as specified above
    remote_ip  =  log_line_data['remote_host'] #The apache parser returns a dictionary. We just want the remote_host key.
    for ip  in remote_ip:
        ip_list.append(remote_ip)  #We are appending the IPs to the list we created above.
 
 
unique_ip_list = set(ip_list)  # We delete the duplicate IP entries from our list.
for ips in unique_ip_list:
        try: #In case the IP is not recognized by the geoip2 database
                locate_ip = reader.city(ips) # we are using the geoip2 module here with the IPs from our list
                print ips, locate_ip.country.name
        except Exception as e:
                print e
