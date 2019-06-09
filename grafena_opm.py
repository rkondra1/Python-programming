#!/usr/bin/env python
'''
Created by r0k00d1 at 28/05/19

Feature: #Enter feature name here
Enter feature description here

Scenario: # Enter scenario name here
Enter steps here

python_version  :3.6
=========================================='''

import urllib.request
import json

endpoints = {

    "usgr" : "http://esm-graphite.glb.prod.walmart.com/render?target=stream.prod.primary_panomss*.ghs_opm_count.count,now&format=json",
    "usgm" : "http://esm-graphite.glb.prod.walmart.com/render?target=stream.prod.us*omsp1_ops.crc_customer_order_oms_gm_opm.*,now)&format=json",
    "ukgr" : "http://esm-graphite.glb.prod.walmart.com/render?target=stream.prod.asda.mtep_order_count.order_cnt),now)&format=json",
    "ukgm" : "http://esm-graphite.glb.prod.walmart.com/render?target=stream.prod.primary_payment_ap.ukgm-auth-success-metrics.count),now)&format=json",
    "canada" : "http://esm-graphite.glb.prod.walmart.com/render?target=stream.prod.gmctprdops.mtep_order_count.order_cnt),now)&format=json",
    "sams" : "http://prod-bdaas.glb.prod.walmart.com/render?target=stream.prod.atgprd.mtep_order_count.order_cnt,now)&format=json",
    "sng" : "http://prod-bdaas.glb.prod.walmart.com/render?target=stream.prod.scsngp1_ro.crc_sams_sg2_opm.order_count,now)&format=json",
    "mexico" : "http://prod-bdaas.glb.prod.walmart.com/render?target=stream.prod.mxgmcfp1_ops.mx_gm_prod_opm.*),now)&format=json",
}

endpoints1w = {

    "usgr" : "http://esm-graphite.glb.prod.walmart.com/render?target=timeShift(stream.prod.primary_panomss*.ghs_opm_count.count,'1w'),'1w'&format=json",
    "usgm" : "http://esm-graphite.glb.prod.walmart.com/render?target=timeShift(stream.prod.us*omsp1_ops.crc_customer_order_oms_gm_opm.*,'1w'),'1w'&format=json",
    "ukgr" : "http://esm-graphite.glb.prod.walmart.com/render?target=timeShift(stream.prod.asda.mtep_order_count.order_cnt,'1w'),'1w'&format=json",
    "ukgm" : "http://esm-graphite.glb.prod.walmart.com/render?target=timeShift(stream.prod.primary_payment_ap.ukgm-auth-success-metrics.count,'1w'),'1w'&format=json",
    "canada" : "http://esm-graphite.glb.prod.walmart.com/render?target=timeShift(stream.prod.gmctprdops.mtep_order_count.order_cnt,'1w'),'1w'&format=json",
    "sams" : "http://prod-bdaas.glb.prod.walmart.com/render?target=timeShift(stream.prod.atgprd.mtep_order_count.order_cnt,'1w'),'1w'&format=json",
    "sng" : "http://prod-bdaas.glb.prod.walmart.com/render?target=timeShift(stream.prod.scsngp1_ro.crc_sams_sg2_opm.order_count,'1w'),'1w'&format=json",
    "mexico" : "http://prod-bdaas.glb.prod.walmart.com/render?target=timeShift(stream.prod.mxgmcfp1_ops.mx_gm_prod_opm.*,'1w')'1w'&format=json",
}

