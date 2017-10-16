import string
import urllib2
import boto
print("Boto version: "+boto.Version)


res = urllib2.urlopen('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key')
res = res.read()

keys = res.split(':')
print("ID: " + keys[0])
print("\nKey: " +keys[1])


