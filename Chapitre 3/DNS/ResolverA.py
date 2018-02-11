import dns.resolver

host = 'alphorm.com'

reponse_ipv4 = dns.resolver.query(host, 'A')
for data in reponse_ipv4:
    print 'Adresse IPv4 : ',data.address


    