endpoints2w = {

    "usgr" : "http://esm-graphite.glb.prod.walmart.com/render?target=timeShift(stream.prod.primary_panomss*.ghs_opm_count.count,'2w'),'2w'))&format=json",
    "usgm" : "http://esm-graphite.glb.prod.walmart.com/render?target=stream.prod.us*omsp1_ops.crc_customer_order_oms_gm_opm.*,'2w'),'2w'&format=json",
    "ukgr" : "http://esm-graphite.glb.prod.walmart.com/render?target=timeShift(stream.prod.asda.mtep_order_count.order_cnt,'2w'),'2w'&format=json",
    "ukgm" : "http://esm-graphite.glb.prod.walmart.com/render?target=timeShift(stream.prod.primary_payment_ap.ukgm-auth-success-metrics.count,'2w'),'2w'&format=json",
    "canada" : "http://esm-graphite.glb.prod.walmart.com/render?target=timeShift(stream.prod.gmctprdops.mtep_order_count.order_cnt,'2w'),'2w'&format=json",
    "sams" : "http://prod-bdaas.glb.prod.walmart.com/render?target=timeShift(stream.prod.atgprd.mtep_order_count.order_cnt,'2w'),'2w'&format=json",
    "sng" : "http://prod-bdaas.glb.prod.walmart.com/render?target=timeShift(stream.prod.scsngp1_ro.crc_sams_sg2_opm.order_count,'2w'),'2w'&format=json",
    "mexico" : "http://prod-bdaas.glb.prod.walmart.com/render?target=timeShift(stream.prod.mxgmcfp1_ops.mx_gm_prod_opm.*,'2w')'2w'&format=json",
}

url_list = [endpoints, endpoints1w, endpoints2w]

apps = {
    "usgr" : "USGR",
    "usgm" : "USGM",
    "ukgr" : "UKGR",
    "ukgm" : "UKGM",
    "canada" : "CANADA",
    "sams" : "SAMS",
    "sng" : "SNG",
    "mexico" : "MEXICO"
}

def usgr():
    sum_usgrdb = 0
    for endpoint in url_list:
        url = endpoint["usgr"]
        response = urllib.request.urlopen(url).read().decode('UTF-8')
        data = json.loads(response)
        for i in range(0, 7):
            opm_usgr_db = (data[i]["datapoints"][0])[0]
            if opm_usgr_db is None:
                opm_usgr_db = 0
            sum_usgrdb = sum_usgrdb + opm_usgr_db
    return sum_usgrdb


def usgm():
    url = endpoints["usgm"]
    response = urllib.request.urlopen(url).read().decode('UTF-8')
    data = json.loads(response)
    sum_usgmdb = 0
    for i in range(0, 6):
        opm_usgm_db = (data[i]["datapoints"][0])[0]
        if opm_usgm_db != None:
            sum_usgmdb = sum_usgmdb + opm_usgm_db
    return sum_usgmdb

def ukgr():
    url = endpoints["ukgr"]
    response = urllib.request.urlopen(url).read().decode('UTF-8')
    data = json.loads(response)
    opm_ukgr = (data[0]["datapoints"][0])[0]
    return opm_ukgr


def ukgm():
    url = endpoints["ukgm"]
    response = urllib.request.urlopen(url).read().decode('UTF-8')
    data = json.loads(response)
    opm_ukgm = (data[0]["datapoints"][0])[0]
    return opm_ukgm

def canada():
    url = endpoints["canada"]
    response = urllib.request.urlopen(url).read().decode('UTF-8')
    data = json.loads(response)
    opm_canada = (data[0]["datapoints"][0])[0]
    return opm_canada

def sams():
    url = endpoints["sams"]
    response = urllib.request.urlopen(url).read().decode('UTF-8')
    data = json.loads(response)
    opm_sams = (data[0]["datapoints"][0])[0]
    return opm_sams

def sng():
    url = endpoints["sng"]
    response = urllib.request.urlopen(url).read().decode('UTF-8')
    data = json.loads(response)
    opm_sng = (data[0]["datapoints"][0])[0]
    if opm_sng == 'null':
        opm_sng = 0
    return opm_sng

def mexico():
    url = endpoints["mexico"]
    response = urllib.request.urlopen(url).read().decode('UTF-8')
    data = json.loads(response)
    sum_mexico = 0
    for i in range(0, 4):
        opm_mexico_db = (data[i]["datapoints"][0])[0]
        if opm_mexico_db != None:
            sum_mexico = sum_mexico + opm_mexico_db
    return sum_mexico



if __name__ == '__main__':
    print("OPM for usgr is :", usgr())
    # print("OPM for usgm is :", usgm())
    # print("OPM for ukgr is :", ukgr())
    # print("OPM for ukgm is :", ukgm())
    # print("OPM for canada is :", canada())
    # print("OPM for sams is :", sams())
    # print("OPM for sng is :", sng())
    # print("OPM for mexico is :", mexico())
