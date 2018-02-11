import dns.resolver

reponse = dns.resolver.query('kondah.com', 'MX')
for data in reponse:
    print 'Serveur MX : ',data.exchange,'Priorite',data.preference

