from bottle import route, run, template, post, request, static_file
from Loan import *
from savings import *
from avg_inflation import *
from bestiReikningur import *

@route('/')
def index():
    return template('main')

@route('/spara', method='POST')
def form():
    amount = request.forms.getall('time')
    return amount

@route('/lan', method='POST')
def form():

    #Period for saving/paying into loan
    periodYears = int(request.forms.get('periodYears'))
    periodMonths = int(request.forms.get('periodMonths'))
    totalPeriod = ( periodYears * 12 ) + periodMonths

    #amount the user has leftover
    monthlyAmount = int(request.forms.get('monthlyAmount'))

    #inflation period
    inflateYstart = request.forms.get('inflYstart')
    inflateMstart = request.forms.get('inflMstart')
    inflateYend = request.forms.get('inflYend')
    inflateMend = request.forms.get('inflMend')
    inflateMstartZero =  "0" if int(inflateMstart) < 10 else ""
    inflateMendZero =  "0" if int(inflateMend) < 10 else ""
    inflPeriodStartKey = inflateYstart + "-" + inflateMstartZero + inflateMstart
    inflPeriodEndKey = inflateYend + "-" + inflateMendZero + inflateMend

    #we're using .getall so these are lists
    name = request.forms.getall('lname')
    principle = request.forms.getall('principle')
    i_rate = request.forms.getall('i_rate')
    term = request.forms.getall('term')
    comp_freq = request.forms.getall('compoundInt')
    indexed = request.forms.getall('indexed')
    userInflation = request.forms.get('inflation')
    loans = []

    #we assume all the lists are equally long, iterate over them and create a list of loans
    for i in range(0, len(principle)):
        loans.append( Loan( name[i], float(principle[i]), float(i_rate[i]), int(term[i]), int(comp_freq[i]), bool(indexed[i]) ) )
        if loans[i].indexed:
            if len(userInflation) > 0:
                loans[i].i_rate += float(userInflation) / 100.0
            else:
                loans[i].i_rate += avg_inflation(inflPeriodStartKey, inflPeriodEndKey) / 100.0


    #metum lánin sem slegin voru inn, evaluate skilar besta láninu
    res = evaluate(loans, totalPeriod, monthlyAmount)

    #Fáum lista yfir greiðslur af upprunalega láninu og breyttu láni m.v. auka greiðslur.
    chartValues = overview(res[0], totalPeriod, monthlyAmount)

    #Hérna ættum við að reikna hversu mikið er sparað

    return template('results', loan = res, maxprof = res[1], chartValues = chartValues, period = res[0].term)

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static')

@route('/static/<path:path>')
def callback(path):
    return static_file(path, root='./static')

run(host='localhost', port=8080)