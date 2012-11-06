#!/usr/bin/python
import json
import datetime
from rdflib.graph import Graph
from rdflib.term import URIRef, Literal, BNode
from rdflib.namespace import Namespace, RDF

DC = Namespace("http://purl.org/dc/terms/")
RDFS = Namespace("http://www.w3.org/2000/01/rdf-schema#")
BASE = Namespace("http://tw.rpi.edu/blah/events/")
S = Namespace("http://tw.rpi.edu/blah/schema/")
ROOT = Namespace("http://tw.rpi.edu")
_XSD_NS = Namespace(u'http://www.w3.org/2001/XMLSchema#')

store = Graph()

for i in json.load(open('a')):
  if 'session' in i.keys():
    #print i['session']
    dt = (datetime.datetime.fromtimestamp(i['timestamp']).strftime('%Y-%m-%d %H:%M:%S'))
    store.add((BASE[i['session']+"/"+str(i['timestamp'])], DC['created'], Literal(dt,datatype=_XSD_NS.datetime)))
    store.add((BASE[i['session']+"/"+str(i['timestamp'])], DC['identifier'], Literal(i['session'])))
    store.add((BASE[i['session']+"/"+str(i['timestamp'])], S['url'], ROOT[i['uri']]))
    store.add((BASE[i['session']+"/"+str(i['timestamp'])], S['method'], ROOT[i['method']]))
    if len(i['request_content']) > 0:
      for j,k in i['request_content'].items():
        contents = BNode()
        store.add((BASE[i['session']+"/"+str(i['timestamp'])], S['content'], contents))
        store.add((contents, S['variableName'], Literal(j)))
        store.add((contents, S['variableValue'], Literal(k)))

print store.serialize(format="turtle")



